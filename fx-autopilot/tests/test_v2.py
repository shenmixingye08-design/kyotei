"""V2 回帰テスト: 未来情報リーク（末尾で確定した日足/4H を含む）・サイズ決定・PAPER 一致・自動昇格なし。"""
from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

TMP = Path(tempfile.mkdtemp())
os.environ.setdefault("FXAP_OUT", str(TMP / "out"))
os.environ.setdefault("FXAP_DATA_DIR", str(TMP / "data"))

from fxap import backtest, research, tournament  # noqa: E402
from fxap.data import synthetic  # noqa: E402
from fxap.paper_engine import PaperEngine  # noqa: E402
from fxap.risk import RiskConfig, RiskEngine, RiskState  # noqa: E402
from fxap.strategies import REGISTRY, v2  # noqa: E402

DATA = synthetic.make_all(n=24000, seed=4)
PAIRS = list(DATA)
V2 = ["v2_d1_donchian", "v2_d1_tsmom", "v2_h4_ema", "v2_trend_carry", "v2_xpair_strength", "v2_session_breakout",
      "v2_ml_d1_logit"]


def spec_for(name, params=None):
    params = params or REGISTRY[name].param_grid()[-1]
    return {"spec_id": f"t_{name}", "strategy": name, "pairs": {p: params for p in PAIRS}, "spec_hash": "h",
            "locked_at": str(DATA["USDJPY"].index[15000]),
            "risk": {**RiskConfig.load().__dict__, **REGISTRY[name](**params).risk_overrides()}}


