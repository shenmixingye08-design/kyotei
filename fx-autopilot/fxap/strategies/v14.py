"""V14 候補（config/research_plan_v14.yaml）: イールドカーブの傾き（Ang & Chen 2010）。

term_c = 10 年国債利回り - 3 か月物金利（FRED/OECD 月次）。判断月の月中 - 31 日時点の、さらに 1 か月前の月の値
（v7/v13 と同じラグ）。最終観測から 6 か月を超えた系列は欠損扱い。
Ang & Chen: 傾き（term）は将来の通貨リターンを強く負に予測する → スコア = -z(term)（カーブが平らな通貨を買う）。
組み合わせ版: -z(term) と金利モメンタム z（v13）の平均（論文は両方が予測力を持ち、キャリーとの相関が低いと報告）。
枠組みは v7/v13 と同じ（8 通貨横断・10 ペア・月次・逆ボラ）。
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .base import register
from .v7 import CCY8, _xs_z
from .v13 import _V13, rate_momentum

STALE_MONTHS = 6
_cache: dict = {}


def _rates():
    if "rates" not in _cache:
        from ..data import fred
        lo = fred.load_monthly_rates(fred.LONG_RATES)
        sh = fred.load_monthly_rates(fred.SHORT_RATES)
        miss = [c for c in CCY8 if c not in lo or c not in sh]
        if miss:
            raise FileNotFoundError(f"長期 / 短期金利がない通貨: {miss}")
        _cache["rates"] = (lo, sh)
    return _cache["rates"]


def _at(s: pd.Series, t: pd.Timestamp) -> float:
    ref = pd.Timestamp(year=t.year, month=t.month, day=1) - pd.DateOffset(months=1)
    past = s[s.index <= ref]
    if not len(past) or past.index[-1] < ref - pd.DateOffset(months=STALE_MONTHS):
        return np.nan
    return float(past.iloc[-1])


def term_spread(index: pd.DatetimeIndex) -> pd.DataFrame:
    lo, sh = _rates()
    naive = index.tz_convert(None) if index.tz is not None else index
    months = pd.Series(naive.to_period("M"), index=index)
    vals = {}
    for mo in months.unique():
        t = pd.Timestamp(mo.start_time) + pd.Timedelta(days=14) - pd.Timedelta(days=31)
        vals[mo] = [_at(lo[c], t) - _at(sh[c], t) for c in CCY8]
    return pd.DataFrame([vals[m] for m in months], index=index, columns=CCY8)


class _V14(_V13):
    version = "v14"
    family = "yield_curve"
    with_ratemom = False

    def scores(self, data):
        from .v7 import currency_scores
        idx = currency_scores(data, ("carry",)).index
        comps = [-_xs_z(term_spread(idx))]
        if self.with_ratemom:
            comps.append(_xs_z(rate_momentum(idx)))
        stack = np.stack([c.to_numpy(dtype=float) for c in comps])
        with np.errstate(all="ignore"):
            return pd.DataFrame(np.nanmean(stack, axis=0), index=idx, columns=CCY8)


@register
class V14Term(_V14):
    name = "v14_term"
    with_ratemom = False


@register
class V14TermRateMom(_V14):
    name = "v14_term_ratemom"
    with_ratemom = True
