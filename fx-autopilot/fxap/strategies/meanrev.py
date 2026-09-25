"""B. Mean Reversion（RSI + Bollinger / ボラ正規化した短期乖離）。"""
from __future__ import annotations

import numpy as np

from .. import features as F
from .base import Strategy, register


@register
class RsiBollinger(Strategy):
    name = "mr_rsi_bb"
    family = "B_meanrev"
    grid = {"rsi_lo": [25, 30], "bb_k": [2.0, 2.5]}

    def generate(self, df, pair):
        p = self.params
        m = F.mid(df)
        r = F.rsi(m["c"], 14)
        mid_b, up, lo = F.bollinger(m["c"], 20, p["bb_k"])
        a = F.atr(m, 14)
        ad = F.adx(m, 14)
        rng = ad < 25                                   # トレンドが弱いときだけ逆張り
        out = self.empty(df.index)
        out.loc[rng & (r < p["rsi_lo"]) & (m["c"] < lo), "entry"] = 1
        out.loc[rng & (r > 100 - p["rsi_lo"]) & (m["c"] > up), "entry"] = -1
        out["exit_long"] = m["c"] >= mid_b
        out["exit_short"] = m["c"] <= mid_b
        out["sl_dist"] = 2.0 * a
        out["max_bars"] = 24
        out.loc[a.isna() | mid_b.isna() | ad.isna(), "entry"] = 0
        return out


@register
class ZScoreReversion(Strategy):
    """EMA からの乖離をボラで正規化した z が閾値を超えたら逆張り。z が 0 付近で決済。"""
    name = "mr_zscore"
    family = "B_meanrev"
    grid = {"n": [24, 72], "z": [2.0, 2.5]}

    def generate(self, df, pair):
        p = self.params
        m = F.mid(df)
        base = F.ema(m["c"], p["n"])
        sd = (m["c"] - base).rolling(p["n"] * 5, min_periods=p["n"] * 2).std()
        z = (m["c"] - base) / sd
        a = F.atr(m, 14)
        out = self.empty(df.index)
        out.loc[(z < -p["z"]) & (z.shift(1) >= -p["z"]), "entry"] = 1
        out.loc[(z > p["z"]) & (z.shift(1) <= p["z"]), "entry"] = -1
        out["exit_long"] = z >= 0
        out["exit_short"] = z <= 0
        out["sl_dist"] = 2.5 * a
        out["max_bars"] = p["n"]
        out.loc[a.isna() | z.isna() | ~np.isfinite(z), "entry"] = 0
        return out