class TestV2(unittest.TestCase):
    def test_no_lookahead_any_cut(self):
        for cut in (20000, 20013, 20020, 19997):
            part = {p: d.iloc[:cut] for p, d in DATA.items()}
            for name in V2:
                s = spec_for(name)
                v2._cache.clear()
                a = research.spec_signals(s, DATA)
                v2._cache.clear()
                b = research.spec_signals(s, part)
                for p in PAIRS:
                    for c in ("entry", "exit_long", "exit_short", "sl_dist", "vol"):
                        x, y = a[p][c].iloc[:cut].to_numpy(dtype=float), b[p][c].to_numpy(dtype=float)
                        self.assertTrue(np.allclose(x, y, equal_nan=True), f"{name}.{p}.{c} cut={cut}")

    def test_v3_no_lookahead(self):
        pairs7 = PAIRS + ["AUDJPY", "GBPJPY", "NZDUSD", "USDCAD", "USDCHF"]
        data7 = synthetic.make_all(pairs=pairs7, n=20000, seed=6)
        for name in ("v3_carry_trend_xs", "v3_carry_trend_mh", "v3_carry_trend_7p", "v3_carry_only",
                     "v4_carry_trend_daily", "v4_carry_trend_daily_fast", "v4_carry_trend_h4",
                     "v5_carry_trend_weekly_10p", "v5_carry_trend_daily_10p", "v9_tsmom_multi", "v11_intraday_region"):
            params = REGISTRY[name].param_grid()[-1]
            s = {"strategy": name, "pairs": {p: params for p in pairs7}}
            for cut in (17000, 17009):
                part = {p: d.iloc[:cut] for p, d in data7.items()}
                v2._cache.clear()
                a = research.spec_signals(s, data7)
                v2._cache.clear()
                b = research.spec_signals(s, part)
                for p in pairs7:
                    for c in ("entry", "exit_long", "exit_short", "sl_dist", "vol"):
                        x, y = a[p][c].iloc[:cut].to_numpy(dtype=float), b[p][c].to_numpy(dtype=float)
                        self.assertTrue(np.allclose(x, y, equal_nan=True), f"{name}.{p}.{c}")

    def test_jpy_conversion_route_unchanged(self):
        """AUDJPY/GBPJPY を追加しても GBP/AUD の円換算は XUSD×USDJPY のまま（既存 LOCK の会計を変えない）。"""
        pairs10 = PAIRS + ["AUDJPY", "GBPJPY", "NZDUSD", "USDCAD", "USDCHF"]
        data10 = synthetic.make_all(pairs=pairs10, n=500, seed=7)
        idx = data10["USDJPY"].index
        t5 = backtest.to_jpy_table({p: data10[p] for p in PAIRS}, idx)
        t10 = backtest.to_jpy_table(data10, idx)
        for c in ("USD", "EUR", "GBP", "AUD"):
            self.assertTrue(np.allclose(t5[c], t10[c], equal_nan=True), c)
        usd = (data10["USDJPY"]["bid_c"] + data10["USDJPY"]["ask_c"]) / 2
        cad = (data10["USDCAD"]["bid_c"] + data10["USDCAD"]["ask_c"]) / 2
        self.assertTrue(np.allclose(t10["CAD"], (usd / cad).reindex(idx)))

    def test_sizing_modes(self):
        eng_v = RiskEngine(RiskConfig.load({"sizing": "vol_target", "vol_target_annual": 0.05}))
        eng_f = RiskEngine(RiskConfig.load({"sizing": "fixed_notional", "fixed_notional_leverage": 1.0}))
        st = RiskState(equity=1e6, hwm=1e6)
        kw = dict(pair="EURUSD", side=1, price=1.1, stop_dist=0.01, quote_jpy=150.0, base_jpy=165.0,
                  spread_obs=0.3, spread_median=0.3)
        lo = eng_v.check_entry(st, vol=0.05, **kw).units
        hi = eng_v.check_entry(st, vol=0.10, **kw).units
        self.assertAlmostEqual(lo / hi, 2.0, delta=0.05)              # ボラ 2 倍 → 数量半分
        self.assertFalse(eng_v.check_entry(st, vol=float("nan"), **kw).approved)
        f1 = eng_f.check_entry(st, vol=0.05, **kw).units
        f2 = eng_f.check_entry(st, vol=0.20, **kw).units
        self.assertEqual(f1, f2)                                       # 固定想定元本はボラに依存しない
        self.assertAlmostEqual(f1 * 165 / 1e6, 1.0, delta=0.02)   # 1,000 通貨単位の切り捨て

    def test_paper_parity_v2(self):
        for name in ("v2_d1_donchian", "v2_xpair_strength"):
            s = spec_for(name)
            rc = RiskConfig.load(s["risk"])
            sig = research.spec_signals(s, DATA)
            bt = backtest.run(DATA, sig, PAIRS, risk_cfg=rc, start=s["locked_at"])
            root = Path(tempfile.mkdtemp())
            PaperEngine(s, DATA, root=root, risk_cfg=rc, now="2100-01-01", check_safety=False).run(
                until=DATA["USDJPY"].index[19000])
            e = PaperEngine(s, DATA, root=root, risk_cfg=rc, now="2100-01-01", check_safety=False)
            e.run()
            pt = pd.read_csv(root / s["spec_id"] / "trades.csv") if (root / s["spec_id"] / "trades.csv").stat().st_size > 1 else pd.DataFrame()
            btt = bt.trades[bt.trades.exit_reason != "end"] if len(bt.trades) else bt.trades
            self.assertEqual(len(pt), len(btt), name)
            if len(pt):
                self.assertAlmostEqual(pt["pnl_jpy"].sum(), btt["pnl_jpy"].sum(), delta=1.0)
                for col in ("strategy_version", "signal_time", "pair", "side", "entry_price", "sl_initial", "tp",
                            "units", "entry_spread_pips", "slippage_pips_entry", "swap_jpy", "exit_price", "pnl_jpy",
                            "equity_after", "drawdown_after"):
                    self.assertIn(col, pt.columns)

    def test_challenger_not_auto_champion(self):
        spec = {"spec_id": "x_v2", "plan_version": "fx_plan_v2", "v2_gate_fail": [], "wf_summary": {"sharpe": 1.0}}
        tournament.STATE = TMP / "t.json"
        st = tournament.update([spec], None, {})
        self.assertIsNone(st["champion"])
        self.assertEqual(st["specs"][0]["status"], "CHALLENGER")


