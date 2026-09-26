"""テスト専用の合成 H1 bid/ask データ（研究結果には絶対に使わない）。"""
from __future__ import annotations

import numpy as np
import pandas as pd

from ..common import PAIRS

START_PRICE = {"USDJPY": 110.0, "EURUSD": 1.15, "EURJPY": 126.5, "GBPUSD": 1.30, "AUDUSD": 0.75,
               "AUDJPY": 82.0, "GBPJPY": 143.0, "NZDUSD": 0.68, "USDCAD": 1.30, "USDCHF": 0.92}


def make(pair: str, n: int = 6000, seed: int = 0, start="2015-01-05", drift=0.0, vol=0.0012,
         spread_pips: float = 0.3) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    idx = pd.date_range(start, periods=int(n * 1.5), freq="1h", tz="UTC")
    wd = idx.weekday
    idx = idx[(wd < 5) & ~((wd == 4) & (idx.hour >= 21))][:n]
    r = rng.normal(drift, vol, n)
    mid_c = START_PRICE[pair] * np.exp(np.cumsum(r))
    mid_o = np.r_[START_PRICE[pair], mid_c[:-1]]
    wig = np.abs(rng.normal(0, vol * 0.6, n)) * mid_c
    mid_h = np.maximum(mid_o, mid_c) + wig
    mid_l = np.minimum(mid_o, mid_c) - wig
    s = spread_pips * PAIRS[pair]["pip"] * (1 + rng.exponential(0.3, n))
    df = pd.DataFrame({
        "bid_o": mid_o - s / 2, "bid_h": mid_h - s / 2, "bid_l": mid_l - s / 2, "bid_c": mid_c - s / 2,
        "ask_o": mid_o + s / 2, "ask_h": mid_h + s / 2, "ask_l": mid_l + s / 2, "ask_c": mid_c + s / 2,
        "volume": rng.uniform(100, 1000, n),
    }, index=idx)
    return df


def make_all(pairs=("USDJPY", "EURUSD", "EURJPY", "GBPUSD", "AUDUSD"), n=6000, seed=0) -> dict:
    return {p: make(p, n=n, seed=seed + i) for i, p in enumerate(pairs)}
