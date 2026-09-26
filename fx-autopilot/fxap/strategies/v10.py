"""V10 候補（config/research_plan_v10.yaml）: キャリー × VIX の暴落リスク・フィルター。

carry = 金利差（base - quote、市場金利、v2.carry_series と同じラグ）。|carry| > 0.5% のとき符号方向が候補。
calm  = VIX 前日終値 <= 過去 252 営業日の中央値（below_median）/ 80 パーセンタイル（below_p80）。
        VIX は FRED VIXCLS（米国の営業日）。日足ラベルの日付より前（< その日）に確定した最新値だけを使う。
calm のときだけ保有、calm でなければ手仕舞い。毎日（日足確定時）判断。sizing = vol_target、SL = 日足 ATR20 × 4。
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .base import register
from .v2 import _V2, _on_h1, carry_series, dframe
from .v3 import _finish

_cache: dict = {}


def vix_calm(rule: str) -> pd.Series:
    """日付（その日の値まで確定）-> calm フラグ。使う側で 1 日ずらす。"""
    if rule in _cache:
        return _cache[rule]
    from ..data import fred
    v = fred.load("VIXCLS").dropna()
    v.index = pd.DatetimeIndex(v.index).normalize()
    q = 0.5 if rule == "below_median" else 0.8
    thr = v.rolling(252, min_periods=200).quantile(q)
    calm = (v <= thr).astype(float).where(thr.notna())
    _cache[rule] = calm
    return calm


@register
class V10CarryVix(_V2):
    name = "v10_carry_vix"
    family = "carry_riskfilter"
    version = "v10"
    grid = {"calm": ["below_median", "below_p80"]}

    def risk_overrides(self) -> dict:
        return {"sizing": "vol_target"}

    def generate(self, df, pair):
        dm = dframe(df)
        d = dm["d"]
        lab = pd.DatetimeIndex(d["label"])
        lab = (lab.tz_convert(None) if lab.tz is not None else lab).normalize()
        calm = vix_calm(self.params["calm"])
        # ラベル日より前に確定した VIX だけ（前日以前の最新値）
        pos = calm.index.searchsorted(lab, side="left") - 1
        cv = np.where(pos >= 0, calm.to_numpy()[np.clip(pos, 0, None)], np.nan)
        c = carry_series(pair, pd.DatetimeIndex(d.index)).to_numpy()
        dirn = np.where(np.abs(c) > 0.005, np.sign(c), 0.0)
        dirn = np.where(cv == 1.0, dirn, np.where(np.isnan(cv), np.nan, 0.0))
        dirn = np.where(d["sd60"].notna().to_numpy(), dirn, np.nan)
        h = _on_h1(pd.Series(dirn, index=d.index), dm)
        dec = dm["is_close"] & h.notna()
        o = self.empty(df.index)
        o["entry"] = np.where(dec, h.fillna(0), 0).astype(int)
        o["exit_long"] = dec & (h <= 0)
        o["exit_short"] = dec & (h >= 0)
        return _finish(o, dm)
