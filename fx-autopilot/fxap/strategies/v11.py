"""V11 候補（config/research_plan_v11.yaml）: 時間帯の季節性（Breedon & Ranaldo 2013）。

通貨は自国の営業時間中に下がる → ペア BASE/QUOTE は BASE 地域の時間帯に売り、QUOTE 地域の時間帯に買い。
時間帯（UTC、H1 足の始値の時刻）: ASIA 0–6 / EUROPE 7–12 / US 16–20。[start, end) の間だけ保有。
始値 start-1 の足の終値で判断 → start の始値で約定。始値 end-1 の足の終値で決済判断 → end の始値で決済。
同じ地域どうしのペアは取引しない。sizing = vol_target、SL = 日足 ATR20 × 4（暴落時のブレーキ）。
"""
from __future__ import annotations

import numpy as np

from ..common import PAIRS
from .base import register
from .v2 import _V2, dframe
from .v3 import _finish

WINDOWS = {"ASIA": (0, 6), "EUROPE": (7, 12), "US": (16, 20)}
REGION = {"JPY": "ASIA", "AUD": "ASIA", "NZD": "ASIA", "EUR": "EUROPE", "GBP": "EUROPE", "CHF": "EUROPE",
          "USD": "US", "CAD": "US"}


@register
class V11IntradayRegion(_V2):
    name = "v11_intraday_region"
    family = "intraday_seasonality"
    version = "v11"
    grid = {"windows": ["asia0_6_eu7_12_us16_20"]}

    def risk_overrides(self) -> dict:
        return {"sizing": "vol_target"}

    def generate(self, df, pair):
        dm = dframe(df)
        o = self.empty(df.index)
        rb, rq = REGION[PAIRS[pair]["base"]], REGION[PAIRS[pair]["quote"]]
        if rb == rq:
            o["vol"] = dm["h1"]["vol"]
            return o
        hr = df.index.hour
        entry = np.zeros(len(df), dtype=int)
        exit_l = np.zeros(len(df), dtype=bool)
        exit_s = np.zeros(len(df), dtype=bool)
        for region, side in ((rb, -1), (rq, 1)):
            a, b = WINDOWS[region]
            entry[hr == (a - 1) % 24] = side
            if side > 0:
                exit_l |= hr == b - 1
            else:
                exit_s |= hr == b - 1
        o["entry"] = entry
        o["exit_long"] = exit_l
        o["exit_short"] = exit_s
        o["max_bars"] = 8
        return _finish(o, dm)
