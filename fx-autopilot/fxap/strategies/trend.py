"""A. Trend Following（EMA クロス + ADX / Donchian ブレイクアウト / 時系列モメンタム）。"""
from __future__ import annotations

import numpy as np

from .. import features as F
from .base import Strategy, cross_dn, cross_up, register


@register
class EmaCrossAdx(Strategy):
    name = "trend_ema_adx"
    family = "A_trend"
    grid = {"fast": [20, 50], "slow": [100, 200], "adx_min": [0, 20]}

    def generate(self, df, pair):
        p = self.params
        if p["fast"] >= p["slow"]:
            return self.empty(df.index)
        m = F.mid(df)
        f, s = F.ema(m["c"], p["fast"]), F.ema(m["c"], p["slow"])
        a = F.atr(m, 14)
        ad = F.adx(m, 14)
        ok = (ad >= p["adx_min"]) if p["adx_min"] > 0 else (ad == ad)
        out = self.empty(df.index)
        out.loc[cross_up(f, s) & ok, "entry"] = 1
        out.loc[cross_dn(f, s) & ok, "entry"] = -1
        out["exit_long"] = f < s
        out["exit_short"] = f > s
        out["sl_dist"] = 2.5 * a
        out["trail_dist"] = 4.0 * a
        out.loc[a.isna() | s.isna(), "entry"] = 0
        return out


@register
class DonchianBreakout(Strategy):
    name = "trend_donchian"
    family = "A_trend"
    grid = {"n": [48, 120, 240], "sl_atr": [3.0, 5.0]}

    def generate(self, df, pair):
        p = self.params
        m = F.mid(df)
        hi, lo = F.donchian_prev(m, p["n"])
        xhi, xlo = F.donchian_prev(m, max(10, p["n"] // 2))
        a = F.atr(m, 24)
        out = self.empty(df.index)
        up = (m["c"] > hi) & (m["c"].shift(1) <= hi.shift(1))
        dn = (m["c"] < lo) & (m["c"].shift(1) >= lo.shift(1))
        out.loc[up, "entry"] = 1
        out.loc[dn, "entry"] = -1
        out["exit_long"] = m["c"] < xlo
        out["exit_short"] = m["c"] > xhi
        out["sl_dist"] = p["sl_atr"] * a
        out.loc[a.isna() | hi.isna(), "entry"] = 0
        return out


@register
class TsMomentum(Strategy):
    """時系列モメンタム: 過去 L 時間のリターン（ボラ正規化）の符号。週1回（月曜 08:00 UTC）判断。"""
    name = "trend_tsmom"
    family = "A_trend"
    grid = {"lookback": [120, 480], "z_min": [0.5, 1.0]}

    def generate(self, df, pair):
        p = self.params
        m = F.mid(df)
        r = np.log(m["c"]).diff()
        vol = r.rolling(480, min_periods=240).std()
        mom = np.log(m["c"] / m["c"].shift(p["lookback"])) / (vol * np.sqrt(p["lookback"]))
        a = F.atr(m, 24)
        dec = (df.index.weekday == 0) & (df.index.hour == 8)
        out = self.empty(df.index)
        out.loc[dec & (mom > p["z_min"]), "entry"] = 1
        out.loc[dec & (mom < -p["z_min"]), "entry"] = -1
        out["exit_long"] = dec & (mom < 0)
        out["exit_short"] = dec & (mom > 0)
        out["sl_dist"] = 6 * a
        out["max_bars"] = 120 * 2
        out.loc[a.isna() | mom.isna(), "entry"] = 0
        return out
