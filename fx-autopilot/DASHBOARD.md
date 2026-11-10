# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-10T15:11 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 870,270 | -9,967 | -11,644 | -94,670 | -129,730 | 14.4% | 0 | 0.00 | 175 | 41% | 0.62 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +6,625 | +8,143 | +8,271 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 997,787 | +0 | -22,412 | -24,957 | -2,213 | 4.0% | 0 | 0.00 | 33 | 52% | 0.97 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,045,853 | +0 | +22,174 | +37,334 | +45,853 | 0.0% | 0 | 0.00 | 35 | 60% | 1.67 |
| mtf_pullback_v1 | RESEARCH_ONLY | 994,881 | -3,122 | +2,001 | -4,792 | -5,119 | 0.9% | 0 | 0.00 | 8 | 38% | 0.79 |
| regime_switch_v1 | RESEARCH_ONLY | 969,701 | +0 | -13,069 | -7,485 | -30,299 | 4.8% | 0 | 0.00 | 44 | 30% | 0.72 |
| trend_donchian_v1 | RESEARCH_ONLY | 964,702 | +5,288 | +3,377 | -43,591 | -35,298 | 5.7% | 2 | 1.64 | 18 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 946,157 | -3,110 | -1,441 | -17,275 | -53,843 | 5.4% | 1 | 2.06 | 43 | 28% | 0.52 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,018,711 | +1,991 | +1,535 | +3,631 | +18,711 | 0.8% | 1 | 0.43 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -13,457 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,008,624 | +7,623 | -7,309 | -1,356 | +8,624 | 1.9% | 0 | 0.00 | 466 | 48% | 1.07 |
| v12_carry_timed | REJECTED | 1,006,499 | +3,549 | +4,692 | +6,499 | +6,499 | 0.3% | 6 | 2.57 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 997,825 | +440 | -2,930 | -2,175 | -2,175 | 0.4% | 3 | 1.18 | 0 | — | — |
| v13_ratemom | REJECTED | 1,006,321 | +2,865 | +10,120 | +6,321 | +6,321 | 0.1% | 6 | 2.70 | 0 | — | — |
| v14_term | REJECTED | 994,686 | -157 | -4,300 | -5,314 | -5,314 | 0.8% | 6 | 2.40 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,001,449 | +1,584 | +2,350 | +1,449 | +1,449 | 0.3% | 2 | 0.95 | 0 | — | — |
| v16_equity_rebal | REJECTED | 992,585 | -974 | -6,940 | -7,415 | -7,415 | 1.2% | 3 | 1.01 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 997,782 | +878 | -4,770 | -2,218 | -2,218 | 0.9% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 999,744 | +993 | -256 | -256 | -256 | 0.0% | 1 | 0.22 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 978,893 | -2,304 | -11,754 | -19,061 | -21,107 | 2.6% | 4 | 3.07 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 983,694 | -1,672 | -11,815 | -16,306 | -16,306 | 1.8% | 1 | 0.72 | 7 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 974,181 | -1,958 | +2,938 | -14,791 | -25,819 | 3.5% | 0 | 0.00 | 15 | 13% | 0.39 |
| v2_trend_carry | CHALLENGER | 1,001,130 | +1,103 | +1,514 | +1,130 | +1,130 | 0.1% | 3 | 0.45 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,001,366 | +337 | +1,486 | +1,366 | +1,366 | 0.2% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,002,728 | +4,173 | +437 | +2,728 | +2,728 | 0.2% | 4 | 2.47 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,529 | +903 | -86 | -471 | -471 | 0.2% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 998,381 | +402 | -1,544 | -1,487 | -1,619 | 0.3% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,001,572 | +1,103 | +1,514 | +1,572 | +1,572 | 0.1% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 999,701 | +904 | +718 | +421 | -299 | 0.1% | 4 | 0.56 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 999,259 | +603 | -1,257 | -741 | -741 | 0.2% | 2 | 0.34 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 997,002 | -408 | -4,568 | -6,996 | -2,998 | 0.9% | 3 | 0.48 | 21 | 33% | 0.54 |
| v5_carry_trend_daily_10p | REJECTED | 995,332 | +820 | +1,297 | -6,779 | -4,668 | 1.1% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 993,461 | +709 | +1,274 | -7,397 | -6,539 | 1.2% | 3 | 0.43 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 995,004 | +76 | -2,422 | -3,990 | -4,996 | 0.7% | 4 | 0.63 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 998,298 | +819 | +472 | -1,582 | -1,702 | 0.5% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 998,298 | +819 | +472 | -1,582 | -1,702 | 0.5% | 4 | 0.73 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,008,256 | +4,302 | +5,506 | +8,256 | +8,256 | 0.0% | 6 | 2.53 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 988,849 | -1,302 | -11,821 | -11,151 | -11,151 | 1.5% | 6 | 2.42 | 0 | — | — |
| v7_cm_monthly | REJECTED | 999,158 | +844 | -2,889 | -842 | -842 | 0.6% | 5 | 1.96 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,010,340 | +3,500 | +10,072 | +10,340 | +10,340 | 0.2% | 7 | 1.40 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,010,340 | +3,500 | +10,072 | +10,340 | +10,340 | 0.2% | 7 | 1.40 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 972,134 | -3,379 | -7,468 | -33,684 | -27,866 | 4.4% | 1 | 0.36 | 17 | 18% | 0.11 |

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
