"""Strategy Tournament（Champion / Challenger）と LIVE 候補判定。

状態:
  RESEARCH_ONLY   : Walk-Forward / VALIDATION のゲート A 不合格。PAPER で観測は続けるが本番候補にしない
  REJECTED        : ゲート A は合格したが TEST / FORWARD / コスト耐性 / DD などのゲート B に不合格
  BACKTEST_PASS   : ゲート B 合格。LOCK 後の PAPER Forward の蓄積待ち
  LIVE_CANDIDATE  : さらに LOCK 後 PAPER Forward（期間・取引数・プラス・乖離）も合格。**LIVE 開始は本人の明示承認が必須**
Champion の交代: Challenger が LOCK 後 PAPER の日次リターンで Champion を統計的に上回った場合のみ
  （差の t 検定 p < 0.05、両者 60 営業日以上、Challenger が BACKTEST_PASS 以上）。自動で LIVE にはしない。
"""
from __future__ import annotations

import json
import math

import numpy as np
import pandas as pd
from scipy import stats

from .common import PAPER_DIR, research_plan, utcnow

STATE = PAPER_DIR / "tournament.json"
ORDER = {"RESEARCH_ONLY": 0, "REJECTED": 1, "BACKTEST_PASS": 2, "CHALLENGER": 2, "LIVE_CANDIDATE": 3}


def _get(df: pd.DataFrame, spec_id, period, variant, col):
    r = df[(df.spec_id == spec_id) & (df.period == period) & (df.variant == variant)]
    if not len(r):
        return None
    v = r.iloc[0].get(col)
    return None if v is None or (isinstance(v, float) and not math.isfinite(v)) else v


def gate_b(spec: dict, s2: pd.DataFrame) -> tuple[bool, list[str], dict]:
    g = research_plan()["gates"]
    sid = spec["spec_id"]
    v = {
        "test_trades": _get(s2, sid, "TEST", "portfolio", "n_trades") or 0,
        "test_pf": _get(s2, sid, "TEST", "portfolio", "profit_factor") or 0,
        "test_sharpe": _get(s2, sid, "TEST", "portfolio", "sharpe"),
        "test_mdd": _get(s2, sid, "TEST", "portfolio", "max_drawdown"),
        "test_halted": _get(s2, sid, "TEST", "portfolio", "halted_at"),
        "stress_pf": _get(s2, sid, "TEST", "portfolio_stress_2x", "profit_factor") or 0,
        "fwd_trades": _get(s2, sid, "FORWARD", "portfolio", "n_trades") or 0,
        "fwd_return": _get(s2, sid, "FORWARD", "portfolio", "net_return"),
        "fwd_sharpe": _get(s2, sid, "FORWARD", "portfolio", "sharpe"),
        "fwd_mdd": _get(s2, sid, "FORWARD", "portfolio", "max_drawdown"),
    }
    f = []
    if spec.get("research_only"):
        f.append("gate_A_failed_all_pairs")
    if v["test_trades"] < g["test_min_trades"]:
        f.append("test_trades")
    if v["test_pf"] < g["test_min_profit_factor"]:
        f.append("test_profit_factor")
    if (v["test_sharpe"] if v["test_sharpe"] is not None else -9) < g["test_min_sharpe"]:
        f.append("test_sharpe")
    if (v["test_mdd"] if v["test_mdd"] is not None else -1) < -g["max_drawdown"]:
        f.append("test_max_drawdown")
    if v["test_halted"]:
        f.append("test_kill_switch")
    if v["stress_pf"] < g["stress_min_profit_factor"]:
        f.append("stress_2x_cost")
    if v["fwd_trades"] < g["forward_min_trades"]:
        f.append("forward_trades")
    if (v["fwd_return"] if v["fwd_return"] is not None else -1) <= 0:
        f.append("forward_not_positive")
    if (v["fwd_mdd"] if v["fwd_mdd"] is not None else -1) < -g["max_drawdown"]:
        f.append("forward_max_drawdown")
    if v["test_sharpe"] is not None and v["fwd_sharpe"] is not None \
            and abs(v["test_sharpe"] - v["fwd_sharpe"]) > g["max_sharpe_divergence"]:
        f.append("test_forward_divergence")
    return len(f) == 0, f, v


