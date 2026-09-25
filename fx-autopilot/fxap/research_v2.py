"""V2 研究（config/research_plan_v2.yaml）。v1 の結果・LOCK は変更しない。

手続き（候補ごと・ポートフォリオ単位）:
  1. 事前登録グリッドの全点を 2010〜最新で 1 回ずつシミュレーション（コスト込み・研究用 Risk: DD Kill 無効）
  2. 拡張窓 Walk-Forward: 年 Y のパラメータ = 2010〜Y-1 の Sharpe 最大（取引 20 以上）。Y = 2014〜2026 の OOS を連結
  3. 連結 OOS で指標・年別・ペア別・レジーム別・コスト 2 倍・DSR（V2 全試行数で補正）→ 事前登録ゲート
  4. LOCK: 同じ規則を LOCK 時点までの全データに適用したパラメータ（expanding_all）
**全期間とも設計者が既に見た期間（汚染あり）。最終判断は LOCK 後の PAPER Forward。**
"""
from __future__ import annotations

import json
import math
import time
from functools import lru_cache

import numpy as np
import pandas as pd
import yaml

from . import backtest, metrics
from .common import CONFIG, LOCK_DIR, OUT, code_hash, settings, sha, utcnow
from .costs import CostProfile
from .research import regime_breakdown, spec_signals
from .risk import RiskConfig
from .strategies import REGISTRY

RESULTS_V2 = OUT / "research" / "results_v2"
VERSION = {"v": "v2"}      # research-v2 --plan v3 で切り替え（事前登録ファイル・結果ディレクトリ・LOCK の plan_version）


def use(version: str):
    VERSION["v"] = version
    global RESULTS_V2
    RESULTS_V2 = OUT / "research" / f"results_{version}"


@lru_cache(maxsize=None)
def _plan(version: str) -> dict:
    return yaml.safe_load((CONFIG / f"research_plan_{version}.yaml").read_text(encoding="utf-8"))


def plan() -> dict:
    return _plan(VERSION["v"])


def _clean(v):
    if isinstance(v, (np.floating,)):
        v = float(v)
    if isinstance(v, float) and not math.isfinite(v):
        return None
    return v


def risk_for(params: dict, strategy: str, research: bool = True) -> dict:
    d = dict(settings()["risk"])
    d.update(plan()["risk_overrides"])
    cls = REGISTRY[strategy]
    if hasattr(cls, "risk_overrides"):
        d.update(cls(**params).risk_overrides())
    if research:
        d["max_drawdown"] = 1.0          # 研究: Kill で観測を止めない（DD はゲートで判定）
    return d


def simulate(data, strategy, params, pairs, cost: CostProfile):
    spec = {"strategy": strategy, "pairs": {p: params for p in pairs}}
    sig = spec_signals(spec, data, pairs)
    return backtest.run(data, sig, pairs, cost=cost, risk_cfg=RiskConfig.load(risk_for(params, strategy)))


def _year_slice(res, y0, y1):
    return metrics.period_slice(res.equity, res.trades, res.exposure, f"{y0}-01-01", f"{y1}-12-31")


def _sharpe(res, y0, y1, min_trades):
    eq, tr, _ = _year_slice(res, y0, y1)
    if len(eq) < 100 or len(tr) < min_trades:
        return -1e9
    r = metrics.daily_returns(eq)
    sd = r.std(ddof=1)
    return float(r.mean() / sd * math.sqrt(260)) if sd > 0 else -1e9


def walk_forward(runs: dict, wf: dict):
    """runs: params_json -> Result。戻り値: (日次 OOS リターン, OOS トレード, 年ごとの選択)"""
    daily, trades, chosen = [], [], []
    for Y in range(wf["first_test_year"], wf["last_test_year"] + 1):
        best, bsr = next(iter(runs)), -1e9
        for k, res in runs.items():
            sr = _sharpe(res, 2010, Y - 1, wf["min_train_trades"])
            if sr > bsr:
                best, bsr = k, sr
        eq, tr, _ = _year_slice(runs[best], Y, Y)
        if len(eq) < 2:
            continue
        daily.append(metrics.daily_returns(eq))
        trades.append(tr.assign(wf_year=Y, wf_params=best))
        chosen.append({"year": Y, "params": best, "train_sharpe": round(bsr, 3)})
    r = pd.concat(daily) if daily else pd.Series(dtype=float)
    T = pd.concat([t for t in trades if len(t)]) if any(len(t) for t in trades) else pd.DataFrame()
    return r, T, chosen


