"""研究パイプライン（事前登録 → Walk-Forward → LOCK → TEST/FORWARD を 1 回だけ評価）。

Stage 1（選択）: データを VALIDATION 終了日で**物理的に切り詰めてから**全戦略 × 全パラメータ × 全ペアを評価。
         Walk-Forward（4 年学習 → 翌 1 年）で「パラメータ選択という手続き」ごと未知期間で評価し、
         最終パラメータは TRAIN の Sharpe 最大で選ぶ。TEST / FORWARD のデータはこの段階のコードに渡らない。
LOCK    : 戦略・ペアごとのパラメータ・Risk 設定・コスト設定・コードハッシュを config/locked/ に固定。
         同じ ID で中身が違う LOCK は拒否（改善は _v2 として別候補）。
Stage 2（検証）: LOCK 済み仕様だけを TEST / FORWARD で評価（コスト・レバレッジ・局面別も）。結果は追記のみ。
"""
from __future__ import annotations

import json
import math
import time

import numpy as np
import pandas as pd

from . import backtest, metrics
from .common import LOCK_DIR, RESULTS, code_hash, research_plan, settings, sha, utcnow
from .costs import CostProfile
from .risk import RiskConfig
from .strategies import REGISTRY, get
from .strategies.regime import label as regime_label
from .strategies.regime import regime_frame

CANDIDATE_STRATEGIES = ["trend_ema_adx", "trend_donchian", "trend_tsmom", "mr_rsi_bb", "mr_zscore",
                        "regime_switch", "mtf_pullback", "ml_logit", "ml_lgbm"]
SPEC_VERSION = "v1"


def _research_risk() -> RiskConfig:
    """Stage 1 は DD による Kill Switch を無効化して全期間を観測する（DD はゲートで判定）。日次・週次の上限は有効。"""
    return RiskConfig.load({"max_drawdown": 1.0})


def truncate(data: dict, end: str) -> dict:
    e = pd.Timestamp(end, tz="UTC") + pd.Timedelta(days=1)
    return {p: d[d.index < e] for p, d in data.items()}


def _slice_metrics(res, start, end):
    eq, tr, ex = metrics.period_slice(res.equity, res.trades, res.exposure, start, end)
    if len(eq) < 50:
        return {"n_trades": 0}
    return metrics.compute(eq, tr, ex)


def _clean(v):
    if isinstance(v, float) and not math.isfinite(v):
        return None
    return v


