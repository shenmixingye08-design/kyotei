"""C. Regime Detection + 戦略切替 / D. Multi Timeframe。

相場状態（4H 足で判定。完成した 4H 足のみ使用）:
  TREND    : ADX(4H) >= adx_trend
  RANGE    : ADX(4H) <  adx_range
  HIGH_VOL : ATR(4H) の過去 1 年での順位 >= 0.95（新規停止）
  LOW_VOL  : 同順位 <= 0.10
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .. import features as F
from .base import Strategy, cross_dn, cross_up, register


def regime_frame(df: pd.DataFrame) -> pd.DataFrame:
    m = F.mid(df)
    h4 = F.higher_tf(m, "4h")
    ind = pd.DataFrame(index=h4.index)
    ind["adx"] = F.adx(h4, 14)
    ind["atr"] = F.atr(h4, 14)
    ind["atr_pct"] = F.pct_rank(ind["atr"] / h4["c"], 6 * 260)
    ind["ema50"] = F.ema(h4["c"], 50)
    ind["ema200"] = F.ema(h4["c"], 200)
    ind["c"] = h4["c"]
    return F.map_to_h1(ind, h4["avail"], df.index)


def label(rf: pd.DataFrame, adx_trend=25, adx_range=20) -> pd.Series:
    lab = pd.Series("NEUTRAL", index=rf.index)
    lab[rf["adx"] >= adx_trend] = "TREND"
    lab[rf["adx"] < adx_range] = "RANGE"
    lab[rf["atr_pct"] >= 0.95] = "HIGH_VOL"
    lab[rf["adx"].isna()] = "UNKNOWN"
    return lab


@register
class RegimeSwitch(Strategy):
    """TREND → 4H EMA 方向への 1H ブレイクアウト / RANGE → RSI+BB 逆張り / HIGH_VOL → 新規停止。"""
    name = "regime_switch"
    family = "C_regime"
    grid = {"adx_trend": [25, 30], "brk": [24, 48]}

    def generate(self, df, pair):
        p = self.params
        m = F.mid(df)
        rf = regime_frame(df)
        lab = label(rf, p["adx_trend"], 20)
        a = F.atr(m, 14)
        hi, lo = F.donchian_prev(m, p["brk"])
        r = F.rsi(m["c"], 14)
        mb, up, lb = F.bollinger(m["c"], 20, 2.0)
        trend_dir = np.sign(rf["ema50"] - rf["ema200"])
        out = self.empty(df.index)
        t_long = (lab == "TREND") & (trend_dir > 0) & (m["c"] > hi)
        t_short = (lab == "TREND") & (trend_dir < 0) & (m["c"] < lo)
        r_long = (lab == "RANGE") & (r < 30) & (m["c"] < lb)
        r_short = (lab == "RANGE") & (r > 70) & (m["c"] > up)
        out.loc[t_long | r_long, "entry"] = 1
        out.loc[t_short | r_short, "entry"] = -1
        is_trend_entry = t_long | t_short
        out["sl_dist"] = np.where(is_trend_entry, 3.0 * a, 2.0 * a)
        out["trail_dist"] = np.where(is_trend_entry, 4.0 * a, np.nan)
        out["tp_dist"] = np.nan
        out["max_bars"] = np.where(is_trend_entry, 240, 24)
        out["exit_long"] = (lab == "HIGH_VOL")
        out["exit_short"] = (lab == "HIGH_VOL")
        out.loc[a.isna() | hi.isna() | mb.isna(), "entry"] = 0
        return out


@register
class MtfPullback(Strategy):
    """4H=環境（EMA50 vs EMA200）/ 1H=方向（EMA50 の傾き）/ エントリー=1H RSI の押し目からの回復。"""
    name = "mtf_pullback"
    family = "D_mtf"
    grid = {"rsi_th": [35, 40], "tp_atr": [2.0, 3.0]}

    def generate(self, df, pair):
        p = self.params
        m = F.mid(df)
        rf = regime_frame(df)
        env = np.sign(rf["ema50"] - rf["ema200"])
        e50 = F.ema(m["c"], 50)
        slope = np.sign(e50 - e50.shift(12))
        r = F.rsi(m["c"], 14)
        a = F.atr(m, 14)
        out = self.empty(df.index)
        long_ = (env > 0) & (slope > 0) & cross_up(r, p["rsi_th"]) & (rf["atr_pct"] < 0.95)
        short_ = (env < 0) & (slope < 0) & cross_dn(r, 100 - p["rsi_th"]) & (rf["atr_pct"] < 0.95)
        out.loc[long_, "entry"] = 1
        out.loc[short_, "entry"] = -1
        out["sl_dist"] = 2.0 * a
        out["tp_dist"] = p["tp_atr"] * a
        out["max_bars"] = 72
        out["exit_long"] = env < 0
        out["exit_short"] = env > 0
        out.loc[a.isna() | env.isna(), "entry"] = 0
        return out