if __name__ == "__main__":
    unittest.main()


class TestDataQuality(unittest.TestCase):
    def test_fred_csv_formats(self):
        from fxap.data import fred
        a = fred.parse_csv("observation_date,IR3TIB01USM156N\n2024-01-01,5.3\n2024-02-01,.\n2024-03-01,5.2\n")
        b = fred.parse_csv("DATE,DEXJPUS\n2024-01-02,141.5\n2024-01-03,143.0\n")
        self.assertEqual(len(a), 2)
        self.assertAlmostEqual(a.iloc[-1], 5.2)
        self.assertEqual(len(b), 2)

    def test_swap_source_switch_and_lag(self):
        from fxap import swap as swapm
        t = pd.Timestamp("2024-06-15", tz="UTC")
        pol = swapm.rate("USD", t)
        idx = pd.date_range("2023-01-01", "2024-12-01", freq="MS")
        swapm.MARKET.clear()
        swapm.MARKET.update({"USD": pd.Series(0.07, index=idx), "JPY": pd.Series(0.001, index=idx)})
        try:
            swapm.use_source("market")
            self.assertAlmostEqual(swapm.rate("USD", t), 0.07)        # 市場金利（1 か月前の値）
            self.assertAlmostEqual(swapm.rate("EUR", t), swapm.policy_rate("EUR", t))   # 系列なし → 表
            # 系列が終わった後は表の変化分で延長
            late = pd.Timestamp("2026-03-15", tz="UTC")
            exp = 0.07 + swapm.policy_rate("USD", pd.Timestamp("2026-02-01")) - swapm.policy_rate("USD", pd.Timestamp("2024-12-01"))
            self.assertAlmostEqual(swapm.rate("USD", late), exp)
        finally:
            swapm.MARKET.clear()
            swapm.use_source("policy")
        self.assertAlmostEqual(swapm.rate("USD", t), pol)           # 既定（policy）に戻る・キャッシュ汚染なし

    def test_crosscheck(self):
        from fxap.data import fred
        d = synthetic.make("USDJPY", n=2000, seed=1)
        mid = (d["bid_c"] + d["ask_c"]) / 2
        noon = mid[mid.index.hour == 16]
        ref = pd.Series(noon.to_numpy() * 1.001, index=noon.index.tz_convert(None).normalize())
        fred.FRED_DIR.mkdir(parents=True, exist_ok=True)
        ref.to_frame("value").to_csv(fred.FRED_DIR / "DEXJPUS.csv")
        out = fred.crosscheck({"USDJPY": d})
        self.assertAlmostEqual(out.iloc[0]["median_abs_diff_pct"], 0.1, delta=0.01)


class TestDbnomicsParse(unittest.TestCase):
    def test_parse(self):
        from fxap.data import fred

        class R:
            status_code = 200
            def json(self):
                return {"series": {"docs": [{"period": ["2020-01", "2020-02", "2020-03"], "value": [1.5, "NA", 0.3]}]}}

        class S:
            def get(self, *a, **k):
                return R()
        s = fred.fetch_dbnomics("IR3TIB01USM156N", S())
        self.assertEqual(len(s), 2)
        self.assertAlmostEqual(float(s.iloc[-1]), 0.3)