# ============================================================ Stage 1
def stage1(data: dict, pairs, strategies=None, log=print) -> dict:
    plan = research_plan()
    sp = plan["splits"]
    wf = plan["walk_forward"]
    sel_end = sp["VALIDATION"][1]
    d1 = truncate(data, sel_end)
    assert all(d.index.max() <= pd.Timestamp(sel_end, tz="UTC") + pd.Timedelta(hours=23) for d in d1.values())
    cost = CostProfile.load()
    rcfg = _research_risk()
    strategies = strategies or CANDIDATE_STRATEGIES
    trials, wf_rows, cand_rows = [], [], []
    years = list(range(wf["first_test_year"], wf["last_test_year"] + 1))
    daily_by_trial: dict = {}
    for sname in strategies:
        cls = REGISTRY[sname]
        for pair in pairs:
            runs = {}
            for params in cls.param_grid():
                t0 = time.time()
                strat = cls(**params)
                sig = strat.generate(d1[pair], pair)
                res = backtest.run(d1, {pair: sig}, [pair], cost=cost, risk_cfg=rcfg)
                runs[json.dumps(params, sort_keys=True)] = res
                row = {"strategy": sname, "pair": pair, "params": json.dumps(params, sort_keys=True)}
                for split in ("TRAIN", "VALIDATION"):
                    m = _slice_metrics(res, *sp[split])
                    for k in ("n_trades", "net_return", "sharpe", "profit_factor", "max_drawdown", "win_rate", "cost_ratio"):
                        row[f"{split.lower()}_{k}"] = _clean(m.get(k))
                trials.append(row)
                daily_by_trial[(sname, pair, row["params"])] = metrics.daily_returns(res.equity)
                log(f"  {sname:15s} {pair} {row['params']:45s} train SR={row['train_sharpe']} "
                    f"val SR={row['validation_sharpe']} ({time.time() - t0:.1f}s)")
            # ---- Walk-Forward: 各年 Y を、[Y-4, Y-1] の Sharpe 最大パラメータで取引
            oos_daily, oos_trades, chosen_list = [], [], []
            for Y in years:
                tr_s, tr_e = f"{Y - wf['train_years']}-01-01", f"{Y - 1}-12-31"
                best, best_sr = next(iter(runs)), -1e9
                for k, res in runs.items():
                    m = _slice_metrics(res, tr_s, tr_e)
                    sr = m.get("sharpe", -1e9) if m.get("n_trades", 0) >= 5 else -1e9
                    if sr > best_sr:
                        best, best_sr = k, sr
                res = runs[best]
                eq, tr, ex = metrics.period_slice(res.equity, res.trades, res.exposure, f"{Y}-01-01", f"{Y}-12-31")
                m = metrics.compute(eq, tr, ex) if len(eq) > 50 else {"n_trades": 0}
                oos_daily.append(metrics.daily_returns(eq))
                oos_trades.append(tr)
                chosen_list.append(best)
                wf_rows.append({"strategy": sname, "pair": pair, "year": Y, "chosen_params": best,
                                "train_sharpe": round(best_sr, 4), "oos_return": _clean(m.get("net_return")),
                                "oos_sharpe": _clean(m.get("sharpe")), "oos_trades": m.get("n_trades", 0),
                                "oos_pf": _clean(m.get("profit_factor"))})
            r = pd.concat(oos_daily) if oos_daily else pd.Series(dtype=float)
            T = pd.concat([x for x in oos_trades if len(x)]) if any(len(x) for x in oos_trades) else pd.DataFrame()
            eq_oos = (1 + r).cumprod() * 1e6
            m_oos = metrics.compute(eq_oos, T) if len(eq_oos) > 50 else {"n_trades": 0}
            yr = [w for w in wf_rows if w["strategy"] == sname and w["pair"] == pair]
            yr_ret = np.array([w["oos_return"] or 0.0 for w in yr])
            max_share = float(yr_ret.max() / yr_ret[yr_ret > 0].sum()) if (yr_ret > 0).any() else 1.0
            # ---- 最終パラメータ: TRAIN Sharpe 最大
            tr_rows = [t for t in trials if t["strategy"] == sname and t["pair"] == pair]
            final = max(tr_rows, key=lambda t: ((t["train_sharpe"] or -1e9) if (t["train_n_trades"] or 0) >= 10
                                                else -1e9, t["params"]))
            cand_rows.append({
                "strategy": sname, "family": cls.family, "pair": pair, "final_params": final["params"],
                "wf_trades": m_oos.get("n_trades", 0), "wf_net_return": _clean(m_oos.get("net_return")),
                "wf_cagr": _clean(m_oos.get("cagr")), "wf_sharpe": _clean(m_oos.get("sharpe")),
                "wf_profit_factor": _clean(m_oos.get("profit_factor")), "wf_max_drawdown": _clean(m_oos.get("max_drawdown")),
                "wf_positive_year_ratio": float((yr_ret > 0).mean()) if len(yr_ret) else 0.0,
                "wf_max_single_year_share": max_share, "wf_param_changes": len(set(chosen_list)),
                "train_sharpe": final["train_sharpe"], "val_sharpe": final["validation_sharpe"],
                "val_profit_factor": final["validation_profit_factor"], "val_trades": final["validation_n_trades"],
                "val_max_drawdown": final["validation_max_drawdown"], "wf_psr": _clean(m_oos.get("psr_vs_zero")),
                "_wf_daily": r,
            })
    # ---- 多重検定: 全試行の Sharpe 分布で Deflated Sharpe
    n_trials = len(trials)
    tr_sr = [t["train_sharpe"] for t in trials if t["train_sharpe"] is not None]
    for c in cand_rows:
        d = metrics.deflated_sharpe(c.pop("_wf_daily"), n_trials, tr_sr)
        c["wf_dsr"] = d.get("dsr")
        c["n_trials"] = n_trials
        c["gate_A"], c["gate_A_fail"] = gate_a(c, plan["gates"])
    return {"trials": pd.DataFrame(trials), "walk_forward": pd.DataFrame(wf_rows),
            "candidates": pd.DataFrame(cand_rows), "selection_end": sel_end, "n_trials": n_trials}


