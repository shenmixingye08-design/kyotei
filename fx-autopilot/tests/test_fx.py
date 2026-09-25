"""回帰テスト（合成データ・ネット不要）: 安全装置・未来情報リーク・約定規則・Risk Engine・PAPER/バックテスト一致・台帳。"""
from __future__ import annotations

import datetime as dt
import lzma
import os
import struct
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

TMP = Path(tempfile.mkdtemp())
os.environ.setdefault("FXAP_OUT", str(TMP / "out"))
os.environ.setdefault("FXAP_DATA_DIR", str(TMP / "data"))

from fxap import backtest, features, ledger, research, safety, sweep  # noqa: E402
from fxap.broker.base import BrokerError, OrderRequest  # noqa: E402
from fxap.broker.paper import PaperBroker  # noqa: E402
from fxap.common import settings  # noqa: E402
from fxap.costs import CostProfile  # noqa: E402
from fxap.data import dukascopy, synthetic  # noqa: E402
from fxap.paper_engine import PaperEngine  # noqa: E402
from fxap.risk import RiskConfig, RiskEngine, RiskState  # noqa: E402
from fxap.strategies import REGISTRY, Strategy, get  # noqa: E402

DATA = synthetic.make_all(n=8000, seed=11)


class OneShot(Strategy):
    """テスト用: 指定した足で 1 回だけ買う。"""
    name = "oneshot"
    grid = {"at": [100], "side": [1], "sl": [0.5], "tp": [np.nan]}

    def generate(self, df, pair):
        out = self.empty(df.index)
        out.iloc[self.params["at"], out.columns.get_loc("entry")] = self.params["side"]
        out["sl_dist"] = self.params["sl"]
        out["tp_dist"] = self.params["tp"]
        return out


class TestSafety(unittest.TestCase):
    def test_default_is_paper(self):
        safety.assert_paper_only()
        s = settings()
        self.assertEqual(s["mode"], "PAPER")
        self.assertIs(s["live_trading_enabled"], False)

    def test_live_config_rejected(self):
        s = dict(settings())
        for bad in ({"mode": "LIVE"}, {"live_trading_enabled": True}, {"broker": "oanda_live"}):
            with self.assertRaises(safety.LiveTradingForbidden):
                safety.assert_paper_only({**s, **bad})

    def test_live_env_rejected(self):
        os.environ["FX_LIVE_TRADING"] = "true"
        try:
            with self.assertRaises(safety.LiveTradingForbidden):
                safety.assert_paper_only()
        finally:
            del os.environ["FX_LIVE_TRADING"]

    def test_live_endpoint_blocked(self):
        with self.assertRaises(safety.LiveTradingForbidden):
            safety.assert_not_live_endpoint("https://api-fxtrade.oanda.com/v3/accounts")
        safety.assert_not_live_endpoint("https://api-fxpractice.oanda.com/v3/accounts")

    def test_no_live_order_code_path(self):
        """LIVE 用のブローカー実装・入出金 API 呼び出しがコードに存在しないこと。"""
        src = "\n".join(p.read_text() for p in Path(__file__).resolve().parents[1].joinpath("fxap").rglob("*.py"))
        for w in ("api-fxtrade.oanda.com/v3", "withdraw(", "transfer_funds(", "external-cash-transfers"):
            if w == "api-fxtrade.oanda.com/v3":
                self.assertNotIn('BASE = "https://api-fxtrade', src)
            else:
                self.assertNotIn(w, src)


class TestNoLookahead(unittest.TestCase):
    def test_signals_unchanged_by_future_data(self):
        df = DATA["EURUSD"]
        cut = 6000
        for name in ["trend_ema_adx", "trend_donchian", "trend_tsmom", "mr_rsi_bb", "mr_zscore", "regime_switch",
                     "mtf_pullback"]:
            s = get(name)
            full = s.generate(df, "EURUSD").iloc[:cut]
            part = s.generate(df.iloc[:cut], "EURUSD")
            for c in ("entry", "exit_long", "exit_short", "sl_dist"):
                a, b = full[c].to_numpy(dtype=float), part[c].to_numpy(dtype=float)
                self.assertTrue(np.allclose(a, b, equal_nan=True), f"{name}.{c} changes with future data")

    def test_higher_tf_uses_completed_bars_only(self):
        m = features.mid(DATA["USDJPY"])
        h4 = features.resample_causal(m, "4h", m.index)
        # H1 足 t に割り当てた 4H 終値は、t 以前の H1 終値のどれかと一致する（未来の終値ではない）
        for t in m.index[500:600]:
            v = h4.loc[t, "c"]
            if np.isfinite(v):
                self.assertIn(round(v, 9), set(np.round(m["c"][m.index <= t].to_numpy()[-12:], 9)))

    def test_ml_walk_forward_is_causal(self):
        df = synthetic.make("EURUSD", n=45000, seed=5, start="2010-01-04")
        cut = 42000
        a = get("ml_logit").generate(df, "EURUSD")["entry"].iloc[:cut].to_numpy()
        b = get("ml_logit").generate(df.iloc[:cut], "EURUSD")["entry"].to_numpy()
        self.assertTrue((a == b).all())


