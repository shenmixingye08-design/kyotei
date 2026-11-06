# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-06T11:05 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 873,972 | +3,472 | -5,334 | -114,343 | -126,028 | 14.0% | 2 | 3.26 | 163 | 40% | 0.60 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,000,471 | -2,147 | -13,348 | -17,674 | +471 | 3.8% | 1 | 2.12 | 32 | 53% | 1.04 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,033,739 | +2,197 | +13,630 | +27,162 | +33,739 | 0.6% | 0 | 0.00 | 33 | 58% | 1.49 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,000,002 | +0 | +7,122 | +328 | +2 | 0.4% | 0 | 0.00 | 7 | 43% | 1.00 |
| regime_switch_v1 | RESEARCH_ONLY | 969,701 | +0 | -5,725 | -21,514 | -30,299 | 4.8% | 0 | 0.00 | 44 | 30% | 0.72 |
| trend_donchian_v1 | RESEARCH_ONLY | 964,771 | +669 | +16 | -47,008 | -35,229 | 5.7% | 3 | 2.52 | 17 | 12% | 0.17 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 956,846 | +6,314 | -6,269 | -18,232 | -43,154 | 4.3% | 3 | 3.77 | 38 | 29% | 0.46 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,017,176 | +0 | -3,460 | +1,511 | +17,176 | 0.9% | 0 | 0.00 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -12,789 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,010,518 | +5,958 | -7,943 | +10,453 | +10,518 | 1.7% | 5 | 2.03 | 431 | 48% | 1.08 |
| v12_carry_timed | REJECTED | 1,005,884 | +5,226 | +5,884 | +5,884 | +5,884 | 0.0% | 6 | 2.57 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 996,320 | -3,381 | -3,680 | -3,680 | -3,680 | 0.5% | 3 | 1.18 | 0 | — | — |
| v13_ratemom | REJECTED | 999,873 | +9,311 | -127 | -127 | -127 | 0.1% | 6 | 2.72 | 0 | — | — |
| v14_term | REJECTED | 995,845 | -4,738 | -4,155 | -4,155 | -4,155 | 0.7% | 6 | 2.40 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,001,833 | +5,356 | +1,833 | +1,833 | +1,833 | 0.0% | 2 | 0.95 | 0 | — | — |
| v16_equity_rebal | REJECTED | 989,562 | -13,178 | -10,438 | -10,438 | -10,438 | 1.5% | 3 | 1.01 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 996,232 | -9,156 | -3,768 | -3,768 | -3,768 | 1.1% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 981,082 | -7,229 | -14,384 | -16,345 | -18,918 | 2.4% | 4 | 3.06 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 989,344 | -5,155 | -8,006 | -10,656 | -10,656 | 1.3% | 0 | 0.00 | 5 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 978,930 | +1,131 | +3,005 | -16,078 | -21,070 | 3.0% | 1 | 1.26 | 14 | 14% | 0.43 |
| v2_trend_carry | CHALLENGER | 1,001,186 | +3,229 | +1,591 | +1,186 | +1,186 | 0.0% | 3 | 0.45 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,002,082 | +4,140 | +1,122 | +2,082 | +2,082 | 0.1% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,001,002 | -396 | +4,801 | +1,002 | +1,002 | 0.4% | 4 | 2.47 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,435 | +981 | -160 | -565 | -565 | 0.2% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 998,267 | -1,271 | -1,638 | -1,601 | -1,733 | 0.3% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,001,628 | +3,229 | +1,591 | +1,628 | +1,628 | 0.0% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 999,607 | +981 | +1,224 | -393 | -393 | 0.1% | 4 | 0.56 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 999,288 | -1,271 | -749 | -712 | -712 | 0.2% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 998,032 | -3,399 | -2,954 | -6,496 | -1,968 | 0.8% | 4 | 0.66 | 18 | 39% | 0.77 |
| v5_carry_trend_daily_10p | REJECTED | 995,582 | +2,700 | +1,998 | -6,639 | -4,418 | 1.1% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 993,752 | +3,839 | +2,028 | -7,000 | -6,248 | 1.2% | 3 | 0.43 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 995,348 | -339 | -3,134 | -3,783 | -4,652 | 0.6% | 4 | 0.63 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 998,637 | +3,148 | -264 | -1,244 | -1,363 | 0.5% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 998,637 | +3,148 | -264 | -1,244 | -1,363 | 0.5% | 4 | 0.73 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,001,491 | -203 | +1,491 | +1,491 | +1,491 | 0.4% | 6 | 2.54 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 988,861 | -13,436 | -11,139 | -11,139 | -11,139 | 1.5% | 6 | 2.42 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,001,331 | +90 | +1,331 | +1,331 | +1,331 | 0.4% | 5 | 1.95 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,009,517 | +12,709 | +9,517 | +9,517 | +9,517 | 0.0% | 7 | 1.41 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,009,517 | +12,709 | +9,517 | +9,517 | +9,517 | 0.0% | 7 | 1.41 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 983,186 | +3,066 | +232 | -22,891 | -16,814 | 3.3% | 1 | 0.36 | 15 | 20% | 0.14 |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.94 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -3.2% | 0.83 | -0.59 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -6.5% | 0.89 | -0.70 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.74 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -8.2% | 0.74 | -1.18 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.22 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.64 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.17 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -7.0% | 0.68 | -0.93 | 1.09 |
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
