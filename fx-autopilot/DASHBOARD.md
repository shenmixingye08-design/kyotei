# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-10-15T21:43 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 958,950 | +5,928 | -25,123 | -41,050 | -41,050 | 5.6% | 1 | 1.25 | 73 | 42% | 0.73 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +128 | +128 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,038,983 | +0 | +16,239 | +38,983 | +38,983 | 0.0% | 0 | 0.00 | 21 | 71% | 2.47 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,033,424 | +11,430 | +24,906 | +33,424 | +33,424 | 0.2% | 2 | 2.47 | 14 | 64% | 2.39 |
| mtf_pullback_v1 | RESEARCH_ONLY | 995,410 | +0 | -4,264 | -4,590 | -4,590 | 0.8% | 0 | 0.00 | 3 | 33% | 0.51 |
| regime_switch_v1 | RESEARCH_ONLY | 1,005,661 | +15,825 | +23,172 | +5,661 | +5,661 | 0.9% | 0 | 0.00 | 21 | 29% | 1.13 |
| trend_donchian_v1 | RESEARCH_ONLY | 989,016 | -9,077 | -22,354 | -10,984 | -10,984 | 3.3% | 1 | 1.63 | 8 | 0% | 0.00 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 955,272 | +2,408 | -16,552 | -44,728 | -44,728 | 4.5% | 2 | 3.03 | 17 | 12% | 0.03 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,015,999 | -913 | +2,115 | +15,999 | +15,999 | 0.3% | 1 | 0.47 | 3 | 67% | 5.81 |
| v10_carry_vix | REJECTED | 998,551 | -8,507 | -5,469 | -1,449 | -1,449 | 1.3% | 6 | 2.31 | 0 | — | — |
| v11_intraday_region | REJECTED | 1,019,331 | +3,195 | +10,900 | +19,331 | +19,331 | 0.0% | 0 | 0.00 | 205 | 57% | 1.47 |
| v12_carry_timed | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 986,751 | -14,186 | -9,427 | -13,249 | -13,249 | 1.8% | 4 | 3.06 | 0 | — | — |
| v2_h4_ema | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 982,203 | +2,781 | -12,186 | -17,797 | -17,797 | 2.7% | 1 | 1.23 | 10 | 10% | 0.30 |
| v2_trend_carry | CHALLENGER | 999,642 | -1,005 | -358 | -358 | -358 | 0.2% | 1 | 0.18 | 0 | — | — |
| v2_xpair_strength | REJECTED | 999,571 | -1,665 | -429 | -429 | -429 | 0.2% | 2 | 0.35 | 0 | — | — |
| v3_carry_only | REJECTED | 997,992 | -3,155 | -2,008 | -2,008 | -2,008 | 0.7% | 2 | 1.42 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,642 | -1,005 | -358 | -358 | -358 | 0.2% | 1 | 0.18 | 0 | — | — |
| v3_carry_trend_mh | REJECTED | 999,510 | -1,005 | -358 | -490 | -490 | 0.2% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 999,642 | -1,005 | -358 | -358 | -358 | 0.2% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 999,932 | -211 | -68 | -68 | -68 | 0.1% | 2 | 0.29 | 1 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 999,642 | -1,005 | -358 | -358 | -358 | 0.2% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,002,372 | -1,742 | -1,683 | +2,372 | +2,372 | 0.4% | 4 | 0.56 | 4 | 25% | 0.18 |
| v5_carry_trend_daily_10p | REJECTED | 999,443 | -4,189 | -2,593 | -557 | -557 | 0.7% | 4 | 0.74 | 1 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 998,193 | -4,191 | -2,379 | -1,807 | -1,807 | 0.7% | 4 | 0.74 | 0 | — | — |
| v6_carry_trend_daily_mkt_7p | REJECTED | 997,634 | -2,967 | -1,546 | -2,366 | -2,366 | 0.4% | 3 | 0.56 | 1 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 999,086 | -2,969 | -795 | -914 | -914 | 0.4% | 3 | 0.56 | 1 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 999,086 | -2,969 | -795 | -914 | -914 | 0.4% | 3 | 0.56 | 1 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 999,277 | -10,984 | -6,507 | -723 | -723 | 1.8% | 5 | 1.90 | 0 | — | — |

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