def _write_value_data(root: Path, drop_cpi=None):
    """V7 テスト用の合成 H.10（日次）と CPI（月次 / 豪 NZ は四半期）。"""
    from fxap.data import fred
    fred.FRED_DIR.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(11)
    days = pd.bdate_range("1998-01-01", "2026-09-30")
    for sid in ("DEXUSEU", "DEXJPUS", "DEXUSUK", "DEXUSAL", "DEXUSNZ", "DEXCAUS", "DEXSZUS"):
        v = np.exp(np.cumsum(rng.normal(0, 0.005, len(days))))
        pd.DataFrame({"value": v}, index=days).to_csv(fred.FRED_DIR / f"{sid}.csv")
    for ccy in fred.CPI:
        p = fred.FRED_DIR / f"CPI_{ccy}.csv"
        if ccy == drop_cpi:
            p.unlink(missing_ok=True)
            continue
        freq = "QS" if ccy in ("AUD", "NZD") else "MS"
        idx = pd.date_range("1995-01-01", "2026-06-01", freq=freq)
        v = 100 * np.exp(np.cumsum(rng.normal(0.002, 0.002, len(idx))))
        pd.DataFrame({"value": v}, index=idx).to_csv(p)


class TestV7(unittest.TestCase):
    PAIRS10 = ["USDJPY", "EURUSD", "EURJPY", "GBPUSD", "AUDUSD", "AUDJPY", "GBPJPY", "NZDUSD", "USDCAD", "USDCHF"]

    def setUp(self):
        from fxap.strategies import v7
        _write_value_data(TMP)
        v7._cache.clear()

    def test_v7_no_lookahead(self):
        from fxap.strategies import v7
        data = synthetic.make_all(pairs=self.PAIRS10, n=20000, seed=8)
        for name in ("v7_ccv_monthly", "v7_cm_monthly", "v7_carry_monthly", "v12_carry_timed", "v13_ratemom",
                     "v13_carry_ratemom"):
            params = REGISTRY[name].param_grid()[0]
            s = {"strategy": name, "pairs": {p: params for p in self.PAIRS10}}
            for cut in (17000, 18011):
                part = {p: d.iloc[:cut] for p, d in data.items()}
                v2._cache.clear()
                a = research.spec_signals(s, data)
                v2._cache.clear()
                b = research.spec_signals(s, part)
                n_entry = 0
                for p in self.PAIRS10:
                    n_entry += int((a[p]["entry"] != 0).sum())
                    for c in ("entry", "exit_long", "exit_short", "sl_dist", "vol"):
                        x, y = a[p][c].iloc[:cut].to_numpy(dtype=float), b[p][c].to_numpy(dtype=float)
                        self.assertTrue(np.allclose(x, y, equal_nan=True), f"{name}.{p}.{c} cut={cut}")
                self.assertGreater(n_entry, 0, name)
        # 月 1 回しか判断しない
        e = research.spec_signals({"strategy": "v7_ccv_monthly",
                                   "pairs": {p: {"threshold": 0.5} for p in self.PAIRS10}}, data)["EURUSD"]
        dec = e.index[(e["entry"] != 0) | e["exit_long"] | e["exit_short"]]
        self.assertLessEqual(pd.Series(dec.to_period("M")).value_counts().max(), 1)
        self.assertIsNotNone(v7)

    def test_value_uses_only_lagged_data(self):
        """バリューは H.10 の 2 か月前の月末値と、公表遅れを入れた CPI しか使わない（未来の値を変えても不変）。"""
        from fxap.data import fred
        from fxap.strategies import v7
        base = v7.value_monthly().copy()
        M = pd.Timestamp("2020-06-01")
        # 2020-05 以降の H.10 と 2020-05 以降の CPI を書き換える → 2020-06 の value は変わらないはず
        for sid in ("DEXUSEU", "DEXJPUS"):
            s = fred.load(sid)
            s[s.index >= "2020-05-01"] *= 1.5
            s.to_frame("value").to_csv(fred.FRED_DIR / f"{sid}.csv")
        s = fred.load("CPI_USD")
        s[s.index >= "2020-05-01"] *= 1.5
        s.to_frame("value").to_csv(fred.FRED_DIR / "CPI_USD.csv")
        v7._cache.clear()
        new = v7.value_monthly()
        self.assertTrue(np.allclose(base.loc[M].to_numpy(dtype=float), new.loc[M].to_numpy(dtype=float), equal_nan=True))
        self.assertFalse(np.allclose(base.loc["2020-09-01"].to_numpy(dtype=float),
                                     new.loc["2020-09-01"].to_numpy(dtype=float), equal_nan=True))

    def test_missing_cpi_blocks(self):
        from fxap.strategies import v7
        _write_value_data(TMP, drop_cpi="CHF")
        v7._cache.clear()
        with self.assertRaises(FileNotFoundError):
            v7.value_inputs()

    def test_paper_parity_v7(self):
        data = synthetic.make_all(pairs=self.PAIRS10, n=20000, seed=9)
        name = "v7_ccv_monthly"
        params = {"threshold": 0.5}
        s = {"spec_id": "t_v7", "strategy": name, "pairs": {p: params for p in self.PAIRS10}, "spec_hash": "h",
             "locked_at": str(data["USDJPY"].index[14000]),
             "risk": {**RiskConfig.load().__dict__, "max_open_positions": 6, "vol_target_annual": 0.03,
                      **REGISTRY[name](**params).risk_overrides()}}
        rc = RiskConfig.load(s["risk"])
        v2._cache.clear()
        sig = research.spec_signals(s, data)
        bt = backtest.run(data, sig, self.PAIRS10, risk_cfg=rc, start=s["locked_at"])
        root = Path(tempfile.mkdtemp())
        PaperEngine(s, data, root=root, risk_cfg=rc, now="2100-01-01", check_safety=False).run(
            until=data["USDJPY"].index[17000])
        PaperEngine(s, data, root=root, risk_cfg=rc, now="2100-01-01", check_safety=False).run()
        f = root / s["spec_id"] / "trades.csv"
        pt = pd.read_csv(f) if f.exists() and f.stat().st_size > 1 else pd.DataFrame()
        btt = bt.trades[bt.trades.exit_reason != "end"] if len(bt.trades) else bt.trades
        self.assertEqual(len(pt), len(btt))
        self.assertGreater(len(btt), 0)
        self.assertAlmostEqual(pt["pnl_jpy"].sum(), btt["pnl_jpy"].sum(), delta=1.0)


