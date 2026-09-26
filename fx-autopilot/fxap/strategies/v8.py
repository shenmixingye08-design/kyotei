"""V8 候補（config/research_plan_v8.yaml）: ドル・キャリー（Lustig, Roussanov & Verdelhan 2014）。

dollar_carry(t) = 外国 7 通貨（EUR JPY GBP AUD NZD CAD CHF）の短期金利の平均 - 米国の短期金利
  （市場金利 FRED/OECD 3 か月物。v7 と同じく月中 - 31 日時点の値 + 公表遅れ 1 か月）
rule=carry           : dollar_carry > 0 なら外貨バスケット買い（7 ペアすべてドル売り方向）、< 0 ならドル買い
rule=carry_and_trend : 上に加えて、ドルバスケットの 126 日トレンド（7 本の z126 の平均）が同じ向きのときだけ保有、違えば手仕舞い
判断は月 1 回（月初の最初の日足確定時）、sizing = vol_target、SL = 日足 ATR20 × 4。
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .. import swap as swapm
from .base import register
from .v2 import _on_h1, dframe
from .v3 import _finish, _z
from .v7 import USD_LEG, _V7XS

FOREIGN = list(USD_LEG)


def dollar_signal(data: dict, rule: str) -> pd.Series:
    """日足ラベル（日付）index の +1（外貨買い）/ -1（ドル買い）/ 0。"""
    legs = {}
    for c, (p, sgn) in USD_LEG.items():
        d = dframe(data[p])["d"]
        legs[c] = pd.Series((sgn * _z(d, 126)).to_numpy(), index=pd.DatetimeIndex(d["label"]).normalize())
    Z = pd.DataFrame(legs)
    Z = Z[~Z.index.duplicated(keep="last")].sort_index()
    naive = Z.index.tz_convert(None) if Z.index.tz is not None else Z.index
    months = pd.Series(naive.to_period("M"), index=Z.index)
    dc = {}
    for mo in months.unique():
        t = pd.Timestamp(mo.start_time) + pd.Timedelta(days=14) - pd.Timedelta(days=31)
        dc[mo] = float(np.mean([swapm.rate(c, t) for c in FOREIGN]) - swapm.rate("USD", t))
    carry = months.map(dc).astype(float)
    sig = np.sign(carry)
    if rule == "carry_and_trend":
        trend = Z.mean(axis=1)
        sig = sig.where(np.sign(trend) == sig, 0.0).where(trend.notna())
    return sig


class _V8(_V7XS):
    version = "v8"
    family = "dollar_carry"
    grid = {"rule": ["carry"]}

    def generate_all(self, data, pairs):
        sig = dollar_signal(data, self.params["rule"])
        out = {}
        leg_of = {p: s for c, (p, s) in USD_LEG.items()}
        for p in pairs:
            df = data[p]
            dm = dframe(df)
            lab = pd.DatetimeIndex(dm["d"]["label"]).normalize()
            dirn = sig.reindex(lab) * leg_of[p]
            h = _on_h1(pd.Series(dirn.to_numpy(), index=dm["d"].index), dm)
            dec = self.monthly_mask(dm) & h.notna()
            o = self.empty(df.index)
            o["entry"] = np.where(dec, h.fillna(0), 0).astype(int)
            o["exit_long"] = dec & (h <= 0)
            o["exit_short"] = dec & (h >= 0)
            out[p] = _finish(o, dm)
        return out


@register
class V8DollarCarry(_V8):
    name = "v8_dollar_carry"
    grid = {"rule": ["carry"]}


@register
class V8DollarCarryTrend(_V8):
    name = "v8_dollar_carry_trend"
    grid = {"rule": ["carry_and_trend"]}
