"""テクニカル指標（すべて因果的: 足 i の値は足 i の終値までのデータだけで計算）。

シグナルは足 i の終値で判断し、約定は足 i+1 の始値（bid/ask）で行う（backtest.py）。
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def mid(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "o": (df["bid_o"] + df["ask_o"]) / 2, "h": (df["bid_h"] + df["ask_h"]) / 2,
        "l": (df["bid_l"] + df["ask_l"]) / 2, "c": (df["bid_c"] + df["ask_c"]) / 2,
    }, index=df.index)


def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).mean()


def wilder(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(alpha=1 / n, adjust=False, min_periods=n).mean()


def atr(m: pd.DataFrame, n: int = 14) -> pd.Series:
    pc = m["c"].shift(1)
    tr = pd.concat([m["h"] - m["l"], (m["h"] - pc).abs(), (m["l"] - pc).abs()], axis=1).max(axis=1)
    return wilder(tr, n)


def rsi(c: pd.Series, n: int = 14) -> pd.Series:
    d = c.diff()
    up = wilder(d.clip(lower=0), n)
    dn = wilder((-d).clip(lower=0), n)
    rs = up / dn.replace(0, np.nan)
    return 100 - 100 / (1 + rs)


def adx(m: pd.DataFrame, n: int = 14) -> pd.Series:
    up = m["h"].diff()
    dn = -m["l"].diff()
    plus_dm = np.where((up > dn) & (up > 0), up, 0.0)
    minus_dm = np.where((dn > up) & (dn > 0), dn, 0.0)
    a = atr(m, n)
    pdi = 100 * wilder(pd.Series(plus_dm, index=m.index), n) / a
    mdi = 100 * wilder(pd.Series(minus_dm, index=m.index), n) / a
    dx = 100 * (pdi - mdi).abs() / (pdi + mdi).replace(0, np.nan)
    return wilder(dx, n)


def bollinger(c: pd.Series, n: int = 20, k: float = 2.0):
    m = sma(c, n)
    sd = c.rolling(n, min_periods=n).std(ddof=0)
    return m, m + k * sd, m - k * sd


def donchian_prev(m: pd.DataFrame, n: int):
    """直前 n 本（現在足を含まない）の最高値・最安値。"""
    return m["h"].rolling(n, min_periods=n).max().shift(1), m["l"].rolling(n, min_periods=n).min().shift(1)


def pct_rank(s: pd.Series, n: int) -> pd.Series:
    """過去 n 本の中での順位（0..1）。現在値を含む過去データのみ。"""
    return s.rolling(n, min_periods=max(20, n // 4)).rank(pct=True)


def higher_tf(m: pd.DataFrame, rule: str = "4h") -> pd.DataFrame:
    """上位足の OHLC と、その足が確定する H1 足の時刻（avail = 窓内の最後の H1 足の開始時刻）。"""
    g = m.resample(rule, label="left", closed="left")
    hi = pd.DataFrame({"o": g["o"].first(), "h": g["h"].max(), "l": g["l"].min(), "c": g["c"].last()})
    hi["avail"] = pd.Series(m.index, index=m.index).resample(rule, label="left", closed="left").max()
    return hi.dropna()


def map_to_h1(ind: pd.DataFrame, avail: pd.Series, index: pd.DatetimeIndex) -> pd.DataFrame:
    """上位足の指標を、確定した時点（avail）以降の H1 足に前方補完で割り当てる。

    末尾の上位足は未完成の可能性があるため捨てる（リアルタイムで未完成の上位足は使わない）。
    上位足（開始 T）の値は、その窓の最後の H1 足の終値で確定 → その H1 足（index=avail）の判断から使える。
    """
    x = ind.iloc[:-1].copy()
    x.index = pd.DatetimeIndex(avail.iloc[:-1])
    x = x[~x.index.duplicated(keep="last")]
    return x.reindex(index, method="ffill")


def resample_causal(m: pd.DataFrame, rule: str, index: pd.DatetimeIndex) -> pd.DataFrame:
    hi = higher_tf(m, rule)
    return map_to_h1(hi[["o", "h", "l", "c"]], hi["avail"], index)
