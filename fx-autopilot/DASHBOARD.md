# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-23T02:04 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -43,153 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +0 | +8,143 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 983,203 | +0 | -9,728 | -40,675 | -16,797 | 5.4% | 0 | 0.00 | 38 | 47% | 0.82 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,007,253 | +7,970 | -20,148 | -12,456 | +7,253 | 4.3% | 2 | 2.78 | 46 | 48% | 1.01 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,007,010 | +0 | +12,129 | +16,707 | +7,010 | 0.0% | 0 | 0.00 | 10 | 50% | 1.29 |
| regime_switch_v1 | RESEARCH_ONLY | 1,000,743 | -1,182 | +37,665 | +2,715 | +743 | 1.7% | 3 | 2.88 | 54 | 28% | 0.71 |
| trend_donchian_v1 | RESEARCH_ONLY | 988,585 | -5,824 | +4,739 | +8,287 | -11,415 | 3.3% | 3 | 1.95 | 20 | 10% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 954,952 | -3,432 | -3,395 | -14,416 | -45,048 | 4.5% | 1 | 1.83 | 49 | 29% | 0.61 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,043,360 | -3,286 | +18,567 | +21,526 | +43,360 | 0.4% | 3 | 2.07 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | +0 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 999,414 | -352 | -10,119 | -18,314 | -586 | 2.8% | 5 | 1.75 | 591 | 48% | 1.00 |
| v12_carry_timed | REJECTED | 1,020,026 | +1,357 | -3,002 | +20,026 | +20,026 | 0.5% | 5 | 2.21 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,009,594 | -32 | -681 | +9,594 | +9,594 | 0.2% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,036,606 | -3,151 | +14,002 | +36,606 | +36,606 | 0.4% | 6 | 2.62 | 0 | — | — |
| v14_term | REJECTED | 996,590 | +85 | +501 | -3,410 | -3,410 | 0.6% | 3 | 1.31 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,019,997 | -882 | +5,534 | +19,997 | +19,997 | 0.2% | 2 | 0.94 | 0 | — | — |
| v16_equity_rebal | REJECTED | 972,263 | +599 | -6,372 | -27,737 | -27,737 | 3.2% | 1 | 0.36 | 2 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 985,522 | +2,502 | -10,709 | -14,478 | -14,478 | 2.2% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,007,729 | -1,765 | +3,898 | +7,729 | +7,729 | 0.2% | 4 | 0.77 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,004,571 | -1,930 | +9,809 | +9,128 | +4,571 | 0.3% | 4 | 2.64 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 991,414 | -664 | +6,658 | -9,004 | -8,586 | 1.1% | 1 | 0.64 | 9 | 11% | 0.12 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 992,662 | -5,151 | +9,712 | +17,102 | -7,338 | 1.6% | 2 | 2.29 | 18 | 22% | 0.74 |
| v2_trend_carry | CHALLENGER | 1,008,499 | -159 | +1,895 | +9,126 | +8,499 | 0.1% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,010,916 | -1,125 | +4,258 | +9,556 | +10,916 | 0.1% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,005,316 | +4,278 | -10,107 | +14,141 | +5,316 | 1.2% | 4 | 2.46 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,003,057 | +701 | -1,315 | +3,683 | +3,057 | 0.2% | 4 | 0.66 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,000,260 | +534 | -1,435 | +440 | +260 | 0.2% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,006,786 | +701 | -261 | +6,834 | +6,786 | 0.2% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,003,146 | +702 | -1,402 | +4,625 | +3,146 | 0.2% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,004,770 | -393 | +1,080 | +4,818 | +4,770 | 0.1% | 4 | 0.65 | 2 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 999,248 | +690 | -381 | -76 | -752 | 0.7% | 4 | 0.65 | 29 | 34% | 0.60 |
| v5_carry_trend_daily_10p | REJECTED | 1,004,837 | +324 | +908 | +10,693 | +4,837 | 0.2% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,000,953 | +66 | +1,299 | +8,540 | +953 | 0.4% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,001,382 | -558 | +1,916 | +2,538 | +1,382 | 0.1% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,008,784 | -738 | +3,488 | +9,521 | +8,784 | 0.1% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,008,784 | -738 | +3,488 | +9,521 | +8,784 | 0.1% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,020,372 | +2,271 | -5,244 | +20,372 | +20,372 | 0.7% | 5 | 2.17 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 989,083 | +904 | -5,341 | -10,917 | -10,917 | 1.4% | 4 | 1.64 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,011,457 | +1,191 | -3,518 | +11,457 | +11,457 | 0.4% | 4 | 1.61 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,036,759 | -916 | +8,595 | +36,759 | +36,759 | 0.2% | 7 | 1.37 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,036,759 | -916 | +8,595 | +36,759 | +36,759 | 0.2% | 7 | 1.37 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 987,935 | -2,540 | +7,391 | +2,004 | -12,065 | 2.9% | 6 | 2.32 | 20 | 20% | 0.12 |

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
