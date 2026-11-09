# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-09T19:55 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 879,017 | +9,367 | -215 | -85,923 | -120,983 | 13.5% | 2 | 4.11 | 169 | 41% | 0.63 |
| ml_logit_v1 | RESEARCH_ONLY | 1,002,592 | +2,464 | +2,464 | +2,592 | +2,592 | 0.0% | 1 | 1.94 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 997,787 | +0 | -23,042 | -24,957 | -2,213 | 4.0% | 0 | 0.00 | 33 | 52% | 0.97 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,045,853 | +14,656 | +17,070 | +37,334 | +45,853 | 0.0% | 0 | 0.00 | 35 | 60% | 1.67 |
| mtf_pullback_v1 | RESEARCH_ONLY | 994,881 | -5,120 | +2,001 | -4,792 | -5,119 | 0.9% | 0 | 0.00 | 8 | 38% | 0.79 |
| regime_switch_v1 | RESEARCH_ONLY | 969,701 | +0 | -13,514 | -7,485 | -30,299 | 4.8% | 0 | 0.00 | 44 | 30% | 0.72 |
| trend_donchian_v1 | RESEARCH_ONLY | 958,505 | -3,244 | -2,686 | -49,789 | -41,495 | 6.3% | 2 | 1.65 | 18 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 948,732 | -13,432 | +5,727 | -14,699 | -51,268 | 5.1% | 2 | 2.97 | 41 | 29% | 0.55 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,016,095 | -1,081 | -1,081 | +1,015 | +16,095 | 1.0% | 1 | 0.43 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -13,457 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,002,996 | -4,591 | -13,682 | -6,983 | +2,996 | 2.4% | 5 | 1.97 | 451 | 47% | 1.01 |
| v12_carry_timed | REJECTED | 1,003,072 | -5,494 | +3,072 | +3,072 | +3,072 | 0.6% | 6 | 2.58 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 997,006 | -1,264 | -2,994 | -2,994 | -2,994 | 0.4% | 3 | 1.18 | 0 | — | — |
| v13_ratemom | REJECTED | 1,003,673 | -1,410 | +3,673 | +3,673 | +3,673 | 0.3% | 6 | 2.71 | 0 | — | — |
| v14_term | REJECTED | 996,002 | -613 | -3,998 | -3,998 | -3,998 | 0.7% | 6 | 2.40 | 0 | — | — |
| v14_term_ratemom | REJECTED | 999,009 | -5,033 | -991 | -991 | -991 | 0.5% | 2 | 0.95 | 0 | — | — |
| v16_equity_rebal | REJECTED | 995,159 | +6,516 | -4,841 | -4,841 | -4,841 | 0.9% | 3 | 1.01 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 997,545 | +1,670 | -2,455 | -2,455 | -2,455 | 1.0% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 998,439 | -1,349 | -1,561 | -1,561 | -1,561 | 0.2% | 1 | 0.22 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 981,123 | -2,587 | -11,388 | -16,831 | -18,877 | 2.4% | 4 | 3.06 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 984,716 | -4,590 | -10,794 | -15,284 | -15,284 | 1.7% | 2 | 1.08 | 5 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 975,215 | -6,632 | +1,771 | -13,757 | -24,785 | 3.4% | 1 | 1.27 | 14 | 14% | 0.43 |
| v2_trend_carry | CHALLENGER | 999,694 | -2,020 | +63 | -306 | -306 | 0.2% | 3 | 0.45 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,000,655 | -2,085 | +308 | +655 | +655 | 0.2% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 998,329 | -3,556 | -986 | -1,671 | -1,671 | 0.6% | 4 | 2.48 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 998,421 | -1,576 | -1,210 | -1,579 | -1,579 | 0.3% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 997,930 | -897 | -2,011 | -1,937 | -2,070 | 0.3% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,000,137 | -2,020 | +63 | +137 | +137 | 0.2% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 998,592 | -1,577 | +173 | -688 | -1,408 | 0.2% | 4 | 0.56 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 998,481 | -1,341 | -1,593 | -1,519 | -1,519 | 0.3% | 2 | 0.34 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 997,629 | -570 | -3,432 | -6,369 | -2,371 | 0.8% | 3 | 0.48 | 21 | 33% | 0.54 |
| v5_carry_trend_daily_10p | REJECTED | 993,938 | -2,374 | +502 | -8,173 | -6,062 | 1.3% | 4 | 0.59 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 992,590 | -2,026 | +707 | -8,268 | -7,410 | 1.3% | 3 | 0.43 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 994,795 | -1,355 | -3,073 | -4,199 | -5,205 | 0.7% | 4 | 0.63 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 996,989 | -2,894 | -1,298 | -2,892 | -3,011 | 0.6% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 996,989 | -2,894 | -1,298 | -2,892 | -3,011 | 0.6% | 4 | 0.73 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,004,569 | -599 | +4,569 | +4,569 | +4,569 | 0.1% | 6 | 2.54 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 990,854 | +1,087 | -9,146 | -9,146 | -9,146 | 1.3% | 6 | 2.42 | 0 | — | — |
| v7_cm_monthly | REJECTED | 997,426 | -4,790 | -2,574 | -2,574 | -2,574 | 0.8% | 5 | 1.96 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,005,877 | -5,833 | +5,877 | +5,877 | +5,877 | 0.6% | 7 | 1.41 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,005,877 | -5,833 | +5,877 | +5,877 | +5,877 | 0.6% | 7 | 1.41 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 974,091 | -8,398 | -6,325 | -31,727 | -25,909 | 4.2% | 3 | 1.27 | 15 | 20% | 0.14 |

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