class TestExecution(unittest.TestCase):
    def _run(self, **p):
        s = OneShot(**p)
        sig = {"EURUSD": s.generate(DATA["EURUSD"], "EURUSD")}
        return backtest.run(DATA, sig, ["EURUSD"], risk_cfg=RiskConfig.load({"max_drawdown": 1.0}))

    def test_fills_next_bar_open_at_ask(self):
        r = self._run(at=100, side=1, sl=0.01)
        t = r.trades.iloc[0]
        idx = DATA["EURUSD"].index
        self.assertEqual(pd.Timestamp(t["entry_time"]), idx[101])
        d = DATA["EURUSD"].iloc[101]
        mid = (d["bid_o"] + d["ask_o"]) / 2
        self.assertGreater(t["entry_price"], mid)          # 買いは mid より高く約定（スプレッド + スリッページ）

    def test_costs_are_charged(self):
        r = self._run(at=100, side=-1, sl=0.01)
        t = r.trades.iloc[0]
        self.assertGreater(t["cost_spread_jpy"], 0)
        self.assertGreater(t["cost_slip_jpy"], 0)
        self.assertLess(t["pnl_jpy"], t["gross_mid_pnl_jpy"] + t["swap_jpy"] + 1e-6)

    def test_stop_before_target_same_bar(self):
        df = DATA["EURUSD"].copy()
        i = 101
        o = df["ask_o"].iloc[i]
        for c in ("bid_h", "ask_h"):
            df.iloc[i + 1, df.columns.get_loc(c)] = o + 0.01
        for c in ("bid_l", "ask_l"):
            df.iloc[i + 1, df.columns.get_loc(c)] = o - 0.01
        data = {**DATA, "EURUSD": df}
        s = OneShot(at=100, side=1, sl=0.002, tp=0.002)
        r = backtest.run(data, {"EURUSD": s.generate(df, "EURUSD")}, ["EURUSD"])
        self.assertEqual(r.trades.iloc[0]["exit_reason"], "sl")

    def test_position_size_scales_with_equity(self):
        s = OneShot(at=100, side=1, sl=0.005)
        sig = {"EURUSD": s.generate(DATA["EURUSD"], "EURUSD")}
        a = backtest.run(DATA, sig, ["EURUSD"], initial_equity=1_000_000).trades.iloc[0]["units"]
        b = backtest.run(DATA, sig, ["EURUSD"], initial_equity=2_000_000).trades.iloc[0]["units"]
        self.assertAlmostEqual(b / a, 2.0, delta=0.05)     # 固定ロットではない

    def test_leverage_cap(self):
        r = self._run(at=100, side=1, sl=0.00001)          # 極小 SL → 数量はレバレッジ上限で頭打ち
        t = r.trades.iloc[0]
        self.assertLessEqual(t["notional_jpy"] / t["equity_at_entry"], settings()["risk"]["max_leverage"] + 1e-6)

    def test_no_pyramiding(self):
        s = get("mr_zscore")
        sig = {"EURUSD": s.generate(DATA["EURUSD"], "EURUSD")}
        r = backtest.run(DATA, sig, ["EURUSD"])
        tr = r.trades.sort_values("entry_time")
        ent, ext = pd.to_datetime(tr["entry_time"]).to_numpy(), pd.to_datetime(tr["exit_time"]).to_numpy()
        self.assertTrue((ent[1:] >= ext[:-1]).all(), "同じペアで建玉が重なっている")

    def test_every_trade_has_stop(self):
        for name in ("trend_ema_adx", "mr_rsi_bb", "regime_switch", "mtf_pullback"):
            sig = get(name).generate(DATA["USDJPY"], "USDJPY")
            e = sig[sig.entry != 0]
            self.assertTrue((e["sl_dist"] > 0).all(), name)