def paper_gate(daily: pd.Series, n_trades: int, test_sharpe) -> tuple[bool, list[str], dict]:
    g = research_plan()["gates"]
    f = []
    days = len(daily)
    months = days / 21.7
    ret = float((1 + daily).prod() - 1) if days else 0.0
    sr = float(daily.mean() / daily.std(ddof=1) * math.sqrt(260)) if days > 5 and daily.std(ddof=1) > 0 else None
    if months < g["forward_min_months"]:
        f.append(f"paper_months<{g['forward_min_months']}")
    if n_trades < g["forward_min_trades"]:
        f.append("paper_trades")
    if ret <= 0:
        f.append("paper_not_positive")
    if sr is not None and test_sharpe is not None and abs(sr - test_sharpe) > g["max_sharpe_divergence"]:
        f.append("paper_backtest_divergence")
    return len(f) == 0, f, {"paper_days": days, "paper_return": ret, "paper_sharpe": sr, "paper_trades": n_trades}


def beats(ch: pd.Series, champ: pd.Series, min_days: int = 60, alpha: float = 0.05) -> dict:
    j = pd.concat([ch, champ], axis=1, keys=["c", "k"]).dropna()
    if len(j) < min_days:
        return {"beats": False, "reason": f"days {len(j)} < {min_days}"}
    d = j["c"] - j["k"]
    t, p = stats.ttest_1samp(d, 0.0)
    p1 = p / 2 if t > 0 else 1 - p / 2
    return {"beats": bool(p1 < alpha and d.mean() > 0), "t": float(t), "p_one_sided": float(p1), "days": len(j)}


def update(specs: list[dict], s2: pd.DataFrame | None, paper: dict) -> dict:
    """paper: spec_id -> {"daily": Series, "n_trades": int}（LOCK 後 PAPER の成績）。"""
    prev = json.loads(STATE.read_text()) if STATE.exists() else {"champion": None, "history": []}
    rows = []
    for sp in specs:
        sid = sp["spec_id"]
        if sp.get("plan_version", "fx_plan_v1") != "fx_plan_v1":
            # V2: バックテストは汚染あり → 事前登録ゲート合格で CHALLENGER。判断は LOCK 後 PAPER のみ
            fb = list(sp.get("v2_gate_fail", []))
            okb = not fb
            vb = {"test_sharpe": (sp.get("wf_summary") or {}).get("sharpe")}
        elif s2 is not None and len(s2):
            okb, fb, vb = gate_b(sp, s2)
        else:
            okb, fb, vb = False, ["stage2_missing"], {}
        pd_ = paper.get(sid, {"daily": pd.Series(dtype=float), "n_trades": 0})
        okp, fp, vp = paper_gate(pd_["daily"], pd_["n_trades"], vb.get("test_sharpe"))
        v2 = sp.get("plan_version", "fx_plan_v1") != "fx_plan_v1"
        if not v2 and sp.get("research_only"):
            status = "RESEARCH_ONLY"
        elif not okb:
            status = "REJECTED"
        elif not okp:
            status = "CHALLENGER" if v2 else "BACKTEST_PASS"
        else:
            status = "LIVE_CANDIDATE"
        rows.append({"spec_id": sid, "status": status, "gate_b_fail": fb, "paper_gate_fail": fp, **vb, **vp})
    champ = prev.get("champion")
    # Champion は LOCK 後 PAPER Forward 合格（LIVE_CANDIDATE）のみ。バックテストだけでは昇格しない（2026-09-25 方針）
    eligible = [r for r in rows if r["status"] == "LIVE_CANDIDATE"]
    event = None
    if champ and champ not in {r["spec_id"] for r in eligible}:
        event = {"at": utcnow().isoformat(), "event": "champion_demoted", "spec_id": champ}
        champ = None
    if champ is None and eligible:
        best = max(eligible, key=lambda r: (ORDER[r["status"]], r.get("test_sharpe") or -9))
        champ = best["spec_id"]
        event = {"at": utcnow().isoformat(), "event": "champion_initial", "spec_id": champ}
    elif champ:
        for r in eligible:
            if r["spec_id"] == champ:
                continue
            b = beats(paper.get(r["spec_id"], {}).get("daily", pd.Series(dtype=float)),
                      paper.get(champ, {}).get("daily", pd.Series(dtype=float)))
            r["vs_champion"] = b
            if b["beats"]:
                event = {"at": utcnow().isoformat(), "event": "champion_replaced", "from": champ, "to": r["spec_id"], **b}
                champ = r["spec_id"]
    state = {"updated_at": utcnow().isoformat(), "champion": champ,
             "champion_note": None if champ else "LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）",
             "challengers": [r["spec_id"] for r in rows if r["status"] == "CHALLENGER"],
             "live_candidates": [r["spec_id"] for r in rows if r["status"] == "LIVE_CANDIDATE"],
             "live_requires_user_approval": True, "specs": rows,
             "history": prev.get("history", []) + ([event] if event else [])}
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False, default=_js))
    return state


def _js(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    return str(o)
