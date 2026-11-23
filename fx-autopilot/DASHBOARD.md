# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-23T07:57 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -43,153 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +0 | +8,143 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 983,203 | +0 | -9,728 | -40,675 | -16,797 | 5.4% | 0 | 0.00 | 38 | 47% | 0.82 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,010,514 | +11,231 | -20,309 | -9,195 | +10,514 | 4.0% | 2 | 2.77 | 46 | 48% | 1.01 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,007,010 | +0 | +12,129 | +16,707 | +7,010 | 0.0% | 0 | 0.00 | 10 | 50% | 1.29 |
| regime_switch_v1 | RESEARCH_ONLY | 1,000,570 | -1,355 | +32,980 | +2,542 | +570 | 1.7% | 3 | 2.88 | 54 | 28% | 0.71 |
| trend_donchian_v1 | RESEARCH_ONLY | 986,827 | -7,582 | +2,684 | +6,529 | -13,173 | 3.5% | 3 | 1.95 | 20 | 10% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 954,270 | -4,114 | -5,404 | -15,098 | -45,730 | 4.6% | 1 | 1.84 | 49 | 29% | 0.61 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,040,598 | -6,048 | +14,731 | +18,764 | +40,598 | 0.7% | 3 | 2.07 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | +0 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,000,995 | +1,228 | -7,313 | -16,734 | +995 | 2.6% | 0 | 0.00 | 596 | 48% | 1.01 |
| v12_carry_timed | REJECTED | 1,019,509 | +840 | -1,791 | +19,509 | +19,509 | 0.5% | 5 | 2.21 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,008,063 | -1,563 | -1,490 | +8,063 | +8,063 | 0.4% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,032,438 | -7,319 | +6,772 | +32,438 | +32,438 | 0.8% | 6 | 2.63 | 0 | — | — |
| v14_term | REJECTED | 996,096 | -410 | +1,145 | -3,904 | -3,904 | 0.7% | 3 | 1.31 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,018,389 | -2,491 | +2,856 | +18,389 | +18,389 | 0.3% | 2 | 0.94 | 0 | — | — |
| v16_equity_rebal | REJECTED | 972,107 | +443 | -4,996 | -27,893 | -27,893 | 3.2% | 1 | 0.37 | 2 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 986,532 | +3,512 | -6,867 | -13,468 | -13,468 | 2.1% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,006,782 | -2,712 | +2,230 | +6,782 | +6,782 | 0.3% | 4 | 0.77 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,001,130 | -5,371 | +4,638 | +5,688 | +1,130 | 0.7% | 4 | 2.65 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 990,351 | -1,727 | +3,084 | -10,067 | -9,649 | 1.2% | 1 | 0.64 | 9 | 11% | 0.12 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 988,284 | -9,530 | +2,633 | +12,723 | -11,716 | 2.1% | 2 | 2.30 | 18 | 22% | 0.74 |
| v2_trend_carry | CHALLENGER | 1,008,305 | -353 | +1,475 | +8,932 | +8,305 | 0.1% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,010,285 | -1,756 | +2,752 | +8,925 | +10,285 | 0.2% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,006,072 | +5,033 | -6,947 | +14,897 | +6,072 | 1.1% | 4 | 2.46 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,003,303 | +947 | -875 | +3,929 | +3,303 | 0.2% | 4 | 0.65 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,000,069 | +343 | -1,165 | +249 | +69 | 0.2% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,007,032 | +947 | -241 | +7,080 | +7,032 | 0.2% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,003,392 | +948 | -962 | +4,871 | +3,392 | 0.2% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,004,220 | -943 | +300 | +4,268 | +4,220 | 0.2% | 4 | 0.65 | 2 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 999,492 | +934 | -370 | +168 | -508 | 0.7% | 4 | 0.65 | 29 | 34% | 0.60 |
| v5_carry_trend_daily_10p | REJECTED | 1,004,320 | -194 | +362 | +10,176 | +4,320 | 0.2% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,000,560 | -327 | +805 | +8,147 | +560 | 0.5% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,000,419 | -1,521 | +986 | +1,576 | +419 | 0.2% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,008,217 | -1,304 | +2,265 | +8,955 | +8,217 | 0.2% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,008,217 | -1,304 | +2,265 | +8,955 | +8,217 | 0.2% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,019,070 | +969 | -4,542 | +19,070 | +19,070 | 0.8% | 5 | 2.18 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 988,447 | +267 | -4,543 | -11,553 | -11,553 | 1.5% | 4 | 1.64 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,010,962 | +695 | -2,433 | +10,962 | +10,962 | 0.4% | 4 | 1.61 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,035,627 | -2,048 | +6,427 | +35,627 | +35,627 | 0.3% | 7 | 1.37 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,035,627 | -2,048 | +6,427 | +35,627 | +35,627 | 0.3% | 7 | 1.37 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 984,809 | -5,666 | +2,790 | -1,122 | -15,191 | 3.2% | 6 | 2.33 | 20 | 20% | 0.12 |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.92 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -2.4% | 0.87 | -0.42 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -10.1% | 0.84 | -1.06 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.72 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -6.9% | 0.79 | -0.94 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.20 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.60 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.17 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -5.4% | 0.76 | -0.67 | 1.09 |
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
