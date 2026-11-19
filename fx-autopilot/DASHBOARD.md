# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-19T20:47 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -69,311 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +0 | +8,143 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 983,203 | -6,907 | -14,352 | -50,518 | -16,797 | 5.4% | 0 | 0.00 | 38 | 47% | 0.82 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,007,859 | -2,859 | -21,554 | -18,482 | +7,859 | 4.2% | 1 | 1.06 | 44 | 50% | 1.10 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,003,620 | +3,981 | +8,738 | +13,317 | +3,620 | 0.0% | 1 | 2.45 | 9 | 44% | 0.99 |
| regime_switch_v1 | RESEARCH_ONLY | 989,602 | +7,523 | +30,750 | -13,496 | -10,398 | 2.8% | 3 | 4.54 | 52 | 27% | 0.62 |
| trend_donchian_v1 | RESEARCH_ONLY | 999,588 | +9,919 | +20,250 | +15,368 | -412 | 2.3% | 3 | 2.82 | 19 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 956,003 | +1,820 | -5,202 | +7,439 | -43,997 | 4.4% | 1 | 2.17 | 48 | 29% | 0.62 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,043,178 | +4,787 | +20,275 | +28,888 | +43,178 | 0.0% | 3 | 2.07 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -3,549 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,002,433 | -7,256 | -5,159 | -8,020 | +2,433 | 2.5% | 5 | 1.93 | 571 | 48% | 1.04 |
| v12_carry_timed | REJECTED | 1,023,322 | +339 | +1,392 | +23,322 | +23,322 | 0.2% | 5 | 2.20 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,011,109 | -204 | +2,522 | +11,109 | +11,109 | 0.1% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,034,332 | +163 | +15,128 | +34,332 | +34,332 | 0.1% | 6 | 2.63 | 0 | — | — |
| v14_term | REJECTED | 997,641 | +946 | +454 | -2,359 | -2,359 | 0.5% | 3 | 1.31 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,020,451 | +884 | +8,280 | +20,451 | +20,451 | 0.0% | 2 | 0.93 | 0 | — | — |
| v16_equity_rebal | REJECTED | 972,991 | +48 | -9,931 | -27,009 | -27,009 | 3.1% | 1 | 0.36 | 2 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 989,136 | +575 | -9,498 | -10,864 | -10,864 | 1.8% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,008,143 | +1,381 | +5,787 | +8,143 | +8,143 | 0.0% | 2 | 0.39 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,005,175 | -240 | +15,140 | +15,381 | +5,175 | 0.2% | 4 | 2.64 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 991,713 | -1,981 | +8,646 | -8,287 | -8,287 | 1.0% | 1 | 0.64 | 9 | 11% | 0.12 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 993,570 | -3,900 | +15,346 | +18,009 | -6,430 | 1.5% | 1 | 1.06 | 18 | 22% | 0.74 |
| v2_trend_carry | CHALLENGER | 1,009,164 | +1,040 | +3,529 | +9,727 | +9,164 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,009,968 | +21 | +4,864 | +11,124 | +9,968 | 0.1% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,013,428 | +2,536 | -1,997 | +14,737 | +13,428 | 0.4% | 4 | 2.44 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,004,702 | +952 | +799 | +5,265 | +4,702 | 0.0% | 4 | 0.65 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,695 | +539 | -4 | +2,390 | +1,695 | 0.0% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,008,432 | +952 | +2,353 | +8,994 | +8,432 | 0.0% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,004,794 | +953 | +714 | +6,327 | +4,794 | 0.0% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,005,550 | +1,126 | +2,842 | +6,112 | +5,550 | 0.0% | 3 | 0.44 | 2 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 1,000,869 | +941 | +1,620 | -696 | +869 | 0.5% | 4 | 0.65 | 29 | 34% | 0.60 |
| v5_carry_trend_daily_10p | REJECTED | 1,006,193 | +329 | +3,903 | +11,054 | +6,193 | 0.0% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,001,701 | +309 | +3,020 | +7,819 | +1,701 | 0.4% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,001,537 | +305 | +2,625 | +5,242 | +1,537 | 0.0% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,008,625 | +435 | +4,854 | +11,878 | +8,625 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,008,625 | +435 | +4,854 | +11,878 | +8,625 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,025,622 | +621 | +1,371 | +25,622 | +25,622 | 0.2% | 5 | 2.16 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 991,305 | -989 | -2,799 | -8,695 | -8,695 | 1.2% | 4 | 1.64 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,014,276 | -536 | +1,497 | +14,276 | +14,276 | 0.1% | 4 | 1.60 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,037,660 | +2,582 | +13,023 | +37,660 | +37,660 | 0.0% | 7 | 1.37 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,037,660 | +2,582 | +13,023 | +37,660 | +37,660 | 0.0% | 7 | 1.37 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 989,757 | -638 | +13,162 | +2,545 | -10,243 | 2.7% | 6 | 2.22 | 19 | 21% | 0.13 |

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
