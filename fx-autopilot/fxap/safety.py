"""PAPER ONLY 安全ゲート。

LIVE（実資金）注文は、本人の明示承認があるまで絶対に行わない。そのため LIVE の発注経路は
**コード上に存在しない**。このモジュールは、設定・環境変数・承認ファイルのどれかが LIVE を示した時点で
例外を投げ、処理全体を止める（「LIVE にしようとした」こと自体を異常として扱う）。
"""
from __future__ import annotations

import os

from .common import CONFIG, settings

LIVE_APPROVAL_FILE = CONFIG / "LIVE_APPROVAL.yaml"   # 存在してはならない（本人承認の記録用。現在は未作成）
LIVE_HOST_MARKERS = ("api-fxtrade.oanda.com", "stream-fxtrade.oanda.com", "api.ibkr.com/live", "fxtrade")


class LiveTradingForbidden(RuntimeError):
    pass


def assert_paper_only(cfg: dict | None = None) -> None:
    s = cfg or settings()
    problems = []
    if s.get("mode") not in ("PAPER", "BACKTEST"):
        problems.append(f"mode={s.get('mode')}")
    if s.get("live_trading_enabled") is not False:
        problems.append("live_trading_enabled is not false")
    if s.get("broker") not in ("paper_sim", "oanda_practice", "ibkr_paper"):
        problems.append(f"broker={s.get('broker')}")
    for k in ("FX_LIVE_TRADING", "LIVE_TRADING_ENABLED", "FXAP_LIVE"):
        if os.environ.get(k, "false").lower() not in ("", "0", "false", "no"):
            problems.append(f"env {k}={os.environ.get(k)}")
    if LIVE_APPROVAL_FILE.exists():
        # 承認ファイルがあっても、LIVE 経路は未実装なので止める（実装と本人承認の両方が揃うまで）
        problems.append("LIVE_APPROVAL.yaml exists but LIVE execution path is not implemented")
    if problems:
        raise LiveTradingForbidden("PAPER ONLY 違反: " + "; ".join(problems))


def assert_not_live_endpoint(url: str) -> None:
    u = url.lower()
    if any(m in u for m in LIVE_HOST_MARKERS):
        raise LiveTradingForbidden(f"LIVE エンドポイントへの接続は禁止: {url}")
