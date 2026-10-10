"""V18 候補（config/research_plan_v18.yaml）: 執行タイミングの修正（判断直後のロールオーバー・スプレッドで新規が止まる問題）。

PAPER Forward で判明: 日足・週足の判断足（20:00 UTC 始値の H1 足、確定は 21:00 UTC）は、米国夏時間の間
NY 17:00 のロールオーバー直前に当たり、スプレッドが中央値の 3 倍を超えるため Risk Engine（spread_normal）が
新規を毎回拒否していた（2026-09-29〜10-09 の 42 件すべてがこの時刻）。バックテストも同じ規則なので、
夏時間の期間の新規エントリーは過去検証でも実質的に落ちていた。

修正（戦略側のみ。エンジン・既存 LOCK は不変）: 判断足で出た新規シグナルを、その後 HOLD_BARS 本の H1 足でも
同じ向きで出し続ける（建玉済みならエンジンが無視、スプレッドが正常に戻った足で約定）。決済シグナルは判断足のまま。
規則・パラメータは v6_carry_trend_daily_mkt_7p / v6_carry_trend_mkt_7p と同一。
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .base import register
from .v6 import V6CarryTrendDailyMkt7P, V6CarryTrendMkt7P

HOLD_BARS = 4


def hold_entries(o: pd.DataFrame, n: int = HOLD_BARS) -> pd.DataFrame:
    e = o["entry"].astype(float).replace(0.0, np.nan)
    held = e.ffill(limit=n).fillna(0.0)
    # 保持中に決済シグナル（反対向きの判断）が出たら、それ以降は保持しない
    stop = ((o["exit_long"] & (held > 0)) | (o["exit_short"] & (held < 0))) & e.isna()
    grp = e.notna().cumsum()                      # 判断ごとの保持区間
    stopped = stop.astype(int).groupby(grp).cummax().astype(bool)
    held = held.where(~stopped, 0.0)
    o = o.copy()
    o["entry"] = held.astype(int)
    o.loc[o["sl_dist"].isna() | o["vol"].isna(), "entry"] = 0
    return o


@register
class V18CarryTrendDailyHold(V6CarryTrendDailyMkt7P):
    name = "v18_carry_trend_daily_hold"
    version = "v18"

    def generate(self, df, pair):
        return hold_entries(super().generate(df, pair))


@register
class V18CarryTrendWeeklyHold(V6CarryTrendMkt7P):
    name = "v18_carry_trend_weekly_hold"
    version = "v18"

    def generate(self, df, pair):
        return hold_entries(super().generate(df, pair))
