"""市場データの保存・増分更新・品質検査。

保存先: data/h1/<PAIR>.parquet（git には含めない。GitHub Actions の cache で引き継ぐ）
各足の index = 足の開始時刻（UTC）。その足の値が利用可能になるのは開始 + 1 時間（available_at）。
"""
from __future__ import annotations

import datetime as dt
import json

import numpy as np
import pandas as pd

from ..common import DATA_DIR, PAIRS, utcnow

H1_DIR = DATA_DIR / "h1"
# 2010 年以降の実績レンジを十分に含む範囲（外れたら復号・桁の誤りとみなし研究を止める）
PLAUSIBLE = {"USDJPY": (70, 180), "EURUSD": (0.9, 1.7), "EURJPY": (90, 200), "GBPUSD": (1.0, 2.0),
             "AUDUSD": (0.5, 1.2)}


def path(pair: str):
    return H1_DIR / f"{pair}.parquet"


def load(pair: str) -> pd.DataFrame:
    p = path(pair)
    if not p.exists():
        raise FileNotFoundError(f"{p} がありません（python -m fxap.cli ingest で取得）")
    df = pd.read_parquet(p)
    df.index = pd.DatetimeIndex(df.index).tz_convert("UTC") if df.index.tz else pd.DatetimeIndex(df.index).tz_localize("UTC")
    return df.sort_index()


def load_all(pairs) -> dict[str, pd.DataFrame]:
    return {p: load(p) for p in pairs}


def save(pair: str, df: pd.DataFrame) -> None:
    H1_DIR.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path(pair))


def ingest(pairs, start: str, now: dt.datetime | None = None, refetch_days: int = 3, chunk_months: int = 24) -> dict:
    """増分取得。既存データの末尾 refetch_days 日を再取得して上書き（当日分の暫定足を確定値で置換）。

    初回は chunk_months ごとに保存する（途中で失敗しても取得済み分は cache に残り、次回はその続きから）。
    """
    from . import dukascopy

    now = (now or utcnow()).replace(minute=0, second=0, microsecond=0)
    report, errors = {}, {}
    for pair in pairs:
        try:
            while True:
                try:
                    old = load(pair)
                except FileNotFoundError:
                    old = pd.DataFrame(columns=dukascopy.COLS)
                since = (old.index.max() - pd.Timedelta(days=refetch_days)).date() if len(old) else dt.date.fromisoformat(start)
                if since < now.date().replace(day=1):
                    since = since.replace(day=1)
                # 取得範囲を chunk_months に制限（月初境界）
                y, m = since.year, since.month + chunk_months
                y, m = y + (m - 1) // 12, (m - 1) % 12 + 1
                chunk_end = min(now.replace(tzinfo=None), dt.datetime(y, m, 1))
                new = dukascopy.fetch_range(pair, since, chunk_end)
                cut = pd.Timestamp(since).tz_localize("UTC")
                merged = pd.concat([old[old.index < cut], new]) if len(old) else new
                merged = merged[~merged.index.duplicated(keep="last")].sort_index()
                save(pair, merged)
                print(f"  {pair}: {since} → {chunk_end:%Y-%m-%d} +{len(new)} rows (total {len(merged)})", flush=True)
                if chunk_end >= now.replace(tzinfo=None):
                    break
            report[pair] = {"rows": int(len(merged)), "first": str(merged.index.min()), "last": str(merged.index.max())}
        except Exception as e:  # noqa: BLE001  取得失敗はそのペアを欠損として報告（架空データで埋めない）
            errors[pair] = repr(e)
            print(f"  {pair}: FETCH ERROR {e!r}", flush=True)
    if errors:
        raise RuntimeError(f"取得失敗: {errors}（取得済み分は保存済み。次回続きから）")
    return report


def quality(df: pd.DataFrame, pair: str) -> dict:
    """品質検査: 重複・逆転気配・異常変動・平日の欠損時間。"""
    if df.empty:
        return {"pair": pair, "rows": 0, "ok": False}
    pip = PAIRS[pair]["pip"]
    spread_c = (df["ask_c"] - df["bid_c"]) / pip
    mid = (df["ask_c"] + df["bid_c"]) / 2
    ret = np.log(mid).diff()
    crossed = int(((df["ask_l"] < df["bid_l"] - 1e-12) | (df["ask_c"] < df["bid_c"] - 1e-12)).sum())
    # 平日（UTC 月 00:00〜金 20:00）で 1 時間を超える欠損
    idx = df.index
    gaps = pd.Series(idx[1:] - idx[:-1], index=idx[1:])
    wd = gaps.index.weekday
    weekday_gaps = gaps[(gaps > pd.Timedelta(hours=1)) & (wd >= 0) & (wd <= 4)
                        & ~((wd == 0) & (gaps <= pd.Timedelta(hours=60)))]
    big_gaps = weekday_gaps[weekday_gaps > pd.Timedelta(hours=3)]
    out = {
        "pair": pair, "rows": int(len(df)), "first": str(idx.min()), "last": str(idx.max()),
        "duplicates": int(idx.duplicated().sum()), "crossed_quotes": crossed,
        "spread_pips_median": round(float(spread_c.median()), 3),
        "spread_pips_p95": round(float(spread_c.quantile(0.95)), 3),
        "spread_pips_max": round(float(spread_c.max()), 2),
        "abs_ret_gt_2pct": int((ret.abs() > 0.02).sum()),
        "weekday_gaps_gt_3h": int(len(big_gaps)),
        "largest_gap_h": round(float(gaps.max() / pd.Timedelta(hours=1)), 1) if len(gaps) else 0,
    }
    lo, hi = PLAUSIBLE[pair]
    out["price_min"] = round(float(mid.min()), 5)
    out["price_max"] = round(float(mid.max()), 5)
    problems = []
    if out["duplicates"]:
        problems.append("duplicates")
    if out["rows"] < 1000:
        problems.append("too_few_rows")
    if not (lo <= out["price_min"] and out["price_max"] <= hi):
        problems.append(f"price_out_of_range[{lo},{hi}]")
    if not (0 <= out["spread_pips_median"] <= 5):
        problems.append("spread_median_implausible")
    if crossed > len(df) * 0.001:
        problems.append("crossed_quotes")
    out["problems"] = problems
    out["ok"] = not problems
    return out


def write_quality_report(frames: dict, dest) -> list[dict]:
    rep = [quality(df, p) for p, df in frames.items()]
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(rep, indent=2, ensure_ascii=False))
    return rep