class TestRisk(unittest.TestCase):
    def setUp(self):
        self.eng = RiskEngine(RiskConfig.load())

    def _chk(self, st, **kw):
        a = dict(pair="EURUSD", side=1, price=1.1, stop_dist=0.002, quote_jpy=150.0, base_jpy=165.0,
                 spread_obs=0.3, spread_median=0.3)
        a.update(kw)
        return self.eng.check_entry(st, **a)

    def test_basic_sizing(self):
        st = RiskState(equity=1e6, hwm=1e6)
        d = self._chk(st)
        self.assertTrue(d.approved)
        self.assertLessEqual(d.units * 0.002 * 150, 1e6 * 0.005 + 1e-6)

    def test_abnormal_spread_blocks(self):
        d = self._chk(RiskState(equity=1e6, hwm=1e6), spread_obs=5.0, spread_median=0.3)
        self.assertIn("spread_normal", d.reasons)

    def test_stale_or_missing_data_blocks(self):
        self.assertIn("data_fresh", self._chk(RiskState(equity=1e6, hwm=1e6), bar_age_hours=10).reasons)
        self.assertIn("data_ok", self._chk(RiskState(equity=1e6, hwm=1e6), price=float("nan")).reasons)

    def test_daily_loss_limit(self):
        st = RiskState(equity=1e6, hwm=1e6)
        t = pd.Timestamp("2024-03-04 01:00", tz="UTC")
        self.eng.on_bar(st, t, 1e6)
        self.eng.on_bar(st, t + pd.Timedelta(hours=2), 0.975e6)
        self.assertIn("daily_loss_limit", self._chk(st).reasons)
        self.eng.on_bar(st, t + pd.Timedelta(days=1), 0.975e6)
        self.assertNotIn("daily_loss_limit", self._chk(st).reasons)

    def test_max_drawdown_kill(self):
        st = RiskState(equity=1e6, hwm=1e6)
        acts = self.eng.on_bar(st, pd.Timestamp("2024-03-04", tz="UTC"), 0.84e6)
        self.assertIn("flatten_kill", acts)
        self.assertIn("kill_switch_off", self._chk(st).reasons)

    def test_disconnected_blocks(self):
        st = RiskState(equity=1e6, hwm=1e6, broker_connected=False)
        self.assertIn("broker_connected", self._chk(st).reasons)

    def test_correlated_exposure(self):
        from fxap.risk import OpenPos
        st = RiskState(equity=1e6, hwm=1e6, positions=[OpenPos("EURJPY", 1, 17000, 2.8e6)])
        d = self._chk(st, stop_dist=0.0001)
        self.assertTrue(not d.approved or d.units * 165 <= 3.0e6 - 2.8e6 + 1000 * 165)


class TestPaper(unittest.TestCase):
    def _spec(self, name="mr_zscore", params=None):
        params = params or {"n": 24, "z": 2.0}
        return {"spec_id": f"t_{name}", "strategy": name, "pairs": {p: params for p in ["EURUSD", "USDJPY"]},
                "spec_hash": "h", "locked_at": str(DATA["EURUSD"].index[3000])}

    def test_parity_with_backtest_and_restart(self):
        spec = self._spec()
        sig = research.spec_signals(spec, DATA)
        bt = backtest.run(DATA, sig, list(spec["pairs"]), start=spec["locked_at"])
        root = Path(tempfile.mkdtemp())
        PaperEngine(spec, DATA, root=root, now="2100-01-01", check_safety=False).run(until=DATA["EURUSD"].index[5000])
        e2 = PaperEngine(spec, DATA, root=root, now="2100-01-01", check_safety=False)
        e2.run()
        pt = pd.read_csv(root / spec["spec_id"] / "trades.csv")
        btt = bt.trades[bt.trades.exit_reason != "end"]
        self.assertEqual(len(pt), len(btt))
        self.assertAlmostEqual(pt["pnl_jpy"].sum(), btt["pnl_jpy"].sum(), delta=1.0)
        self.assertTrue(e2.ledger.verify()[0])
        # 再実行しても新しい足が無ければ注文は増えない（冪等）
        n = len(e2.ledger.records("order"))
        r = PaperEngine(spec, DATA, root=root, now="2100-01-01", check_safety=False).run()
        self.assertEqual(r["bars_new"], 0)
        self.assertEqual(len(e2.ledger.records("order")), n)

    def test_spec_change_rejected(self):
        spec = self._spec()
        root = Path(tempfile.mkdtemp())
        PaperEngine(spec, DATA, root=root, now="2100-01-01", check_safety=False).run(until=DATA["EURUSD"].index[3500])
        with self.assertRaises(RuntimeError):
            PaperEngine({**spec, "spec_hash": "changed"}, DATA, root=root, check_safety=False)

    def test_order_failures_trigger_kill(self):
        spec = self._spec()
        root = Path(tempfile.mkdtemp())
        br = PaperBroker(CostProfile.load())
        br.fail_next = 100
        e = PaperEngine(spec, DATA, root=root, broker=br, now="2100-01-01", check_safety=False)
        r = e.run()
        self.assertGreaterEqual(r["errors"], 3)
        self.assertTrue(r["halted"])
        self.assertTrue(e.ledger.records("kill_switch"))

    def test_disconnect_stops(self):
        spec = self._spec()
        root = Path(tempfile.mkdtemp())
        br = PaperBroker(CostProfile.load())
        br.connected = False
        r = PaperEngine(spec, DATA, root=root, broker=br, now="2100-01-01", check_safety=False).run()
        self.assertEqual(r.get("stopped"), "broker_disconnected")
        self.assertEqual(r["orders"], 0)

    def test_duplicate_client_id(self):
        br = PaperBroker(CostProfile.load())
        req = OrderRequest("abc", "EURUSD", 1, 1000, sl=0.01)
        self.assertEqual(br.place_order(req)["status"], "accepted")
        self.assertEqual(br.place_order(req)["status"], "duplicate")
        self.assertEqual(br.place_order(OrderRequest("x", "EURUSD", 1, 1000, sl=None))["status"], "rejected")
        br.fail_next = 1
        with self.assertRaises(BrokerError):
            br.place_order(OrderRequest("y", "EURUSD", 1, 1000, sl=0.01))


