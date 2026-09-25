"""V2 候補（config/research_plan_v2.yaml に事前登録）。v1 の戦略・LOCK は変更しない。

共通の約束:
  - 日足は NY クローズ（21:00 UTC）区切り。日足の値は、その日の最後の H1 足の終値で確定 → その足で判断 → 次の H1 始値で約定
  - 4H 足も完成した足のみ使用（features.map_to_h1）
  - "vol" 列 = 日次実現ボラ（60 日、年率）。vol_target サイズ決定で使う
  - sizing はパラメータとして持ち、risk_overrides() で Risk Engine に渡す（数量は Risk Engine が決める）
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .. import features as F
from .. import swap as swapm
from ..common import PAIRS
from .base import Strategy, cross_dn, cross_up, register

SESSIONS = {"all": (0, 24), "tokyo": (0, 8), "london": (7, 16), "ny": (12, 21),
            "tokyo_london": (6, 9), "london_ny": (12, 16)}
CURRENCIES = ["USD", "EUR", "JPY", "GBP", "AUD"]

_cache: dict = {}


def _key(df, tag):
    return (tag, id(df), len(df), str(df.index[-1]) if len(df) else "")


def dframe(df: pd.DataFrame) -> dict:
    """日足指標（日足 index）と H1 への割り当て（因果的）。"""
    k = _key(df, "d")
    if k in _cache:
        return _cache[k]
    m = F.mid(df)
    d = F.daily(m)
    ind = pd.DataFrame(index=d.index)
    ind["c"], ind["h"], ind["l"] = d["c"], d["h"], d["l"]
    lr = np.log(d["c"]).diff()
    ind["atr20"] = F.atr(d[["o", "h", "l", "c"]], 20)
    ind["sd60"] = lr.rolling(60, min_periods=40).std()
    ind["vol"] = ind["sd60"] * np.sqrt(260)
    ind["label"] = d.index
    h1, dec, labs = F.map_complete(ind, d["avail"], pd.Timedelta(hours=24), df.index)
    dd = ind.loc[labs].copy()
    dd["dec"] = dec
    is_close = pd.Series(df.index.isin(dec), index=df.index)
    out = {"d": dd, "h1": h1, "is_close": is_close}
    _cache[k] = out
    return out


def rframe(df):
    """4H レジーム（v1 regime_frame と同じ指標。確定判定だけ map_complete に置き換え）。"""
    k = _key(df, "r")
    if k not in _cache:
        m = F.mid(df)
        h4 = F.higher_tf(m, "4h")
        ind = pd.DataFrame(index=h4.index)
        ind["adx"] = F.adx(h4, 14)
        ind["atr"] = F.atr(h4, 14)
        ind["atr_pct"] = F.pct_rank(ind["atr"] / h4["c"], 6 * 260)
        ind["ema50"] = F.ema(h4["c"], 50)
        ind["ema200"] = F.ema(h4["c"], 200)
        ind["f20"], ind["s100"] = F.ema(h4["c"], 20), F.ema(h4["c"], 100)
        ind["c"] = h4["c"]
        ind["label"] = ind.index
        h1, dec, labs = F.map_complete(ind, h4["avail"], pd.Timedelta(hours=4), df.index)
        _cache[k] = (h1, dec, ind, labs)
    return _cache[k][0]


def rframe_events(df):
    rframe(df)
    return _cache[_key(df, "r")]


def regime_ok(rf: pd.DataFrame, mode: str) -> pd.Series:
    if mode == "trend_only":
        return rf["adx"] >= 20
    if mode == "no_high_vol":
        return rf["atr_pct"] < 0.90
    return pd.Series(True, index=rf.index)


def _on_h1(daily_series: pd.Series, dfm: dict) -> pd.Series:
    """日足 index の値を、その日足が確定した H1 足（判断足）だけに置く（それ以外は NaN）。"""
    d = dfm["d"]
    s = pd.Series(daily_series.reindex(d.index).values, index=pd.DatetimeIndex(d["dec"]))
    s = s[~s.index.duplicated(keep="last")]
    return s.reindex(dfm["is_close"].index)


class _V2(Strategy):
    version = "v2"

    def risk_overrides(self) -> dict:
        return {"sizing": self.params.get("sizing", "risk_stop")}

    @staticmethod
    def weekly_mask(dfm) -> pd.Series:
        """火曜 NY クローズ（= 月曜 21:00 UTC 開始の日足）で週 1 回判断。"""
        lab = dfm["d"]["label"]
        return _on_h1(pd.Series(lab.dt.weekday == 0, index=lab.index).astype(float), dfm) == 1.0


# ------------------------------------------------------------------ 1. 中期トレンド
@register
class V2D1Donchian(_V2):
    name = "v2_d1_donchian"
    family = "trend_mid"
    grid = {"n": [20, 55, 100], "regime": ["none", "trend_only", "no_high_vol"],
            "sizing": ["risk_stop", "vol_target", "fixed_notional"]}

    def generate(self, df, pair):
        p = self.params
        dm = dframe(df)
        d = dm["d"]
        hi = d["h"].rolling(p["n"], min_periods=p["n"]).max().shift(1)
        lo = d["l"].rolling(p["n"], min_periods=p["n"]).min().shift(1)
        xhi = d["h"].rolling(p["n"] // 2).max().shift(1)
        xlo = d["l"].rolling(p["n"] // 2).min().shift(1)
        up = (d["c"] > hi) & (d["c"].shift(1) <= hi.shift(1))
        dn = (d["c"] < lo) & (d["c"].shift(1) >= lo.shift(1))
        out = self.empty(df.index)
        e = _on_h1(up.astype(float) - dn.astype(float), dm).fillna(0)
        ok = regime_ok(rframe(df), p["regime"]).fillna(False)
        out["entry"] = np.where(ok, e, 0).astype(int)
        out["exit_long"] = _on_h1((d["c"] < xlo).astype(float), dm) == 1.0
        out["exit_short"] = _on_h1((d["c"] > xhi).astype(float), dm) == 1.0
        out["sl_dist"] = 3.0 * dm["h1"]["atr20"]
        out["vol"] = dm["h1"]["vol"]
        out.loc[out["sl_dist"].isna() | out["vol"].isna(), "entry"] = 0
        return out


@register
class V2D1TSMom(_V2):
    name = "v2_d1_tsmom"
    family = "trend_mid"
    grid = {"lookback": [63, 126, 252], "sizing": ["risk_stop", "vol_target", "fixed_notional"]}

    def generate(self, df, pair):
        p = self.params
        dm = dframe(df)
        d = dm["d"]
        z = np.log(d["c"] / d["c"].shift(p["lookback"])) / (d["sd60"] * np.sqrt(p["lookback"]))
        wk = self.weekly_mask(dm)
        zz = _on_h1(z, dm)
        out = self.empty(df.index)
        out["entry"] = np.where(wk & (zz > 0), 1, np.where(wk & (zz < 0), -1, 0))
        out["sl_dist"] = 4.0 * dm["h1"]["atr20"]
        out["vol"] = dm["h1"]["vol"]
        out.loc[out["sl_dist"].isna() | out["vol"].isna(), "entry"] = 0
        return out


@register
class V2H4Ema(_V2):
    name = "v2_h4_ema"
    family = "trend_mid"
    grid = {"fast_slow": ["20_100", "50_200"], "adx_min": [0, 20], "regime": ["none", "trend_only", "no_high_vol"]}

    def generate(self, df, pair):
        p = self.params
        h1, dec, ind, labs = rframe_events(df)
        fcol, scol = ("f20", "s100") if p["fast_slow"] == "20_100" else ("ema50", "ema200")
        f, sl = ind[fcol], ind[scol]
        up = cross_up(f, sl) & (ind["adx"] >= p["adx_min"])
        dn = cross_dn(f, sl) & (ind["adx"] >= p["adx_min"])
        sig = (up.astype(float) - dn.astype(float))
        # 4H 足が確定した H1 足（判断足）だけにイベントを置く
        ev = pd.Series(0.0, index=df.index)
        ev.loc[dec] = sig.loc[labs].fillna(0).to_numpy()
        state = np.sign(h1[fcol] - h1[scol])
        ok = regime_ok(h1, p["regime"]).fillna(False)
        out = self.empty(df.index)
        out["entry"] = np.where(ok, ev, 0).astype(int)
        out["exit_long"] = state < 0
        out["exit_short"] = state > 0
        out["sl_dist"] = 3.0 * h1["atr"]
        out["trail_dist"] = 3.0 * h1["atr"]
        out["vol"] = dframe(df)["h1"]["vol"]
        out.loc[out["sl_dist"].isna() | out["vol"].isna(), "entry"] = 0
        return out


# ------------------------------------------------------------------ 2. Trend × Carry
def carry_series(pair: str, index: pd.DatetimeIndex) -> pd.Series:
    b, q = PAIRS[pair]["base"], PAIRS[pair]["quote"]
    months = pd.Series(index.tz_convert(None).to_period("M"), index=index)
    vals = {mo: swapm.carry_lagged(b, q, pd.Timestamp(mo.start_time, tz="UTC") + pd.Timedelta(days=14))
            for mo in months.unique()}
    return months.map(vals).astype(float)


@register
class V2TrendCarry(_V2):
    name = "v2_trend_carry"
    family = "trend_carry"
    grid = {"mode": ["agree", "carry_trend_filter", "composite"], "sizing": ["risk_stop", "vol_target"]}

    def generate(self, df, pair):
        p = self.params
        dm = dframe(df)
        d = dm["d"]
        z = np.log(d["c"] / d["c"].shift(126)) / (d["sd60"] * np.sqrt(126))
        zz = _on_h1(z, dm)
        c = carry_series(pair, df.index)
        if p["mode"] == "agree":
            dirn = np.where((np.sign(zz) == np.sign(c)) & (c.abs() > 0.005), np.sign(zz), 0)
        elif p["mode"] == "carry_trend_filter":
            dirn = np.where((c.abs() > 0.005) & (zz * np.sign(c) > -0.5), np.sign(c), 0)
        else:
            sc = zz + c / 0.02
            dirn = np.where(sc.abs() > 0.5, np.sign(sc), 0)
        dirn = pd.Series(np.nan_to_num(dirn), index=df.index)
        wk = self.weekly_mask(dm) & zz.notna()
        out = self.empty(df.index)
        out["entry"] = np.where(wk, dirn, 0).astype(int)
        out["exit_long"] = wk & (dirn <= 0)
        out["exit_short"] = wk & (dirn >= 0)
        out["sl_dist"] = 4.0 * dm["h1"]["atr20"]
        out["vol"] = dm["h1"]["vol"]
        out.loc[out["sl_dist"].isna() | out["vol"].isna(), "entry"] = 0
        return out


# ------------------------------------------------------------------ 4. Cross-Pair（通貨強弱）
def strength_scores(data: dict, pairs, lookback: int) -> pd.DataFrame:
    """各ペアのスコア = 強弱(base) - 強弱(quote)。強弱 = そのペアのボラ正規化リターンの符号付き平均（日足 index）。"""
    rets = {}
    for p in pairs:
        d = dframe(data[p])["d"]
        r = np.log(d["c"] / d["c"].shift(lookback)) / (d["sd60"] * np.sqrt(lookback))
        rets[p] = pd.Series(r.values, index=pd.DatetimeIndex(d["label"]).normalize())
    R = pd.DataFrame(rets)
    R = R[~R.index.duplicated(keep="last")]
    S = pd.DataFrame(0.0, index=R.index, columns=CURRENCIES)
    n = pd.DataFrame(0.0, index=R.index, columns=CURRENCIES)
    for p in pairs:
        b, q = PAIRS[p]["base"], PAIRS[p]["quote"]
        v = R[p]
        ok = v.notna()
        S.loc[ok, b] += v[ok]
        S.loc[ok, q] -= v[ok]
        n.loc[ok, b] += 1
        n.loc[ok, q] += 1
    S = S / n.replace(0, np.nan)
    return pd.DataFrame({p: S[PAIRS[p]["base"]] - S[PAIRS[p]["quote"]] for p in pairs})


@register
class V2XPairStrength(_V2):
    name = "v2_xpair_strength"
    family = "cross_pair"
    needs_all_pairs = True
    grid = {"lookback": [20, 60, 120], "top_k": [2, 3], "sizing": ["risk_stop", "vol_target", "fixed_notional"]}

    def generate_all(self, data: dict, pairs) -> dict:
        p = self.params
        sc = strength_scores(data, pairs, p["lookback"])
        rank = sc.abs().rank(axis=1, ascending=False, method="first")
        dirn = np.sign(sc).where(rank <= p["top_k"], 0.0).fillna(0.0)
        out = {}
        for pair in pairs:
            df = data[pair]
            dm = dframe(df)
            lab = pd.DatetimeIndex(dm["d"]["label"]).normalize()
            dd = pd.Series(dirn[pair].reindex(lab).values, index=dm["d"].index)
            h = _on_h1(dd, dm)
            wk = self.weekly_mask(dm) & h.notna()
            o = self.empty(df.index)
            o["entry"] = np.where(wk, h.fillna(0), 0).astype(int)
            o["exit_long"] = wk & (h <= 0)
            o["exit_short"] = wk & (h >= 0)
            o["sl_dist"] = 4.0 * dm["h1"]["atr20"]
            o["vol"] = dm["h1"]["vol"]
            o.loc[o["sl_dist"].isna() | o["vol"].isna(), "entry"] = 0
            out[pair] = o
        return out

    def generate(self, df, pair):
        raise RuntimeError("v2_xpair_strength は generate_all（全ペア）で生成する")


# ------------------------------------------------------------------ 3. Session Filter
@register
class V2SessionBreakout(_V2):
    name = "v2_session_breakout"
    family = "session"
    grid = {"session": list(SESSIONS)}

    def generate(self, df, pair):
        p = self.params
        m = F.mid(df)
        rf = rframe(df)
        trend = np.sign(rf["ema50"] - rf["ema200"])
        hi, lo = F.donchian_prev(m, 24)
        a, b = SESSIONS[p["session"]]
        hr = df.index.hour
        ins = (hr >= a) & (hr < b)
        out = self.empty(df.index)
        out.loc[ins & (trend > 0) & (m["c"] > hi) & (m["c"].shift(1) <= hi.shift(1)), "entry"] = 1
        out.loc[ins & (trend < 0) & (m["c"] < lo) & (m["c"].shift(1) >= lo.shift(1)), "entry"] = -1
        out["exit_long"] = trend < 0
        out["exit_short"] = trend > 0
        atr4 = rf["atr"]
        out["sl_dist"] = 1.5 * atr4
        out["trail_dist"] = 3.0 * atr4
        out["max_bars"] = 72
        out["vol"] = dframe(df)["h1"]["vol"]
        out.loc[out["sl_dist"].isna() | out["vol"].isna() | hi.isna(), "entry"] = 0
        return out


# ------------------------------------------------------------------ ML（日足・プール学習）
@register
class V2MLD1Logit(_V2):
    name = "v2_ml_d1_logit"
    family = "ml"
    needs_all_pairs = True
    grid = {"th": [0.55, 0.60]}
    H = 5
    _pcache: dict = {}

    def _proba(self, data, pairs):
        key = tuple((p, len(data[p]), str(data[p].index[-1])) for p in pairs)
        if key in V2MLD1Logit._pcache:
            return V2MLD1Logit._pcache[key]
        from sklearn.linear_model import LogisticRegression
        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import StandardScaler
        st = {L: strength_scores(data, pairs, L) for L in (20, 60)}
        rows = []
        for p in pairs:
            dm = dframe(data[p])
            d = dm["d"]
            lab = pd.DatetimeIndex(d["label"]).normalize()
            X = pd.DataFrame(index=d.index)
            for L in (5, 20, 60, 126, 252):
                X[f"z{L}"] = np.log(d["c"] / d["c"].shift(L)) / (d["sd60"] * np.sqrt(L))
            X["volr"] = d["sd60"] / d["sd60"].rolling(250, min_periods=100).mean()
            X["carry"] = carry_series(p, pd.DatetimeIndex(d.index)).values
            for L in (20, 60):
                X[f"str{L}"] = st[L][p].reindex(lab).values
            fwd = np.log(d["c"].shift(-self.H) / d["c"])
            X["y"] = (fwd > 0).astype(float).where(fwd.notna())
            X["pair"] = p
            rows.append(X)
        A = pd.concat(rows).sort_index()
        feats = [c for c in A.columns if c not in ("y", "pair")]
        A["proba"] = np.nan
        for Y in range(2014, A.index.max().year + 1):
            t0 = pd.Timestamp(f"{Y}-01-01", tz="UTC")
            t1 = pd.Timestamp(f"{Y + 1}-01-01", tz="UTC")
            purge = t0 - pd.Timedelta(days=self.H + 3)
            tr = (A.index < purge) & A[feats].notna().all(axis=1) & A["y"].notna()
            te = (A.index >= t0) & (A.index < t1) & A[feats].notna().all(axis=1)
            if tr.sum() < 2000 or not te.any():
                continue
            mdl = make_pipeline(StandardScaler(), LogisticRegression(C=0.1, max_iter=500))
            mdl.fit(A.loc[tr, feats].to_numpy(), A.loc[tr, "y"].to_numpy())
            A.loc[te, "proba"] = mdl.predict_proba(A.loc[te, feats].to_numpy())[:, 1]
        out = {p: A.loc[A["pair"] == p, "proba"] for p in pairs}
        V2MLD1Logit._pcache[key] = out
        return out

    def generate_all(self, data, pairs):
        pr = self._proba(data, pairs)
        th = self.params["th"]
        out = {}
        for p in pairs:
            df = data[p]
            dm = dframe(df)
            h = _on_h1(pr[p], dm)
            o = self.empty(df.index)
            o["entry"] = np.where(h > th, 1, np.where(h < 1 - th, -1, 0))
            o["sl_dist"] = 3.0 * dm["h1"]["atr20"]
            o["max_bars"] = self.H * 24
            o["vol"] = dm["h1"]["vol"]
            o.loc[o["sl_dist"].isna() | o["vol"].isna(), "entry"] = 0
            out[p] = o
        return out

    def generate(self, df, pair):
        raise RuntimeError("v2_ml_d1_logit は generate_all（全ペア）で生成する")
