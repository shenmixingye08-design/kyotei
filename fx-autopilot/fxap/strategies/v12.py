"""V12 候補（config/research_plan_v12.yaml）: キャリー・ポートフォリオ自体のトレンドでタイミング（Bertolini 2010）。

1. 通貨スコア = 8 通貨の市場金利の横断 z（v7 の carry-only と同じ）
2. キャリー・ポートフォリオの日次リターン（直物部分のみ）= Σ_c w_c(t-1) × r_c(t)
   w_c = S_c / Σ|S_c|（高金利を買い・低金利を売る）、r_c = 対 USD 通貨指数の日次 log 変化（USD は 0）
3. そのポートフォリオの過去 lookback 営業日の累積リターン > 0 のときだけ、v7 と同じペア変換（|S_b - S_q| > 0.5）で保有。
   ≤ 0 なら全ペア手仕舞い。判断は月 1 回（v7 と同じ）、sizing = vol_target、SL = 日足 ATR20 × 4。
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from ..common import PAIRS
from .base import register
from .v2 import _on_h1, dframe
from .v3 import _finish
from .v7 import CCY8, USD_LEG, _V7XS, currency_scores


def usd_index(data) -> pd.DataFrame:
    idx = {}
    for c, (p, sgn) in USD_LEG.items():
        d = dframe(data[p])["d"]
        idx[c] = pd.Series(sgn * np.log(d["c"].to_numpy()), index=pd.DatetimeIndex(d["label"]).normalize())
    L = pd.DataFrame(idx)
    L = L[~L.index.duplicated(keep="last")].sort_index()
    L["USD"] = 0.0
    return L[CCY8]


def carry_timing(data, lookback: int) -> tuple[pd.DataFrame, pd.Series]:
    S = currency_scores(data, ("carry",))
    L = usd_index(data).reindex(S.index)
    w = S.div(S.abs().sum(axis=1), axis=0)
    r = (w.shift(1) * L.diff()).sum(axis=1, min_count=len(CCY8) - 1)
    mom = r.rolling(lookback, min_periods=int(lookback * 0.8)).sum()
    ok = (mom > 0).astype(float).where(mom.notna())
    return S, ok


@register
class V12CarryTimed(_V7XS):
    name = "v12_carry_timed"
    version = "v12"
    family = "carry_timing"
    factors = ("carry",)
    grid = {"lookback": [63, 126]}

    def generate_all(self, data, pairs):
        S, ok = carry_timing(data, self.params["lookback"])
        out = {}
        for p in pairs:
            df = data[p]
            dm = dframe(df)
            b, q = PAIRS[p]["base"], PAIRS[p]["quote"]
            sc = S[b] - S[q]
            dirn = np.sign(sc).where(sc.abs() > 0.5, 0.0).where(sc.notna())
            dirn = dirn.where(ok == 1.0, 0.0).where(ok.notna())
            lab = pd.DatetimeIndex(dm["d"]["label"]).normalize()
            h = _on_h1(pd.Series(dirn.reindex(lab).to_numpy(), index=dm["d"].index), dm)
            dec = self.monthly_mask(dm) & h.notna()
            o = self.empty(df.index)
            o["entry"] = np.where(dec, h.fillna(0), 0).astype(int)
            o["exit_long"] = dec & (h <= 0)
            o["exit_short"] = dec & (h >= 0)
            out[p] = _finish(o, dm)
        return out
