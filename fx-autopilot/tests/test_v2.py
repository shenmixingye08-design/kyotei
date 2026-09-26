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
                     "v5_carry_trend_weekly_10p", "v5_carry_trend_daily_10p"):
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
