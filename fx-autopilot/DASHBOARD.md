# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-10-23T17:41 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 905,575 | -6,131 | -46,586 | -94,425 | -94,425 | 10.9% | 2 | 2.82 | 113 | 40% | 0.60 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,023,878 | +0 | -9,843 | +23,878 | +23,878 | 1.5% | 0 | 0.00 | 24 | 62% | 1.57 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,020,550 | +2,275 | -13,513 | +20,550 | +20,550 | 1.9% | 2 | 2.28 | 22 | 55% | 1.44 |
| mtf_pullback_v1 | RESEARCH_ONLY | 990,302 | +0 | +0 | -9,698 | -9,698 | 1.3% | 0 | 0.00 | 4 | 25% | 0.33 |
| regime_switch_v1 | RESEARCH_ONLY | 998,478 | +2,718 | -9,468 | -1,522 | -1,522 | 1.9% | 1 | 1.06 | 29 | 34% | 0.95 |
| trend_donchian_v1 | RESEARCH_ONLY | 980,658 | -302 | -3,518 | -19,342 | -19,342 | 4.1% | 3 | 2.22 | 11 | 9% | 0.22 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 969,776 | +3,784 | +13,790 | -30,224 | -30,224 | 3.0% | 2 | 3.29 | 25 | 20% | 0.25 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,022,516 | +2,811 | +5,691 | +22,516 | +22,516 | 0.1% | 2 | 1.04 | 4 | 75% | 6.25 |
| v10_carry_vix | REJECTED | 993,074 | -950 | -4,761 | -6,926 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,016,945 | +2,991 | +6,672 | +16,945 | +16,945 | 0.3% | 5 | 1.97 | 286 | 56% | 1.29 |
| v12_carry_timed | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 995,931 | +3,448 | +7,964 | -4,069 | -4,069 | 0.9% | 2 | 1.66 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 1,000,031 | +730 | +31 | +31 | +31 | 0.2% | 2 | 1.29 | 0 | — | — |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 975,561 | +0 | +0 | -24,439 | -24,439 | 3.3% | 0 | 0.00 | 11 | 9% | 0.26 |
| v2_trend_carry | CHALLENGER | 999,617 | +328 | -42 | -383 | -383 | 0.2% | 2 | 0.29 | 0 | — | — |
| v2_xpair_strength | REJECTED | 1,001,588 | +937 | +2,271 | +1,588 | +1,588 | 0.0% | 2 | 0.35 | 0 | — | — |
| v3_carry_only | REJECTED | 992,092 | +145 | -6,975 | -7,908 | -7,908 | 1.2% | 3 | 1.86 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,617 | +328 | -42 | -383 | -383 | 0.2% | 2 | 0.29 | 0 | — | — |
| v3_carry_trend_mh | REJECTED | 999,972 | +484 | +445 | -28 | -28 | 0.1% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,000,104 | +484 | +445 | +104 | +104 | 0.1% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 998,673 | +484 | -905 | -1,327 | -1,327 | 0.2% | 1 | 0.18 | 2 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,000,104 | +484 | +445 | +104 | +104 | 0.1% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 999,544 | +100 | -3,389 | -456 | -456 | 0.7% | 4 | 0.66 | 12 | 33% | 0.30 |
| v5_carry_trend_daily_10p | REJECTED | 994,544 | +732 | -3,255 | -5,456 | -5,456 | 1.2% | 4 | 0.74 | 1 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 992,683 | +118 | -3,863 | -7,317 | -7,317 | 1.3% | 3 | 0.43 | 1 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 999,071 | +943 | +2,323 | -929 | -929 | 0.3% | 2 | 0.35 | 2 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 999,490 | +943 | +1,289 | -510 | -510 | 0.4% | 2 | 0.35 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 999,490 | +943 | +1,289 | -510 | -510 | 0.4% | 2 | 0.35 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 986,083 | -82 | -7,490 | -13,917 | -13,917 | 3.1% | 1 | 0.18 | 5 | 0% | 0.00 |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.96 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -3.2% | 0.83 | -0.59 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -4.6% | 0.92 | -0.50 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.75 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -8.5% | 0.73 | -1.25 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.24 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.66 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.17 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -7.7% | 0.65 | -1.05 | 1.09 |
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
