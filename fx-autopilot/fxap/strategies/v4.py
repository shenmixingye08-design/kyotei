"""V4 候補（config/research_plan_v4.yaml に事前登録）: トレンド×キャリーの高頻度版。V1〜V3 は変更しない。

共通: score = トレンド z + carry/2%、|score| > 閾値で符号方向に保有。判断タイミングだけが V2/V3（週 1 回）と違う。
SL = 日足 ATR20 × 4。キャリーは政策金利差（1 か月ラグ）。
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .. import features as F
from .base import register
from .v2 import _V2, _on_h1, carry_series, dframe
from .v3 import _finish, _z


def _signals(self, df, zz: pd.Series, decide: pd.Series, pair: str, dm):
    c = carry_series(pair, df.index)
    sc = zz + c / 0.02
    dirn = pd.Series(np.where(sc.abs() > self.params["threshold"], np.sign(sc), 0), index=df.index).fillna(0)
    d = decide & zz.notna()
    o = self.empty(df.index)
    o["entry"] = np.where(d, dirn, 0).astype(int)
    o["exit_long"] = d & (dirn <= 0)
    o["exit_short"] = d & (dirn >= 0)
    return _finish(o, dm)


@register
class V4CarryTrendDaily(_V2):
    name = "v4_carry_trend_daily"
    family = "trend_carry"
    version = "v4"
    grid = {"threshold": [0.5, 1.0]}

    def generate(self, df, pair):
        dm = dframe(df)
        return _signals(self, df, _on_h1(_z(dm["d"], 126), dm), dm["is_close"], pair, dm)


@register
class V4CarryTrendDailyFast(_V2):
    name = "v4_carry_trend_daily_fast"
    family = "trend_carry"
    version = "v4"
    grid = {"threshold": [0.5, 1.0]}

    def generate(self, df, pair):
        dm = dframe(df)
        d = dm["d"]
        return _signals(self, df, _on_h1((_z(d, 20) + _z(d, 63)) / 2, dm), dm["is_close"], pair, dm)


@register
class V4CarryTrendH4(_V2):
    name = "v4_carry_trend_h4"
    family = "trend_carry"
    version = "v4"
    grid = {"threshold": [0.5, 1.0]}

    def generate(self, df, pair):
        dm = dframe(df)
        h4 = F.higher_tf(F.mid(df), "4h")
        lr = np.log(h4["c"]).diff()
        ind = pd.DataFrame(index=h4.index)
        ind["z"] = np.log(h4["c"] / h4["c"].shift(126)) / (lr.rolling(360, min_periods=180).std() * np.sqrt(126))
        h1, dec, _ = F.map_complete(ind, h4["avail"], pd.Timedelta(hours=4), df.index)
        zz = pd.Series(np.nan, index=df.index)
        zz.loc[dec] = h1.loc[dec, "z"].to_numpy()
        decide = pd.Series(df.index.isin(dec), index=df.index)
        return _signals(self, df, zz, decide, pair, dm)
