"""評価指標（利益額だけで判断しない）。

日次リターン（UTC 日末の口座残高）から Sharpe/Sortino/CAGR/MaxDD を、トレード一覧から PF・勝率・期待値などを計算する。
多重検定の補正として Probabilistic / Deflated Sharpe（Bailey & López de Prado）も出す（ai-investment-research の
aiquant/metrics.py と同じ式を FX 用に移植）。
"""
from __future__ import annotations

import math

import numpy as np
import pandas as pd
from scipy import stats

from .common import PERIODS_PER_YEAR_DAILY as PY


def daily_returns(equity: pd.Series) -> pd.Series:
    d = equity.resample("1D").last().dropna()
    d = d[d.index.weekday < 5] if len(d) > 10 else d
    return d.pct_change().dropna()


def max_drawdown(equity: pd.Series) -> float:
    if equity.empty:
        return 0.0
    return float((equity / equity.cummax() - 1).min())


def _streak(x) -> int:
    best = cur = 0
    for v in x:
        cur = cur + 1 if v else 0
        best = max(best, cur)
    return best


def compute(equity: pd.Series, trades: pd.DataFrame, exposure: pd.Series | None = None,
            initial: float | None = None) -> dict:
    eq = equity.dropna()
    if len(eq) < 2:
        return {"n_trades": 0}
    initial = initial or float(eq.iloc[0])
    r = daily_returns(eq)
    years = max((eq.index[-1] - eq.index[0]).days / 365.25, 1e-9)
    final = float(eq.iloc[-1])
    net = final / initial - 1
    cagr = (final / initial) ** (1 / years) - 1 if final > 0 else -1.0
    sd = r.std(ddof=1) if len(r) > 2 else 0.0
    sharpe = float(r.mean() / sd * math.sqrt(PY)) if sd > 0 else 0.0
    dn = r[r < 0]
    dsd = math.sqrt((dn ** 2).sum() / len(r)) if len(dn) else 0.0
    sortino = float(r.mean() / dsd * math.sqrt(PY)) if dsd > 0 else 0.0
    mdd = max_drawdown(eq)
    out = {
        "start": str(eq.index[0])[:10], "end": str(eq.index[-1])[:10], "years": round(years, 2),
        "net_return": net, "cagr": cagr, "sharpe": sharpe, "sortino": sortino, "max_drawdown": mdd,
        "annual_vol": float(sd * math.sqrt(PY)) if sd else 0.0,
        "net_profit_jpy": final - initial,
        "recovery_factor": float((final - initial) / (abs(mdd) * eq.cummax().max())) if mdd < 0 else None,
    }
    t = trades if trades is not None else pd.DataFrame()
    n = len(t)
    out["n_trades"] = n
    if n:
        p = t["pnl_jpy"].to_numpy()
        wins, losses = p[p > 0], p[p <= 0]
        gp, gl = wins.sum(), -losses.sum()
        costs = float(t["cost_spread_jpy"].sum() + t["cost_slip_jpy"].sum() + t["commission_jpy"].sum())
        swap = float(t["swap_jpy"].sum())
        gross_mid = float(t["gross_mid_pnl_jpy"].sum())
        out.update({
            "profit_factor": float(gp / gl) if gl > 0 else float("inf"),
            "win_rate": float(len(wins) / n),
            "avg_win_jpy": float(wins.mean()) if len(wins) else 0.0,
            "avg_loss_jpy": float(losses.mean()) if len(losses) else 0.0,
            "payoff_ratio": float(wins.mean() / -losses.mean()) if len(wins) and len(losses) and losses.mean() < 0 else None,
            "expectancy_jpy": float(p.mean()),
            "expectancy_r": float(t["r_multiple"].mean()) if "r_multiple" in t else None,
            "max_consecutive_losses": _streak(p <= 0),
            "trades_per_year": n / years,
            "avg_bars_held": float(t["bars"].mean()),
            "total_cost_jpy": costs, "swap_jpy": swap,
            "gross_mid_pnl_jpy": gross_mid,
            # Cost Ratio = 取引コスト / Mid ベースの総利益（>1 ならコストが優位性を上回る）
            "cost_ratio": float(costs / gross_mid) if gross_mid > 0 else None,
            "cost_per_trade_jpy": costs / n,
            "turnover_annual": float(t["notional_jpy"].sum() * 2 / eq.mean() / years),
        })
    if exposure is not None and len(exposure):
        e = exposure.reindex(eq.index).fillna(0)
        out["exposure_time"] = float((e > 0).mean())
        out["avg_leverage"] = float(e[e > 0].mean()) if (e > 0).any() else 0.0
        out["max_leverage"] = float(e.max())
    if len(r) > 30 and sd > 0:
        out["psr_vs_zero"] = probabilistic_sharpe(r.mean() / sd, len(r), float(stats.skew(r)), float(stats.kurtosis(r)))
        out["t_stat"] = float(r.mean() / sd * math.sqrt(len(r)))
    return {k: (round(v, 6) if isinstance(v, float) and math.isfinite(v) else v) for k, v in out.items()}