def oos_summary(r: pd.Series, T: pd.DataFrame, initial=1e6) -> dict:
    if len(r) < 20:
        return {"n_trades": 0}
    eq = (1 + r).cumprod() * initial
    eq.index = pd.DatetimeIndex(eq.index)
    m = metrics.compute(eq, T if len(T) else pd.DataFrame(), None, initial)
    return m


def yearly_table(r: pd.Series, T: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for y, g in r.groupby(r.index.year):
        t = T[T["wf_year"] == y] if len(T) else T
        p = t["pnl_jpy"] if len(t) else pd.Series(dtype=float)
        gl = -p[p <= 0].sum()
        rows.append({"year": int(y), "return": float((1 + g).prod() - 1), "trades": int(len(t)),
                     "profit_factor": float(p[p > 0].sum() / gl) if gl > 0 else None,
                     "cost_jpy": float((t["cost_spread_jpy"] + t["cost_slip_jpy"] + t["commission_jpy"]).sum()) if len(t) else 0.0,
                     "swap_jpy": float(t["swap_jpy"].sum()) if len(t) else 0.0})
    return pd.DataFrame(rows)


def pair_table(T: pd.DataFrame) -> pd.DataFrame:
    if not len(T):
        return pd.DataFrame()
    rows = []
    for p, g in T.groupby("pair"):
        x = g["pnl_jpy"]
        gl = -x[x <= 0].sum()
        rows.append({"pair": p, "trades": int(len(g)), "pnl_jpy": float(x.sum()),
                     "profit_factor": float(x[x > 0].sum() / gl) if gl > 0 else None,
                     "win_rate": float((x > 0).mean()),
                     "avg_cost_jpy": float((g["cost_spread_jpy"] + g["cost_slip_jpy"] + g["commission_jpy"]).mean()),
                     "swap_jpy": float(g["swap_jpy"].sum())})
    return pd.DataFrame(rows)


def gate(c: dict, g: dict) -> list[str]:
    f = []
    if (c.get("n_trades") or 0) < g["wf_min_trades"]:
        f.append("trades")
    if (c.get("profit_factor") or 0) < g["wf_min_profit_factor"]:
        f.append("profit_factor")
    if (c.get("sharpe") or -9) < g["wf_min_sharpe"]:
        f.append("sharpe")
    if (c.get("positive_year_ratio") or 0) < g["wf_min_positive_year_ratio"]:
        f.append("positive_years")
    if (c.get("max_single_year_share") if c.get("max_single_year_share") is not None else 1) > g["wf_max_single_year_share"]:
        f.append("single_year_dependence")
    if (c.get("max_drawdown") if c.get("max_drawdown") is not None else -1) < -g["wf_max_drawdown"]:
        f.append("max_drawdown")
    if g["both_subperiods_positive"] and not ((c.get("ret_A") or -1) > 0 and (c.get("ret_B") or -1) > 0):
        f.append("subperiod_not_positive")
    if (c.get("stress_pf") or 0) < g["stress_min_profit_factor"]:
        f.append("fragile_to_cost_2x")
    if (c.get("positive_pairs") or 0) < g["min_positive_pairs"]:
        f.append("few_positive_pairs")
    if (c.get("max_regime_share") if c.get("max_regime_share") is not None else 1) > g["max_regime_profit_share"]:
        f.append("single_regime_dependence")
    if (c.get("dsr") or 0) < g["deflated_sharpe_min"]:
        f.append("deflated_sharpe")
    if "min_pnl_ex_top5" in g and not ((c.get("diag_pnl_ex_top5") or -1) > g["min_pnl_ex_top5"]):
        f.append("top5_trade_dependence")
    if "max_top1_share" in g and (c.get("diag_top1_share") if c.get("diag_top1_share") is not None else 1) > g["max_top1_share"]:
        f.append("top1_trade_dependence")
    return f


def run(data: dict, only=None, log=print) -> dict:
    P = plan()
    pairs = P["pairs"]
    wf = P["walk_forward"]
    cost = CostProfile.load(P["cost_profile"])
    stress = CostProfile.load(P["stress_profile"])
    names = [n for n in P["candidates"] if not only or n in only]
    refs = [n for n in P["reference_v1"] if not only or n in only]
    all_runs, full_rows, cands = {}, [], []
    t_all = time.time()
    for name in names + refs:
        cls = REGISTRY[name]
        grid = cls.param_grid()
        runs = {}
        for params in grid:
            t0 = time.time()
            k = json.dumps(params, sort_keys=True)
            res = simulate(data, name, params, pairs, cost)
            runs[k] = res
            row = {"candidate": name, "is_v2": name in names, "params": k}
            for tag, (a, b) in (("full", (2010, 2026)), ("A", (2014, 2021)), ("B", (2022, 2026))):
                eq, tr, ex = _year_slice(res, a, b)
                m = metrics.compute(eq, tr, ex) if len(eq) > 50 else {}
                for kk in ("n_trades", "net_return", "sharpe", "profit_factor", "max_drawdown", "cost_ratio"):
                    row[f"{tag}_{kk}"] = _clean(m.get(kk))
            full_rows.append(row)
            log(f"  {name:22s} {k:70s} full SR={row['full_sharpe']} ({time.time() - t0:.0f}s)")
        all_runs[name] = runs
    trial_sr = [r["full_sharpe"] for r in full_rows if r["is_v2"] and r["full_sharpe"] is not None]
    n_trials = sum(1 for r in full_rows if r["is_v2"])
    yearly, pairsT, regimes, chosen_all = [], [], [], []
    for name in names + refs:
        runs = all_runs[name]
        r, T, chosen = walk_forward(runs, wf)
        m = oos_summary(r, T)
        yt = yearly_table(r, T)
        yr = yt["return"].to_numpy() if len(yt) else np.array([])
        pos = yr[yr > 0]
        m["positive_year_ratio"] = float((yr > 0).mean()) if len(yr) else 0.0
        m["max_single_year_share"] = float(pos.max() / pos.sum()) if len(pos) else 1.0
        a0, a1 = wf["subperiods"]["A_2014_2021"]
        b0, b1 = wf["subperiods"]["B_2022_2026"]
        m["ret_A"] = float((1 + r[(r.index.year >= a0) & (r.index.year <= a1)]).prod() - 1) if len(r) else None
        m["ret_B"] = float((1 + r[(r.index.year >= b0) & (r.index.year <= b1)]).prod() - 1) if len(r) else None
        pt = pair_table(T)
        m["positive_pairs"] = int((pt["pnl_jpy"] > 0).sum()) if len(pt) else 0
        rg = pd.DataFrame(regime_breakdown(name, T, data)) if len(T) else pd.DataFrame()
        if len(rg):
            r4 = rg[rg.dimension == "regime4h"]
            prof = r4["pnl_jpy"].clip(lower=0)
            m["max_regime_share"] = float(prof.max() / prof.sum()) if prof.sum() > 0 else 1.0
        # コスト 2 倍: WF で選ばれたパラメータの列を stress コストで再現
        sruns = {k: simulate(data, name, json.loads(k), pairs, stress) for k in {c["params"] for c in chosen}}
        sr_, sT = _replay(sruns, chosen)
        sm = oos_summary(sr_, sT)
        m["stress_pf"] = sm.get("profit_factor")
        m["stress_net_return"] = sm.get("net_return")
        d = metrics.deflated_sharpe(r, max(2, n_trials), trial_sr)
        m["dsr"] = d.get("dsr")
        m["n_trials_v2"] = n_trials
        m["final_params"] = max(runs, key=lambda k: (_sharpe(runs[k], 2010, 2026, wf["min_train_trades"]), k))
        m["param_changes"] = len({c["params"] for c in chosen})
        # 診断（報告のみ・ゲートには使わない。ゲートは事前登録から変更しない）: 少数トレードへの利益集中と直近期間
        if len(T):
            pn = T["pnl_jpy"].sort_values(ascending=False)
            tot = float(pn.sum())
            m["diag_top1_share"] = float(pn.iloc[0] / tot) if tot > 0 else None
            m["diag_top5_share"] = float(pn.iloc[:5].sum() / tot) if tot > 0 else None
            m["diag_pnl_ex_top5"] = float(pn.iloc[5:].sum())
            rest = pn.iloc[5:]
            gl = -rest[rest <= 0].sum()
            m["diag_pf_ex_top5"] = float(rest[rest > 0].sum() / gl) if gl > 0 else None
            m["diag_swap_share"] = float(T["swap_jpy"].sum() / tot) if tot > 0 else None
        m["diag_ret_2024_2026"] = float((1 + r[r.index.year >= 2024]).prod() - 1) if len(r) else None
        fails = gate(m, P["gates"]) if name in names else ["reference_v1"]
        cands.append({"candidate": name, "is_v2": name in names, "family": REGISTRY[name].family,
                      **{k: _clean(v) for k, v in m.items()}, "gate_fail": fails})
        yearly += [{"candidate": name, **row} for row in yt.to_dict("records")]
        pairsT += [{"candidate": name, **row} for row in pt.to_dict("records")]
        regimes += [{"candidate": name, **row} for row in rg.to_dict("records")] if len(rg) else []
        chosen_all += [{"candidate": name, **c} for c in chosen]
        log(f"  WF {name:22s} trades={m.get('n_trades')} ret={m.get('net_return')} PF={m.get('profit_factor')} "
            f"SR={m.get('sharpe')} DD={m.get('max_drawdown')} fail={fails}")
    C = pd.DataFrame(cands)
    # ML は同じ手続きの最良の単純 V2 戦略を上回ること
    simple = C[(C.is_v2) & (C.family != "ml")]
    best_simple = simple["sharpe"].max() if len(simple) else None
    for i, row in C.iterrows():
        if row["is_v2"] and row["family"] == "ml" and P["gates"]["ml_must_beat_best_simple"]:
            if best_simple is None or (row["sharpe"] or -9) <= best_simple:
                C.at[i, "gate_fail"] = list(row["gate_fail"]) + ["ml_not_better_than_simple"]
    C["status"] = [("CHALLENGER" if not f else "REJECTED") if v else "REFERENCE_V1" for f, v in zip(C["gate_fail"], C["is_v2"])]
    log(f"V2 research done in {time.time() - t_all:.0f}s")
    return {"candidates": C, "grid": pd.DataFrame(full_rows), "yearly": pd.DataFrame(yearly),
            "pairs": pd.DataFrame(pairsT), "regimes": pd.DataFrame(regimes), "chosen": pd.DataFrame(chosen_all)}


def _replay(runs_by_param: dict, chosen: list):
    daily, trades = [], []
    for c in chosen:
        res = runs_by_param[c["params"]]
        eq, tr, _ = _year_slice(res, c["year"], c["year"])
        if len(eq) < 2:
            continue
        daily.append(metrics.daily_returns(eq))
        trades.append(tr.assign(wf_year=c["year"]))
    r = pd.concat(daily) if daily else pd.Series(dtype=float)
    T = pd.concat([t for t in trades if len(t)]) if any(len(t) for t in trades) else pd.DataFrame()
    return r, T


def lock(C: pd.DataFrame, data_end: str, log=print) -> list[dict]:
    LOCK_DIR.mkdir(parents=True, exist_ok=True)
    P = plan()
    specs = []
    for _, r in C[C.is_v2].iterrows():
        params = json.loads(r["final_params"])
        spec = {
            "spec_id": r["candidate"], "strategy": r["candidate"], "strategy_version": VERSION["v"],
            "family": r["family"], "plan_version": P["plan_version"],
            "pairs": {p: params for p in P["pairs"]}, "trade_pairs": list(P["pairs"]),
            "risk": risk_for(params, r["candidate"], research=False), "cost_profile": P["cost_profile"],
            "selection": "expanding_all (2010〜LOCK 時点、Sharpe 最大)", "selection_data_end": data_end,
            "v2_status": r["status"], "v2_gate_fail": list(r["gate_fail"]),
            "wf_summary": {k: _clean(r.get(k)) for k in ("n_trades", "net_return", "profit_factor", "sharpe",
                                                           "max_drawdown", "ret_A", "ret_B", "stress_pf", "dsr")},
            "contaminated_backtest": True, "research_only": r["status"] != "CHALLENGER",
            "code_hash": code_hash(),
        }
        body = {k: v for k, v in spec.items() if k not in ("wf_summary", "v2_status", "v2_gate_fail", "research_only")}
        spec["spec_hash"] = sha(body)
        path = LOCK_DIR / f"{spec['spec_id']}.json"
        if path.exists():
            # LOCK ファイルは作成後に一切書き換えない。再計算で中身（パラメータ・Risk・コスト）が変わった場合だけ別ログに記録
            old = json.loads(path.read_text())
            keys = ("pairs", "trade_pairs", "risk", "cost_profile", "strategy")
            if any(old.get(k) != spec.get(k) for k in keys):
                RESULTS_V2.mkdir(parents=True, exist_ok=True)
                with (RESULTS_V2 / "relock_refusals.jsonl").open("a", encoding="utf-8") as f:
                    f.write(json.dumps({"at": utcnow().isoformat(), "spec_id": spec["spec_id"],
                                        "diff_keys": [k for k in keys if old.get(k) != spec.get(k)],
                                        "new_params": next(iter(spec["pairs"].values()))}, ensure_ascii=False) + "\n")
                log(f"  LOCK 済み {spec['spec_id']} は変更しない（再計算の結果が異なる。改善は次バージョンで）")
            specs.append(old)
            continue
        spec["locked_at"] = utcnow().isoformat()
        path.write_text(json.dumps(spec, indent=2, ensure_ascii=False))
        log(f"  LOCK {spec['spec_id']} params={params} status={r['status']}")
        specs.append(spec)
    return specs


def write(out: dict, specs: list, data_end: str) -> str:
    d = RESULTS_V2 / utcnow().strftime("%Y%m%d")
    d.mkdir(parents=True, exist_ok=True)
    for k, v in out.items():
        v2 = v.copy()
        if "gate_fail" in v2:
            v2["gate_fail"] = v2["gate_fail"].map(lambda x: ";".join(x))
        v2.to_csv(d / f"{k}.csv", index=False)
    md = summary_md(out, specs, data_end)
    (d / f"SUMMARY_{VERSION['v'].upper()}.md").write_text(md, encoding="utf-8")
    import shutil
    latest = RESULTS_V2 / "LATEST"
    if latest.exists():
        shutil.rmtree(latest)
    shutil.copytree(d, latest)
    return md


def summary_md(out, specs, data_end) -> str:
    from .report import _t
    P, F2, D = "{:+.1%}", "{:.2f}", "{:.1%}"
    C = out["candidates"].copy()
    C["gate_fail"] = C["gate_fail"].map(lambda x: ", ".join(x))
    L = [f"# FX AUTOPILOT {VERSION['v'].upper()} 研究結果（{utcnow():%Y-%m-%d %H:%M} UTC、データ〜{data_end}）", "",
         f"**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_{VERSION['v']}.yaml`", "",
         "> **検証汚染の申告**: " + " ".join(str(plan().get("contamination", "")).split()), "",
         "コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。",
         "単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。", "",
         "## 候補一覧（WF OOS 連結・コスト込み）", "",
         _t(C.sort_values(["is_v2", "sharpe"], ascending=[False, False]),
            ["candidate", "status", "n_trades", "net_return", "cagr", "profit_factor", "sharpe", "sortino", "max_drawdown",
             "expectancy_jpy", "cost_per_trade_jpy", "cost_ratio", "max_consecutive_losses", "positive_year_ratio",
             "max_single_year_share", "ret_A", "ret_B", "stress_pf", "positive_pairs", "max_regime_share", "dsr",
             "param_changes", "gate_fail"],
            {"net_return": P, "cagr": P, "profit_factor": F2, "sharpe": F2, "sortino": F2, "max_drawdown": D,
             "expectancy_jpy": "{:,.0f}", "cost_per_trade_jpy": "{:,.0f}", "cost_ratio": F2,
             "positive_year_ratio": "{:.0%}", "max_single_year_share": "{:.0%}", "ret_A": P, "ret_B": P,
             "stress_pf": F2, "max_regime_share": "{:.0%}", "dsr": F2}),
         "ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。", "",
         "## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近", "",
         _t(C[C.is_v2], ["candidate", "status", "n_trades", "diag_top1_share", "diag_top5_share", "diag_pnl_ex_top5",
                         "diag_pf_ex_top5", "diag_swap_share", "diag_ret_2024_2026"],
            {"diag_top1_share": "{:.0%}", "diag_top5_share": "{:.0%}", "diag_pnl_ex_top5": "{:+,.0f}",
             "diag_pf_ex_top5": F2, "diag_swap_share": "{:.0%}", "diag_ret_2024_2026": P}),
         "上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。", ""]
    Y = out["yearly"]
    if len(Y):
        L += ["## 年別 Return（WF OOS）", "",
              _t(Y.pivot_table(index="year", columns="candidate", values="return").reset_index(),
                 ["year"] + list(C["candidate"]), {k: P for k in C["candidate"]}),
              "## 年別 Profit Factor（WF OOS）", "",
              _t(Y.pivot_table(index="year", columns="candidate", values="profit_factor").reset_index(),
                 ["year"] + list(C["candidate"]), {k: F2 for k in C["candidate"]})]
    Pt = out["pairs"]
    if len(Pt):
        L += ["## 通貨ペア別（WF OOS）", "",
              _t(Pt, ["candidate", "pair", "trades", "pnl_jpy", "profit_factor", "win_rate", "avg_cost_jpy", "swap_jpy"],
                 {"pnl_jpy": "{:+,.0f}", "profit_factor": F2, "win_rate": "{:.0%}", "avg_cost_jpy": "{:,.0f}",
                  "swap_jpy": "{:+,.0f}"})]
    R = out["regimes"]
    if len(R):
        L += ["## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）", "",
              _t(R, ["candidate", "dimension", "state", "trades", "pnl_jpy", "win_rate", "profit_factor"],
                 {"pnl_jpy": "{:+,.0f}", "win_rate": "{:.0%}", "profit_factor": F2})]
    G = out["grid"]
    for dim, cands in (("session", ["v2_session_breakout"]), ("sizing", ["v2_d1_donchian", "v2_d1_tsmom", "v2_xpair_strength", "v2_trend_carry",
                                  "v3_carry_trend_xs", "v3_carry_only"]),
                       ("regime", ["v2_d1_donchian", "v2_h4_ema"])):
        g = G[G.candidate.isin(cands)].copy()
        if not len(g):
            continue
        g[dim] = g["params"].map(lambda s: json.loads(s).get(dim))
        agg = g.groupby(["candidate", dim]).agg(full_sharpe=("full_sharpe", "mean"), A_sharpe=("A_sharpe", "mean"),
                                                B_sharpe=("B_sharpe", "mean"), full_pf=("full_profit_factor", "mean"),
                                                full_ret=("full_net_return", "mean"), trades=("full_n_trades", "mean"),
                                                max_dd=("full_max_drawdown", "mean")).reset_index()
        L += [f"## 比較: {dim}（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）", "",
              _t(agg, ["candidate", dim, "trades", "full_ret", "full_pf", "full_sharpe", "A_sharpe", "B_sharpe", "max_dd"],
                 {"full_ret": P, "full_pf": F2, "full_sharpe": F2, "A_sharpe": F2, "B_sharpe": F2, "trades": "{:.0f}",
                  "max_dd": D})]
    L += ["## LOCK（V2・PAPER Forward 用）", "",
          _t(pd.DataFrame([{"spec_id": s["spec_id"], "status": s.get("v2_status"), "params": json.dumps(next(iter(s["pairs"].values())), ensure_ascii=False),
                            "sizing": s["risk"].get("sizing"), "locked_at": s.get("locked_at", "")[:16],
                            "spec_hash": s["spec_hash"][:12]} for s in specs]),
             ["spec_id", "status", "params", "sizing", "locked_at", "spec_hash"]),
          "CHALLENGER でも自動で Champion にはならない。Champion 昇格は LOCK 後 PAPER Forward（3 か月・20 取引・プラス・乖離）合格が必須。", ""]
    return "\n".join(L)
