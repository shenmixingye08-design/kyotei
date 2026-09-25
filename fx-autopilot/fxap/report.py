"""研究結果の保存（CSV / JSON）と SUMMARY.md の生成。"""
from __future__ import annotations

import json
import shutil

import pandas as pd

from .common import RESULTS, research_plan, settings, utcnow


def _t(df: pd.DataFrame, cols: list, fmt: dict | None = None, max_rows: int = 200) -> str:
    if df is None or not len(df):
        return "_（なし）_\n"
    fmt = fmt or {}
    cols = [c for c in cols if c in df.columns]
    out = ["| " + " | ".join(cols) + " |", "|" + "|".join("---" for _ in cols) + "|"]
    for _, r in df.head(max_rows).iterrows():
        cells = []
        for c in cols:
            v = r[c]
            if v is None or (isinstance(v, float) and pd.isna(v)):
                cells.append("—")
            elif c in fmt:
                try:
                    cells.append(fmt[c].format(v))
                except (ValueError, TypeError):
                    cells.append(str(v))
            else:
                cells.append(str(v))
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out) + "\n"


P = "{:+.1%}"
F2 = "{:.2f}"
D = "{:.1%}"


def write(outdir, quality, s1: dict | None, specs, s2: dict, rnd: pd.DataFrame, micro: pd.DataFrame, tour: dict):
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "data_quality.json").write_text(json.dumps(quality, indent=2, ensure_ascii=False))
    if s1:
        for k in ("trials", "walk_forward", "candidates"):
            s1[k].to_csv(outdir / f"{k}.csv", index=False)
    for k, v in s2.items():
        v.to_csv(outdir / f"{k}.csv", index=False)
    rnd.to_csv(outdir / "random_baseline.csv", index=False)
    micro.to_csv(outdir / "microstructure.csv", index=False)
    (outdir / "locked_specs.json").write_text(json.dumps(specs, indent=2, ensure_ascii=False, default=str))
    (outdir / "tournament.json").write_text(json.dumps(tour, indent=2, ensure_ascii=False, default=str))
    md = summary_md(quality, s1, specs, s2, rnd, micro, tour)
    (outdir / "SUMMARY.md").write_text(md, encoding="utf-8")
    latest = RESULTS / "LATEST"
    if latest.exists():
        shutil.rmtree(latest)
    shutil.copytree(outdir, latest)
    return md


