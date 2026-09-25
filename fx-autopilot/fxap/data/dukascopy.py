"""Dukascopy 公開ヒストリカルデータ（bid / ask 別）の取得と復号。

URL（月は 0 始まり、日は 1 始まり。時刻はすべて UTC）:
  完了した月の H1 足:   {base}/{PAIR}/{YYYY}/{MM0}/{BID|ASK}_candles_hour_1.bi5
  完了した日の M1 足:   {base}/{PAIR}/{YYYY}/{MM0}/{DD}/{BID|ASK}_candles_min_1.bi5
  1 時間分のティック:   {base}/{PAIR}/{YYYY}/{MM0}/{DD}/{HH}h_ticks.bi5
bi5 = LZMA 圧縮。足は 24byte（>i 時刻オフセット秒, >i open, close, low, high, >f volume）、
ティックは 20byte（>i ミリ秒オフセット, >i ask, bid, >f ask_vol, bid_vol）。整数価格 × point = 価格。

取得できない場合に架空データで埋めることはしない（欠損として記録し、取引禁止の判定に使う）。
"""
from __future__ import annotations

import datetime as dt
import lzma
import struct
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd
import requests

from ..common import PAIRS

BASE = "https://datafeed.dukascopy.com/datafeed"
UA = {"User-Agent": "Mozilla/5.0 (fx-autopilot research; PAPER ONLY)"}
COLS = ["bid_o", "bid_h", "bid_l", "bid_c", "ask_o", "ask_h", "ask_l", "ask_c", "volume"]


class FetchError(RuntimeError):
    pass


def _get(url: str, session: requests.Session, retries: int = 4) -> bytes | None:
    """200 → bytes / 404 → None（その期間はデータなし）/ それ以外は再試行の後 FetchError。"""
    last = None
    for k in range(retries):
        try:
            r = session.get(url, headers=UA, timeout=30)
            if r.status_code == 200:
                return r.content
            if r.status_code == 404:
                return None
            last = f"HTTP {r.status_code}"
        except requests.RequestException as e:  # noqa: PERF203
            last = repr(e)
        time.sleep(1.5 * (2 ** k))
    raise FetchError(f"{url}: {last}")


def decode_candles(raw: bytes, start: dt.datetime, point: float, seconds_unit: int = 1) -> pd.DataFrame:
    if not raw:
        return pd.DataFrame(columns=["o", "h", "l", "c", "v"])
    data = lzma.decompress(raw)
    n = len(data) // 24
    arr = struct.unpack(">" + "iiiiif" * n, data[: n * 24])
    a = np.array(arr, dtype=float).reshape(n, 6)
    idx = pd.to_datetime(start) + pd.to_timedelta(a[:, 0] * seconds_unit, unit="s")
    df = pd.DataFrame({"o": a[:, 1] * point, "c": a[:, 2] * point, "l": a[:, 3] * point,
                       "h": a[:, 4] * point, "v": a[:, 5]}, index=idx)
    bad = (df["l"] > df[["o", "c"]].min(axis=1) + 1e-12) | (df["h"] < df[["o", "c"]].max(axis=1) - 1e-12)
    if bad.any():
        raise FetchError(f"candle layout check failed ({int(bad.sum())} bad rows)")
    return df


def decode_ticks(raw: bytes, hour_start: dt.datetime, point: float) -> pd.DataFrame:
    if not raw:
        return pd.DataFrame(columns=["ask", "bid", "av", "bv"])
    data = lzma.decompress(raw)
    n = len(data) // 20
    arr = struct.unpack(">" + "iiiff" * n, data[: n * 20])
    a = np.array(arr, dtype=float).reshape(n, 5)
    idx = pd.to_datetime(hour_start) + pd.to_timedelta(a[:, 0], unit="ms")
    return pd.DataFrame({"ask": a[:, 1] * point, "bid": a[:, 2] * point, "av": a[:, 3], "bv": a[:, 4]}, index=idx)


def _combine(bid: pd.DataFrame, ask: pd.DataFrame) -> pd.DataFrame:
    if bid.empty or ask.empty:
        return pd.DataFrame(columns=COLS)
    j = bid.join(ask, how="inner", lsuffix="_b", rsuffix="_a")
    out = pd.DataFrame({
        "bid_o": j["o_b"], "bid_h": j["h_b"], "bid_l": j["l_b"], "bid_c": j["c_b"],
        "ask_o": j["o_a"], "ask_h": j["h_a"], "ask_l": j["l_a"], "ask_c": j["c_a"],
        "volume": j["v_b"] + j["v_a"],
    })
    return out


def _resample_h1(m: pd.DataFrame) -> pd.DataFrame:
    if m.empty:
        return m
    g = m.resample("1h", label="left", closed="left")
    out = pd.DataFrame({
        "bid_o": g["bid_o"].first(), "bid_h": g["bid_h"].max(), "bid_l": g["bid_l"].min(), "bid_c": g["bid_c"].last(),
        "ask_o": g["ask_o"].first(), "ask_h": g["ask_h"].max(), "ask_l": g["ask_l"].min(), "ask_c": g["ask_c"].last(),
        "volume": g["volume"].sum(),
    })
    return out.dropna()


