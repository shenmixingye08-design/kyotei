"""FRED（セントルイス連銀）の公開 CSV（API キー不要）。

1. 短期金利: OECD 月次 3 か月物インターバンク金利 IR3TIB01{国}M156N（%）→ スワップ / キャリーの近似に使う
2. 為替の検証用: 米連銀 H.10 正午レート（日次）→ Dukascopy 価格のクロスチェック
取得できない場合に値を作って埋めることはしない（欠損として扱う）。
"""
from __future__ import annotations

import io
import shutil
import subprocess
import time

import pandas as pd
import requests

from ..common import DATA_DIR

FRED_CSV = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}"
# 同じ系列の別経路（fredgraph が GitHub Actions から read timeout になることがあるため順に試す）
FRED_URLS = (FRED_CSV,
             "https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}&cosd=2008-01-01",
             "https://alfred.stlouisfed.org/graph/alfredgraph.csv?id={sid}",
             "https://fred.stlouisfed.org/series/{sid}/downloaddata/{sid}.csv")
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36 "
      "fx-autopilot-research")
FRESH_DAYS = 3        # これより新しいローカル CSV（Actions cache）は再取得しない
FRED_DIR = DATA_DIR / "fred"
SHORT_RATES = {"USD": "IR3TIB01USM156N", "EUR": "IR3TIB01EZM156N", "JPY": "IR3TIB01JPM156N",
               "GBP": "IR3TIB01GBM156N", "AUD": "IR3TIB01AUM156N", "NZD": "IR3TIB01NZM156N",
               "CAD": "IR3TIB01CAM156N", "CHF": "IR3TIB01CHM156N"}
# H.10: 値の向き（"base_per_quote"= 1 base あたり quote、つまりペア表記どおり / "inverse"= 逆数でペアになる）
H10 = {"USDJPY": ("DEXJPUS", False), "EURUSD": ("DEXUSEU", False), "GBPUSD": ("DEXUSUK", False),
       "AUDUSD": ("DEXUSAL", False), "NZDUSD": ("DEXUSNZ", False), "USDCAD": ("DEXCAUS", False),
       "USDCHF": ("DEXSZUS", False)}


def parse_csv(text: str) -> pd.Series:
    df = pd.read_csv(io.StringIO(text))
    dcol = df.columns[0]
    vcol = df.columns[1]
    v = pd.to_numeric(df[vcol].replace(".", pd.NA), errors="coerce")
    s = pd.Series(v.to_numpy(dtype=float), index=pd.to_datetime(df[dcol]), name=vcol).dropna()
    return s


def _looks_csv(text: str) -> bool:
    head = text.lstrip()[:200].lower()
    return bool(head) and "<html" not in head and "," in head


def _curl(url: str, timeout: int) -> str | None:
    if not shutil.which("curl"):
        return None
    r = subprocess.run(["curl", "-sSfL", "--compressed", "-m", str(timeout), "-A", UA, url],
                       capture_output=True, text=True, timeout=timeout + 10)
    return r.stdout if r.returncode == 0 else None


def fetch(sid: str, session=None, retries: int = 2, timeout=(10, 60)) -> pd.Series:
    """複数 URL × (requests, curl) を順に試す。どれも駄目なら RuntimeError（値は作らない）。"""
    s = session or requests.Session()
    errs = []
    for k in range(retries):
        for tpl in FRED_URLS:
            url = tpl.format(sid=sid)
            try:
                r = s.get(url, timeout=timeout, headers={"User-Agent": UA, "Accept": "text/csv,*/*"})
                if r.status_code == 200 and _looks_csv(r.text):
                    return parse_csv(r.text)
                errs.append(f"{url}: HTTP {r.status_code}")
            except requests.RequestException as e:  # noqa: PERF203
                errs.append(f"{url}: {type(e).__name__}")
            try:
                t = _curl(url, timeout[1])
                if t and _looks_csv(t):
                    return parse_csv(t)
                errs.append(f"{url}: curl failed")
            except (subprocess.SubprocessError, OSError) as e:
                errs.append(f"{url}: curl {type(e).__name__}")
        time.sleep(3 * (2 ** k))
    raise RuntimeError(f"FRED {sid}: " + " | ".join(errs[-4:]))


