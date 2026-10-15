# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-10-15T11:40 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 961,619 | +6,209 | -32,491 | -38,381 | -38,381 | 5.4% | 1 | 1.66 | 72 | 43% | 0.74 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,554 | +554 | +554 | +554 | +554 | 0.1% | 1 | 1.88 | 0 | — | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,038,983 | +13,248 | +23,348 | +38,983 | +38,983 | 0.0% | 0 | 0.00 | 21 | 71% | 2.47 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,034,414 | +18,779 | +30,096 | +34,414 | +34,414 | 0.0% | 2 | 2.46 | 14 | 64% | 2.39 |
| mtf_pullback_v1 | RESEARCH_ONLY | 995,410 | +0 | -4,264 | -4,590 | -4,590 | 0.8% | 0 | 0.00 | 3 | 33% | 0.51 |
| regime_switch_v1 | RESEARCH_ONLY | 1,003,889 | +29,319 | +16,974 | +3,889 | +3,889 | 1.1% | 2 | 2.98 | 19 | 21% | 0.60 |
| trend_donchian_v1 | RESEARCH_ONLY | 990,092 | -14,068 | -27,253 | -9,908 | -9,908 | 3.2% | 1 | 1.63 | 8 | 0% | 0.00 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 956,741 | -7,062 | -20,493 | -43,259 | -43,259 | 4.3% | 3 | 4.51 | 16 | 12% | 0.03 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,015,339 | -1,963 | -2,086 | +15,339 | +15,339 | 0.3% | 1 | 0.47 | 3 | 67% | 5.81 |
| v10_carry_vix | REJECTED | 1,000,250 | -8,727 | -6,531 | +250 | +250 | 1.2% | 6 | 2.30 | 0 | — | — |
| v11_intraday_region | REJECTED | 1,017,294 | +6,135 | +13,097 | +17,294 | +17,294 | 0.1% | 5 | 2.00 | 195 | 56% | 1.45 |
| v12_carry_timed | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 988,203 | -11,752 | -8,312 | -11,797 | -11,797 | 1.7% | 4 | 3.06 | 0 | — | — |
| v2_h4_ema | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 982,294 | +2,872 | -15,462 | -17,706 | -17,706 | 2.7% | 1 | 1.23 | 10 | 10% | 0.30 |
| v2_trend_carry | CHALLENGER | 999,764 | -370 | -236 | -236 | -236 | 0.2% | 1 | 0.18 | 0 | — | — |
| v2_xpair_strength | REJECTED | 1,000,086 | -19 | +86 | +86 | +86 | 0.2% | 2 | 0.35 | 0 | — | — |
| v3_carry_only | REJECTED | 997,633 | -2,981 | -2,367 | -2,367 | -2,367 | 0.7% | 2 | 1.42 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,764 | -370 | -236 | -236 | -236 | 0.2% | 1 | 0.18 | 0 | — | — |
| v3_carry_trend_mh | REJECTED | 999,632 | -370 | -236 | -368 | -368 | 0.2% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 999,764 | -370 | -236 | -236 | -236 | 0.2% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,000,062 | +982 | +62 | +62 | +62 | 0.1% | 2 | 0.29 | 1 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 999,764 | -370 | -236 | -236 | -236 | 0.2% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,002,373 | -1,507 | -3,085 | +2,373 | +2,373 | 0.4% | 4 | 0.56 | 3 | 33% | 0.41 |
| v5_carry_trend_daily_10p | REJECTED | 1,000,797 | -1,210 | -2,629 | +797 | +797 | 0.6% | 4 | 0.74 | 1 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 999,551 | -1,205 | -2,409 | -449 | -449 | 0.6% | 4 | 0.74 | 0 | — | — |
| v6_carry_trend_daily_mkt_7p | REJECTED | 998,579 | +204 | -992 | -1,421 | -1,421 | 0.3% | 3 | 0.56 | 1 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,000,030 | +202 | +149 | +30 | +30 | 0.3% | 3 | 0.56 | 1 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 1,000,030 | +202 | +149 | +30 | +30 | 0.3% | 3 | 0.56 | 1 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 1,003,233 | -1,357 | -6,695 | +3,233 | +3,233 | 1.4% | 5 | 1.89 | 0 | — | — |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.96 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -3.2% | 0.83 | -0.60 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -5.6% | 0.90 | -0.63 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.75 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -7.6% | 0.75 | -1.13 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.25 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.67 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.18 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -7.7% | 0.65 | -1.06 | 1.09 |
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
