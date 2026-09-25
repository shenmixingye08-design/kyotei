"""F. Statistical / ML（Logistic Regression / LightGBM / Random Forest）。

- ラベル: 足 i の終値から H 本後の終値までの mid 対数リターンの符号（足 i の判断時点では未知）
- Walk-Forward: 年 Y を予測するモデルは「Y の開始 - H 本（パージ）」より前のデータだけで学習（毎年再学習、拡張窓）
- 取引: 上昇確率 > th で買い、< 1-th で売り。SL/TP は ATR 基準、H 本で時間切れ
- Deep Learning は単純モデルを明確に上回る証拠がない限り採用しない（現時点で未実装）
"""
from __future__ import annotations

import warnings

import numpy as np
import pandas as pd

from .. import features as F
from .base import Strategy, register
from .regime import regime_frame

FIRST_MODEL_YEAR = 2014
MAX_TRAIN_YEARS = 6


def make_features(df: pd.DataFrame) -> pd.DataFrame:
    m = F.mid(df)
    c = m["c"]
    lr = np.log(c).diff()
    a = F.atr(m, 14)
    X = pd.DataFrame(index=df.index)
    for k in (1, 4, 12, 24, 72, 120):
        X[f"ret_{k}"] = np.log(c / c.shift(k))
    X["vol_24"] = lr.rolling(24).std()
    X["vol_ratio"] = X["vol_24"] / lr.rolling(240).std()
    X["atr_rel"] = a / c
    X["rsi14"] = F.rsi(c, 14)
    X["adx14"] = F.adx(m, 14)
    X["d_ema50"] = (c - F.ema(c, 50)) / a
    X["d_ema200"] = (c - F.ema(c, 200)) / a
    mb, up, lb = F.bollinger(c, 20, 2.0)
    X["bb_pos"] = (c - mb) / (up - mb)
    X["hour_sin"] = np.sin(2 * np.pi * df.index.hour / 24)
    X["hour_cos"] = np.cos(2 * np.pi * df.index.hour / 24)
    X["dow"] = df.index.weekday
    X["spread_rel"] = (df["ask_c"] - df["bid_c"]) / a
    rf = regime_frame(df)
    X["adx4h"] = rf["adx"]
    X["atr_pct4h"] = rf["atr_pct"]
    X["env4h"] = (rf["ema50"] - rf["ema200"]) / rf["atr"]
    return X.replace([np.inf, -np.inf], np.nan)


def _model(kind: str):
    if kind == "logit":
        from sklearn.linear_model import LogisticRegression
        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import StandardScaler
        return make_pipeline(StandardScaler(), LogisticRegression(C=0.1, max_iter=500))
    if kind == "rf":
        from sklearn.ensemble import RandomForestClassifier
        return RandomForestClassifier(n_estimators=150, max_depth=6, min_samples_leaf=200, n_jobs=-1, random_state=0)
    if kind == "lgbm":
        import lightgbm as lgb
        return lgb.LGBMClassifier(n_estimators=200, learning_rate=0.03, num_leaves=15, min_child_samples=300,
                                  subsample=0.8, subsample_freq=1, colsample_bytree=0.8, reg_lambda=1.0,
                                  random_state=0, verbose=-1)
    raise ValueError(kind)


def walk_forward_proba(df: pd.DataFrame, kind: str, horizon: int, first_year: int = FIRST_MODEL_YEAR,
                       step_years: int = 1) -> pd.Series:
    X = make_features(df)
    c = F.mid(df)["c"]
    fwd = np.log(c.shift(-horizon) / c)
    y = (fwd > 0).astype(float).where(fwd.notna())
    proba = pd.Series(np.nan, index=df.index)
    last_year = df.index.max().year
    for Y in range(first_year, last_year + 1, step_years):
        t0 = pd.Timestamp(f"{Y}-01-01", tz="UTC")
        t1 = pd.Timestamp(f"{Y + step_years}-01-01", tz="UTC")
        test = (df.index >= t0) & (df.index < t1)
        if not test.any():
            continue
        # パージ: ラベル期間（H 本先）が t0 以降に掛かる学習サンプルを除く
        pos0 = int(np.searchsorted(df.index, t0))
        train_end = max(0, pos0 - horizon)
        lo = df.index.searchsorted(t0 - pd.DateOffset(years=MAX_TRAIN_YEARS))
        tr = np.zeros(len(df), bool)
        tr[lo:train_end] = True
        ok = tr & X.notna().all(axis=1).to_numpy() & y.notna().to_numpy()
        if ok.sum() < 5000:
            continue
        mdl = _model(kind)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            mdl.fit(X[ok].to_numpy(), y[ok].to_numpy())
            te = test & X.notna().all(axis=1).to_numpy()
            if te.any():
                proba[te] = mdl.predict_proba(X[te].to_numpy())[:, 1]
    return proba


class _MLBase(Strategy):
    family = "F_ml"
    kind = "logit"
    grid = {"horizon": [12], "th": [0.55, 0.60]}
    _cache: dict = {}

    def generate(self, df, pair):
        p = self.params
        key = (self.kind, pair, p["horizon"], len(df), str(df.index[0]), str(df.index[-1]))
        if key not in _MLBase._cache:
            _MLBase._cache[key] = walk_forward_proba(df, self.kind, p["horizon"])
        pr = _MLBase._cache[key]
        m = F.mid(df)
        a = F.atr(m, 14)
        out = self.empty(df.index)
        out.loc[pr > p["th"], "entry"] = 1
        out.loc[pr < 1 - p["th"], "entry"] = -1
        out["sl_dist"] = 2.0 * a
        out["tp_dist"] = 2.0 * a
        out["max_bars"] = p["horizon"]
        out.loc[a.isna() | pr.isna(), "entry"] = 0
        return out


@register
class MLLogit(_MLBase):
    name = "ml_logit"
    kind = "logit"


@register
class MLLightGBM(_MLBase):
    name = "ml_lgbm"
    kind = "lgbm"
