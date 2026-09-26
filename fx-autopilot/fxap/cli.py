"""FX AUTOPILOT CLI（PAPER ONLY）。

  python -m fxap.cli ingest                 # Dukascopy から H1 bid/ask を取得・増分更新 → 品質検査
  python -m fxap.cli research [--stage1]    # Stage1(WF) → LOCK → Stage2(TEST/FORWARD) → Tournament → SUMMARY.md
  python -m fxap.cli paper                  # LOCK 済み仕様を LOCK 後の新しい足で PAPER 運用 → Tournament → Dashboard
  python -m fxap.cli dashboard | verify | sweep | safety
  python -m fxap.cli kill-switch status|engage|release --spec <id> --reason ... --by <本人の名前>
"""
from __future__ import annotations

import argparse
import json
import sys
import time

import pandas as pd

from . import safety
from .common import PAPER_DIR, RESULTS, settings, sha, utcnow


def _pairs():
    return settings()["pairs"]


def cmd_ingest(a):
    from .data import store
    pairs = a.pairs.split(",") if a.pairs else _pairs()
    rep = store.ingest(pairs, a.start or settings()["data"]["start"])
    print(json.dumps(rep, indent=2))
    if a.pairs:
        return 0
    return cmd_quality(a)


def cmd_quality(a):
    """全ペアの品質検査。欠損・古いデータ・異常値があれば exit 1（研究・PAPER を止める）。"""
    from .data import store
    from .research import load_locked
    # 全体を止めるのは円換算に必須の USDJPY だけ。他のペアの欠損・品質 NG は、そのペアを使う仕様だけが取引しない（cmd_paper）
    try:
        frames = store.load_all(_pairs(), required={"USDJPY"})
    except FileNotFoundError as e:
        print(f"データ欠損: {e}", file=sys.stderr)
        return 1
    q = store.write_quality_report(frames, RESULTS / "data_quality.json")
    for r in q:
        print(r)
    missing = sorted(set(_pairs()) - set(frames))
    bad = [r["pair"] for r in q if not r.get("ok")] + missing
    used = _required_pairs(load_locked())
    if "USDJPY" in bad:
        print("データ品質 NG: USDJPY（円換算に必須）", file=sys.stderr)
        return 1
    if bad:
        print(f"warning: データ欠損/品質 NG {bad}。LOCK 済み仕様で影響: {sorted(set(bad) & used)}（該当仕様は今回取引しない）",
              file=sys.stderr)
    return 0


def _fingerprint(frames):
    return {p: {"rows": int(len(d)), "first": str(d.index.min()), "last": str(d.index.max()),
                "sha_2021": sha(pd.util.hash_pandas_object(d[d.index < pd.Timestamp("2022-01-01", tz="UTC")]).sum().item())}
            for p, d in frames.items()}


def cmd_research(a):
    from . import report, research, tournament
    from .data import store
    safety.assert_paper_only()
    t0 = time.time()
    # v1 は LOCK 時の 5 ペアだけで評価する（後から追加したペアで v1 の結果・ランダム比較が変わらないように）
    v1 = [s for s in research.load_locked() if s.get("plan_version", "fx_plan_v1") == "fx_plan_v1"]
    v1_pairs = sorted({p for s in v1 for p in s["pairs"]}) or ["USDJPY", "EURUSD", "EURJPY", "GBPUSD", "AUDUSD"]
    frames = store.load_all(v1_pairs)
    quality = [store.quality(d, p) for p, d in frames.items()]
    locked = research.load_locked()
    s1 = None
    if a.stage1 or len(locked) < len(research.CANDIDATE_STRATEGIES):
        print("== Stage 1（TRAIN+VALIDATION のみ）")
        s1 = research.stage1(frames, v1_pairs, strategies=a.only.split(",") if a.only else None)
        print("== LOCK")
        research.lock_specs(s1["candidates"], s1["selection_end"], _fingerprint(frames))
        locked = research.load_locked()
    locked = [s for s in locked if s.get("plan_version", "fx_plan_v1") == "fx_plan_v1"]   # V2 以降は research-v2
    if a.only:
        locked = [s for s in locked if s["strategy"] in a.only.split(",")]
    print(f"== Stage 2（LOCK 済み {len(locked)} 仕様を TEST / FORWARD で評価）")
    s2 = research.stage2(locked, frames)
    print("== ランダム売買ベンチマーク / マイクロストラクチャ")
    rnd = research.random_baseline(frames, v1_pairs, seeds=a.seeds)
    micro = research.microstructure(frames)
    allspecs = research.load_locked()
    tour = tournament.update(allspecs, s2["stage2"], _paper_perf(allspecs))
    out = RESULTS / utcnow().strftime("%Y%m%d")
    md = report.write(out, quality, s1, locked, s2, rnd, micro, tour)
    _registry_append(s2["stage2"], locked)
    print(md[:3000])
    print(f"done in {time.time() - t0:.0f}s → {out}")
    return 0