def gate_a(c: dict, g: dict):
    fails = []

    def need(name, ok):
        if not ok:
            fails.append(name)

    need("wf_trades", (c["wf_trades"] or 0) >= g["wf_min_trades"])
    need("wf_profit_factor", (c["wf_profit_factor"] or 0) >= g["wf_min_profit_factor"])
    need("wf_sharpe", (c["wf_sharpe"] or -9) >= g["wf_min_sharpe"])
    need("wf_positive_years", c["wf_positive_year_ratio"] >= g["wf_min_positive_year_ratio"])
    need("wf_single_year_share", c["wf_max_single_year_share"] <= g["max_single_year_profit_share"])
    need("wf_max_drawdown", (c["wf_max_drawdown"] or -1) >= -g["max_drawdown"])
    need("val_profit_factor", (c["val_profit_factor"] or 0) >= g["val_min_profit_factor"])
    return (len(fails) == 0), ";".join(fails)


# ============================================================ LOCK
def lock_specs(cands: pd.DataFrame, selection_end: str, data_fingerprint: dict, log=print) -> list[dict]:
    LOCK_DIR.mkdir(parents=True, exist_ok=True)
    cfg = settings()
    specs = []
    for sname, g in cands.groupby("strategy", sort=False):
        spec = {
            "spec_id": f"{sname}_{SPEC_VERSION}",
            "strategy": sname, "strategy_version": REGISTRY[sname].version, "family": REGISTRY[sname].family,
            "pairs": {r["pair"]: json.loads(r["final_params"]) for _, r in g.iterrows()},
            "gate_A_pairs": [r["pair"] for _, r in g.iterrows() if r["gate_A"]],
            # 取引ペア: ゲート A 合格ペア。合格ゼロなら全ペアを「研究観測のみ」で PAPER 追跡（LIVE 候補にはならない）
            "trade_pairs": [r["pair"] for _, r in g.iterrows() if r["gate_A"]] or list(g["pair"]),
            "research_only": not bool(g["gate_A"].any()),
            "risk": cfg["risk"], "cost_profile": cfg["costs"]["default_profile"],
            "plan_version": research_plan()["plan_version"], "selection_data_end": selection_end,
            "data_fingerprint": data_fingerprint, "code_hash": code_hash(),
        }
        body = {k: v for k, v in spec.items() if k not in ("data_fingerprint",)}
        spec["spec_hash"] = sha(body)
        path = LOCK_DIR / f"{spec['spec_id']}.json"
        if path.exists():
            old = json.loads(path.read_text())
            if old["spec_hash"] != spec["spec_hash"]:
                log(f"  LOCK 済み {spec['spec_id']} と中身が異なるため既存 LOCK を使用（変更は新バージョンで）")
                diff = {k: (old.get(k), spec.get(k)) for k in ("pairs", "risk", "code_hash") if old.get(k) != spec.get(k)}
                old.setdefault("relock_refusals", []).append({"at": utcnow().isoformat(), "diff_keys": list(diff)})
                path.write_text(json.dumps(old, indent=2, ensure_ascii=False))
            specs.append(old)
            continue
        spec["locked_at"] = utcnow().isoformat()
        path.write_text(json.dumps(spec, indent=2, ensure_ascii=False))
        log(f"  LOCK {spec['spec_id']} {spec['spec_hash'][:12]}")
        specs.append(spec)
    return specs


