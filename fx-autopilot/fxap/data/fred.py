"""FRED（セントルイス連銀）の公開 CSV（API キー不要）。

1. 短期金利: OECD 月次 3 か月物インターバンク金利 IR3TIB01{国}M156N（%）→ スワップ / キャリーの近似に使う
2. 為替の検証用: 米連銀 H.10 正午レート（日次）→ Dukascopy 価格のクロスチェック
取得できない場合に値を作って埋めることはしない（欠損として扱う）。
"""
from __future__ import annotations

import io
import time

import pandas as pd
import requests

from ..common import DATA_DIR

FRED_CSV = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}"
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


def fetch(sid: str, session=None, retries: int = 4) -> pd.Series:
    s = session or requests.Session()
    last = None
    for k in range(retries):
        try:
            r = s.get(FRED_CSV.format(sid=sid), timeout=30, headers={"User-Agent": "fx-autopilot research"})
            if r.status_code == 200 and r.text.strip():
                return parse_csv(r.text)
            last = f"HTTP {r.status_code}"
        except requests.RequestException as e:  # noqa: PERF203
            last = repr(e)
        time.sleep(2 * (2 ** k))
    raise RuntimeError(f"FRED {sid}: {last}")


def ingest(log=print) -> dict:
    FRED_DIR.mkdir(parents=True, exist_ok=True)
    rep = {}
    ids = list(SHORT_RATES.values()) + [v[0] for v in H10.values()]
    with requests.Session() as ses:
        for sid in ids:
            try:
                ser = fetch(sid, ses)
                ser.to_frame("value").to_csv(FRED_DIR / f"{sid}.csv")
                rep[sid] = {"rows": int(len(ser)), "first": str(ser.index.min())[:10], "last": str(ser.index.max())[:10]}
            except Exception as e:  # noqa: BLE001
                rep[sid] = {"error": repr(e)}
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
