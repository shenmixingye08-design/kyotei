# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-12T20:09 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | -13,673 | -92,153 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +8,143 | +8,271 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 997,555 | +0 | -5,063 | -28,180 | -2,445 | 4.1% | 0 | 0.00 | 35 | 51% | 0.97 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,028,767 | -5,861 | -6,228 | +13,131 | +28,767 | 2.2% | 2 | 2.90 | 38 | 55% | 1.37 |
| mtf_pullback_v1 | RESEARCH_ONLY | 994,881 | +0 | -5,120 | -528 | -5,119 | 0.9% | 0 | 0.00 | 8 | 38% | 0.79 |
| regime_switch_v1 | RESEARCH_ONLY | 958,896 | +4,402 | -10,805 | -14,510 | -41,104 | 5.8% | 3 | 4.15 | 50 | 26% | 0.59 |
| trend_donchian_v1 | RESEARCH_ONLY | 979,719 | +2,282 | +18,684 | -20,490 | -20,281 | 4.2% | 3 | 2.88 | 19 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 962,392 | +1,253 | +12,185 | -2,090 | -37,608 | 3.8% | 2 | 3.12 | 45 | 29% | 0.57 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,022,964 | +2,915 | +5,788 | +6,116 | +22,964 | 0.4% | 1 | 0.43 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -13,976 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,006,941 | -4,252 | +2,448 | -4,764 | +6,941 | 2.0% | 5 | 1.94 | 496 | 48% | 1.07 |
| v12_carry_timed | REJECTED | 1,022,035 | -24 | +24,841 | +22,035 | +22,035 | 0.1% | 6 | 2.53 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,008,932 | +590 | +14,173 | +8,932 | +8,932 | 0.0% | 3 | 1.17 | 0 | — | — |
| v13_ratemom | REJECTED | 1,019,701 | +5,119 | +25,874 | +19,701 | +19,701 | 0.1% | 6 | 2.66 | 0 | — | — |
| v14_term | REJECTED | 997,092 | -3,098 | +2,000 | -2,908 | -2,908 | 0.6% | 5 | 1.96 | 1 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,012,608 | +3,298 | +15,864 | +12,608 | +12,608 | 0.0% | 2 | 0.94 | 0 | — | — |
| v16_equity_rebal | REJECTED | 982,620 | -4,618 | -14,519 | -17,380 | -17,380 | 2.2% | 3 | 1.02 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 998,459 | -3,765 | +354 | -1,541 | -1,541 | 0.9% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,002,464 | +2,059 | +2,464 | +2,464 | +2,464 | 0.0% | 2 | 0.39 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 990,705 | +973 | +8,949 | -6,746 | -9,295 | 1.4% | 3 | 2.25 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 983,376 | -436 | -8,159 | -16,624 | -16,624 | 1.9% | 1 | 0.65 | 8 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 978,376 | +4,196 | +577 | -1,045 | -21,624 | 3.0% | 1 | 1.12 | 15 | 13% | 0.39 |
| v2_trend_carry | CHALLENGER | 1,005,739 | +1,343 | +7,254 | +5,739 | +5,739 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,005,257 | +1,969 | +5,472 | +5,257 | +5,257 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,015,492 | -304 | +20,007 | +15,492 | +15,492 | 0.0% | 4 | 2.44 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,003,998 | +600 | +6,492 | +3,998 | +3,998 | 0.0% | 4 | 0.55 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,778 | -129 | +4,244 | +1,910 | +1,778 | 0.0% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,006,181 | +1,343 | +7,254 | +6,181 | +6,181 | 0.0% | 3 | 0.44 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,004,174 | +599 | +6,499 | +4,884 | +4,174 | 0.0% | 4 | 0.55 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,002,795 | +614 | +4,241 | +2,795 | +2,795 | 0.0% | 2 | 0.33 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 999,328 | +474 | +4 | -4,458 | -672 | 0.7% | 3 | 0.44 | 28 | 36% | 0.65 |
| v5_carry_trend_daily_10p | REJECTED | 1,002,483 | +1,423 | +10,011 | +797 | +2,483 | 0.4% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 998,781 | +1,079 | +7,894 | -1,656 | -1,219 | 0.7% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 999,051 | +497 | +4,645 | +712 | -949 | 0.3% | 4 | 0.62 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,003,935 | +1,965 | +8,211 | +4,054 | +3,935 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,003,935 | +1,965 | +8,211 | +4,054 | +3,935 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,024,357 | -416 | +28,707 | +24,357 | +24,357 | 0.1% | 6 | 2.49 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 994,282 | -2,310 | +1,858 | -5,718 | -5,718 | 0.9% | 5 | 1.97 | 1 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,013,091 | +429 | +16,590 | +13,091 | +13,091 | 0.0% | 5 | 1.93 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,024,952 | +4,162 | +25,055 | +24,952 | +24,952 | 0.0% | 7 | 1.38 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,024,952 | +4,162 | +25,055 | +24,952 | +24,952 | 0.0% | 7 | 1.38 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 977,107 | +4,887 | -2,501 | -27,257 | -22,893 | 3.9% | 6 | 2.25 | 18 | 17% | 0.11 |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.94 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -3.2% | 0.83 | -0.58 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -8.0% | 0.87 | -0.85 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.73 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -7.6% | 0.76 | -1.06 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.21 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.62 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.17 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -7.6% | 0.66 | -1.00 | 1.09 |
| v10_carry_vix | REJECTED | — | — | — | — | — | — | — | — | — |
| v11_intraday_region | REJECTED | — | — | — | — | — | — | — | — | — |
| v12_carry_timed | REJECTED | — | — | — | — | — | — | — | — | — |
| v13_carry_ratemom | REJECTED | — | — | — | — | — | — | — | — | — |
| v13_ratemom | REJECTED | — | — | — | — | — | — | — | — | — |
| v14_term | REJECTED | — | — | — | — | — | — | — | — | — |
| v14_term_ratemom | REJECTED | — | — | — | — | — | — | — | — | — |
| v16_equity_rebal | REJECTED | — | — | — | — | — | — | — | — | — |
| v16_equity_rebal_carry | REJECTED | — | — | — | — | — | — | — | — | — |
| v2_d1_donchian | REJECTED | — | — | — | — | — | — | — | — | — |
| v2_d1_tsmom | REJECTED | — | — | — | — | — | — | — | — | — |
| v2_h4_ema | REJECTED | — | — | — | — | — | — | — | — | — |
| v2_ml_d1_logit | REJECTED | — | — | — | — | — | — | — | — | — |
| v2_session_breakout | REJECTED | — | — | — | — | — | — | — | — | — |
| v2_trend_carry | CHALLENGER | — | — | — | — | — | — | — | — | — |
| v2_xpair_strength | REJECTED | — | — | — | — | — | — | — | — | — |
| v3_carry_only | REJECTED | — | — | — | — | — | — | — | — | — |
| v3_carry_trend_7p | REJECTED | — | — | — | — | — | — | — | — | — |
| v3_carry_trend_mh | REJECTED | — | — | — | — | — | — | — | — | — |
| v3_carry_trend_xs | REJECTED | — | — | — | — | — | — | — | — | — |
| v4_carry_trend_daily | REJECTED | — | — | — | — | — | — | — | — | — |
| v4_carry_trend_daily_fast | REJECTED | — | — | — | — | — | — | — | — | — |
| v4_carry_trend_h4 | REJECTED | — | — | — | — | — | — | — | — | — |
| v5_carry_trend_daily_10p | REJECTED | — | — | — | — | — | — | — | — | — |
| v5_carry_trend_weekly_10p | REJECTED | — | — | — | — | — | — | — | — | — |
| v6_carry_trend_daily_mkt_7p | REJECTED | — | — | — | — | — | — | — | — | — |
| v6_carry_trend_mkt_7p | REJECTED | — | — | — | — | — | — | — | — | — |
| v6_trend_carry_mkt_5p | REJECTED | — | — | — | — | — | — | — | — | — |
| v7_carry_monthly | REJECTED | — | — | — | — | — | — | — | — | — |
| v7_ccv_monthly | REJECTED | — | — | — | — | — | — | — | — | — |
| v7_cm_monthly | REJECTED | — | — | — | — | — | — | — | — | — |
| v8_dollar_carry | REJECTED | — | — | — | — | — | — | — | — | — |
| v8_dollar_carry_trend | REJECTED | — | — | — | — | — | — | — | — | — |
| v9_tsmom_multi | REJECTED | — | — | — | — | — | — | — | — | — |

詳細: `research/results/LATEST/SUMMARY.md` ／ 台帳: `paper_forward/<spec>/ledger.jsonl`（ハッシュチェーン）