def cmd_research_v2(a):
    from . import dashboard, research_v2, tournament
    from .data import store
    from .research import load_locked
    safety.assert_paper_only()
    research_v2.use(a.plan)
    frames = store.load_all(research_v2.plan()["pairs"] + ["USDJPY"])
    data_end = str(max(d.index.max() for d in frames.values()))
    out = research_v2.run(frames, only=a.only.split(",") if a.only else None)
    specs = research_v2.lock(out["candidates"], data_end)
    md = research_v2.write(out, specs, data_end)
    allspecs = load_locked()
    s2p = RESULTS / "LATEST" / "stage2.csv"
    s2 = pd.read_csv(s2p) if s2p.exists() else None
    tournament.update(allspecs, s2, _paper_perf(allspecs))
    dashboard.build()
    print(md[:6000])
    return 0


def _registry_append(st: pd.DataFrame, specs):
    """研究レジストリ（追記のみ）: 仕様ハッシュ × 期間 × 変種の初回評価だけを記録。"""
    path = RESULTS / "registry.csv"
    hashes = {s["spec_id"]: s["spec_hash"] for s in specs}
    st = st.assign(spec_hash=st["spec_id"].map(hashes), evaluated_at=utcnow().isoformat())
    if path.exists():
        old = pd.read_csv(path)
        seen = set(zip(old.spec_hash, old.period, old.variant))
        st = st[[(h, p, v) not in seen for h, p, v in zip(st.spec_hash, st.period, st.variant)]]
        if len(st):
            pd.concat([old, st]).to_csv(path, index=False)
    else:
        st.to_csv(path, index=False)


def _paper_perf(specs) -> dict:
    from . import metrics
    from .paper_engine import load_paper
    out = {}
    init = float(settings()["account"]["initial_equity"])
    for s in specs:
        p = load_paper(s["spec_id"])
        eq = p["equity"]
        if len(eq):
            eq = pd.concat([pd.Series([init], index=[eq.index[0] - pd.Timedelta(hours=1)]), eq])
        out[s["spec_id"]] = {"daily": metrics.daily_returns(eq) if len(eq) > 2 else pd.Series(dtype=float),
                             "n_trades": int(len(p["trades"]))}
    return out


def _required_pairs(specs) -> set:
    req = {"USDJPY"}          # 円換算に必須
    for s in specs:
        req |= set(s.get("trade_pairs") or s["pairs"])
    return req


def cmd_paper(a):
    from . import dashboard, tournament
    from .data import store
    from .paper_engine import PaperEngine
    from .research import load_locked
    safety.assert_paper_only()
    specs = load_locked()
    frames = store.load_all(_pairs(), required={"USDJPY"})
    bad = [p for p, d in frames.items() if not store.quality(d, p).get("ok")]
    for p in bad:
        print(f"warning: {p} はデータ品質 NG のため、このペアを使う仕様は今回処理しない", file=sys.stderr)
        frames.pop(p)
    if not specs:
        print("LOCK 済み仕様がありません（research を先に実行）")
        return 1
    init = float(settings()["account"]["initial_equity"])
    failed = []
    for s in specs:
        need = set(s.get("trade_pairs") or s["pairs"])
        if not need <= set(frames):
            print(f"{s['spec_id']}: データ欠損 {sorted(need - set(frames))} のため今回は処理しない（新規注文なし）", file=sys.stderr)
            failed.append(s["spec_id"])
            continue
        try:
            eng = PaperEngine(s, frames, initial_equity=init)
            r = eng.run()
            print(json.dumps(r, default=str))
        except Exception as e:  # noqa: BLE001  1 つの仕様の失敗で他の仕様の PAPER を止めない
            print(f"{s['spec_id']}: PAPER エラー {e!r}", file=sys.stderr)
            failed.append(s["spec_id"])
    s2p = RESULTS / "LATEST" / "stage2.csv"
    s2 = pd.read_csv(s2p) if s2p.exists() else None
    tournament.update(specs, s2, _paper_perf(specs))
    try:
        dashboard.build()
    except Exception as e:  # noqa: BLE001  表示の失敗で PAPER 状態のコミットを止めない（台帳検証は下で必ず実行）
        print(f"dashboard build failed (PAPER state is still saved): {e!r}", file=sys.stderr)
    rc = cmd_verify(a)
    if failed:
        print(f"PAPER を処理できなかった仕様: {failed}", file=sys.stderr)
    return rc


