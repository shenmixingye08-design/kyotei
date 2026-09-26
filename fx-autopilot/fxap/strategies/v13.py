"""V13 候補（config/research_plan_v13.yaml）: 金利モメンタム（金融政策の方向）。

rate_mom_c = 3 か月物市場金利の 6 か月変化（v7 の carry と同じラグ: 月中 - 31 日時点、さらに公表遅れ 1 か月）。
利上げ方向の通貨は買われ、利下げ方向の通貨は売られやすい（金利水準ではなく「変化」を見る）。
8 通貨で横断 z → 通貨スコア（factors に応じて carry と平均）→ ペアのスコア = S_base - S_quote、|スコア| > threshold で保有。
判断は月 1 回、sizing = vol_target、SL = 日足 ATR20 × 4（v7 と同じ枠組み）。
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .. import swap as swapm
from ..common import PAIRS
from .base import register
from .v2 import _on_h1, dframe
from .v3 import _finish
from .v7 import CCY8, _V7XS, _xs_z, currency_scores

MOM_MONTHS = 6


def rate_momentum(index: pd.DatetimeIndex) -> pd.DataFrame:
    naive = index.tz_convert(None) if index.tz is not None else index
    months = pd.Series(naive.to_period("M"), index=index)
    vals = {}
    for mo in months.unique():
        t1 = pd.Timestamp(mo.start_time) + pd.Timedelta(days=14) - pd.Timedelta(days=31)
        t0 = t1 - pd.DateOffset(months=MOM_MONTHS)
        vals[mo] = [swapm.rate(c, t1) - swapm.rate(c, t0) for c in CCY8]
    return pd.DataFrame([vals[m] for m in months], index=index, columns=CCY8)


class _V13(_V7XS):
    version = "v13"
    family = "rate_momentum"
    use_carry = False

    def scores(self, data):
        base = currency_scores(data, ("carry",))          # 日足ラベル index（carry の z）
        rm = _xs_z(rate_momentum(base.index))
        if not self.use_carry:
            return rm
        stack = np.stack([base.to_numpy(dtype=float), rm.to_numpy(dtype=float)])
        with np.errstate(all="ignore"):
            return pd.DataFrame(np.nanmean(stack, axis=0), index=base.index, columns=CCY8)

    def generate_all(self, data, pairs):
        S = self.scores(data)
        th = self.params["threshold"]
        out = {}
        for p in pairs:
            df = data[p]
            dm = dframe(df)
            b, q = PAIRS[p]["base"], PAIRS[p]["quote"]
            sc = S[b] - S[q]
            dirn = np.sign(sc).where(sc.abs() > th, 0.0).where(sc.notna())
            lab = pd.DatetimeIndex(dm["d"]["label"]).normalize()
            h = _on_h1(pd.Series(dirn.reindex(lab).to_numpy(), index=dm["d"].index), dm)
            dec = self.monthly_mask(dm) & h.notna()
            o = self.empty(df.index)
            o["entry"] = np.where(dec, h.fillna(0), 0).astype(int)
            o["exit_long"] = dec & (h <= 0)
            o["exit_short"] = dec & (h >= 0)
            out[p] = _finish(o, dm)
        return out


@register
class V13RateMom(_V13):
    name = "v13_ratemom"
    use_carry = False


@register
class V13CarryRateMom(_V13):
    name = "v13_carry_ratemom"
    use_carry = True
