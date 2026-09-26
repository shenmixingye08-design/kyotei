"""V16 候補（config/research_plan_v16.yaml）: 株式ポートフォリオのリバランス・フロー（Hau & Rey 2006, Camanho, Hau & Rey 2022）。

自国の株価が他国より上がると、海外投資家・国内投資家は資産配分を元に戻すため「上がった国の株を売り、その通貨も売る」。
→ 過去 3 か月の株価上昇率（自国通貨建て、OECD 月次株価指数）が高い通貨ほど、その後弱くなる。
equity_c = log(EQ_c[m-1] / EQ_c[m-4])（判断月 m の 1 か月前までの値。月次指数の公表遅れを考慮）。最終観測から 3 か月超は欠損。
スコア = -z(equity)（株が相対的に下がった国の通貨を買う）。枠組みは v7/v13〜v15 と同じ（8 通貨横断・10 ペア・月次・逆ボラ）。
比較: キャリー（v7）と等ウェイトで合成した版。
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .base import register
from .v7 import CCY8, _xs_z, currency_scores
from .v13 import _V13

LOOKBACK = 3
LAG = 1
STALE = 3
_cache: dict = {}


def _eq():
    if "eq" not in _cache:
        from ..data import fred
        eq = fred.load_equity()
        miss = [c for c in CCY8 if c not in eq]
        if miss:
            raise FileNotFoundError(f"株価指数がない通貨: {miss}")
        _cache["eq"] = eq
    return _cache["eq"]


def equity_momentum(index: pd.DatetimeIndex) -> pd.DataFrame:
    eq = _eq()
    naive = index.tz_convert(None) if index.tz is not None else index
    months = pd.Series(naive.to_period("M"), index=index)
    vals = {}
    for mo in months.unique():
        m1 = pd.Timestamp(mo.start_time) - pd.DateOffset(months=LAG)
        m0 = m1 - pd.DateOffset(months=LOOKBACK)
        row = []
        for c in CCY8:
            s = eq[c]
            p1 = s[s.index <= m1]
            p0 = s[s.index <= m0]
            if not len(p1) or not len(p0) or p1.index[-1] < m1 - pd.DateOffset(months=STALE):
                row.append(np.nan)
            else:
                row.append(float(np.log(p1.iloc[-1] / p0.iloc[-1])))
        vals[mo] = row
    return pd.DataFrame([vals[m] for m in months], index=index, columns=CCY8)


class _V16(_V13):
    version = "v16"
    family = "equity_rebalancing"
    with_carry = False

    def scores(self, data):
        carry = currency_scores(data, ("carry",))
        idx = carry.index
        comps = [-_xs_z(equity_momentum(idx))]
        if self.with_carry:
            comps.append(carry)
        stack = np.stack([c.to_numpy(dtype=float) for c in comps])
        with np.errstate(all="ignore"):
            return pd.DataFrame(np.nanmean(stack, axis=0), index=idx, columns=CCY8)


@register
class V16EquityRebal(_V16):
    name = "v16_equity_rebal"
    with_carry = False


@register
class V16EquityRebalCarry(_V16):
    name = "v16_equity_rebal_carry"
    with_carry = True
