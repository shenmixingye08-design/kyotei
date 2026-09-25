"""イベント駆動のバー単位バックテスト（複数ペア同時・Risk Engine 内蔵）。

時系列の約束（未来情報リークの防止）:
  足 i の終値で判断（シグナル・Risk 判定・数量計算）→ 足 i+1 の始値で約定（実効 bid/ask + スリッページ）
  SL/TP は足 i+1 以降の高値・安値で判定。同じ足で SL と TP の両方に触れた場合は SL を先とみなす（保守的）
  始値が SL を越えて窓を開けた場合は始値で約定（SL 価格より不利）
  トレーリングストップは足の終値確定後に更新し、次の足から有効
コスト: スプレッド（実効 bid/ask）・スリッページ・手数料・スワップを損益から控除。Mid 判定はしない。
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from . import swap as swapm
from .common import PAIRS
from .costs import CostProfile, commission_jpy, effective_quotes
from .risk import OpenPos, RiskConfig, RiskEngine, RiskState

SIG_COLS = ["entry", "exit_long", "exit_short", "sl_dist", "tp_dist", "trail_dist", "max_bars"]


def to_jpy_table(data: dict, index: pd.DatetimeIndex) -> pd.DataFrame:
    """各通貨 → JPY の換算レート（mid 終値、過去値の前方補完のみ）。"""
    mids = {p: ((d["bid_c"] + d["ask_c"]) / 2).reindex(index, method="ffill") for p, d in data.items()}
    out = pd.DataFrame(index=index)
    out["JPY"] = 1.0
    if "USDJPY" in mids:
        out["USD"] = mids["USDJPY"]
    for ccy in ("EUR", "GBP", "AUD"):
        if f"{ccy}JPY" in mids:
            out[ccy] = mids[f"{ccy}JPY"]
        elif f"{ccy}USD" in mids and "USD" in out:
            out[ccy] = mids[f"{ccy}USD"] * out["USD"]
    return out


@dataclass
class Position:
    pair: str
    side: int
    units: float
    entry_time: pd.Timestamp
    entry_price: float
    entry_mid: float
    sl: float
    tp: float
    trail_dist: float
    max_bars: float
    bars: int = 0
    best_close: float = float("nan")
    cost_spread: float = 0.0     # JPY
    cost_slip: float = 0.0
    commission: float = 0.0
    swap: float = 0.0
    equity_at_entry: float = 0.0
    risk_jpy: float = 0.0
    notional_jpy: float = 0.0


@dataclass
class Result:
    equity: pd.Series
    trades: pd.DataFrame
    exposure: pd.Series           # 総建玉 / 残高（各足）
    risk_log: list = field(default_factory=list)
    halted_at: str | None = None
    kill_reason: str = ""
    meta: dict = field(default_factory=dict)


def run(data: dict, signals: dict, trade_pairs=None, cost: CostProfile | None = None,
        risk_cfg: RiskConfig | None = None, initial_equity: float = 1_000_000.0,
        start=None, end=None, spread_median_window: int = 500, log_rejections: bool = False) -> Result:
    cost = cost or CostProfile.load()
    risk_cfg = risk_cfg or RiskConfig.load()
    trade_pairs = list(trade_pairs or signals.keys())
    eng = RiskEngine(risk_cfg)

    # ---- 共通タイムライン
    idx = None
    for p in trade_pairs:
        ix = data[p].index
        if start is not None:
            ix = ix[ix >= pd.Timestamp(start, tz="UTC")]
        if end is not None:
            ix = ix[ix <= pd.Timestamp(end, tz="UTC") + pd.Timedelta(hours=23)]
        idx = ix if idx is None else idx.union(ix)
    T = len(idx)
    conv = to_jpy_table(data, idx)
    conv_np = {c: conv[c].to_numpy() for c in conv.columns}

    Q, S, has = {}, {}, {}
    for p in trade_pairs:
        q = effective_quotes(data[p], p, cost)
        q["spread_med"] = q["spread_obs_pips"].rolling(spread_median_window, min_periods=50).median().shift(1)
        q = q.reindex(idx)
        has[p] = q["mid_c"].notna().to_numpy()
        Q[p] = {c: q[c].to_numpy() for c in q.columns}
        s = signals[p].reindex(idx)
        S[p] = {c: (s[c].to_numpy(dtype=float) if c in s else np.full(T, np.nan)) for c in SIG_COLS}
        S[p]["entry"] = np.nan_to_num(S[p]["entry"])
        for c in ("exit_long", "exit_short"):
            S[p][c] = np.nan_to_num(S[p][c]) > 0

    cash = initial_equity
    st = RiskState(equity=initial_equity, hwm=initial_equity)
    positions: dict[str, Position] = {}
    pending_entry: dict[str, tuple] = {}
    pending_exit: dict[str, str] = {}
    last_close = {p: np.nan for p in trade_pairs}
    last_bar_i = {p: -1 for p in trade_pairs}
    trades = []
    eq_arr = np.full(T, np.nan)
    expo_arr = np.zeros(T)
    risk_log = []
    halted_at = None

    def q2j(p, i):
        return conv_np[PAIRS[p]["quote"]][i]

    def b2j(p, i):
        return conv_np[PAIRS[p]["base"]][i]

    def q2j_o(p, i):     # 始値・足中の約定は直前の足の終値で換算（同じ足の終値を使わない）
        return conv_np[PAIRS[p]["quote"]][max(i - 1, 0)]

    def b2j_o(p, i):
        return conv_np[PAIRS[p]["base"]][max(i - 1, 0)]

    def usd_o(i):
        return conv_np["USD"][max(i - 1, 0)] if "USD" in conv_np else 150.0

    def close_pos(p, i, price, reason, slip_pips=0.0):
        nonlocal cash
        pos = positions.pop(p)
        pip = PAIRS[p]["pip"]
        slip = slip_pips * pip
        fill = price - pos.side * slip
        qj = q2j_o(p, i)
        pnl_price = (fill - pos.entry_price) * pos.side * pos.units * qj
        half_spread = (Q[p]["ask_o"][i] - Q[p]["bid_o"][i]) / 2
        pos.cost_spread += half_spread * pos.units * qj
        pos.cost_slip += slip * pos.units * qj
        comm = commission_jpy(pos.units * b2j_o(p, i), usd_o(i), cost)
        pos.commission += comm
        cash += pnl_price - comm          # 建玉時の手数料・スワップは発生時に cash へ反映済み
        net = pnl_price - pos.commission + pos.swap
        trades.append({
            "pair": p, "side": pos.side, "entry_time": pos.entry_time, "exit_time": idx[i],
            "entry_price": pos.entry_price, "exit_price": fill, "units": pos.units,
            "notional_jpy": pos.notional_jpy, "pnl_jpy": net,
            "gross_mid_pnl_jpy": net + pos.cost_spread + pos.cost_slip + pos.commission - pos.swap,
            "cost_spread_jpy": pos.cost_spread, "cost_slip_jpy": pos.cost_slip,
            "commission_jpy": pos.commission, "swap_jpy": pos.swap,
            "risk_jpy": pos.risk_jpy, "r_multiple": net / pos.risk_jpy if pos.risk_jpy > 0 else np.nan,
            "equity_at_entry": pos.equity_at_entry, "ret_on_equity": net / pos.equity_at_entry,
            "bars": pos.bars, "exit_reason": reason,
        })

    for i in range(T):
        t = idx[i]
        # ---------------- 1) 始値: 約定待ちの決済 → 新規
        for p in trade_pairs:
            if not has[p][i]:
                continue
            q = Q[p]
            if p in positions and p in pending_exit:
                pos = positions[p]
                px = q["bid_o"][i] if pos.side > 0 else q["ask_o"][i]
                close_pos(p, i, px, pending_exit.pop(p), cost.slippage_pips_market)
            pending_exit.pop(p, None)
            if p in pending_entry and p not in positions:
                side, units, sl_d, tp_d, tr_d, mb, risk_jpy = pending_entry.pop(p)
                pip = PAIRS[p]["pip"]
                raw = q["ask_o"][i] if side > 0 else q["bid_o"][i]
                fill = raw + side * cost.slippage_pips_market * pip
                qj, bj = q2j_o(p, i), b2j_o(p, i)
                notional = units * bj
                comm = commission_jpy(notional, usd_o(i), cost)
                cash -= comm
                pos = Position(p, side, units, t, fill, q["mid_o"][i],
                               sl=fill - side * sl_d, tp=(fill + side * tp_d) if math.isfinite(tp_d) else np.nan,
                               trail_dist=tr_d, max_bars=mb, best_close=q["mid_o"][i],
                               cost_spread=abs(raw - q["mid_o"][i]) * units * qj,
                               cost_slip=cost.slippage_pips_market * pip * units * qj,
                               commission=comm, equity_at_entry=st.equity, risk_jpy=risk_jpy, notional_jpy=notional)
                positions[p] = pos
            pending_entry.pop(p, None)

        # ---------------- 2) 足中: SL / TP（SL 優先）・スワップ
        for p in list(positions):
            if not has[p][i]:
                continue
            q, pos = Q[p], positions[p]
            pip = PAIRS[p]["pip"]
            if pos.side > 0:
                if q["bid_o"][i] <= pos.sl and pos.entry_time != t:
                    close_pos(p, i, q["bid_o"][i], "gap_sl", cost.slippage_pips_stop)
                elif q["bid_l"][i] <= pos.sl:
                    close_pos(p, i, pos.sl, "sl", cost.slippage_pips_stop)
                elif math.isfinite(pos.tp) and q["bid_h"][i] >= pos.tp:
                    close_pos(p, i, pos.tp, "tp")
            else:
                if q["ask_o"][i] >= pos.sl and pos.entry_time != t:
                    close_pos(p, i, q["ask_o"][i], "gap_sl", cost.slippage_pips_stop)
                elif q["ask_h"][i] >= pos.sl:
                    close_pos(p, i, pos.sl, "sl", cost.slippage_pips_stop)
                elif math.isfinite(pos.tp) and q["ask_l"][i] <= pos.tp:
                    close_pos(p, i, pos.tp, "tp")
            if p in positions:
                days = swapm.rollover_days(t)
                if days:
                    b, qc = PAIRS[p]["base"], PAIRS[p]["quote"]
                    amt = pos.units * b2j_o(p, i) * swapm.nightly_rate(b, qc, pos.side, t, cost.swap_markup_annual) * days
                    pos.swap += amt
                    cash += amt

        # ---------------- 3) 終値: 評価・Risk
        unreal = 0.0
        gross = 0.0
        for p in trade_pairs:
            if has[p][i]:
                last_close[p] = i
        for p, pos in positions.items():
            j = last_close[p]
            px = Q[p]["bid_c"][j] if pos.side > 0 else Q[p]["ask_c"][j]
            unreal += (px - pos.entry_price) * pos.side * pos.units * q2j(p, i)
            gross += pos.units * b2j(p, i)
        equity = cash + unreal
        eq_arr[i] = equity
        expo_arr[i] = gross / equity if equity > 0 else np.nan
        acts = eng.on_bar(st, t, equity)
        if "flatten_kill" in acts and halted_at is None:
            halted_at = str(t)
            for p in list(positions):
                pending_exit[p] = "kill"
            risk_log.append({"t": str(t), "event": "kill_switch", "reason": st.kill_reason})
        if halted_at is not None:
            # Kill Switch 後は新規なし。未決済は次の始値で全決済
            for p in list(positions):
                pending_exit[p] = "kill"
            pending_entry.clear()
            if not positions and i < T - 1:
                eq_arr[i + 1:] = equity
                break
            continue

        # ---------------- 4) 終値: 時間切れ・トレーリング更新・シグナル
        for p in trade_pairs:
            if not has[p][i]:
                continue
            s, q = S[p], Q[p]
            pos = positions.get(p)
            if pos is not None:
                pos.bars += 1
                c = q["mid_c"][i]
                if pos.side > 0:
                    pos.best_close = max(pos.best_close, c)
                else:
                    pos.best_close = min(pos.best_close, c)
                td = s["trail_dist"][i]
                if math.isfinite(pos.trail_dist) and math.isfinite(td) and td > 0:
                    new = pos.best_close - pos.side * td
                    pos.sl = max(pos.sl, new) if pos.side > 0 else min(pos.sl, new)
                if math.isfinite(pos.max_bars) and pos.bars >= pos.max_bars:
                    pending_exit[p] = "time"
                elif (pos.side > 0 and s["exit_long"][i]) or (pos.side < 0 and s["exit_short"][i]):
                    pending_exit[p] = "signal"
                elif s["entry"][i] == -pos.side:
                    pending_exit[p] = "signal"      # 反対シグナルで決済（ドテンは次の足で判断）
            e = int(s["entry"][i])
            if e == 0 or (pos is not None and p not in pending_exit):
                continue
            if pos is not None and pos.side == e:
                continue
            sl_d = s["sl_dist"][i]
            open_after = [OpenPos(x.pair, x.side, x.units, x.notional_jpy)
                          for k, x in positions.items() if k not in pending_exit]
            open_after += [OpenPos(k, v[0], v[1], v[1] * b2j(k, i)) for k, v in pending_entry.items()]
            st.positions = open_after
            price = q["ask_c"][i] if e > 0 else q["bid_c"][i]
            age = 0.0
            if last_bar_i[p] >= 0:
                age = (t - idx[last_bar_i[p]]) / pd.Timedelta(hours=1) - 1
                if t.weekday() == 6 or (t.weekday() == 0 and age > 40):
                    age = 0.0     # 週明けの最初の足（週末ギャップは異常ではない）
            dec = eng.check_entry(st, p, e, price, sl_d, q2j(p, i), b2j(p, i),
                                  q["spread_obs_pips"][i], q["spread_med"][i], bar_age_hours=max(0.0, age))
            if dec.approved:
                pending_entry[p] = (e, dec.units, sl_d, s["tp_dist"][i], s["trail_dist"][i], s["max_bars"][i],
                                    dec.units * sl_d * q2j(p, i))
            elif log_rejections:
                risk_log.append({"t": str(t), "pair": p, "side": e, "reasons": dec.reasons})
        for p in trade_pairs:
            if has[p][i]:
                last_bar_i[p] = i

    # 期末: 未決済は最後の足の終値（実効 bid/ask）で決済して損益に含める
    for p in list(positions):
        j = last_close[p]
        pos = positions[p]
        px = Q[p]["bid_c"][j] if pos.side > 0 else Q[p]["ask_c"][j]
        close_pos(p, j, px, "end", cost.slippage_pips_market)
    if T:
        eq_arr[-1] = cash if halted_at is None or not np.isfinite(eq_arr[-1]) else eq_arr[-1]
    eq = pd.Series(eq_arr, index=idx).ffill()
    tr = pd.DataFrame(trades)
    return Result(equity=eq, trades=tr, exposure=pd.Series(expo_arr, index=idx), risk_log=risk_log,
                  halted_at=halted_at, kill_reason=st.kill_reason,
                  meta={"cost_profile": cost.name, "risk": risk_cfg.__dict__, "initial_equity": initial_equity,
                        "pairs": trade_pairs})
