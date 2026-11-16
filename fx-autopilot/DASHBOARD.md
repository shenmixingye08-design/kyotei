# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-16T19:59 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | -17,105 | -88,857 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +5,679 | +8,143 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 992,931 | -1,208 | -4,856 | -40,791 | -7,069 | 4.5% | 0 | 0.00 | 36 | 50% | 0.92 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,022,896 | -4,601 | -22,957 | -8,996 | +22,896 | 2.8% | 1 | 1.37 | 41 | 54% | 1.28 |
| mtf_pullback_v1 | RESEARCH_ONLY | 994,881 | +0 | +0 | +4,579 | -5,119 | 0.9% | 0 | 0.00 | 8 | 38% | 0.79 |
| regime_switch_v1 | RESEARCH_ONLY | 972,100 | +9,010 | +2,399 | -32,322 | -27,900 | 4.5% | 3 | 2.93 | 51 | 25% | 0.59 |
| trend_donchian_v1 | RESEARCH_ONLY | 985,840 | +2,793 | +27,335 | +1,099 | -14,160 | 3.6% | 3 | 2.86 | 19 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 960,689 | +2,448 | +11,957 | +1,470 | -39,311 | 3.9% | 1 | 1.10 | 46 | 28% | 0.57 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,031,108 | +6,270 | +15,013 | +14,962 | +31,108 | 0.0% | 3 | 2.09 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -3,414 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,007,553 | -2,006 | +4,557 | -4,476 | +7,553 | 2.0% | 5 | 1.93 | 526 | 49% | 1.07 |
| v12_carry_timed | REJECTED | 1,022,123 | +124 | +19,052 | +22,123 | +22,123 | 0.1% | 6 | 2.53 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,009,340 | -393 | +12,334 | +9,340 | +9,340 | 0.1% | 3 | 1.17 | 0 | — | — |
| v13_ratemom | REJECTED | 1,027,650 | +5,251 | +23,977 | +27,650 | +27,650 | 0.0% | 6 | 2.64 | 0 | — | — |
| v14_term | REJECTED | 995,773 | +407 | -230 | -4,227 | -4,227 | 0.7% | 4 | 1.64 | 2 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,016,569 | +2,163 | +17,560 | +16,569 | +16,569 | 0.0% | 2 | 0.94 | 0 | — | — |
| v16_equity_rebal | REJECTED | 974,967 | -3,197 | -20,192 | -25,033 | -25,033 | 2.9% | 2 | 0.70 | 1 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 991,606 | -3,947 | -5,939 | -8,394 | -8,394 | 1.5% | 3 | 1.08 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,005,301 | +1,451 | +6,862 | +5,301 | +5,301 | 0.0% | 2 | 0.39 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 998,440 | +3,691 | +17,317 | +13,034 | -1,560 | 0.6% | 3 | 2.24 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 989,122 | +4,065 | +4,405 | -10,878 | -10,878 | 1.3% | 2 | 1.36 | 8 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 989,360 | +6,292 | +14,144 | +13,799 | -10,640 | 2.0% | 2 | 1.99 | 15 | 13% | 0.39 |
| v2_trend_carry | CHALLENGER | 1,007,222 | +699 | +7,527 | +7,872 | +7,222 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,008,322 | +1,567 | +7,668 | +9,328 | +8,322 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,012,178 | -2,249 | +13,849 | +14,750 | +12,178 | 0.5% | 4 | 2.45 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,004,240 | +20 | +5,819 | +4,890 | +4,240 | 0.0% | 4 | 0.55 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,028 | -503 | +3,098 | +1,811 | +1,028 | 0.1% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,007,664 | +699 | +7,527 | +8,315 | +7,664 | 0.0% | 3 | 0.44 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,004,415 | +20 | +5,823 | +5,189 | +4,415 | 0.0% | 4 | 0.55 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,004,312 | +704 | +5,832 | +4,963 | +4,312 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 1,000,256 | +707 | +2,627 | -2,095 | +256 | 0.6% | 3 | 0.44 | 29 | 34% | 0.60 |
| v5_carry_trend_daily_10p | REJECTED | 1,004,442 | +779 | +10,504 | +7,280 | +4,442 | 0.2% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,000,376 | +899 | +7,785 | +4,466 | +376 | 0.5% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 999,553 | +160 | +4,758 | +3,327 | -447 | 0.2% | 3 | 0.51 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,006,655 | +1,350 | +9,666 | +8,977 | +6,655 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,006,655 | +1,350 | +9,666 | +8,977 | +6,655 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,023,432 | -893 | +18,863 | +23,432 | +23,432 | 0.2% | 6 | 2.49 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 992,451 | -1,463 | +1,597 | -7,549 | -7,549 | 1.1% | 5 | 1.97 | 1 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,013,700 | -389 | +16,274 | +13,700 | +13,700 | 0.2% | 5 | 1.93 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,031,124 | +3,379 | +25,246 | +31,124 | +31,124 | 0.0% | 7 | 1.38 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,031,124 | +3,379 | +25,246 | +31,124 | +31,124 | 0.0% | 7 | 1.38 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 984,970 | +4,856 | +10,879 | -7,369 | -15,030 | 3.2% | 6 | 2.23 | 19 | 21% | 0.13 |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.93 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -2.4% | 0.87 | -0.43 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -9.1% | 0.86 | -0.96 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.73 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -8.0% | 0.75 | -1.12 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.20 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.61 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.17 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -7.1% | 0.68 | -0.91 | 1.09 |
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
