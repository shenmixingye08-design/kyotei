"""執行コストモデル（Bid/Ask・スプレッド・スリッページ・手数料・スワップ・執行遅延）。

- 価格は Dukascopy の bid/ask 実測値。業者の「原則固定」スプレッドがそれより広い場合は広い方を使う
  （実効スプレッド = max(実測, 固定) × spread_mult）
- 買いは ask、売りは bid で約定。成行・逆指値（SL）は不利方向にスリッページを加える。利確（TP）は指値なので加えない
- 執行遅延: 足 i の終値で判断 → 足 i+1 の始値で約定（最低 1 本の遅延。backtest.py が保証）
- 手数料: 想定元本 × commission_bp（最低 commission_min_usd）
Mid 価格だけで損益を判定することはしない。
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from .common import PAIRS, settings
from .features import mid


@dataclass
class CostProfile:
    name: str
    fixed_spread_pips: dict
    slippage_pips_market: float
    slippage_pips_stop: float
    commission_bp: float
    commission_min_usd: float
    swap_markup_annual: float
    spread_mult: float = 1.0

    @classmethod
    def load(cls, name: str | None = None, cfg: dict | None = None) -> "CostProfile":
        c = (cfg or settings())["costs"]
        name = name or c["default_profile"]
        p = dict(c["profiles"][name])
        return cls(name=name, **p)


def effective_quotes(df: pd.DataFrame, pair: str, prof: CostProfile) -> pd.DataFrame:
    """実効 bid/ask の OHLC（numpy で高速に参照するための列）。"""
    pip = PAIRS[pair]["pip"]
    m = mid(df)
    s_o = (df["ask_o"] - df["bid_o"]).clip(lower=0)
    s_c = (df["ask_c"] - df["bid_c"]).clip(lower=0)
    fixed = prof.fixed_spread_pips.get(pair, 0.0) * pip
    so = np.maximum(s_o * prof.spread_mult, fixed)
    sc = np.maximum(s_c * prof.spread_mult, fixed)
    sb = np.maximum(so, sc)   # 足中の高安は始値・終値スプレッドの大きい方で保守的に
    return pd.DataFrame({
        "mid_o": m["o"], "mid_h": m["h"], "mid_l": m["l"], "mid_c": m["c"],
        "bid_o": m["o"] - so / 2, "ask_o": m["o"] + so / 2,
        "bid_h": m["h"] - sb / 2, "ask_h": m["h"] + sb / 2,
        "bid_l": m["l"] - sb / 2, "ask_l": m["l"] + sb / 2,
        "bid_c": m["c"] - sc / 2, "ask_c": m["c"] + sc / 2,
        "spread_obs_pips": s_c / pip,          # Risk Engine の異常スプレッド判定は実測値で行う
        "spread_eff_pips": sc / pip,
    }, index=df.index)


def commission_jpy(notional_jpy: float, usdjpy: float, prof: CostProfile) -> float:
    if prof.commission_bp <= 0 and prof.commission_min_usd <= 0:
        return 0.0
    c = notional_jpy * prof.commission_bp / 1e4
    return max(c, prof.commission_min_usd * usdjpy)