class TestV8(unittest.TestCase):
    PAIRS7 = ["EURUSD", "USDJPY", "GBPUSD", "AUDUSD", "NZDUSD", "USDCAD", "USDCHF"]

    def test_v8_no_lookahead_and_basket(self):
        data = synthetic.make_all(pairs=self.PAIRS7, n=20000, seed=12)
        for name in ("v8_dollar_carry", "v8_dollar_carry_trend"):
            params = REGISTRY[name].param_grid()[0]
            s = {"strategy": name, "pairs": {p: params for p in self.PAIRS7}}
            for cut in (17000, 18011):
                part = {p: d.iloc[:cut] for p, d in data.items()}
                v2._cache.clear()
                a = research.spec_signals(s, data)
                v2._cache.clear()
                b = research.spec_signals(s, part)
                for p in self.PAIRS7:
                    for c in ("entry", "exit_long", "exit_short", "sl_dist", "vol"):
                        x, y = a[p][c].iloc[:cut].to_numpy(dtype=float), b[p][c].to_numpy(dtype=float)
                        self.assertTrue(np.allclose(x, y, equal_nan=True), f"{name}.{p}.{c} cut={cut}")
        # carry 規則: 同じ判断日に、XXXUSD と USDXXX は逆向き（= すべて同じドルの向き）
        a = research.spec_signals({"strategy": "v8_dollar_carry",
                                   "pairs": {p: {"rule": "carry"} for p in self.PAIRS7}}, data)
        e1, e2 = a["EURUSD"]["entry"], a["USDJPY"]["entry"]
        both = (e1 != 0) & (e2 != 0)
        self.assertTrue(both.any())
        self.assertTrue((e1[both] == -e2[both]).all())

    def test_prior_trials_counts_history(self):
        from fxap import research_v2
        self.assertGreaterEqual(research_v2.prior_trials("v8"), 5 * 39)


