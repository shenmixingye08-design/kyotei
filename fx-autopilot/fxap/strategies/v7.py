"""V7 候補（config/research_plan_v7.yaml に事前登録）: 通貨ファクターの横断ポートフォリオ（キャリー × モメンタム × バリュー）。

本人の依頼（2026-09-26「強くなる方法を調べて」→「V7 やって」）。文献の要点:
  - キャリー・モメンタム・バリューは互いの相関が低く、組み合わせると分散効果が大きい（Menkhoff et al., Asness et al.）
  - ボラティリティが高い時に建玉を減らすと Sharpe が上がる（Moreira & Muir）→ sizing = vol_target（逆ボラ）
  - 少数ペアの大相場に賭けるより、多通貨を毎月ランキングして分散保有する

定義（すべて通貨 8 つ: USD EUR JPY GBP AUD NZD CAD CHF の横断比較。値は判断時点で入手済みのものだけ）:
  - carry_c   = 3 か月物市場金利（FRED/OECD、公表遅れ 1 か月 + シグナル用にさらに 31 日ラグ。swap.carry と同じ扱い）
  - mom_c     = 対 USD 通貨指数（Dukascopy 日足）のボラ正規化リターン z63 と z252 の平均
  - value_c   = -(5 年間の実質為替変化)。実質為替 = 対 USD 名目（H.10 月末値、2 か月前）× CPI_c / CPI_US
                （CPI は公表遅れ: 月次 2 か月・四半期 5 か月。最終観測から 12 か月を超えたら欠損扱い）
  - 各ファクターを判断日ごとに 8 通貨で標準化（z）→ 使うファクターの平均 = 通貨スコア S_c（欠損ファクターは除いて平均）
  - ペアのスコア = S_base - S_quote。|スコア| > threshold なら符号方向に保有、それ以外は手仕舞い
  - 判断は月 1 回（その月の最初の日足確定時 = NY クローズ）。SL = 日足 ATR20 × 4（暴落時のブレーキ）
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .. import swap as swapm
from ..common import PAIRS
from .base import register
from .v2 import _V2, _on_h1, dframe
from .v3 import _finish

CCY8 = ["USD", "EUR", "JPY", "GBP", "AUD", "NZD", "CAD", "CHF"]
# 対 USD の通貨指数（1 通貨あたりの USD、log）をどのペアから作るか: (pair, 符号)
USD_LEG = {"EUR": ("EURUSD", 1), "JPY": ("USDJPY", -1), "GBP": ("GBPUSD", 1), "AUD": ("AUDUSD", 1),
           "NZD": ("NZDUSD", 1), "CAD": ("USDCAD", -1), "CHF": ("USDCHF", -1)}
H10_LEG = {"EUR": ("DEXUSEU", 1), "JPY": ("DEXJPUS", -1), "GBP": ("DEXUSUK", 1), "AUD": ("DEXUSAL", 1),
           "NZD": ("DEXUSNZ", 1), "CAD": ("DEXCAUS", -1), "CHF": ("DEXSZUS", -1)}
VALUE_YEARS = 5
H10_LAG_MONTHS = 2            # 月末値の公表（週次）を確実に待つ
CPI_STALE_MONTHS = 12
MIN_CCY = 5                   # 横断標準化に必要な通貨数

_cache: dict = {}


def value_inputs():
    """(H.10 月末 log 指数 DataFrame, CPI dict)。無ければ FileNotFoundError。"""
    if "value_inputs" in _cache:
        return _cache["value_inputs"]
    from ..data import fred
    cols = {}
    for c, (sid, sgn) in H10_LEG.items():
        s = fred.load(sid)
        s = s[s > 0]
        cols[c] = sgn * np.log(s.resample("ME").last())
    lx = pd.DataFrame(cols)
    lx.index = lx.index.to_period("M").to_timestamp()
    lx["USD"] = 0.0
    cpi = fred.load_cpi()
    miss = [c for c in CCY8 if c not in cpi]
    if miss:
        raise FileNotFoundError(f"CPI がない通貨: {miss}")
    _cache["value_inputs"] = (lx, cpi)
    return _cache["value_inputs"]


def value_monthly() -> pd.DataFrame:
    """月（月初 index）-> 通貨ごとの value（その月の判断で使える値。ラグ適用済み）。"""
    if "value" in _cache:
        return _cache["value"]
    lx, cpi = value_inputs()
    months = pd.date_range("1995-01-01", pd.Timestamp.now().normalize(), freq="MS")
    out = pd.DataFrame(index=months, columns=CCY8, dtype=float)

    def cpi_at(c, M):
        info = cpi[c]
        ref = M - pd.DateOffset(months=info["lag_months"])
        if ref > info["last_obs"] + pd.DateOffset(months=CPI_STALE_MONTHS):
            return np.nan
        s = info["cpi"]
        s = s[s.index <= ref]
        return float(np.log(s.iloc[-1])) if len(s) else np.nan

    for M in months:
        ref = M - pd.DateOffset(months=H10_LAG_MONTHS)
        ref0 = ref - pd.DateOffset(years=VALUE_YEARS)
        if ref not in lx.index or ref0 not in lx.index:
            continue
        us1, us0 = cpi_at("USD", M), cpi_at("USD", M - pd.DateOffset(years=VALUE_YEARS))
        for c in CCY8:
            q1 = lx.at[ref, c] + cpi_at(c, M) - us1
            q0 = lx.at[ref0, c] + cpi_at(c, M - pd.DateOffset(years=VALUE_YEARS)) - us0
            out.at[M, c] = -(q1 - q0)
    _cache["value"] = out
    return out


def _xs_z(F: pd.DataFrame) -> pd.DataFrame:
    n = F.notna().sum(axis=1)
    z = F.sub(F.mean(axis=1), axis=0).div(F.std(axis=1), axis=0)
    return z.where(n >= MIN_CCY)


def currency_scores(data: dict, factors: tuple) -> pd.DataFrame:
    """日足ラベル（日付）index × 8 通貨の通貨スコア S_c。"""
    # 対 USD 通貨指数（日足）
    idx = {}
    for c, (p, sgn) in USD_LEG.items():
        d = dframe(data[p])["d"]
        idx[c] = pd.Series(sgn * np.log(d["c"].to_numpy()), index=pd.DatetimeIndex(d["label"]).normalize())
    L = pd.DataFrame(idx)
    L = L[~L.index.duplicated(keep="last")].sort_index()
    naive = L.index.tz_convert(None) if L.index.tz is not None else L.index
    L["USD"] = 0.0
    L = L[CCY8]
    comps = []
    if "mom" in factors:
        # 通貨指数自体のボラで正規化（USD は他通貨の平均の逆 = 横断で自然に決まるので 0 のまま）
        r = L.diff()
        sd = r.rolling(60, min_periods=40).std().replace(0, np.nan)
        z63 = (L - L.shift(63)) / (sd * np.sqrt(63))
        z252 = (L - L.shift(252)) / (sd * np.sqrt(252))
        mom = (z63 + z252) / 2
        mom["USD"] = 0.0
        mom = mom.where(z252[[c for c in CCY8 if c != "USD"]].notna().all(axis=1), axis=0)
        comps.append(_xs_z(mom))
    if "carry" in factors:
        months = pd.Series(naive.to_period("M"), index=L.index)
        vals = {}
        for mo in months.unique():
            t = pd.Timestamp(mo.start_time) + pd.Timedelta(days=14) - pd.Timedelta(days=31)
            vals[mo] = [swapm.rate(c, t) for c in CCY8]
        C = pd.DataFrame([vals[m] for m in months], index=L.index, columns=CCY8)
        comps.append(_xs_z(C))
    if "value" in factors:
        V = value_monthly()
        mstart = naive.to_period("M").to_timestamp()
        Vd = pd.DataFrame(V.reindex(mstart).to_numpy(), index=L.index, columns=CCY8)
        comps.append(_xs_z(Vd))
    stack = np.stack([c.to_numpy(dtype=float) for c in comps])
    with np.errstate(all="ignore"):
        S = np.nanmean(stack, axis=0)
    return pd.DataFrame(S, index=L.index, columns=CCY8)


class _V7XS(_V2):
    version = "v7"
    family = "fx_factors"
    needs_all_pairs = True
    factors: tuple = ()
    grid = {"threshold": [0.5, 1.0]}

    def risk_overrides(self) -> dict:
        return {"sizing": "vol_target"}

    @staticmethod
    def monthly_mask(dm) -> pd.Series:
        lab = pd.DatetimeIndex(dm["d"]["label"])
        lab = lab.tz_convert(None) if lab.tz is not None else lab
        first = pd.Series(lab.to_period("M"), index=dm["d"].index)
        is_first = (first != first.shift(1)).astype(float)
        return _on_h1(is_first, dm) == 1.0

    def generate_all(self, data, pairs):
        S = currency_scores(data, self.factors)
        th = self.params["threshold"]
        out = {}
        for p in pairs:
            df = data[p]
            dm = dframe(df)
            b, q = PAIRS[p]["base"], PAIRS[p]["quote"]
            sc = S[b] - S[q]
            dirn = np.sign(sc).where(sc.abs() > th, 0.0).where(sc.notna())
            lab = pd.DatetimeIndex(dm["d"]["label"]).normalize()
            h = _on_h1(pd.Series(dirn.reindex(lab).to_numpy(), index=dm["d"].index), dm)
            dec = self.monthly_mask(dm) & h.notna()
            o = self.empty(df.index)
            o["entry"] = np.where(dec, h.fillna(0), 0).astype(int)
            o["exit_long"] = dec & (h <= 0)
            o["exit_short"] = dec & (h >= 0)
            out[p] = _finish(o, dm)
        return out

    def generate(self, df, pair):
        raise RuntimeError(f"{self.name} は generate_all（全ペア）で生成する")


@register
class V7CarryMomValue(_V7XS):
    """本命: キャリー + モメンタム + バリュー。"""
    name = "v7_ccv_monthly"
    factors = ("carry", "mom", "value")


@register
class V7CarryMom(_V7XS):
    """比較: キャリー + モメンタム（バリューなし）。バリューの上乗せ効果を見る。"""
    name = "v7_cm_monthly"
    factors = ("carry", "mom")


@register
class V7CarryOnly(_V7XS):
    """ベンチマーク: キャリーのみ（同じ横断・月次・逆ボラの枠組み）。"""
    name = "v7_carry_monthly"
    factors = ("carry",)
