"""V15 候補（config/research_plan_v15.yaml）: 金利系ファンダメンタルズの合成（キャリー・金利モメンタム・カーブの傾き）。

3 つとも論文で予測力が報告され、互いの相関が低いとされる情報:
  carry     = 短期金利の水準（v7）       … 高金利を買う
  rate_mom  = 短期金利の 6 か月変化（v13） … 利上げ方向を買う
  -term     = -(10 年 - 3 か月)（v14）     … カーブが平らな通貨を買う
各 z を等ウェイトで平均した通貨スコア。枠組みは v7/v13/v14 と同じ（8 通貨横断・10 ペア・月次・逆ボラ）。
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .base import register
from .v7 import CCY8, _xs_z, currency_scores
from .v13 import _V13, rate_momentum
from .v14 import term_spread


@register
class V15RatesComposite(_V13):
    name = "v15_rates_composite"
    version = "v15"
    family = "rates_composite"

    def scores(self, data):
        carry = currency_scores(data, ("carry",))
        idx = carry.index
        comps = [carry, _xs_z(rate_momentum(idx)), -_xs_z(term_spread(idx))]
        stack = np.stack([c.to_numpy(dtype=float) for c in comps])
        with np.errstate(all="ignore"):
            return pd.DataFrame(np.nanmean(stack, axis=0), index=idx, columns=CCY8)
