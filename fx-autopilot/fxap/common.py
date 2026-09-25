"""共通: パス・設定・通貨ペアのメタデータ・時刻。"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
from functools import lru_cache
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config"
DATA_DIR = Path(os.environ.get("FXAP_DATA_DIR", ROOT / "data"))
OUT = Path(os.environ.get("FXAP_OUT", ROOT))          # テストでは一時ディレクトリに向ける
RESULTS = OUT / "research" / "results"
PAPER_DIR = OUT / "paper_forward"
PUBLIC = OUT / "public"
LOCK_DIR = OUT / "config" / "locked"

# pip の大きさ・価格の桁（Dukascopy の整数価格の除数）
PAIRS = {
    "USDJPY": {"base": "USD", "quote": "JPY", "pip": 0.01, "point": 1e-3},
    "EURUSD": {"base": "EUR", "quote": "USD", "pip": 0.0001, "point": 1e-5},
    "EURJPY": {"base": "EUR", "quote": "JPY", "pip": 0.01, "point": 1e-3},
    "GBPUSD": {"base": "GBP", "quote": "USD", "pip": 0.0001, "point": 1e-5},
    "AUDUSD": {"base": "AUD", "quote": "USD", "pip": 0.0001, "point": 1e-5},
}
PERIODS_PER_YEAR_DAILY = 260   # FX の営業日数（月〜金）


def utcnow() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def iso(t) -> str:
    return (t if isinstance(t, str) else t.isoformat())


@lru_cache(maxsize=None)
def _load(name: str) -> dict:
    return yaml.safe_load((CONFIG / name).read_text(encoding="utf-8"))


def settings() -> dict:
    return _load("settings.yaml")


def research_plan() -> dict:
    return _load("research_plan.yaml")


def sha(obj) -> str:
    s = obj if isinstance(obj, str) else json.dumps(obj, sort_keys=True, default=str, ensure_ascii=False)
    return hashlib.sha256(s.encode()).hexdigest()


def code_hash(paths=None) -> str:
    """戦略・バックテスト・コスト・リスクのコードのハッシュ（LOCK 後の改変検出用）。"""
    base = ROOT / "fxap"
    files = paths or sorted(
        [p for p in base.rglob("*.py") if p.parent.name in ("fxap", "strategies")
         and p.name in ("backtest.py", "costs.py", "risk.py", "features.py", "swap.py")
         or p.parent.name == "strategies"])
    h = hashlib.sha256()
    for p in files:
        h.update(p.name.encode())
        h.update(p.read_bytes())
    return h.hexdigest()
