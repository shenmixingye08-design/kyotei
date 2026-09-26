"""V5 候補（config/research_plan_v5.yaml に事前登録）: 既存規則をそのまま 10 ペアへ（パラメータ探索なし）。

目的は「設計に使っていない通貨（NZD / CAD / CHF）でも同じ規則が機能するか」の確認。V1〜V4 は変更しない。
"""
from __future__ import annotations

from .base import register
from .v3 import V3CarryTrend7P
from .v4 import V4CarryTrendDaily


@register
class V5CarryTrendWeekly10P(V3CarryTrend7P):
    """v2_trend_carry / v3_carry_trend_7p と同じ規則（週 1 回、z126 + carry/2%、|score| > 0.5）。"""
    name = "v5_carry_trend_weekly_10p"
    version = "v5"
    grid = {"sizing": ["risk_stop"]}


@register
class V5CarryTrendDaily10P(V4CarryTrendDaily):
    """v4_carry_trend_daily と同じ規則（毎日判断、閾値 0.5 に固定）。"""
    name = "v5_carry_trend_daily_10p"
    version = "v5"
    grid = {"threshold": [0.5]}
