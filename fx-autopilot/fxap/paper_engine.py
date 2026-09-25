"""PAPER 実行エンジン（LOCK 済み仕様を LOCK 後の未知データで運用する Forward Test）。

Market Data → Signal Engine → Risk Engine → Order Engine → Broker Adapter → Execution Confirmation →
Position Manager → PnL / Drawdown → Logging（ハッシュチェーン台帳）→ Research Database（equity.csv / trades.csv）

- 足は時系列順に 1 本ずつ処理する（GitHub Actions で数時間おきに起動し、前回以降に確定した足を順に処理）。
  足 i の終値で判断した注文は足 i+1 の始値で約定する（リアルタイム運用と同じ遅延を再現）
- 冪等性: client_order_id = hash(spec, pair, 判断足, 方向)。送信済み ID は再送しない（再実行・再起動でも二重注文なし）
- 発注失敗: 台帳に記録し、その判断では再送しない（次のシグナルを待つ）。連続失敗 3 回で Kill Switch
- API 切断: 新規・決済とも送らず処理を中断（状態は保存。次回起動で再開）
- データ欠損・古いデータ・異常スプレッド: 新規禁止（Risk Engine）
- Kill Switch: 最大 DD 到達・連続発注失敗で自動発動 → 全決済。解除は本人のみ（cli kill-switch release --by）
- Forward 期間中に仕様（パラメータ・Risk）を変えることはできない（spec_hash 不一致なら停止）
"""
from __future__ import annotations

import csv
import json
import math

import numpy as np
import pandas as pd

from . import safety
from .backtest import to_jpy_table
from .broker.base import BrokerDisconnected, BrokerError, OrderRequest
from .broker.paper import PaperBroker
from .common import PAIRS, PAPER_DIR, sha, utcnow
from .costs import CostProfile, effective_quotes
from .ledger import Ledger
from .research import spec_signals
from .risk import OpenPos, RiskConfig, RiskEngine, RiskState

QCOLS = ["mid_o", "mid_c", "bid_o", "ask_o", "bid_h", "ask_h", "bid_l", "ask_l", "bid_c", "ask_c",
         "spread_obs_pips", "spread_med"]


def market_open(t: pd.Timestamp) -> bool:
    wd, h = t.weekday(), t.hour
    return not ((wd == 4 and h >= 21) or wd == 5 or (wd == 6 and h < 21))


