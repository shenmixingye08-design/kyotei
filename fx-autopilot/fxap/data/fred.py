"""FRED（セントルイス連銀）の公開 CSV（API キー不要）。

1. 短期金利: OECD 月次 3 か月物インターバンク金利 IR3TIB01{国}M156N（%）→ スワップ / キャリーの近似に使う
2. 為替の検証用: 米連銀 H.10 正午レート（日次）→ Dukascopy 価格のクロスチェック / V7 のバリュー（長期の実質為替）
3. 消費者物価（V7 のバリュー = 5 年の実質為替変化）: 通貨ごとに候補系列を順に試し、最新まで続いている最初のものを使う
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
# FRED に届かない場合の代替: DBnomics の OECD MEI ミラー（同じ OECD 3 か月物金利 IR3TIB01）
DBNOMICS = "https://api.db.nomics.world/v22/series/OECD/MEI/{cc}.{sub}.ST.M?observations=1&format=json"
# 3 か月物の代替系列（国によって IR3TIB が無い: 米国は CD 3M、豪 NZ は銀行手形 3M など）
DBN_SUBJECTS = ("IR3TIB01", "IR3TBB01", "IR3TCD01")
DBN_CC = {"IR3TIB01USM156N": "USA", "IR3TIB01EZM156N": "EA19", "IR3TIB01JPM156N": "JPN", "IR3TIB01GBM156N": "GBR",
          "IR3TIB01AUM156N": "AUS", "IR3TIB01NZM156N": "NZL", "IR3TIB01CAM156N": "CAN", "IR3TIB01CHM156N": "CHE"}
BUDGET_SEC = 360      # ingest 全体の時間上限（届かないサイトで CI を止めない）
FRESH_DAYS = 3        # これより新しいローカル CSV（Actions cache）は再取得しない
FRED_DIR = DATA_DIR / "fred"
SHORT_RATES = {"USD": "IR3TIB01USM156N", "EUR": "IR3TIB01EZM156N", "JPY": "IR3TIB01JPM156N",
               "GBP": "IR3TIB01GBM156N", "AUD": "IR3TIB01AUM156N", "NZD": "IR3TIB01NZM156N",
               "CAD": "IR3TIB01CAM156N", "CHF": "IR3TIB01CHM156N"}
# H.10: 値の向き（"base_per_quote"= 1 base あたり quote、つまりペア表記どおり / "inverse"= 逆数でペアになる）
H10 = {"USDJPY": ("DEXJPUS", False), "EURUSD": ("DEXUSEU", False), "GBPUSD": ("DEXUSUK", False),
       "AUDUSD": ("DEXUSAL", False), "NZDUSD": ("DEXUSNZ", False), "USDCAD": ("DEXCAUS", False),
       "USDCHF": ("DEXSZUS", False)}


# CPI: 通貨 -> 候補 FRED 系列（上から順に試す）。保存名は CPI_{ccy}.csv（どの系列かは rates_ingest.json に記録）
CPI = {"USD": ["CPIAUCSL", "CPALTT01USM661N"],
       "EUR": ["CP0000EZ19M086NEST", "CPALTT01EZM661N", "CP0000EA20M086NEST"],
       "JPY": ["CPALTT01JPM661N", "JPNCPIALLMINMEI"],
       "GBP": ["CPALTT01GBM661N", "GBRCPIALLMINMEI"],
       "AUD": ["CPALTT01AUQ661N", "AUSCPIALLQINMEI"],
       "NZD": ["CPALTT01NZQ661N", "NZLCPIALLQINMEI"],
       "CAD": ["CPALTT01CAM661N", "CANCPIALLMINMEI"],
       "CHF": ["CPALTT01CHM661N", "CHECPIALLMINMEI"]}
CPI_MAX_AGE_DAYS = 270      # 最終観測がこれより古い系列は「最新まで続いていない」とみなして次の候補へ


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


def _curl(url: str, timeout: int, ua: str | None = UA) -> str | None:
    if not shutil.which("curl"):
        return None
    r = subprocess.run(["curl", "-sSfL", "--compressed", "-m", str(timeout)] + (["-A", ua] if ua else []) + [url],
                       capture_output=True, text=True, timeout=timeout + 10)
    return r.stdout if r.returncode == 0 else None


def fetch(sid: str, session=None, retries: int = 1, timeout=(8, 25)) -> pd.Series:
    """複数 URL × (requests, curl) を順に試す。どれも駄目なら RuntimeError（値は作らない）。"""
    s = session or requests.Session()
    errs = []
    for k in range(retries):
        for tpl in FRED_URLS:
            url = tpl.format(sid=sid)
            try:   # 既定 UA の curl（Actions の疎通確認で 200 が返った経路）を最初に試す
                t = _curl(url, timeout[1], ua=None)
                if t and _looks_csv(t):
                    return parse_csv(t)
                errs.append(f"{url}: curl(default UA) failed")
            except (subprocess.SubprocessError, OSError) as e:
                errs.append(f"{url}: curl {type(e).__name__}")
            try:
                r = s.get(url, timeout=timeout, headers={"Accept": "text/csv,*/*"})
                if r.status_code == 200 and _looks_csv(r.text):
                    return parse_csv(r.text)
                errs.append(f"{url}: HTTP {r.status_code}")
            except requests.RequestException as e:  # noqa: PERF203
                errs.append(f"{url}: {type(e).__name__}")
        if k + 1 < retries:
            time.sleep(3 * (2 ** k))
    raise RuntimeError(f"FRED {sid}: " + " | ".join(errs[-4:]))


def fetch_cpi(ccy: str, session=None):
    """候補系列を順に試し、最終観測が CPI_MAX_AGE_DAYS 以内の最初の系列を返す（(series, sid)）。"""
    errs, stale = [], None
    for sid in CPI[ccy]:
        try:
            ser = fetch(sid, session)
        except RuntimeError as e:
            errs.append(str(e)[:120])
            continue
        age = (pd.Timestamp.now() - ser.index.max()).days
        if age <= CPI_MAX_AGE_DAYS:
            return ser, sid
        errs.append(f"{sid}: last {ser.index.max():%Y-%m} (stale)")
        stale = stale or (ser, sid + "(stale)")
    if stale is not None:          # 全候補が古い場合は古い系列を使う（V7 側で観測日の古さを判定する）
        return stale
    raise RuntimeError(f"CPI {ccy}: " + " | ".join(errs))


def load_cpi() -> dict:
    """ccy -> 月次 CPI（月初 index、四半期系列は月へ前方埋め）と公表遅れ（月）。無い通貨は含めない。"""
    out = {}
    for ccy in CPI:
        try:
            s = load(f"CPI_{ccy}")
        except FileNotFoundError:
            continue
        s = s[s > 0]
        s.index = pd.DatetimeIndex(s.index).to_period("M").to_timestamp()
        s = s[~s.index.duplicated(keep="last")].sort_index()
        quarterly = len(s) > 3 and pd.Series(s.index).diff().dt.days.median() > 60
        m = s.resample("MS").ffill()
        out[ccy] = {"cpi": m, "lag_months": 5 if quarterly else 2, "last_obs": s.index.max()}
    return out


def fetch_dbnomics(sid: str, session=None, timeout=(8, 25)) -> pd.Series:
    """DBnomics（OECD MEI ミラー）から同じ系列を取る。FRED と同じ % 単位・月次。"""
    cc = DBN_CC.get(sid)
    if cc is None:
        raise RuntimeError(f"DBnomics: {sid} は対象外")
    s = session or requests.Session()
    errs = []
    docs = []
    for sub in DBN_SUBJECTS:
        r = s.get(DBNOMICS.format(cc=cc, sub=sub), timeout=timeout, headers={"User-Agent": UA})
        if r.status_code == 200:
            docs = r.json().get("series", {}).get("docs", [])
            if docs:
                break
        errs.append(f"{cc}.{sub}: HTTP {r.status_code}")
    if not docs:
        raise RuntimeError("DBnomics " + ", ".join(errs))
    d = docs[0]
    v = pd.to_numeric(pd.Series(d["value"]), errors="coerce").to_numpy(dtype=float)
    ser = pd.Series(v, index=pd.to_datetime(pd.Series(d["period"]).astype(str)), name=sid).dropna()
    if not len(ser):
        raise RuntimeError(f"DBnomics {cc}: empty")
    return ser


def _obs_fresh(sid: str) -> bool:
    """キャッシュの最終観測日が新しいか（月次 120 日 / 日次 21 日以内）。古い代替ソース（DBnomics の
    終了済み MEI 等）で取った CSV を、FRED が取れるようになった後も使い続けないため。"""
    try:
        last = load(sid).index.max()
    except Exception:  # noqa: BLE001
        return False
    lim = 120 if sid in SHORT_RATES.values() else (200 if sid.startswith("CPI_") else 21)
    return (pd.Timestamp.now() - pd.Timestamp(last).tz_localize(None)).days <= lim


def ingest(log=print, max_consecutive_fail: int = 2) -> dict:
    """取得済みで新しい CSV（Actions cache 由来）は再利用。グループ（短期金利 / H.10）ごとに、
    連続で全経路失敗するか時間上限を超えたら残りを打ち切る（届かないサイトで CI を止めない）。"""
    FRED_DIR.mkdir(parents=True, exist_ok=True)
    rep = {}
    groups = [list(SHORT_RATES.values()), [v[0] for v in H10.values()], [f"CPI_{c}" for c in CPI]]
    with requests.Session() as ses:
        for ids in groups:
            fails, t0 = 0, time.time()
            for sid in ids:
                p = FRED_DIR / f"{sid}.csv"
                if p.exists() and (time.time() - p.stat().st_mtime) < FRESH_DAYS * 86400 and _obs_fresh(sid):
                    rep[sid] = {"cached": True, "rows": int(len(load(sid)))}
                elif fails >= max_consecutive_fail or time.time() - t0 > BUDGET_SEC / 2:
                    rep[sid] = {"skipped": "source unreachable this run", **({"stale_cache": True} if p.exists() else {})}
                else:
                    try:
                        try:
                            if sid.startswith("CPI_"):
                                ser, src = fetch_cpi(sid[4:], ses)
                            else:
                                ser, src = fetch(sid, ses), "fred"
                        except RuntimeError as e1:
                            if sid not in DBN_CC:
                                raise
                            try:
                                ser, src = fetch_dbnomics(sid, ses), "dbnomics_oecd_mei"
                            except Exception as e2:  # noqa: BLE001
                                raise RuntimeError(f"{e1} || {e2!r}") from e2
                        ser.to_frame("value").to_csv(p)
                        rep[sid] = {"source": src, "rows": int(len(ser)), "first": str(ser.index.min())[:10],
                                    "last": str(ser.index.max())[:10]}
                        fails = 0
                    except Exception as e:  # noqa: BLE001
                        fails += 1
                        rep[sid] = {"error": str(e)[:600], **({"stale_cache": True} if p.exists() else {})}
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
