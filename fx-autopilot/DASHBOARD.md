# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-10T03:52 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 878,934 | +2,657 | +858 | -86,006 | -121,066 | 13.5% | 2 | 4.11 | 170 | 41% | 0.62 |
| ml_logit_v1 | RESEARCH_ONLY | 1,003,626 | +3,498 | +3,498 | +3,626 | +3,626 | 0.0% | 0 | 0.00 | 2 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 997,787 | +0 | -23,267 | -24,957 | -2,213 | 4.0% | 0 | 0.00 | 33 | 52% | 0.97 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,045,853 | +9,447 | +13,922 | +37,334 | +45,853 | 0.0% | 0 | 0.00 | 35 | 60% | 1.67 |
| mtf_pullback_v1 | RESEARCH_ONLY | 994,881 | -5,120 | +2,001 | -4,792 | -5,119 | 0.9% | 0 | 0.00 | 8 | 38% | 0.79 |
| regime_switch_v1 | RESEARCH_ONLY | 969,701 | +0 | -14,784 | -7,485 | -30,299 | 4.8% | 0 | 0.00 | 44 | 30% | 0.72 |
| trend_donchian_v1 | RESEARCH_ONLY | 958,191 | -175 | -1,963 | -50,102 | -41,809 | 6.3% | 2 | 1.65 | 18 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 948,670 | -8,309 | +8,668 | -14,762 | -51,330 | 5.1% | 2 | 3.72 | 42 | 29% | 0.53 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,015,502 | -1,674 | -1,674 | +422 | +15,502 | 1.1% | 1 | 0.43 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -13,457 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,006,231 | +1,667 | -10,529 | -3,749 | +6,231 | 2.1% | 5 | 1.77 | 456 | 48% | 1.05 |
| v12_carry_timed | REJECTED | 1,001,862 | -4,176 | +1,531 | +1,862 | +1,862 | 0.8% | 6 | 2.58 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 996,417 | -2,806 | -4,460 | -3,583 | -3,583 | 0.5% | 3 | 1.18 | 0 | — | — |
| v13_ratemom | REJECTED | 1,001,432 | -4,585 | +1,122 | +1,432 | +1,432 | 0.5% | 6 | 2.71 | 0 | — | — |
| v14_term | REJECTED | 995,784 | -701 | -3,867 | -4,216 | -4,216 | 0.7% | 6 | 2.40 | 0 | — | — |
| v14_term_ratemom | REJECTED | 997,724 | -5,277 | -2,894 | -2,276 | -2,276 | 0.7% | 2 | 0.96 | 0 | — | — |
| v16_equity_rebal | REJECTED | 996,652 | +4,304 | -2,049 | -3,348 | -3,348 | 0.8% | 3 | 1.01 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 998,511 | +1,699 | -1,109 | -1,489 | -1,489 | 0.9% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 998,143 | -788 | -1,857 | -1,857 | -1,857 | 0.2% | 1 | 0.22 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 980,020 | -6,414 | -12,730 | -17,934 | -19,980 | 2.5% | 4 | 3.06 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 983,622 | -5,228 | -11,887 | -16,378 | -16,378 | 1.8% | 1 | 0.72 | 7 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 974,181 | -6,598 | +1,265 | -14,791 | -25,819 | 3.5% | 0 | 0.00 | 15 | 13% | 0.39 |
| v2_trend_carry | CHALLENGER | 999,312 | -1,666 | -500 | -688 | -688 | 0.3% | 3 | 0.45 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,000,048 | -2,179 | -651 | +48 | +48 | 0.3% | 3 | 0.47 | 0 | — | — |
| v3_carry_only | REJECTED | 998,396 | -2,307 | -1,161 | -1,604 | -1,604 | 0.6% | 4 | 2.48 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 998,179 | -1,445 | -1,634 | -1,821 | -1,821 | 0.3% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 997,836 | -1,049 | -2,286 | -2,031 | -2,164 | 0.3% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 999,755 | -1,666 | -500 | -245 | -245 | 0.3% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 998,349 | -1,446 | -213 | -931 | -1,651 | 0.3% | 4 | 0.56 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 998,247 | -1,269 | -1,998 | -1,753 | -1,753 | 0.3% | 2 | 0.34 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 998,056 | +162 | -2,859 | -5,942 | -1,944 | 0.8% | 3 | 0.48 | 21 | 33% | 0.54 |
| v5_carry_trend_daily_10p | REJECTED | 993,342 | -2,289 | -613 | -8,768 | -6,658 | 1.3% | 4 | 0.59 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 991,987 | -1,725 | -529 | -8,871 | -8,013 | 1.3% | 3 | 0.43 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 994,476 | -1,803 | -3,861 | -4,518 | -5,524 | 0.7% | 4 | 0.63 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 996,231 | -3,126 | -2,415 | -3,650 | -3,769 | 0.7% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 996,231 | -3,126 | -2,415 | -3,650 | -3,769 | 0.7% | 4 | 0.73 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,003,831 | -1,285 | +3,476 | +3,831 | +3,831 | 0.2% | 6 | 2.54 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 991,251 | -1,317 | -8,963 | -8,749 | -8,749 | 1.2% | 6 | 2.42 | 0 | — | — |
| v7_cm_monthly | REJECTED | 996,607 | -4,559 | -4,398 | -3,393 | -3,393 | 0.8% | 5 | 1.96 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,004,137 | -4,771 | +3,540 | +4,137 | +4,137 | 0.8% | 7 | 1.41 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,004,137 | -4,771 | +3,540 | +4,137 | +4,137 | 0.8% | 7 | 1.41 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 972,166 | -7,857 | -8,775 | -33,652 | -27,834 | 4.4% | 1 | 0.36 | 17 | 18% | 0.11 |

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
