"""決定論的 Risk Engine（バックテスト・PAPER 共通）。

戦略・ML が何を出しても、Risk Engine が NO なら注文は作られない。数量は Risk Engine が決める（固定ロット禁止）。
  - 1 トレードのリスク = 口座残高 × risk_per_trade（SL 距離から数量を逆算）
  - 最大レバレッジ（総建玉 / 残高）・最大ポジション数・通貨ペアごと 1 建玉（ナンピン・倍プッシュ禁止）
  - 通貨別ネット建玉（相関エクスポージャー。口座通貨 JPY は除く）
  - Daily / Weekly Loss Limit（新規停止）・Maximum Drawdown（全決済 + Kill Switch）
  - 異常スプレッド・データ欠損 / 古いデータ・API 切断 → 新規禁止
  - Kill Switch は自動で入るが、解除は本人のみ
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

import pandas as pd

from .common import PAIRS, settings


@dataclass
class RiskConfig:
    risk_per_trade: float = 0.005
    max_leverage: float = 5.0
    max_open_positions: int = 3
    max_positions_per_pair: int = 1
    max_currency_exposure: float = 3.0
    daily_loss_limit: float = 0.02
    weekly_loss_limit: float = 0.04
    max_drawdown: float = 0.15
    spread_max_mult: float = 3.0
    max_bar_staleness_hours: float = 3
    min_units: int = 1000
    lot_step: int = 1000

    @classmethod
    def load(cls, overrides: dict | None = None, cfg: dict | None = None) -> "RiskConfig":
        d = dict((cfg or settings())["risk"])
        d.update(overrides or {})
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


@dataclass
class OpenPos:
    pair: str
    side: int
    units: float
    notional_jpy: float


@dataclass
class RiskState:
    equity: float
    hwm: float
    day_key: str = ""
    week_key: str = ""
    day_start_equity: float = 0.0
    week_start_equity: float = 0.0
    kill_switch: bool = False
    kill_reason: str = ""
    positions: list = field(default_factory=list)       # list[OpenPos]（約定済み + 約定待ち）
    broker_connected: bool = True

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if k != "positions"}


@dataclass
class Decision:
    approved: bool
    units: float = 0.0
    reasons: list = field(default_factory=list)
    checks: dict = field(default_factory=dict)


class RiskEngine:
    def __init__(self, cfg: RiskConfig):
        self.cfg = cfg

    # ------------------------------------------------------------ 毎足（全ペア処理後）
    def on_bar(self, st: RiskState, t: pd.Timestamp, equity: float) -> list[str]:
        """戻り値: 実行すべきアクション（'flatten_kill'）。"""
        st.equity = equity
        st.hwm = max(st.hwm, equity)
        dk = t.strftime("%Y-%m-%d")
        iso = t.isocalendar()
        wk = f"{iso[0]}-W{iso[1]:02d}"
        if dk != st.day_key:
            st.day_key, st.day_start_equity = dk, equity
        if wk != st.week_key:
            st.week_key, st.week_start_equity = wk, equity
        actions = []
        dd = 1 - equity / st.hwm if st.hwm > 0 else 0
        if dd >= self.cfg.max_drawdown and not st.kill_switch:
            st.kill_switch, st.kill_reason = True, f"max_drawdown {dd:.1%} at {t}"
            actions.append("flatten_kill")
        if equity <= 0 and not st.kill_switch:
            st.kill_switch, st.kill_reason = True, "equity <= 0"
            actions.append("flatten_kill")
        return actions

    def daily_blocked(self, st: RiskState) -> bool:
        return st.day_start_equity > 0 and st.equity / st.day_start_equity - 1 <= -self.cfg.daily_loss_limit

    def weekly_blocked(self, st: RiskState) -> bool:
        return st.week_start_equity > 0 and st.equity / st.week_start_equity - 1 <= -self.cfg.weekly_loss_limit

    # ------------------------------------------------------------ 新規注文
    def check_entry(self, st: RiskState, pair: str, side: int, price: float, stop_dist: float,
                    quote_jpy: float, base_jpy: float, spread_obs: float, spread_median: float,
                    bar_age_hours: float = 0.0, data_ok: bool = True) -> Decision:
        c = self.cfg
        checks, reasons = {}, []

        def chk(name, ok, val=None):
            checks[name] = {"ok": bool(ok), "value": val}
            if not ok:
                reasons.append(name)

        chk("kill_switch_off", not st.kill_switch, st.kill_reason)
        chk("broker_connected", st.broker_connected)
        chk("data_ok", data_ok and all(math.isfinite(x) for x in (price, stop_dist, quote_jpy, base_jpy)))
        chk("data_fresh", bar_age_hours <= c.max_bar_staleness_hours, round(bar_age_hours, 2))
        sp_ok = math.isfinite(spread_obs) and (not math.isfinite(spread_median) or spread_median <= 0
                                               or spread_obs <= c.spread_max_mult * spread_median)
        chk("spread_normal", sp_ok, (round(spread_obs, 3), round(spread_median, 3) if math.isfinite(spread_median) else None))
        chk("daily_loss_limit", not self.daily_blocked(st))
        chk("weekly_loss_limit", not self.weekly_blocked(st))
        chk("max_open_positions", len(st.positions) < c.max_open_positions, len(st.positions))
        same = [p for p in st.positions if p.pair == pair]
        chk("one_position_per_pair", len(same) < c.max_positions_per_pair, len(same))
        chk("stop_loss_set", math.isfinite(stop_dist) and stop_dist > 0, stop_dist)
        if reasons:
            return Decision(False, 0.0, reasons, checks)

        eq = st.equity
        units = c.risk_per_trade * eq / (stop_dist * quote_jpy)
        # レバレッジ上限
        gross = sum(p.notional_jpy for p in st.positions)
        cap_lev = max(0.0, (c.max_leverage * eq - gross) / base_jpy)
        # 通貨別ネット建玉（JPY 以外）
        exp = self.currency_exposure(st.positions)
        b, q = PAIRS[pair]["base"], PAIRS[pair]["quote"]
        cap_ccy = float("inf")
        for ccy, sign in ((b, side), (q, -side)):
            if ccy == "JPY":
                continue
            cur = exp.get(ccy, 0.0)
            room = c.max_currency_exposure * eq - sign * cur    # 同方向に増える分の余地
            cap_ccy = min(cap_ccy, max(0.0, room) / base_jpy)
        units = min(units, cap_lev, cap_ccy)
        units = math.floor(units / c.lot_step) * c.lot_step
        checks["sizing"] = {"ok": units >= c.min_units, "value": {
            "units": units, "risk_jpy": round(units * stop_dist * quote_jpy, 2),
            "notional_jpy": round(units * base_jpy, 2), "lev_after": round((gross + units * base_jpy) / eq, 3),
            "cap_leverage_units": round(cap_lev), "cap_currency_units": round(cap_ccy) if math.isfinite(cap_ccy) else None}}
        if units < c.min_units:
            return Decision(False, 0.0, ["size_below_minimum"], checks)
        return Decision(True, float(units), [], checks)

    @staticmethod
    def currency_exposure(positions) -> dict:
        exp: dict = {}
        for p in positions:
            b, q = PAIRS[p.pair]["base"], PAIRS[p.pair]["quote"]
            exp[b] = exp.get(b, 0.0) + p.side * p.notional_jpy
            exp[q] = exp.get(q, 0.0) - p.side * p.notional_jpy
        return exp
