# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-14T03:17 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | -7,738 | -88,713 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +8,143 | +8,271 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 994,138 | -3,416 | -3,649 | -44,845 | -5,862 | 4.4% | 1 | 1.95 | 35 | 51% | 0.97 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,027,497 | -1,209 | -3,700 | +7,083 | +27,497 | 2.3% | 1 | 1.87 | 39 | 54% | 1.32 |
| mtf_pullback_v1 | RESEARCH_ONLY | 994,881 | +0 | -5,120 | -528 | -5,119 | 0.9% | 0 | 0.00 | 8 | 38% | 0.79 |
| regime_switch_v1 | RESEARCH_ONLY | 963,090 | +4,900 | -6,611 | -25,192 | -36,910 | 5.4% | 3 | 2.96 | 51 | 25% | 0.59 |
| trend_donchian_v1 | RESEARCH_ONLY | 983,047 | +4,131 | +21,298 | -15,212 | -16,953 | 3.9% | 3 | 2.87 | 19 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 958,241 | -2,624 | -3,923 | +5,524 | -41,759 | 4.2% | 1 | 1.10 | 46 | 28% | 0.57 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,024,838 | +2,227 | +7,662 | +7,897 | +24,838 | 0.2% | 1 | 0.43 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -13,567 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,009,559 | +2,012 | +1,972 | -6,577 | +9,559 | 1.8% | 0 | 0.00 | 516 | 48% | 1.08 |
| v12_carry_timed | REJECTED | 1,021,999 | -45 | +13,433 | +21,999 | +21,999 | 0.1% | 6 | 2.53 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,009,733 | +847 | +11,463 | +9,733 | +9,733 | 0.1% | 3 | 1.17 | 0 | — | — |
| v13_ratemom | REJECTED | 1,022,400 | +3,502 | +17,317 | +22,400 | +22,400 | 0.0% | 6 | 2.66 | 0 | — | — |
| v14_term | REJECTED | 995,366 | -1,767 | -1,250 | -4,634 | -4,634 | 0.7% | 4 | 1.64 | 2 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,014,406 | +2,235 | +10,365 | +14,406 | +14,406 | 0.0% | 2 | 0.94 | 0 | — | — |
| v16_equity_rebal | REJECTED | 978,164 | -4,924 | -10,479 | -21,836 | -21,836 | 2.6% | 2 | 0.70 | 1 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 995,553 | -3,383 | -323 | -4,447 | -4,447 | 1.2% | 3 | 1.08 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,003,850 | +1,628 | +4,062 | +3,850 | +3,850 | 0.0% | 2 | 0.39 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 994,749 | +4,680 | +11,039 | -6,118 | -5,251 | 1.0% | 3 | 2.24 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 985,056 | +2,061 | -4,250 | -14,944 | -14,944 | 1.7% | 2 | 1.36 | 8 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 983,067 | +5,575 | +1,220 | +3,646 | -16,933 | 2.6% | 1 | 1.11 | 15 | 13% | 0.39 |
| v2_trend_carry | CHALLENGER | 1,006,522 | +934 | +4,808 | +5,856 | +6,522 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,006,755 | +1,732 | +4,015 | +5,516 | +6,755 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,014,428 | -1,162 | +12,543 | +13,334 | +14,428 | 0.3% | 4 | 2.44 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,004,219 | +288 | +4,223 | +3,553 | +4,219 | 0.0% | 4 | 0.55 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,531 | -268 | +2,704 | +998 | +1,531 | 0.0% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,006,965 | +934 | +4,808 | +6,299 | +6,965 | 0.0% | 3 | 0.44 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,004,395 | +288 | +4,227 | +4,252 | +4,395 | 0.0% | 4 | 0.55 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,003,609 | +936 | +3,787 | +2,943 | +3,609 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 999,549 | +199 | +1,350 | -4,609 | -451 | 0.7% | 3 | 0.44 | 29 | 34% | 0.60 |
| v5_carry_trend_daily_10p | REJECTED | 1,003,664 | +1,358 | +7,352 | +86 | +3,664 | 0.3% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 999,477 | +828 | +4,860 | -2,853 | -523 | 0.6% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 999,393 | +399 | +3,243 | -1,266 | -607 | 0.2% | 4 | 0.62 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,005,305 | +1,600 | +5,423 | +3,193 | +5,305 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,005,305 | +1,600 | +5,423 | +3,193 | +5,305 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,024,324 | -190 | +19,156 | +24,324 | +24,324 | 0.2% | 6 | 2.49 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 993,914 | -503 | +4,147 | -6,086 | -6,086 | 0.9% | 5 | 1.97 | 1 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,014,089 | +1,066 | +11,873 | +14,089 | +14,089 | 0.1% | 5 | 1.93 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,027,744 | +3,350 | +16,035 | +27,744 | +27,744 | 0.0% | 7 | 1.38 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,027,744 | +3,350 | +16,035 | +27,744 | +27,744 | 0.0% | 7 | 1.38 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 980,114 | +3,829 | -2,375 | -30,135 | -19,886 | 3.6% | 6 | 2.24 | 19 | 21% | 0.13 |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.93 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -2.4% | 0.87 | -0.43 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -9.1% | 0.86 | -0.96 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.73 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -8.0% | 0.75 | -1.12 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.20 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.61 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.17 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -7.1% | 0.68 | -0.91 | 1.09 |
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
