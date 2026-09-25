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
        pairs7 = PAIRS + ["AUDJPY", "GBPJPY"]
        data7 = synthetic.make_all(pairs=pairs7, n=20000, seed=6)
        for name in ("v3_carry_trend_xs", "v3_carry_trend_mh", "v3_carry_trend_7p", "v3_carry_only",
                     "v4_carry_trend_daily", "v4_carry_trend_daily_fast", "v4_carry_trend_h4"):
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
        pairs7 = PAIRS + ["AUDJPY", "GBPJPY"]
        data7 = synthetic.make_all(pairs=pairs7, n=500, seed=7)
        idx = data7["USDJPY"].index
        t5 = backtest.to_jpy_table({p: data7[p] for p in PAIRS}, idx)
        t7 = backtest.to_jpy_table(data7, idx)
        for c in ("USD", "EUR", "GBP", "AUD"):
            self.assertTrue(np.allclose(t5[c], t7[c], equal_nan=True), c)

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