def ingest(log=print, max_consecutive_fail: int = 2) -> dict:
    """取得済みで新しい CSV（Actions cache 由来）は再利用。連続で全経路失敗したら残りは打ち切る（時間を浪費しない）。"""
    FRED_DIR.mkdir(parents=True, exist_ok=True)
    rep = {}
    ids = list(SHORT_RATES.values()) + [v[0] for v in H10.values()]
    fails = 0
    with requests.Session() as ses:
        for sid in ids:
            p = FRED_DIR / f"{sid}.csv"
            if p.exists() and (time.time() - p.stat().st_mtime) < FRESH_DAYS * 86400:
                rep[sid] = {"cached": True, "rows": int(len(load(sid)))}
            elif fails >= max_consecutive_fail:
                rep[sid] = {"skipped": "FRED unreachable this run", **({"stale_cache": True} if p.exists() else {})}
            else:
                try:
                    ser = fetch(sid, ses)
                    ser.to_frame("value").to_csv(p)
                    rep[sid] = {"rows": int(len(ser)), "first": str(ser.index.min())[:10], "last": str(ser.index.max())[:10]}
                    fails = 0
                except Exception as e:  # noqa: BLE001
                    fails += 1
                    rep[sid] = {"error": str(e)[:400], **({"stale_cache": True} if p.exists() else {})}
            log(f"  FRED {sid}: {rep[sid]}")
    return rep


def load(sid: str) -> pd.Series:
    p = FRED_DIR / f"{sid}.csv"
    if not p.exists():
        raise FileNotFoundError(f"{p} がありません（python -m fxap.cli ingest-fred）")
    df = pd.read_csv(p, index_col=0, parse_dates=True)
    return df["value"].astype(float)


def load_short_rates() -> dict:
    """ccy -> 月初 index の小数金利。1 つも無ければ FileNotFoundError。"""
    out = {}
    for ccy, sid in SHORT_RATES.items():
        try:
            s = load(sid) / 100.0
            s.index = pd.DatetimeIndex(s.index).to_period("M").to_timestamp()
            out[ccy] = s[~s.index.duplicated(keep="last")].sort_index()
        except FileNotFoundError:
            continue
    if not out:
        raise FileNotFoundError("FRED 短期金利が 1 つもありません")
    return out


def crosscheck(frames: dict) -> pd.DataFrame:
    """Dukascopy の mid（16:00 UTC 足の終値 ≒ NY 正午）と H.10 正午レートの日次比較。"""
    rows = []
    for pair, (sid, _inv) in H10.items():
        if pair not in frames:
            continue
        try:
            ref = load(sid)
        except FileNotFoundError:
            continue
        d = frames[pair]
        mid = (d["bid_c"] + d["ask_c"]) / 2
        noon = mid[mid.index.hour == 16]
        noon.index = noon.index.tz_convert(None).normalize()
        j = pd.concat([noon, ref], axis=1, keys=["duka", "h10"]).dropna()
        if not len(j):
            continue
        diff = (j["duka"] / j["h10"] - 1).abs()
        rows.append({"pair": pair, "days": int(len(j)), "median_abs_diff_pct": round(float(diff.median() * 100), 4),
                     "p99_abs_diff_pct": round(float(diff.quantile(0.99) * 100), 4),
                     "max_abs_diff_pct": round(float(diff.max() * 100), 3),
                     "days_gt_0_5pct": int((diff > 0.005).sum()), "days_gt_1pct": int((diff > 0.01).sum()),
                     "worst_day": str(diff.idxmax())[:10]})
    return pd.DataFrame(rows)