def yearly(equity: pd.Series, trades: pd.DataFrame) -> pd.DataFrame:
    eq = equity.dropna()
    ye = eq.resample("YE").last()
    start = pd.concat([pd.Series([eq.iloc[0]], index=[eq.index[0]]), ye.iloc[:-1]])
    ret = ye.to_numpy() / start.to_numpy() - 1
    df = pd.DataFrame({"year": ye.index.year, "return": ret})
    if len(trades):
        g = trades.groupby(pd.to_datetime(trades["exit_time"]).dt.year)
        df = df.merge(pd.DataFrame({"year": list(g.groups), "trades": g.size().values,
                                    "pnl_jpy": g["pnl_jpy"].sum().values}), on="year", how="left")
    return df


def period_slice(equity: pd.Series, trades: pd.DataFrame, exposure: pd.Series | None, start, end):
    s = pd.Timestamp(start, tz="UTC")
    e = pd.Timestamp(end, tz="UTC") + pd.Timedelta(days=1) if end else equity.index.max() + pd.Timedelta(hours=1)
    eq = equity[(equity.index >= s) & (equity.index < e)]
    tr = trades[(pd.to_datetime(trades["entry_time"]) >= s) & (pd.to_datetime(trades["entry_time"]) < e)] if len(trades) else trades
    ex = exposure[(exposure.index >= s) & (exposure.index < e)] if exposure is not None else None
    return eq, tr, ex


def probabilistic_sharpe(sr: float, n: int, skew: float, kurt_excess: float, sr_bench: float = 0.0) -> float:
    if n < 3:
        return float("nan")
    denom = math.sqrt(max(1e-12, 1 - skew * sr + (kurt_excess + 2) / 4 * sr ** 2))
    return float(stats.norm.cdf((sr - sr_bench) * math.sqrt(n - 1) / denom))


def deflated_sharpe(r: pd.Series, n_trials: int, trial_sharpes_annual: list | None = None) -> dict:
    r = r.dropna()
    n = len(r)
    if n < 30 or r.std() == 0:
        return {"dsr": None, "n_trials": n_trials}
    sr = r.mean() / r.std(ddof=1)
    if trial_sharpes_annual and len(trial_sharpes_annual) > 1:
        var_sr = float(np.var(np.array(trial_sharpes_annual) / math.sqrt(PY), ddof=1))
    else:
        var_sr = 1.0 / n
    g = 0.5772156649
    N = max(2, n_trials)
    sr0 = math.sqrt(var_sr) * ((1 - g) * stats.norm.ppf(1 - 1 / N) + g * stats.norm.ppf(1 - 1 / (N * math.e)))
    return {"dsr": round(probabilistic_sharpe(sr, n, float(stats.skew(r)), float(stats.kurtosis(r)), sr0), 4),
            "sr0_annual": round(sr0 * math.sqrt(PY), 4), "n_trials": n_trials}