def load_locked() -> list[dict]:
    return [json.loads(p.read_text()) for p in sorted(LOCK_DIR.glob("*.json"))]


# ============================================================ Stage 2
def spec_signals(spec: dict, data: dict, pairs=None) -> dict:
    out = {}
    for p in (pairs or spec["pairs"]):
        out[p] = get(spec["strategy"], **spec["pairs"][p]).generate(data[p], p)
    return out


def stage2(specs: list[dict], data: dict, log=print) -> dict:
    plan = research_plan()
    sp = plan["splits"]
    cfg = settings()
    rows, lev_rows, regime_rows, event_rows, yearly_rows = [], [], [], [], []
    base_cost = CostProfile.load()
    for spec in specs:
        t0 = time.time()
        sig = spec_signals(spec, data)
        pairs = list(spec.get("trade_pairs") or spec["pairs"])
        rcfg = RiskConfig.load(cfg=cfg)

        def run(start, end, pp=None, cost=base_cost, risk=rcfg):
            pp = pp or pairs
            return backtest.run(data, {p: sig[p] for p in pp}, pp, cost=cost, risk_cfg=risk, start=start, end=end)

        for period in ("TEST", "FORWARD"):
            s, e = sp[period]
            variants = [("portfolio", pairs, base_cost), ("portfolio_stress_2x", pairs, CostProfile.load("stress_2x")),
                        ("portfolio_ibkr", pairs, CostProfile.load("ibkr"))]
            variants += [(p, [p], base_cost) for p in spec["pairs"]]
            for vname, pp, cst in variants:
                res = run(s, e, pp, cst)
                m = metrics.compute(res.equity, res.trades, res.exposure)
                rows.append({"spec_id": spec["spec_id"], "period": period, "variant": vname, "cost_profile": cst.name,
                             "halted_at": res.halted_at, **{k: _clean(v) for k, v in m.items()}})
        # レバレッジ比較（TEST + FORWARD を通しで、同じシグナル）
        for lname, lp in cfg["leverage_profiles"].items():
            res = run(sp["TEST"][0], None, risk=RiskConfig.load(lp, cfg=cfg))
            m = metrics.compute(res.equity, res.trades, res.exposure)
            lev_rows.append({"spec_id": spec["spec_id"], "leverage_profile": lname, **lp, "halted_at": res.halted_at,
                             **{k: _clean(m.get(k)) for k in ("n_trades", "net_return", "cagr", "sharpe", "max_drawdown",
                                                              "profit_factor", "avg_leverage", "max_leverage")}})
        # 全期間（研究用の Kill 無効設定）: 年別・局面別・イベント別
        full = run(None, None, risk=_research_risk())
        for _, yr in metrics.yearly(full.equity, full.trades).iterrows():
            yearly_rows.append({"spec_id": spec["spec_id"], **{k: _clean(v) for k, v in yr.to_dict().items()}})
        regime_rows += regime_breakdown(spec["spec_id"], full.trades, data)
        for ev, (a, b) in plan["events"].items():
            eq, tr, _ = metrics.period_slice(full.equity, full.trades, None, a, b)
            if len(eq) < 2:
                continue
            event_rows.append({"spec_id": spec["spec_id"], "event": ev, "return": float(eq.iloc[-1] / eq.iloc[0] - 1),
                               "max_drawdown": metrics.max_drawdown(eq), "trades": int(len(tr)),
                               "pnl_jpy": float(tr["pnl_jpy"].sum()) if len(tr) else 0.0})
        log(f"  stage2 {spec['spec_id']} ({time.time() - t0:.0f}s)")
    return {"stage2": pd.DataFrame(rows), "leverage": pd.DataFrame(lev_rows), "regimes": pd.DataFrame(regime_rows),
            "events": pd.DataFrame(event_rows), "yearly": pd.DataFrame(yearly_rows)}


