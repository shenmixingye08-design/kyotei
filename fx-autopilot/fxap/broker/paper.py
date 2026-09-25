"""PaperBroker: 内部 PAPER 口座シミュレータ（実資金・実注文なし）。

約定規則は backtest.py と同一（テスト test_paper_backtest_parity で一致を確認）:
  成行注文は受け付けた次の足の始値（実効 bid/ask + スリッページ）で約定
  SL/TP は足中の高安で判定（SL 優先）、窓開けは始値で約定、TP は指値（スリッページなし）
  スワップは 21:00 UTC の足で計上（水曜 3 日分）
"""
from __future__ import annotations

import math

import numpy as np

from .. import swap as swapm
from ..common import PAIRS
from ..costs import CostProfile, commission_jpy
from .base import BrokerAdapter, BrokerDisconnected, BrokerError, Fill, OrderRequest


class PaperBroker(BrokerAdapter):
    name = "paper_sim"
    is_paper = True

    def __init__(self, cost: CostProfile, initial_equity: float = 1_000_000.0, state: dict | None = None):
        self.cost = cost
        s = state or {}
        self.cash = float(s.get("cash", initial_equity))
        self.positions: dict = s.get("positions", {})       # pair -> dict
        self.pending: list = s.get("pending", [])           # 未約定の成行注文（dict）
        self.client_ids: set = set(s.get("client_ids", []))
        self.fills: list = []
        self.connected = True
        self.fail_next = s.get("fail_next", 0)              # テスト用: 次の n 回の発注を失敗させる
        self.quotes: dict = {}                              # pair -> 最新の実効気配（足の終値）
        self.conv: dict = {}

    # ------------------------------------------------------------------ 状態
    def to_state(self) -> dict:
        return {"cash": self.cash, "positions": self.positions, "pending": self.pending,
                "client_ids": sorted(self.client_ids)}

    def is_connected(self) -> bool:
        return self.connected

    def _need(self):
        if not self.connected:
            raise BrokerDisconnected("paper broker disconnected")

    def known_client_ids(self) -> set:
        return set(self.client_ids)

    def get_account(self) -> dict:
        self._need()
        unreal = sum(self._unreal(p) for p in self.positions)
        gross = sum(v["units"] * self.conv.get(PAIRS[p]["base"], np.nan) for p, v in self.positions.items())
        eq = self.cash + unreal
        return {"cash": self.cash, "unrealized": unreal, "equity": eq, "gross_notional": gross,
                "leverage": gross / eq if eq > 0 else None, "available": eq - gross / 25.0}

    def get_positions(self) -> list[dict]:
        self._need()
        return [{"pair": p, **v} for p, v in self.positions.items()]

    def get_quote(self, pair: str) -> dict:
        self._need()
        return self.quotes.get(pair, {})

    def get_fills(self, since=None) -> list[Fill]:
        return list(self.fills)

    # ------------------------------------------------------------------ 注文
    def place_order(self, req: OrderRequest) -> dict:
        self._need()
        if req.client_order_id in self.client_ids:
            return {"status": "duplicate", "client_order_id": req.client_order_id}
        if self.fail_next > 0:
            self.fail_next -= 1
            raise BrokerError("simulated order failure")
        if req.reason == "entry":
            if req.sl is None or not math.isfinite(req.sl) or req.sl <= 0:
                return {"status": "rejected", "reason": "stop_loss_required"}
            if req.units <= 0:
                return {"status": "rejected", "reason": "units"}
        self.client_ids.add(req.client_order_id)
        self.pending.append(req.to_dict())
        return {"status": "accepted", "client_order_id": req.client_order_id}

    def close_position(self, pair: str, reason: str, client_order_id: str) -> dict:
        self._need()
        if pair not in self.positions:
            return {"status": "no_position"}
        if client_order_id in self.client_ids:
            return {"status": "duplicate"}
        self.client_ids.add(client_order_id)
        pos = self.positions[pair]
        self.pending.append(OrderRequest(client_order_id, pair, -pos["side"], pos["units"], reason=f"exit:{reason}").to_dict())
        return {"status": "accepted"}

    def cancel_pending_entries(self) -> int:
        n = sum(1 for o in self.pending if o["reason"] == "entry")
        self.pending = [o for o in self.pending if o["reason"] != "entry"]
        return n

    def modify_stop(self, pair: str, new_sl_price: float) -> dict:
        self._need()
        if pair not in self.positions:
            return {"status": "no_position"}
        pos = self.positions[pair]
        old = pos["sl"]
        pos["sl"] = max(old, new_sl_price) if pos["side"] > 0 else min(old, new_sl_price)   # SL は不利方向に動かさない
        return {"status": "ok", "sl": pos["sl"]}

    # ------------------------------------------------------------------ シミュレーション時計（PaperEngine が呼ぶ）
    def _q2j(self, pair):
        return self.conv[PAIRS[pair]["quote"]]

    def _b2j(self, pair):
        return self.conv[PAIRS[pair]["base"]]

    def _unreal(self, pair):
        pos = self.positions[pair]
        q = self.quotes.get(pair)
        if not q:
            return 0.0
        px = q["bid_c"] if pos["side"] > 0 else q["ask_c"]
        return (px - pos["entry_price"]) * pos["side"] * pos["units"] * self._q2j(pair)

    def _close(self, pair, t, q, price, reason, slip_pips) -> Fill:
        pos = self.positions.pop(pair)
        pip = PAIRS[pair]["pip"]
        slip = slip_pips * pip
        fill = price - pos["side"] * slip
        qj = self._q2j(pair)
        pnl_price = (fill - pos["entry_price"]) * pos["side"] * pos["units"] * qj
        pos["cost_spread"] += (q["ask_o"] - q["bid_o"]) / 2 * pos["units"] * qj
        pos["cost_slip"] += slip * pos["units"] * qj
        comm = commission_jpy(pos["units"] * self._b2j(pair), self.conv.get("USD", 150.0), self.cost)
        pos["commission"] += comm
        self.cash += pnl_price - comm
        net = pnl_price - pos["commission"] + pos["swap"]
        trade = {"pair": pair, "side": pos["side"], "entry_time": pos["entry_time"], "exit_time": str(t),
                 "entry_price": pos["entry_price"], "exit_price": fill, "units": pos["units"],
                 "notional_jpy": pos["notional_jpy"], "pnl_jpy": net,
                 "gross_mid_pnl_jpy": net + pos["cost_spread"] + pos["cost_slip"] + pos["commission"] - pos["swap"],
                 "cost_spread_jpy": pos["cost_spread"], "cost_slip_jpy": pos["cost_slip"],
                 "commission_jpy": pos["commission"], "swap_jpy": pos["swap"], "risk_jpy": pos["risk_jpy"],
                 "r_multiple": net / pos["risk_jpy"] if pos["risk_jpy"] > 0 else None,
                 "equity_at_entry": pos["equity_at_entry"], "ret_on_equity": net / pos["equity_at_entry"],
                 "bars": pos["bars"], "exit_reason": reason}
        f = Fill(pos["client_order_id"] + ":close", pair, -pos["side"], pos["units"], fill, str(t), "close", reason,
                 realized_pnl_jpy=net, commission_jpy=comm, trade=trade)
        self.fills.append(f)
        return f

    def on_bar_open(self, t, quotes: dict, conv: dict, equity_now: float) -> list[Fill]:
        """足の始値: 約定待ちの成行注文を処理（決済 → 新規の順）。"""
        self.conv = conv
        out = []
        c = self.cost
        rest = []
        for o in sorted(self.pending, key=lambda o: 0 if o["reason"].startswith("exit") else 1):
            p = o["pair"]
            q = quotes.get(p)
            if q is None:
                rest.append(o)              # そのペアの足が無い → 次の足まで待つ
                continue
            pip = PAIRS[p]["pip"]
            if o["reason"].startswith("exit"):
                if p in self.positions:
                    pos = self.positions[p]
                    px = q["bid_o"] if pos["side"] > 0 else q["ask_o"]
                    out.append(self._close(p, t, q, px, o["reason"].split(":", 1)[1], c.slippage_pips_market))
                continue
            if p in self.positions:
                continue                    # 既に建玉あり（重複新規は捨てる）
            side = o["side"]
            raw = q["ask_o"] if side > 0 else q["bid_o"]
            fill = raw + side * c.slippage_pips_market * pip
            qj, bj = self._q2j(p), self._b2j(p)
            notional = o["units"] * bj
            comm = commission_jpy(notional, conv.get("USD", 150.0), c)
            self.cash -= comm
            tp = o["tp"]
            self.positions[p] = {
                "client_order_id": o["client_order_id"], "side": side, "units": o["units"], "entry_time": str(t),
                "entry_price": fill, "sl": fill - side * o["sl"],
                "tp": (fill + side * tp) if tp is not None and math.isfinite(tp) else None,
                "trail": o["trail"] if o["trail"] is not None and math.isfinite(o["trail"]) else None,
                "max_bars": o["max_bars"] if o["max_bars"] is not None and math.isfinite(o["max_bars"]) else None,
                "bars": 0, "best_close": q["mid_o"], "cost_spread": abs(raw - q["mid_o"]) * o["units"] * qj,
                "cost_slip": c.slippage_pips_market * pip * o["units"] * qj, "commission": comm, "swap": 0.0,
                "equity_at_entry": equity_now, "risk_jpy": o["meta"].get("risk_jpy", 0.0), "notional_jpy": notional}
            out.append(Fill(o["client_order_id"], p, side, o["units"], fill, str(t), "open", "entry",
                            cost_spread_jpy=self.positions[p]["cost_spread"], commission_jpy=comm))
        self.pending = rest
        self.fills += [f for f in out if f.kind == "open"]
        return out

    def on_bar_range(self, t, quotes: dict) -> list[Fill]:
        """足中: SL / TP（SL 優先・窓開けは始値）とスワップ。"""
        out = []
        c = self.cost
        for p in list(self.positions):
            q = quotes.get(p)
            if q is None:
                continue
            pos = self.positions[p]
            fresh = pos["entry_time"] == str(t)
            if pos["side"] > 0:
                if q["bid_o"] <= pos["sl"] and not fresh:
                    out.append(self._close(p, t, q, q["bid_o"], "gap_sl", c.slippage_pips_stop))
                elif q["bid_l"] <= pos["sl"]:
                    out.append(self._close(p, t, q, pos["sl"], "sl", c.slippage_pips_stop))
                elif pos["tp"] is not None and q["bid_h"] >= pos["tp"]:
                    out.append(self._close(p, t, q, pos["tp"], "tp", 0.0))
            else:
                if q["ask_o"] >= pos["sl"] and not fresh:
                    out.append(self._close(p, t, q, q["ask_o"], "gap_sl", c.slippage_pips_stop))
                elif q["ask_h"] >= pos["sl"]:
                    out.append(self._close(p, t, q, pos["sl"], "sl", c.slippage_pips_stop))
                elif pos["tp"] is not None and q["ask_l"] <= pos["tp"]:
                    out.append(self._close(p, t, q, pos["tp"], "tp", 0.0))
            if p in self.positions:
                days = swapm.rollover_days(t)
                if days:
                    b, qc = PAIRS[p]["base"], PAIRS[p]["quote"]
                    amt = pos["units"] * self._b2j(p) * swapm.nightly_rate(b, qc, pos["side"], t, c.swap_markup_annual) * days
                    pos["swap"] += amt
                    self.cash += amt
        return out

    def on_bar_close(self, t, quotes: dict, conv: dict):
        self.conv = conv
        for p, q in quotes.items():
            self.quotes[p] = q
