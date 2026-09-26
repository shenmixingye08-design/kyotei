"""V9 候補（config/research_plan_v9.yaml）: 複数期間の時系列モメンタム（Hurst, Ooi & Pedersen 2017）。

s = (sign(r21) + sign(r63) + sign(r252)) / 3（日足終値の対数リターン）
agree=all      : |s| = 1（3 期間すべて一致）のときだけ s の向きに保有、それ以外は手仕舞い
agree=majority : 常に s の符号（多数決）の向きに保有
毎日（日足確定時）判断。sizing = vol_target、SL = 日足 ATR20 × 4。
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .base import register
from .v2 import _V2, _on_h1, dframe
from .v3 import _finish


@register
class V9TSMomMulti(_V2):
    name = "v9_tsmom_multi"
    family = "trend_multi"
    version = "v9"
    grid = {"agree": ["all", "majority"]}

    def risk_overrides(self) -> dict:
        return {"sizing": "vol_target"}

    def generate(self, df, pair):
        dm = dframe(df)
        c = dm["d"]["c"]
        s = sum(np.sign(np.log(c / c.shift(L))) for L in (21, 63, 252)) / 3
        s = s.where(c.shift(252).notna())
        if self.params["agree"] == "all":
            dirn = np.sign(s).where(s.abs() > 0.99, 0.0).where(s.notna())
        else:
            dirn = np.sign(s)
        h = _on_h1(dirn, dm)
        dec = dm["is_close"] & h.notna()
        o = self.empty(df.index)
        o["entry"] = np.where(dec, h.fillna(0), 0).astype(int)
        o["exit_long"] = dec & (h <= 0)
        o["exit_short"] = dec & (h >= 0)
        return _finish(o, dm)
