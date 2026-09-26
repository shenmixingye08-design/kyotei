"""V6 候補（config/research_plan_v6.yaml）: 既存規則はそのまま、キャリーとスワップを市場金利（FRED/OECD 3 か月物）で計算。

目的: v2_trend_carry などの成績が「記憶ベースの政策金利近似表」にどれだけ依存していたかの感度分析。
規則・パラメータは既存と同一（グリッドなし）。金利ソースは計画ファイルの swap_source: market で切り替わる。
"""
from __future__ import annotations

from .base import register
from .v2 import V2TrendCarry
from .v3 import V3CarryTrend7P
from .v4 import V4CarryTrendDaily


@register
class V6TrendCarryMkt5P(V2TrendCarry):
    """v2_trend_carry の LOCK と同じ（composite / risk_stop、5 ペア）。"""
    name = "v6_trend_carry_mkt_5p"
    version = "v6"
    grid = {"mode": ["composite"], "sizing": ["risk_stop"]}


@register
class V6CarryTrendMkt7P(V3CarryTrend7P):
    """v3_carry_trend_7p と同じ（週次、7 ペア）。"""
    name = "v6_carry_trend_mkt_7p"
    version = "v6"


@register
class V6CarryTrendDailyMkt7P(V4CarryTrendDaily):
    """v4_carry_trend_daily と同じ（日次、閾値 0.5 に固定、7 ペア）。"""
    name = "v6_carry_trend_daily_mkt_7p"
    version = "v6"
    grid = {"threshold": [0.5]}