class TestLedgerSweepData(unittest.TestCase):
    def test_tamper_detected(self):
        p = Path(tempfile.mkdtemp()) / "l.jsonl"
        L = ledger.Ledger(p)
        for i in range(5):
            L.append("fill", pnl=-100 * i)
        self.assertTrue(L.verify()[0])
        lines = p.read_text().splitlines()
        p.write_text("\n".join(lines[:2] + lines[3:]) + "\n")      # 負けトレードを 1 行削除
        self.assertFalse(ledger.Ledger(p).verify()[0])

    def test_sweep(self):
        r = sweep.compute(equity=1_600_000, realized_ytd=500_000, unrealized=0, hwm=1_600_000)
        self.assertAlmostEqual(r["tax_reserve"], round(500_000 * 0.20315), delta=1)
        self.assertEqual(r["ibkr_transfer_candidate"], 1_600_000 - r["keep_in_fx_account"])
        r = sweep.compute(equity=900_000, realized_ytd=-100_000, unrealized=0, hwm=1_000_000)
        self.assertEqual(r["ibkr_transfer_candidate"], 0)
        self.assertIn("NOT EXECUTED", r["execution"])

    def test_dukascopy_decoder(self):
        rec = [(0, 110000, 110050, 109950, 110100, 12.5), (3600, 110050, 110020, 110000, 110080, 3.0)]
        raw = lzma.compress(b"".join(struct.pack(">5if", *r) for r in rec), format=lzma.FORMAT_ALONE)
        df = dukascopy.decode_candles(raw, dt.datetime(2024, 1, 1), 1e-3)
        self.assertAlmostEqual(df["o"].iloc[0], 110.0)
        self.assertAlmostEqual(df["h"].iloc[0], 110.1)
        self.assertEqual(df.index[1], pd.Timestamp("2024-01-01 01:00"))
        bad = lzma.compress(struct.pack(">5if", 0, 110000, 110050, 110200, 110100, 1.0), format=lzma.FORMAT_ALONE)
        with self.assertRaises(dukascopy.FetchError):
            dukascopy.decode_candles(bad, dt.datetime(2024, 1, 1), 1e-3)
        ticks = lzma.compress(struct.pack(">3i2f", 1500, 110010, 110000, 1.0, 2.0), format=lzma.FORMAT_ALONE)
        t = dukascopy.decode_ticks(ticks, dt.datetime(2024, 1, 1, 5), 1e-3)
        self.assertAlmostEqual(t["ask"].iloc[0] - t["bid"].iloc[0], 0.01)

    def test_registry_has_all_families(self):
        fams = {REGISTRY[n].family for n in research.CANDIDATE_STRATEGIES}
        self.assertTrue({"A_trend", "B_meanrev", "C_regime", "D_mtf", "F_ml"} <= fams)


if __name__ == "__main__":
    unittest.main()
