# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-06T19:56 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 870,882 | -4,704 | -4,817 | -120,152 | -129,118 | 14.3% | 2 | 3.27 | 164 | 40% | 0.60 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 997,787 | -4,831 | -16,032 | -16,749 | -2,213 | 4.0% | 0 | 0.00 | 33 | 52% | 0.97 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,033,114 | -1,880 | +8,631 | +26,368 | +33,114 | 0.7% | 2 | 2.97 | 33 | 58% | 1.49 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,000,002 | +0 | +7,122 | +328 | +2 | 0.4% | 0 | 0.00 | 7 | 43% | 1.00 |
| regime_switch_v1 | RESEARCH_ONLY | 969,701 | +0 | -7,763 | -19,043 | -30,299 | 4.8% | 0 | 0.00 | 44 | 30% | 0.72 |
| trend_donchian_v1 | RESEARCH_ONLY | 961,730 | +695 | +1,890 | -50,307 | -38,270 | 6.0% | 2 | 1.65 | 18 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 963,539 | +13,332 | +12,291 | -12,535 | -36,461 | 3.6% | 3 | 4.08 | 39 | 28% | 0.44 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,017,176 | +0 | -6,206 | +1,537 | +17,176 | 0.9% | 0 | 0.00 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -13,535 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,008,395 | +3,903 | -11,374 | +4,439 | +8,395 | 1.9% | 5 | 1.95 | 436 | 49% | 1.09 |
| v12_carry_timed | REJECTED | 1,008,532 | +11,337 | +8,532 | +8,532 | +8,532 | 0.0% | 6 | 2.57 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 998,254 | +3,496 | -1,746 | -1,746 | -1,746 | 0.3% | 3 | 1.18 | 0 | — | — |
| v13_ratemom | REJECTED | 1,005,926 | +12,100 | +5,926 | +5,926 | +5,926 | 0.1% | 6 | 2.70 | 0 | — | — |
| v14_term | REJECTED | 997,279 | +2,187 | -2,721 | -2,721 | -2,721 | 0.5% | 6 | 2.40 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,004,044 | +7,299 | +4,044 | +4,044 | +4,044 | 0.0% | 2 | 0.95 | 0 | — | — |
| v16_equity_rebal | REJECTED | 988,804 | -8,334 | -11,196 | -11,196 | -11,196 | 1.6% | 3 | 1.01 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 995,381 | -2,723 | -4,619 | -4,619 | -4,619 | 1.2% | 3 | 1.08 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 984,659 | +2,903 | -13,278 | -13,289 | -15,341 | 2.0% | 4 | 3.05 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 989,321 | -2,214 | -7,987 | -10,679 | -10,679 | 1.3% | 1 | 0.53 | 5 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 981,879 | +4,080 | +9,781 | -14,663 | -18,121 | 2.7% | 1 | 1.26 | 14 | 14% | 0.43 |
| v2_trend_carry | CHALLENGER | 1,001,662 | +3,178 | +1,564 | +1,662 | +1,662 | 0.0% | 3 | 0.45 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,002,924 | +3,139 | +1,048 | +2,924 | +2,924 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,001,181 | +5,696 | +4,509 | +1,181 | +1,181 | 0.4% | 4 | 2.47 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,902 | +2,396 | -196 | -98 | -98 | 0.1% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 998,707 | +1,173 | -1,702 | -1,161 | -1,293 | 0.2% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,002,105 | +3,178 | +1,564 | +2,105 | +2,105 | 0.0% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,000,074 | +2,398 | +1,188 | +74 | +74 | 0.1% | 4 | 0.56 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 999,728 | +1,173 | -813 | -272 | -272 | 0.2% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 998,121 | -1,203 | -2,972 | -6,254 | -1,879 | 0.8% | 2 | 0.33 | 20 | 35% | 0.55 |
| v5_carry_trend_daily_10p | REJECTED | 996,392 | +3,920 | +1,735 | -6,604 | -3,608 | 1.0% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 994,735 | +3,848 | +1,910 | -6,798 | -5,265 | 1.1% | 3 | 0.43 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 996,181 | +1,775 | -3,216 | -3,160 | -3,819 | 0.6% | 4 | 0.63 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 999,952 | +4,228 | +136 | +72 | -48 | 0.3% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 999,952 | +4,228 | +136 | +72 | -48 | 0.3% | 4 | 0.73 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,004,815 | +9,164 | +4,815 | +4,815 | +4,815 | 0.1% | 6 | 2.54 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 989,938 | -2,486 | -10,062 | -10,062 | -10,062 | 1.3% | 6 | 2.42 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,002,410 | +5,909 | +2,410 | +2,410 | +2,410 | 0.3% | 5 | 1.95 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,011,961 | +12,063 | +11,961 | +11,961 | +11,961 | 0.0% | 7 | 1.40 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,011,961 | +12,063 | +11,961 | +11,961 | +11,961 | 0.0% | 7 | 1.40 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 983,209 | +3,600 | -1,175 | -24,932 | -16,791 | 3.3% | 1 | 0.36 | 15 | 20% | 0.14 |

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
