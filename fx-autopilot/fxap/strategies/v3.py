"""V3 候補（config/research_plan_v3.yaml に事前登録）。V1/V2 の戦略・LOCK は変更しない。

共通: V2 と同じ日足（NY クローズ区切り・確定判定は map_complete）・週 1 回（火曜 NY クローズ）判断・
キャリー = 政策金利差（1 か月ラグ）・SL = 日足 ATR20 × 4。
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .base import register
from .v2 import _V2, _on_h1, carry_series, dframe


def _z(d: pd.DataFrame, L: int) -> pd.Series:
    return np.log(d["c"] / d["c"].shift(L)) / (d["sd60"] * np.sqrt(L))


def _finish(o, dm, sl_mult=4.0):
    o["sl_dist"] = sl_mult * dm["h1"]["atr20"]
    o["vol"] = dm["h1"]["vol"]
    o.loc[o["sl_dist"].isna() | o["vol"].isna(), "entry"] = 0
    return o


@register
class V3CarryTrendXS(_V2):
    """全ペアの score = z126 + carry/2% を週次で比較し、|score| 上位 k ペアを score の符号方向に保有。"""
    name = "v3_carry_trend_xs"
    family = "trend_carry"
    version = "v3"
    needs_all_pairs = True
    grid = {"top_k": [2, 3, 4], "sizing": ["risk_stop", "vol_target"]}

    def generate_all(self, data, pairs):
        k = self.params["top_k"]
        scores = {}
        for p in pairs:
            dm = dframe(data[p])
            d = dm["d"]
            lab = pd.DatetimeIndex(d["label"]).normalize()
            c = carry_series(p, pd.DatetimeIndex(d.index)).to_numpy()
            scores[p] = pd.Series((_z(d, 126) + c / 0.02).to_numpy(), index=lab)
        S = pd.DataFrame(scores)
        S = S[~S.index.duplicated(keep="last")]
        rank = S.abs().rank(axis=1, ascending=False, method="first")
        dirn = np.sign(S).where(rank <= k, 0.0).where(S.notna())
        out = {}
        for p in pairs:
            df = data[p]
            dm = dframe(df)
            lab = pd.DatetimeIndex(dm["d"]["label"]).normalize()
            h = _on_h1(pd.Series(dirn[p].reindex(lab).to_numpy(), index=dm["d"].index), dm)
            wk = self.weekly_mask(dm) & h.notna()
            o = self.empty(df.index)
            o["entry"] = np.where(wk, h.fillna(0), 0).astype(int)
            o["exit_long"] = wk & (h <= 0)
            o["exit_short"] = wk & (h >= 0)
            out[p] = _finish(o, dm)
        return out

    def generate(self, df, pair):
        raise RuntimeError("v3_carry_trend_xs は generate_all（全ペア）で生成する")


@register
class V3CarryTrendMH(_V2):
    """ペアごと: 複数期間トレンド z = 平均(z63, z126, z252) + carry/2%。|score| > 閾値で符号方向。"""
    name = "v3_carry_trend_mh"
    family = "trend_carry"
    version = "v3"
    grid = {"threshold": [0.5, 1.0], "trail": ["none", "atr3"]}

    def generate(self, df, pair):
        p = self.params
        dm = dframe(df)
        d = dm["d"]
        z = (_z(d, 63) + _z(d, 126) + _z(d, 252)) / 3
        zz = _on_h1(z, dm)
        c = carry_series(pair, df.index)
        sc = zz + c / 0.02
        dirn = pd.Series(np.where(sc.abs() > p["threshold"], np.sign(sc), 0), index=df.index).fillna(0)
        wk = self.weekly_mask(dm) & zz.notna()
        o = self.empty(df.index)
        o["entry"] = np.where(wk, dirn, 0).astype(int)
        o["exit_long"] = wk & (dirn <= 0)
        o["exit_short"] = wk & (dirn >= 0)
        if p["trail"] == "atr3":
            o["trail_dist"] = 3.0 * dm["h1"]["atr20"]
        return _finish(o, dm)


@register
class V3CarryTrend7P(_V2):
    """v2_trend_carry の composite 規則（z126 + carry/2%、|score| > 0.5）をそのまま 7 ペアへ（グリッドなし）。"""
    name = "v3_carry_trend_7p"
    family = "trend_carry"
    version = "v3"
    grid = {"sizing": ["risk_stop"]}

    def generate(self, df, pair):
        dm = dframe(df)
        d = dm["d"]
        zz = _on_h1(_z(d, 126), dm)
        c = carry_series(pair, df.index)
        sc = zz + c / 0.02
        dirn = pd.Series(np.where(sc.abs() > 0.5, np.sign(sc), 0), index=df.index).fillna(0)
        wk = self.weekly_mask(dm) & zz.notna()
        o = self.empty(df.index)
        o["entry"] = np.where(wk, dirn, 0).astype(int)
        o["exit_long"] = wk & (dirn <= 0)
        o["exit_short"] = wk & (dirn >= 0)
        return _finish(o, dm)


@register
class V3CarryOnly(_V2):
    """ベンチマーク: |金利差| > 0.5% ならキャリーの受け取り方向（トレンドは見ない）。"""
    name = "v3_carry_only"
    family = "carry"
    version = "v3"
    grid = {"sizing": ["risk_stop", "vol_target"]}

    def generate(self, df, pair):
        dm = dframe(df)
        d = dm["d"]
        c = carry_series(pair, df.index)
        dirn = pd.Series(np.where(c.abs() > 0.005, np.sign(c), 0), index=df.index).fillna(0)
        ok = _on_h1(d["sd60"], dm).notna()
        wk = self.weekly_mask(dm) & ok
        o = self.empty(df.index)
        o["entry"] = np.where(wk, dirn, 0).astype(int)
        o["exit_long"] = wk & (dirn <= 0)
        o["exit_short"] = wk & (dirn >= 0)
        return _finish(o, dm)