def summary_md(quality, s1, specs, s2, rnd, micro, tour) -> str:
    plan = research_plan()
    cfg = settings()
    sp = plan["splits"]
    L = [f"# FX AUTOPILOT 研究結果（{utcnow():%Y-%m-%d %H:%M} UTC）", "",
         "**PAPER / BACKTEST のみ。利益を保証するものではありません。LIVE は本人の明示承認まで開始しません。**", "",
         "## データ", "",
         "Dukascopy 公開ヒストリカル（bid / ask 別 H1 足。Mid ではなく bid/ask で約定判定）", "",
         _t(pd.DataFrame(quality), ["pair", "rows", "first", "last", "spread_pips_median", "spread_pips_p95",
                                     "weekday_gaps_gt_3h", "crossed_quotes", "abs_ret_gt_2pct"]),
         "## データ分割（事前登録 `config/research_plan.yaml`）", "",
         f"- TRAIN {sp['TRAIN'][0]}〜{sp['TRAIN'][1]} ／ VALIDATION {sp['VALIDATION'][0]}〜{sp['VALIDATION'][1]}"
         f"（Stage 1 はこの 2 区間だけに切り詰めたデータで実行）",
         f"- TEST {sp['TEST'][0]}〜{sp['TEST'][1]} ／ FORWARD {sp['FORWARD'][0]}〜最新（LOCK 後に 1 回だけ評価）",
         f"- Walk-Forward: 学習 {plan['walk_forward']['train_years']} 年 → 検証 1 年を "
         f"{plan['walk_forward']['first_test_year']}〜{plan['walk_forward']['last_test_year']} で繰り返し",
         f"- コスト（既定 {cfg['costs']['default_profile']}）: 実効スプレッド = max(実測, 国内業者の原則固定) + スリッページ "
         f"（成行 {cfg['costs']['profiles']['retail_jp']['slippage_pips_market']} pip / 逆指値 "
         f"{cfg['costs']['profiles']['retail_jp']['slippage_pips_stop']} pip）+ スワップ（政策金利差 − 年1%）+ 1 本の執行遅延",
         f"- Risk: 1 トレード {cfg['risk']['risk_per_trade']:.1%}、最大レバレッジ {cfg['risk']['max_leverage']} 倍、"
         f"日次 {cfg['risk']['daily_loss_limit']:.0%} / 週次 {cfg['risk']['weekly_loss_limit']:.0%} 損失で新規停止、"
         f"DD {cfg['risk']['max_drawdown']:.0%} で全決済 + Kill Switch", ""]
    if s1:
        c = s1["candidates"].copy()
        L += ["## Stage 1: Walk-Forward（TRAIN+VALIDATION 内・パラメータ選択込みの未知年成績）", "",
              f"試行数（戦略 × パラメータ × ペア）: **{s1['n_trials']}**（Deflated Sharpe の補正に使用）", "",
              _t(c.sort_values(["strategy", "pair"]),
                 ["strategy", "pair", "wf_trades", "wf_net_return", "wf_sharpe", "wf_profit_factor", "wf_max_drawdown",
                  "wf_positive_year_ratio", "wf_dsr", "val_sharpe", "val_profit_factor", "gate_A", "gate_A_fail"],
                 {"wf_net_return": P, "wf_sharpe": F2, "wf_profit_factor": F2, "wf_max_drawdown": D,
                  "wf_positive_year_ratio": "{:.0%}", "wf_dsr": F2, "val_sharpe": F2, "val_profit_factor": F2}),
              f"ゲート A 合格: **{int(c['gate_A'].sum())} / {len(c)}**", ""]
    L += ["## LOCK した仕様", "",
          _t(pd.DataFrame([{"spec_id": s["spec_id"], "trade_pairs": " ".join(s.get("trade_pairs", [])),
                            "research_only": s.get("research_only"), "locked_at": s.get("locked_at", "")[:16],
                            "spec_hash": s["spec_hash"][:12]} for s in specs]),
             ["spec_id", "trade_pairs", "research_only", "locked_at", "spec_hash"])]
    st = s2["stage2"]
    port = st[st.variant.isin(["portfolio", "portfolio_stress_2x", "portfolio_ibkr"])]
    L += ["## Stage 2: TEST / FORWARD（LOCK 後・1 回だけ）ポートフォリオ", "",
          _t(port.sort_values(["spec_id", "period", "variant"]),
             ["spec_id", "period", "variant", "n_trades", "net_return", "cagr", "profit_factor", "sharpe", "sortino",
              "max_drawdown", "win_rate", "payoff_ratio", "expectancy_jpy", "max_consecutive_losses", "recovery_factor",
              "exposure_time", "avg_leverage", "turnover_annual", "total_cost_jpy", "cost_ratio", "halted_at"],
             {"net_return": P, "cagr": P, "profit_factor": F2, "sharpe": F2, "sortino": F2, "max_drawdown": D,
              "win_rate": "{:.0%}", "payoff_ratio": F2, "expectancy_jpy": "{:,.0f}", "recovery_factor": F2,
              "exposure_time": "{:.0%}", "avg_leverage": F2, "turnover_annual": "{:.0f}", "total_cost_jpy": "{:,.0f}",
              "cost_ratio": F2}),
          "## Stage 2: 通貨ペア別（retail_jp コスト）", "",
          _t(st[~st.variant.str.startswith("portfolio")].sort_values(["spec_id", "variant", "period"]),
             ["spec_id", "variant", "period", "n_trades", "net_return", "profit_factor", "sharpe", "max_drawdown", "cost_ratio"],
             {"net_return": P, "profit_factor": F2, "sharpe": F2, "max_drawdown": D, "cost_ratio": F2}),
          "## レバレッジ比較（同一シグナル・TEST 開始〜最新）", "",
          _t(s2["leverage"], ["spec_id", "leverage_profile", "risk_per_trade", "max_leverage", "n_trades", "net_return",
                              "cagr", "sharpe", "max_drawdown", "avg_leverage", "halted_at"],
             {"net_return": P, "cagr": P, "sharpe": F2, "max_drawdown": D, "avg_leverage": F2}),
          "## 年別（全期間・研究用設定）", "",
          _t(s2["yearly"].pivot_table(index="year", columns="spec_id", values="return").reset_index()
             if len(s2["yearly"]) else s2["yearly"],
             ["year"] + sorted(s2["yearly"]["spec_id"].unique().tolist()) if len(s2["yearly"]) else [],
             {k: P for k in (s2["yearly"]["spec_id"].unique() if len(s2["yearly"]) else [])}),
          "## 相場局面別（エントリー時点の状態・全期間）", "",
          _t(s2["regimes"], ["spec_id", "dimension", "state", "trades", "pnl_jpy", "win_rate", "profit_factor"],
             {"pnl_jpy": "{:+,.0f}", "win_rate": "{:.0%}", "profit_factor": F2}),
          "## イベント期間（金融危機・急変相場）", "",
          _t(s2["events"], ["spec_id", "event", "return", "max_drawdown", "trades", "pnl_jpy"],
             {"return": P, "max_drawdown": D, "pnl_jpy": "{:+,.0f}"}), ""]
    if len(rnd):
        g = rnd.groupby("pair").agg(sharpe_mean=("sharpe", "mean"), sharpe_p95=("sharpe", lambda x: x.quantile(0.95)),
                                    net_return_mean=("net_return", "mean"), trades=("n_trades", "mean"),
                                    cost_ratio=("cost_ratio", "mean")).reset_index()
        L += ["## ランダム売買（ベンチマーク・TRAIN+VALIDATION・10 シード）", "",
              _t(g, ["pair", "sharpe_mean", "sharpe_p95", "net_return_mean", "trades", "cost_ratio"],
                 {"sharpe_mean": F2, "sharpe_p95": F2, "net_return_mean": P, "trades": "{:.0f}", "cost_ratio": F2}), ""]
    if len(micro):
        g = micro.groupby("pair").apply(lambda x: pd.Series({
            "spread_min_hour": int(x.loc[x.spread_median_pips.idxmin(), "hour_utc"]),
            "spread_min": x.spread_median_pips.min(),
            "spread_max_hour": int(x.loc[x.spread_median_pips.idxmax(), "hour_utc"]),
            "spread_max": x.spread_median_pips.max(),
            "best_spread_to_range": x.spread_to_range.min(), "worst_spread_to_range": x.spread_to_range.max()}),
            include_groups=False).reset_index()
        L += ["## Market Microstructure（直近 2 年・UTC 時間帯別の実測スプレッド）", "",
              _t(g, ["pair", "spread_min_hour", "spread_min", "spread_max_hour", "spread_max", "best_spread_to_range",
                     "worst_spread_to_range"], {"spread_min": F2, "spread_max": F2, "best_spread_to_range": "{:.3f}",
                                                "worst_spread_to_range": "{:.3f}"}),
              "スプレッド / 1 時間の値幅 が大きい時間帯（NY クローズ〜オセアニア早朝）はコスト負けしやすい。"
              "Risk Engine は実測スプレッドが直近中央値の 3 倍を超える足で新規を禁止する。", ""]
    rows = pd.DataFrame(tour.get("specs", []))
    L += ["## Strategy Tournament", "",
          f"Champion: **{tour.get('champion') or 'CASH（取引しない）'}**" + (f" — {tour.get('champion_note')}" if tour.get("champion_note") else ""),
          f"LIVE 候補: **{', '.join(tour.get('live_candidates', [])) or 'なし'}**（LIVE 開始には本人の明示承認が必須）", "",
          _t(rows.assign(gate_b_fail=rows["gate_b_fail"].map(lambda x: ", ".join(x)) if len(rows) else None,
                         paper_gate_fail=rows["paper_gate_fail"].map(lambda x: ", ".join(x)) if len(rows) else None)
             if len(rows) else rows, ["spec_id", "status", "gate_b_fail", "paper_gate_fail"]), ""]
    return "\n".join(L)
