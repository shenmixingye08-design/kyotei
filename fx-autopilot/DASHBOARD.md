# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-13T02:04 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | -12,102 | -94,283 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +8,143 | +8,271 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 997,555 | +0 | -5,063 | -28,180 | -2,445 | 4.1% | 0 | 0.00 | 35 | 51% | 0.97 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,029,243 | -5,054 | -4,496 | +13,607 | +29,243 | 2.2% | 2 | 2.89 | 38 | 55% | 1.37 |
| mtf_pullback_v1 | RESEARCH_ONLY | 994,881 | +0 | -5,120 | -528 | -5,119 | 0.9% | 0 | 0.00 | 8 | 38% | 0.79 |
| regime_switch_v1 | RESEARCH_ONLY | 958,912 | +3,718 | -10,789 | -14,494 | -41,088 | 5.8% | 3 | 4.15 | 50 | 26% | 0.59 |
| trend_donchian_v1 | RESEARCH_ONLY | 980,238 | +4,943 | +18,718 | -19,259 | -19,762 | 4.1% | 3 | 2.87 | 19 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 961,415 | +2,687 | +9,732 | -5,233 | -38,585 | 3.9% | 2 | 3.13 | 45 | 29% | 0.57 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,023,219 | +3,093 | +6,043 | +6,076 | +23,219 | 0.3% | 1 | 0.43 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -13,648 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,007,962 | -3,113 | +1,668 | -2,336 | +7,962 | 1.9% | 5 | 1.76 | 501 | 48% | 1.06 |
| v12_carry_timed | REJECTED | 1,021,922 | +1,254 | +21,190 | +21,922 | +21,922 | 0.1% | 6 | 2.53 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,008,404 | +1,177 | +12,358 | +8,404 | +8,404 | 0.1% | 3 | 1.17 | 0 | — | — |
| v13_ratemom | REJECTED | 1,018,770 | +3,871 | +23,463 | +18,770 | +18,770 | 0.2% | 6 | 2.67 | 0 | — | — |
| v14_term | REJECTED | 997,238 | -2,470 | +1,214 | -2,762 | -2,762 | 0.5% | 5 | 1.96 | 1 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,012,059 | +3,196 | +13,947 | +12,059 | +12,059 | 0.1% | 2 | 0.94 | 0 | — | — |
| v16_equity_rebal | REJECTED | 982,124 | -4,962 | -12,762 | -17,876 | -17,876 | 2.2% | 3 | 1.02 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 998,497 | -2,477 | +245 | -1,503 | -1,503 | 0.9% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,002,424 | +2,106 | +2,424 | +2,424 | +2,424 | 0.0% | 2 | 0.39 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 989,708 | +1,122 | +7,169 | -7,635 | -10,292 | 1.5% | 3 | 2.26 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 983,285 | +163 | -7,346 | -16,715 | -16,715 | 1.9% | 1 | 0.65 | 8 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 979,011 | +4,831 | +1,212 | -411 | -20,989 | 3.0% | 1 | 1.12 | 15 | 13% | 0.39 |
| v2_trend_carry | CHALLENGER | 1,005,670 | +1,546 | +6,459 | +5,801 | +5,670 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,005,079 | +1,798 | +4,711 | +5,446 | +5,079 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,015,106 | +1,275 | +17,495 | +15,199 | +15,106 | 0.1% | 4 | 2.44 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,003,885 | +910 | +5,748 | +4,016 | +3,885 | 0.0% | 4 | 0.55 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,600 | +135 | +3,671 | +1,864 | +1,600 | 0.0% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,006,112 | +1,546 | +6,459 | +6,244 | +6,112 | 0.0% | 3 | 0.44 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,004,061 | +910 | +5,754 | +5,003 | +4,061 | 0.0% | 4 | 0.55 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,002,754 | +863 | +3,803 | +2,886 | +2,754 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 999,151 | +348 | -25 | -4,386 | -849 | 0.7% | 3 | 0.44 | 28 | 36% | 0.65 |
| v5_carry_trend_daily_10p | REJECTED | 1,002,456 | +1,881 | +8,834 | +1,438 | +2,456 | 0.4% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 998,734 | +1,280 | +6,927 | -1,034 | -1,266 | 0.7% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 998,802 | +598 | +3,939 | +952 | -1,198 | 0.3% | 4 | 0.62 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,003,792 | +2,005 | +7,270 | +4,490 | +3,792 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,003,792 | +2,005 | +7,270 | +4,490 | +3,792 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,024,131 | +1,031 | +25,469 | +24,131 | +24,131 | 0.1% | 6 | 2.49 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 993,684 | -1,448 | +1,080 | -6,316 | -6,316 | 1.0% | 5 | 1.97 | 1 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,012,890 | +1,817 | +13,838 | +12,890 | +12,890 | 0.1% | 5 | 1.93 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,025,140 | +4,784 | +22,434 | +25,140 | +25,140 | 0.0% | 7 | 1.38 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,025,140 | +4,784 | +22,434 | +25,140 | +25,140 | 0.0% | 7 | 1.38 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 976,729 | +5,488 | -3,650 | -25,807 | -23,271 | 4.0% | 5 | 1.89 | 19 | 21% | 0.13 |

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
