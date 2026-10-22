# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-10-22T05:02 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 910,708 | -10,706 | -47,927 | -89,292 | -89,292 | 10.4% | 2 | 2.97 | 105 | 40% | 0.60 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | -532 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,033,721 | +0 | -5,262 | +33,721 | +33,721 | 0.6% | 0 | 0.00 | 22 | 68% | 2.06 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,028,019 | +1,236 | -4,419 | +28,019 | +28,019 | 1.2% | 2 | 2.94 | 19 | 58% | 1.69 |
| mtf_pullback_v1 | RESEARCH_ONLY | 990,302 | +0 | -5,107 | -9,698 | -9,698 | 1.3% | 0 | 0.00 | 4 | 25% | 0.33 |
| regime_switch_v1 | RESEARCH_ONLY | 1,001,886 | -1,763 | -4,500 | +1,886 | +1,886 | 1.6% | 0 | 0.00 | 28 | 36% | 1.03 |
| trend_donchian_v1 | RESEARCH_ONLY | 983,443 | +462 | -4,543 | -16,557 | -16,557 | 3.8% | 2 | 2.21 | 10 | 10% | 0.26 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 953,996 | +2,779 | +1,960 | -46,004 | -46,004 | 4.6% | 2 | 2.88 | 23 | 17% | 0.20 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,015,416 | -34 | +314 | +15,416 | +15,416 | 0.3% | 2 | 1.05 | 4 | 75% | 6.25 |
| v10_carry_vix | REJECTED | 994,936 | -3,701 | -5,724 | -5,064 | -5,064 | 1.7% | 6 | 2.50 | 1 | 100% | — |
| v11_intraday_region | REJECTED | 1,010,433 | +387 | -7,563 | +10,433 | +10,433 | 0.9% | 5 | 1.67 | 261 | 53% | 1.18 |
| v12_carry_timed | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 989,954 | -1,611 | -1,057 | -10,046 | -10,046 | 1.5% | 2 | 1.67 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 997,947 | -2,053 | -2,053 | -2,053 | -2,053 | 0.2% | 1 | 0.67 | 0 | — | — |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 975,561 | +0 | -3,861 | -24,439 | -24,439 | 3.3% | 0 | 0.00 | 11 | 9% | 0.26 |
| v2_trend_carry | CHALLENGER | 999,173 | -164 | -358 | -827 | -827 | 0.2% | 2 | 0.29 | 0 | — | — |
| v2_xpair_strength | REJECTED | 999,220 | -11 | -489 | -780 | -780 | 0.3% | 2 | 0.35 | 0 | — | — |
| v3_carry_only | REJECTED | 995,993 | -2,144 | -903 | -4,007 | -4,007 | 0.9% | 3 | 1.85 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,173 | -164 | -358 | -827 | -827 | 0.2% | 2 | 0.29 | 0 | — | — |
| v3_carry_trend_mh | REJECTED | 999,209 | -219 | -190 | -791 | -791 | 0.2% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 999,341 | -219 | -190 | -659 | -659 | 0.2% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 997,910 | -455 | -1,420 | -2,090 | -2,090 | 0.3% | 1 | 0.18 | 2 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 999,341 | -219 | -190 | -659 | -659 | 0.2% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,000,744 | -939 | -1,261 | +744 | +744 | 0.5% | 4 | 0.66 | 9 | 44% | 0.47 |
| v5_carry_trend_daily_10p | REJECTED | 994,222 | -1,397 | -5,747 | -5,778 | -5,778 | 1.2% | 4 | 0.74 | 1 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 992,969 | -1,395 | -5,755 | -7,031 | -7,031 | 1.2% | 4 | 0.74 | 0 | — | — |
| v6_carry_trend_daily_mkt_7p | REJECTED | 996,697 | +9 | -1,516 | -3,303 | -3,303 | 0.5% | 2 | 0.36 | 2 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 997,116 | +9 | -2,549 | -2,884 | -2,884 | 0.6% | 2 | 0.36 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 997,116 | +9 | -2,549 | -2,884 | -2,884 | 0.6% | 2 | 0.36 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 986,309 | -1,683 | -14,958 | -13,691 | -13,691 | 3.0% | 3 | 0.86 | 3 | 0% | 0.00 |

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
