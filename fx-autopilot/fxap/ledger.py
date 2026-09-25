"""追記専用・ハッシュチェーン付きの JSONL 台帳（注文・約定・Risk 判定・Kill Switch・残高）。

各行は直前行の hash を含む。1 行でも書き換える・削除すると verify() が失敗する（負けトレードの削除を検出）。
"""
from __future__ import annotations

import json
from pathlib import Path

from .common import sha, utcnow


class Ledger:
    def __init__(self, path: Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._last = None

    def _tail_hash(self) -> str:
        if self._last is not None:
            return self._last
        h = "GENESIS"
        if self.path.exists():
            with self.path.open(encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        h = json.loads(line)["hash"]
        self._last = h
        return h

    def append(self, event: str, /, **payload) -> dict:
        prev = self._tail_hash()
        rec = {"ts": utcnow().isoformat(), "event": event, **payload, "prev": prev}
        rec["hash"] = sha({k: v for k, v in rec.items() if k != "hash"})
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False, default=str) + "\n")
        self._last = rec["hash"]
        return rec

    def records(self, event: str | None = None) -> list[dict]:
        if not self.path.exists():
            return []
        out = []
        with self.path.open(encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    if event is None or r["event"] == event:
                        out.append(r)
        return out

    def verify(self) -> tuple[bool, str]:
        prev = "GENESIS"
        for i, r in enumerate(self.records()):
            if r.get("prev") != prev:
                return False, f"line {i + 1}: prev mismatch"
            body = {k: v for k, v in r.items() if k != "hash"}
            if sha(json.loads(json.dumps(body, default=str))) != r["hash"]:
                return False, f"line {i + 1}: hash mismatch"
            prev = r["hash"]
        return True, "ok"