def cmd_dashboard(a):
    from . import dashboard
    d = dashboard.build()
    print(f"dashboard: champion={d['champion']} papers={len(d['papers'])}")
    return 0


def cmd_verify(a):
    from .ledger import Ledger
    safety.assert_paper_only()
    bad = 0
    for p in sorted(PAPER_DIR.glob("*/ledger.jsonl")):
        ok, msg = Ledger(p).verify()
        print(f"{p.parent.name}: {msg}")
        bad += not ok
    return 1 if bad else 0


def cmd_sweep(a):
    from . import dashboard
    d = dashboard.build()
    print(json.dumps(d.get("sweep") or {"note": "Champion 不在または PAPER 未開始のため計算対象なし"}, indent=2, ensure_ascii=False))
    return 0


def cmd_safety(a):
    safety.assert_paper_only()
    print("PAPER ONLY safety gate: OK")
    return 0


def cmd_kill(a):
    path = PAPER_DIR / a.spec / "state.json"
    st = json.loads(path.read_text())
    rs = st.setdefault("risk_state", {})
    from .ledger import Ledger
    led = Ledger(PAPER_DIR / a.spec / "ledger.jsonl")
    if a.action == "status":
        print(json.dumps({"halted": st.get("halted"), "kill_switch": rs.get("kill_switch"), "reason": rs.get("kill_reason")},
                         ensure_ascii=False))
        return 0
    if a.action == "engage":
        st["halted"] = True
        rs["kill_switch"], rs["kill_reason"] = True, f"manual: {a.reason}"
        led.append("kill_switch", reason=f"manual: {a.reason}", by=a.by or "manual")
    elif a.action == "release":
        if not a.by or a.by.lower() in ("auto", "system", "ci", "github-actions", "claude"):
            print("Kill Switch の解除は本人のみ（--by <本人の名前>）", file=sys.stderr)
            return 2
        if not sys.stdin.isatty():
            print("解除は対話端末からのみ可能です", file=sys.stderr)
            return 2
        st["halted"] = False
        rs["kill_switch"], rs["kill_reason"] = False, ""
        rs["hwm"] = rs.get("equity", rs.get("hwm"))
        led.append("kill_switch_release", reason=a.reason, by=a.by)
    path.write_text(json.dumps(st, indent=2, ensure_ascii=False))
    print("ok")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(prog="fxap")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("ingest")
    s.add_argument("--start")
    s.add_argument("--pairs")
    s.set_defaults(fn=cmd_ingest)
    sub.add_parser("quality").set_defaults(fn=cmd_quality)
    s = sub.add_parser("research-v2")
    s.add_argument("--only")
    s.add_argument("--plan", default="v2", help="v2 | v3（config/research_plan_<plan>.yaml）")
    s.set_defaults(fn=cmd_research_v2)
    s = sub.add_parser("research")
    s.add_argument("--stage1", action="store_true", help="LOCK 済みでも Stage 1 を再計算（LOCK は変更しない）")
    s.add_argument("--only")
    s.add_argument("--seeds", type=int, default=10)
    s.set_defaults(fn=cmd_research)
    for name, fn in (("paper", cmd_paper), ("dashboard", cmd_dashboard), ("verify", cmd_verify),
                     ("sweep", cmd_sweep), ("safety", cmd_safety)):
        sub.add_parser(name).set_defaults(fn=fn)
    s = sub.add_parser("kill-switch")
    s.add_argument("action", choices=["status", "engage", "release"])
    s.add_argument("--spec", required=True)
    s.add_argument("--reason", default="")
    s.add_argument("--by")
    s.set_defaults(fn=cmd_kill)
    a = ap.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