def ticks_to_h1(t: pd.DataFrame, hour_start) -> pd.DataFrame:
    if t.empty:
        return pd.DataFrame(columns=COLS)
    row = {"bid_o": t["bid"].iloc[0], "bid_h": t["bid"].max(), "bid_l": t["bid"].min(), "bid_c": t["bid"].iloc[-1],
           "ask_o": t["ask"].iloc[0], "ask_h": t["ask"].max(), "ask_l": t["ask"].min(), "ask_c": t["ask"].iloc[-1],
           "volume": float(t["av"].sum() + t["bv"].sum())}
    return pd.DataFrame([row], index=pd.DatetimeIndex([pd.Timestamp(hour_start)]))


def month_h1(pair: str, year: int, month: int, session: requests.Session) -> pd.DataFrame:
    point = PAIRS[pair]["point"]
    start = dt.datetime(year, month, 1)
    parts = {}
    for side in ("BID", "ASK"):
        raw = _get(f"{BASE}/{pair}/{year}/{month - 1:02d}/{side}_candles_hour_1.bi5", session)
        if raw is None:
            # 月次ファイルが無い → 日次の M1 足から作る
            days = []
            d = start.date()
            while d.month == month:
                f = day_h1(pair, d, session)
                if f is not None and len(f):
                    days.append(f)
                d += dt.timedelta(days=1)
            return pd.concat(days) if days else pd.DataFrame(columns=COLS)
        parts[side] = decode_candles(raw, start, point)
    return _combine(parts["BID"], parts["ASK"])


def day_h1(pair: str, day: dt.date, session: requests.Session) -> pd.DataFrame | None:
    """完了した日の M1 足 → H1。ファイルがまだ無ければ None。"""
    point = PAIRS[pair]["point"]
    start = dt.datetime(day.year, day.month, day.day)
    parts = {}
    for side in ("BID", "ASK"):
        raw = _get(f"{BASE}/{pair}/{day.year}/{day.month - 1:02d}/{day.day:02d}/{side}_candles_min_1.bi5", session)
        if raw is None:
            return None
        parts[side] = decode_candles(raw, start, point)
    return _resample_h1(_combine(parts["BID"], parts["ASK"]))


def hour_from_ticks(pair: str, hour: dt.datetime, session: requests.Session) -> pd.DataFrame:
    point = PAIRS[pair]["point"]
    raw = _get(f"{BASE}/{pair}/{hour.year}/{hour.month - 1:02d}/{hour.day:02d}/{hour.hour:02d}h_ticks.bi5", session)
    return ticks_to_h1(decode_ticks(raw or b"", hour, point), hour)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """週末などの出来高ゼロ・値動きなしの足を除き、UTC の tz-aware index に揃える。"""
    if df.empty:
        return df
    df = df[~df.index.duplicated(keep="last")].sort_index()
    flat = (df["volume"] <= 0) & (df["bid_h"] == df["bid_l"])
    df = df[~flat]
    if df.index.tz is None:
        df.index = df.index.tz_localize("UTC")
    return df.astype(float)


def fetch_range(pair: str, start: dt.date, end_utc: dt.datetime, workers: int = 8,
                session: requests.Session | None = None) -> pd.DataFrame:
    """start から end_utc（その時点で完了している足）までの H1 bid/ask 足。"""
    s = session or requests.Session()
    end_utc = end_utc.replace(tzinfo=None)
    this_month = dt.datetime(end_utc.year, end_utc.month, 1)
    months = []
    y, m = start.year, start.month
    while dt.datetime(y, m, 1) < this_month:
        months.append((y, m))
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    with ThreadPoolExecutor(workers) as ex:
        frames = list(ex.map(lambda ym: month_h1(pair, ym[0], ym[1], s), months))
    # 当月: 完了した日は M1 → H1、当日（と M1 が未公開の日）は完了した時間のティック
    d = max(this_month.date(), start)
    days = []
    while d < end_utc.date():
        days.append(d)
        d += dt.timedelta(days=1)
    with ThreadPoolExecutor(workers) as ex:
        dayframes = list(ex.map(lambda x: (x, day_h1(pair, x, s)), days))
    hours = []
    for x, f in dayframes:
        if f is None:
            hours += [dt.datetime(x.year, x.month, x.day, h) for h in range(24)]
        else:
            frames.append(f)
    today = dt.datetime(end_utc.year, end_utc.month, end_utc.day)
    h = today
    while h + dt.timedelta(hours=1) <= end_utc:
        hours.append(h)
        h += dt.timedelta(hours=1)
    with ThreadPoolExecutor(workers) as ex:
        frames += list(ex.map(lambda hh: hour_from_ticks(pair, hh, s), hours))
    frames = [f for f in frames if f is not None and len(f)]
    if not frames:
        return pd.DataFrame(columns=COLS)
    return clean(pd.concat(frames))