def regime_breakdown(spec_id: str, trades: pd.DataFrame, data: dict) -> list[dict]:
    """エントリー時点の相場状態（4H レジーム + 月次の方向・ボラ）ごとの損益。"""
    if trades is None or not len(trades):
        return []
    out = []
    tr = trades.copy()
    tr["entry_time"] = pd.to_datetime(tr["entry_time"])
    labs = []
    for pair, g in tr.groupby("pair"):
        rf = regime_frame(data[pair])
        lab = regime_label(rf).reindex(g["entry_time"], method="ffill").to_numpy()
        c = ((data[pair]["bid_c"] + data[pair]["ask_c"]) / 2).resample("ME").last()
        mret = np.log(c).diff()
        mvol = np.log((data[pair]["bid_c"] + data[pair]["ask_c"]) / 2).diff().resample("ME").std()
        vol_hi = mvol > mvol.expanding(12).median()
        direction = np.where(mret > 0.02, "UP", np.where(mret < -0.02, "DOWN", "FLAT"))
        mk = (g["entry_time"].dt.tz_convert(None).dt.to_period("M").dt.to_timestamp(how="end")
              .dt.normalize().dt.tz_localize("UTC"))
        dd = pd.Series(direction, index=c.index.normalize())
        vv = pd.Series(np.where(vol_hi.to_numpy(), "HIGH_VOL", "LOW_VOL"), index=vol_hi.index.normalize())
        labs.append(pd.DataFrame({"i": g.index, "regime4h": lab, "month_dir": dd.reindex(mk).to_numpy(),
                                  "month_vol": vv.reindex(mk).to_numpy()}))
    L = pd.concat(labs).set_index("i")
    tr = tr.join(L)
    for col in ("regime4h", "month_dir", "month_vol"):
        for k, g in tr.groupby(col):
            p = g["pnl_jpy"]
            gl = -p[p <= 0].sum()
            out.append({"spec_id": spec_id, "dimension": col, "state": k, "trades": int(len(g)),
                        "pnl_jpy": float(p.sum()), "win_rate": float((p > 0).mean()),
                        "profit_factor": float(p[p > 0].sum() / gl) if gl > 0 else None})
    return out


def random_baseline(data: dict, pairs, seeds=10) -> pd.DataFrame:
    plan = research_plan()
    sel_end = plan["splits"]["VALIDATION"][1]
    d1 = truncate(data, sel_end)
    rows = []
    for pair in pairs:
        for s in range(seeds):
            sig = get("random", p=0.01, seed=s).generate(d1[pair], pair)
            res = backtest.run(d1, {pair: sig}, [pair], risk_cfg=_research_risk())
            m = metrics.compute(res.equity, res.trades)
            rows.append({"pair": pair, "seed": s, "sharpe": m.get("sharpe"), "net_return": m.get("net_return"),
                         "profit_factor": m.get("profit_factor"), "n_trades": m.get("n_trades"),
                         "cost_ratio": m.get("cost_ratio")})
    return pd.DataFrame(rows)


def microstructure(data: dict) -> pd.DataFrame:
    """セッション（UTC 時間帯）ごとの実測スプレッドとボラティリティ（直近 2 年）。"""
    from .common import PAIRS
    rows = []
    for pair, d in data.items():
        d = d[d.index >= d.index.max() - pd.Timedelta(days=730)]
        pip = PAIRS[pair]["pip"]
        sp = (d["ask_c"] - d["bid_c"]) / pip
        m = (d["ask_c"] + d["bid_c"]) / 2
        rng = ((d["ask_h"] + d["bid_h"]) / 2 - (d["ask_l"] + d["bid_l"]) / 2) / pip
        for h in range(24):
            k = d.index.hour == h
            if k.sum() == 0:
                continue
            rows.append({"pair": pair, "hour_utc": h, "spread_median_pips": round(float(sp[k].median()), 3),
                         "spread_p95_pips": round(float(sp[k].quantile(0.95)), 3),
                         "range_median_pips": round(float(rng[k].median()), 2),
                         "spread_to_range": round(float(sp[k].median() / max(rng[k].median(), 1e-9)), 4),
                         "volume_median": float(d["volume"][k].median()), "bars": int(k.sum())})
        del m
    return pd.DataFrame(rows)