class TestV10(unittest.TestCase):
    PAIRS10 = TestV7.PAIRS10

    def setUp(self):
        from fxap.data import fred
        from fxap.strategies import v10
        fred.FRED_DIR.mkdir(parents=True, exist_ok=True)
        rng = np.random.default_rng(21)
        days = pd.bdate_range("2008-01-01", "2026-09-30")
        v = 18 * np.exp(np.cumsum(rng.normal(0, 0.05, len(days))) * 0.2)
        pd.DataFrame({"value": v}, index=days).to_csv(fred.FRED_DIR / "VIXCLS.csv")
        v10._cache.clear()

    def test_v10_no_lookahead(self):
        data = synthetic.make_all(pairs=self.PAIRS10, n=20000, seed=13)
        for params in REGISTRY["v10_carry_vix"].param_grid():
            s = {"strategy": "v10_carry_vix", "pairs": {p: params for p in self.PAIRS10}}
            for cut in (17000, 18011):
                part = {p: d.iloc[:cut] for p, d in data.items()}
                v2._cache.clear()
                a = research.spec_signals(s, data)
                v2._cache.clear()
                b = research.spec_signals(s, part)
                n = 0
                for p in self.PAIRS10:
                    n += int((a[p]["entry"] != 0).sum())
                    for c in ("entry", "exit_long", "exit_short", "sl_dist", "vol"):
                        x, y = a[p][c].iloc[:cut].to_numpy(dtype=float), b[p][c].to_numpy(dtype=float)
                        self.assertTrue(np.allclose(x, y, equal_nan=True), f"{params}.{p}.{c} cut={cut}")
                self.assertGreater(n, 0)

    def test_vix_same_day_not_used(self):
        """判断日当日以降の VIX を書き換えても、その日のシグナルは変わらない。"""
        from fxap.data import fred
        from fxap.strategies import v10
        data = synthetic.make_all(pairs=self.PAIRS10, n=20000, seed=14)
        s = {"strategy": "v10_carry_vix", "pairs": {p: {"calm": "below_median"} for p in self.PAIRS10}}
        v2._cache.clear()
        a = research.spec_signals(s, data)["USDJPY"]
        t = data["USDJPY"].index[18000]
        cut = (t - pd.Timedelta(hours=30)).tz_convert(None).normalize()
        vv = fred.load("VIXCLS")
        vv[vv.index >= cut] = 1000.0
        vv.to_frame("value").to_csv(fred.FRED_DIR / "VIXCLS.csv")
        v10._cache.clear()
        v2._cache.clear()
        b = research.spec_signals(s, data)["USDJPY"]
        early = a.index < cut.tz_localize("UTC")
        self.assertTrue(np.array_equal(a.loc[early, "entry"].to_numpy(), b.loc[early, "entry"].to_numpy()))


class TestV11(unittest.TestCase):
    def test_windows(self):
        """USDJPY: アジア時間（0–6 UTC）は買い（JPY 安）、米州時間（16–20）は売り。同地域ペアは取引なし。"""
        pairs10 = TestV7.PAIRS10
        data = synthetic.make_all(pairs=pairs10, n=3000, seed=15)
        sig = research.spec_signals({"strategy": "v11_intraday_region",
                                     "pairs": {p: {"windows": "asia0_6_eu7_12_us16_20"} for p in pairs10}}, data)
        u = sig["USDJPY"]
        hrs = u.index.hour
        self.assertTrue((u["entry"][hrs == 23] >= 0).all() and (u["entry"][hrs == 23] == 1).any())
        self.assertTrue((u["entry"][hrs == 15] == -1).any())
        self.assertTrue(u["exit_long"][hrs == 5].all())
        self.assertEqual(int((sig["AUDJPY"]["entry"] != 0).sum()), 0)
        self.assertEqual(int((sig["USDCAD"]["entry"] != 0).sum()), 0)
        e = sig["EURUSD"]
        self.assertTrue((e["entry"][e.index.hour == 6] == -1).any())   # 欧州時間は EUR 売り
