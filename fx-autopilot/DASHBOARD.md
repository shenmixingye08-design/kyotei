# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-26T17:16 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -32,010 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,009,588 | +0 | +1,318 | +9,460 | +9,588 | 0.1% | 0 | 0.00 | 4 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 981,634 | +3,026 | -1,569 | -37,021 | -18,366 | 5.6% | 0 | 0.00 | 42 | 48% | 0.82 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,030,801 | +4,488 | +21,584 | +3,868 | +30,801 | 2.0% | 0 | 0.00 | 53 | 53% | 1.25 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,014,945 | +5,548 | +12,634 | +29,322 | +14,945 | 0.1% | 2 | 2.96 | 12 | 50% | 1.32 |
| regime_switch_v1 | RESEARCH_ONLY | 1,001,353 | -2,800 | +14,036 | +15,224 | +1,353 | 1.7% | 0 | 0.00 | 59 | 31% | 1.01 |
| trend_donchian_v1 | RESEARCH_ONLY | 984,818 | -4,864 | -13,796 | +11,297 | -15,182 | 3.7% | 2 | 1.25 | 22 | 9% | 0.13 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 948,209 | -3,775 | -8,158 | -16,688 | -51,791 | 5.2% | 2 | 2.88 | 50 | 28% | 0.61 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,044,639 | +277 | +3,234 | +20,294 | +44,639 | 1.2% | 2 | 1.65 | 7 | 71% | 10.47 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | +0 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,005,953 | +333 | +1,829 | -16,739 | +5,953 | 2.1% | 2 | 0.84 | 646 | 48% | 1.04 |
| v12_carry_timed | REJECTED | 1,019,580 | +5,527 | -2,271 | +19,580 | +19,580 | 0.8% | 5 | 2.21 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,007,900 | +2,314 | -2,453 | +7,900 | +7,900 | 0.7% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,029,099 | -876 | -3,470 | +29,099 | +29,099 | 1.8% | 5 | 2.30 | 1 | 0% | 0.00 |
| v14_term | REJECTED | 994,411 | +3,300 | -1,572 | -5,589 | -5,589 | 0.8% | 3 | 1.31 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,020,348 | +306 | +560 | +20,348 | +20,348 | 0.7% | 2 | 0.93 | 0 | — | — |
| v16_equity_rebal | REJECTED | 970,125 | +0 | -3,532 | -29,875 | -29,875 | 3.4% | 0 | 0.00 | 3 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 987,620 | +3,013 | -2,038 | -12,380 | -12,380 | 1.9% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,007,891 | -1,615 | +109 | +7,891 | +7,891 | 0.5% | 4 | 0.77 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,005,323 | +637 | +1,394 | +5,251 | +5,323 | 1.5% | 4 | 2.64 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 991,763 | +0 | +628 | -5,605 | -8,237 | 1.0% | 0 | 0.00 | 10 | 20% | 0.57 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 988,504 | +0 | -4,100 | +9,738 | -11,496 | 2.0% | 0 | 0.00 | 20 | 25% | 0.76 |
| v2_trend_carry | CHALLENGER | 1,009,361 | +257 | +395 | +8,886 | +9,361 | 0.2% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,010,936 | -973 | +1,321 | +8,740 | +10,936 | 0.3% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,010,253 | +6,798 | -3,673 | +12,413 | +10,253 | 0.7% | 4 | 2.45 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,004,580 | +1,169 | -157 | +4,105 | +4,580 | 0.1% | 4 | 0.65 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,120 | +1,167 | -530 | +302 | +1,120 | 0.1% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,008,309 | +1,169 | -157 | +7,358 | +8,309 | 0.1% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,004,670 | +1,171 | -159 | +5,408 | +4,670 | 0.1% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,005,471 | +247 | +120 | +4,521 | +5,471 | 0.3% | 3 | 0.44 | 3 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 997,814 | +239 | -3,090 | -4,260 | -2,186 | 0.8% | 3 | 0.44 | 32 | 34% | 0.43 |
| v5_carry_trend_daily_10p | REJECTED | 1,004,456 | +1,764 | -1,262 | +7,292 | +4,456 | 0.3% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,000,783 | +1,286 | -424 | +6,393 | +783 | 0.5% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,001,525 | +99 | +373 | +1,839 | +1,525 | 0.4% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,009,257 | -342 | +958 | +9,153 | +9,257 | 0.3% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,009,257 | -342 | +958 | +9,153 | +9,257 | 0.3% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,017,141 | +7,156 | -7,199 | +17,141 | +17,141 | 1.0% | 5 | 2.18 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 990,936 | +2,298 | -359 | -9,064 | -9,064 | 1.2% | 4 | 1.64 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,011,597 | +4,319 | -1,722 | +11,597 | +11,597 | 0.6% | 4 | 1.61 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,035,175 | +1,615 | -865 | +35,175 | +35,175 | 0.8% | 7 | 1.37 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,035,175 | +1,615 | -865 | +35,175 | +35,175 | 0.8% | 7 | 1.37 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 984,171 | +1,596 | -3,395 | -1,051 | -15,829 | 3.2% | 6 | 2.33 | 20 | 20% | 0.12 |

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