class PaperEngine:
    def __init__(self, spec: dict, data: dict, root=None, broker=None, cost: CostProfile | None = None,
                 risk_cfg: RiskConfig | None = None, initial_equity: float = 1_000_000.0, start=None,
                 spread_median_window: int = 500, now=None, check_safety: bool = True):
        if check_safety:
            safety.assert_paper_only()
        self.spec = spec
        self.data = data
        self.pairs = list(spec.get("trade_pairs") or spec["pairs"])
        self.dir = (root or PAPER_DIR) / spec["spec_id"]
        self.dir.mkdir(parents=True, exist_ok=True)
        self.ledger = Ledger(self.dir / "ledger.jsonl")
        self.cost = cost or CostProfile.load(spec.get("cost_profile"))
        self.risk_cfg = risk_cfg or RiskConfig.load(spec.get("risk"))
        self.risk = RiskEngine(self.risk_cfg)
        self.state_path = self.dir / "state.json"
        self.now = now
        st = json.loads(self.state_path.read_text()) if self.state_path.exists() else None
        if st and st["spec_hash"] != spec["spec_hash"]:
            raise RuntimeError(f"{spec['spec_id']}: LOCK 後に仕様が変わっています（Forward 中の変更は禁止。新バージョンで）")
        self.st = st or {"spec_id": spec["spec_id"], "spec_hash": spec["spec_hash"], "last_bar": None,
                         "started_at": utcnow().isoformat(),
                         "start": str(pd.Timestamp(start or spec.get("locked_at"))), "halted": False,
                         "consecutive_order_errors": 0, "bars_processed": 0}
        rs = self.st.get("risk_state")
        self.rstate = RiskState(**rs) if rs else RiskState(equity=initial_equity, hwm=initial_equity)
        self.broker = broker or PaperBroker(self.cost, initial_equity, self.st.get("broker_state"))
        self.spread_median_window = spread_median_window
        self.mgmt = self.st.get("mgmt", {})     # pair -> {"last_bar_i_time": ...}

    # ------------------------------------------------------------------ 実行
    def run(self, until=None, log=print) -> dict:
        start = pd.Timestamp(self.st["start"])
        start = start.tz_localize("UTC") if start.tzinfo is None else start
        last = pd.Timestamp(self.st["last_bar"]) if self.st["last_bar"] else None
        if last is not None and last.tzinfo is None:
            last = last.tz_localize("UTC")
        sig = spec_signals(self.spec, self.data, self.pairs)
        Q = {}
        idx = None
        for p in self.pairs:
            q = effective_quotes(self.data[p], p, self.cost)
            q["spread_med"] = q["spread_obs_pips"].rolling(self.spread_median_window, min_periods=50).median().shift(1)
            Q[p] = q
            ix = q.index[q.index >= start]
            idx = ix if idx is None else idx.union(ix)
        if until is not None:
            u = pd.Timestamp(until)
            idx = idx[idx <= (u.tz_localize("UTC") if u.tzinfo is None else u)]
        full_idx = idx
        conv = to_jpy_table(self.data, full_idx)
        new = idx[idx > last] if last is not None else idx
        summary = {"spec_id": self.spec["spec_id"], "bars_new": int(len(new)), "fills": 0, "orders": 0,
                   "rejections": 0, "errors": 0, "halted": self.st["halted"]}
        if not len(new):
            self._save()
            return summary
        self.ledger.append("run_start", spec_id=self.spec["spec_id"], first_bar=str(new[0]), last_bar=str(new[-1]),
                           broker=self.broker.name)
        now = pd.Timestamp(self.now) if self.now is not None else pd.Timestamp(utcnow())
        now = now.tz_localize("UTC") if now.tzinfo is None else now
        pos_in_full = {t: k for k, t in enumerate(full_idx)}
        qrec = {p: Q[p].loc[Q[p].index.isin(new), QCOLS].to_dict("index") for p in self.pairs}
        srec = {p: sig[p].loc[sig[p].index.isin(new)].to_dict("index") for p in self.pairs}
        conv_rec = conv.to_dict("records")
        eq_rows = []
        for t in new:
            k = pos_in_full[t]
            conv_prev = conv_rec[max(k - 1, 0)]
            conv_now = conv_rec[k]
            quotes = {p: qrec[p][t] for p in self.pairs if t in qrec[p]}
            try:
                if not self.broker.is_connected():
                    raise BrokerDisconnected("disconnected before bar")
                fills = self.broker.on_bar_open(t, quotes, conv_prev, self.rstate.equity)
                fills += self.broker.on_bar_range(t, quotes)
                for f in fills:
                    self.ledger.append("fill", **{k2: v for k2, v in f.__dict__.items()})
                summary["fills"] += len(fills)
                self.broker.on_bar_close(t, quotes, conv_now)
                acct = self.broker.get_account()
            except BrokerDisconnected as e:
                self.rstate.broker_connected = False
                self.ledger.append("broker_disconnected", bar=str(t), error=str(e))
                log(f"  [{self.spec['spec_id']}] API 切断: 処理を停止（{t}）")
                summary["stopped"] = "broker_disconnected"
                break
            self.rstate.broker_connected = True
            eq = acct["equity"]
            eq_rows.append((str(t), round(eq, 2), round(acct["cash"], 2), round(acct["gross_notional"], 2),
                            len(self.broker.positions)))
            acts = self.risk.on_bar(self.rstate, t, eq)
            if "flatten_kill" in acts and not self.st["halted"]:
                self._kill(t, self.rstate.kill_reason)
            if self.st["halted"] or self.rstate.kill_switch:
                self.st["halted"] = True
                for p in list(self.broker.positions):
                    self.broker.close_position(p, "kill", sha(f"{self.spec['spec_id']}|{p}|{t}|kill")[:24])
                self._mark(t, quotes)
                continue
            self._manage_and_signal(t, quotes, srec, conv_now, now, t == new[-1], summary)
            self._mark(t, quotes)
            self.st["bars_processed"] += 1
        self._append_equity(eq_rows)
        if eq_rows:
            self.ledger.append("equity", bar=eq_rows[-1][0], equity=eq_rows[-1][1], cash=eq_rows[-1][2],
                               gross_notional=eq_rows[-1][3], open_positions=eq_rows[-1][4],
                               risk=self.rstate.to_dict())
        self._write_trades()
        self._save()
        summary["halted"] = self.st["halted"]
        summary["equity"] = self.rstate.equity
        self.ledger.append("run_end", **summary)
        return summary

    def _mark(self, t, quotes):
        for p in quotes:
            self.mgmt.setdefault(p, {})["last_bar"] = str(t)
        self.st["last_bar"] = str(t)

    def _kill(self, t, reason):
        self.st["halted"] = True
        self.rstate.kill_switch = True
        self.rstate.kill_reason = reason
        n = self.broker.cancel_pending_entries() if hasattr(self.broker, "cancel_pending_entries") else 0
        self.ledger.append("kill_switch", bar=str(t), reason=reason, cancelled_entries=n)

    def _manage_and_signal(self, t, quotes, sig, conv, now, is_latest, summary):
        exiting = set()
        for p in self.pairs:
            if p not in quotes:
                continue
            s = sig[p].get(t)
            q = quotes[p]
            pos = self.broker.positions.get(p)
            if pos is not None:
                pos["bars"] += 1
                c = q["mid_c"]
                pos["best_close"] = max(pos["best_close"], c) if pos["side"] > 0 else min(pos["best_close"], c)
                td = s["trail_dist"] if s is not None else np.nan
                if pos["trail"] is not None and td == td and td > 0:
                    self.broker.modify_stop(p, pos["best_close"] - pos["side"] * td)
                reason = None
                if pos["max_bars"] is not None and pos["bars"] >= pos["max_bars"]:
                    reason = "time"
                elif s is not None and ((pos["side"] > 0 and bool(s["exit_long"])) or (pos["side"] < 0 and bool(s["exit_short"]))):
                    reason = "signal"
                elif s is not None and int(s["entry"]) == -pos["side"]:
                    reason = "signal"
                if reason:
                    r = self._safe(lambda: self.broker.close_position(
                        p, reason, sha(f"{self.spec['spec_id']}|{p}|{t}|exit")[:24]), t, summary)
                    if r is not None:
                        exiting.add(p)
                        self.ledger.append("order", bar=str(t), pair=p, action="close", reason=reason, result=r)
            if s is None:
                continue
            e = int(s["entry"])
            if e == 0 or (pos is not None and p not in exiting) or (pos is not None and pos["side"] == e):
                continue
            positions = [OpenPos(k, v["side"], v["units"], v["notional_jpy"])
                         for k, v in self.broker.positions.items() if k not in exiting]
            positions += [OpenPos(o["pair"], o["side"], o["units"], o["units"] * conv[PAIRS[o["pair"]]["base"]])
                          for o in self.broker.pending if o["reason"] == "entry"]
            self.rstate.positions = positions
            prev = self.mgmt.get(p, {}).get("last_bar")
            age = 0.0
            if prev:
                age = (t - pd.Timestamp(prev)) / pd.Timedelta(hours=1) - 1
                if t.weekday() == 6 or (t.weekday() == 0 and age > 40):
                    age = 0.0
            if is_latest and market_open(now):
                age = max(age, (now - (t + pd.Timedelta(hours=1))) / pd.Timedelta(hours=1))
            data_ok = all(isinstance(v, float) and math.isfinite(v) for k2, v in q.items() if k2 != "spread_med")
            price = q["ask_c"] if e > 0 else q["bid_c"]
            qj, bj = conv[PAIRS[p]["quote"]], conv[PAIRS[p]["base"]]
            dec = self.risk.check_entry(self.rstate, p, e, price, float(s["sl_dist"]), qj, bj,
                                        q["spread_obs_pips"], q["spread_med"], bar_age_hours=max(0.0, age),
                                        data_ok=data_ok)
            if not dec.approved:
                summary["rejections"] += 1
                self.ledger.append("risk_reject", bar=str(t), pair=p, side=e, reasons=dec.reasons)
                continue
            cid = sha(f"{self.spec['spec_id']}|{p}|{t}|{e}|entry")[:24]
            if cid in self.broker.known_client_ids():
                continue
            req = OrderRequest(cid, p, e, dec.units, sl=float(s["sl_dist"]),
                               tp=float(s["tp_dist"]) if s["tp_dist"] == s["tp_dist"] else None,
                               trail=float(s["trail_dist"]) if s["trail_dist"] == s["trail_dist"] else None,
                               max_bars=float(s["max_bars"]) if s["max_bars"] == s["max_bars"] else None,
                               decided_at=str(t), meta={"risk_jpy": dec.units * float(s["sl_dist"]) * qj,
                                                        "checks": dec.checks.get("sizing")})
            r = self._safe(lambda: self.broker.place_order(req), t, summary)
            if r is not None:
                summary["orders"] += 1
                self.ledger.append("order", bar=str(t), pair=p, action="open", side=e, units=dec.units,
                                   client_order_id=cid, result=r)

    def _safe(self, fn, t, summary):
        try:
            r = fn()
            self.st["consecutive_order_errors"] = 0
            return r
        except BrokerDisconnected:
            raise
        except BrokerError as e:
            summary["errors"] += 1
            self.st["consecutive_order_errors"] += 1
            self.ledger.append("order_error", bar=str(t), error=str(e))
            if self.st["consecutive_order_errors"] >= 3:
                self._kill(t, "3 consecutive order errors")
            return None

    # ------------------------------------------------------------------ 保存
    def _save(self):
        self.st["risk_state"] = self.rstate.to_dict()
        self.st["broker_state"] = self.broker.to_state() if hasattr(self.broker, "to_state") else {}
        self.st["mgmt"] = self.mgmt
        self.state_path.write_text(json.dumps(self.st, indent=2, ensure_ascii=False, default=str))

    def _append_equity(self, rows):
        path = self.dir / "equity.csv"
        new = not path.exists()
        with path.open("a", newline="") as f:
            w = csv.writer(f)
            if new:
                w.writerow(["bar", "equity", "cash", "gross_notional", "open_positions"])
            w.writerows(rows)

    def _write_trades(self):
        trades = [r["trade"] for r in self.ledger.records("fill") if r.get("kind") == "close" and r.get("trade")]
        pd.DataFrame(trades).to_csv(self.dir / "trades.csv", index=False)


def load_paper(spec_id: str, root=None) -> dict:
    d = (root or PAPER_DIR) / spec_id
    eq = pd.read_csv(d / "equity.csv") if (d / "equity.csv").exists() else pd.DataFrame()
    tr = pd.read_csv(d / "trades.csv") if (d / "trades.csv").exists() and (d / "trades.csv").stat().st_size > 1 else pd.DataFrame()
    st = json.loads((d / "state.json").read_text()) if (d / "state.json").exists() else {}
    if len(eq):
        s = pd.Series(eq["equity"].values, index=pd.to_datetime(eq["bar"], utc=True))
        s = s[~s.index.duplicated(keep="last")]
    else:
        s = pd.Series(dtype=float)
    return {"equity": s, "trades": tr, "state": st}
