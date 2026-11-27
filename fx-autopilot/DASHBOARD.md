# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-27T12:38 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -24,244 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,009,588 | +0 | +1,318 | +9,460 | +9,588 | 0.1% | 0 | 0.00 | 4 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 980,387 | -1,246 | -2,816 | -38,267 | -19,613 | 5.7% | 1 | 1.84 | 42 | 48% | 0.82 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,030,801 | +0 | +24,016 | +8,760 | +30,801 | 2.0% | 0 | 0.00 | 53 | 53% | 1.25 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,013,881 | -1,999 | +6,871 | +28,258 | +13,881 | 0.2% | 2 | 2.96 | 12 | 50% | 1.32 |
| regime_switch_v1 | RESEARCH_ONLY | 1,001,353 | +0 | +2,220 | +22,480 | +1,353 | 1.7% | 0 | 0.00 | 59 | 31% | 1.01 |
| trend_donchian_v1 | RESEARCH_ONLY | 979,992 | -5,115 | -10,649 | +7,611 | -20,008 | 4.2% | 2 | 1.25 | 22 | 9% | 0.13 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 951,941 | +4,862 | -4,220 | -17,194 | -48,059 | 4.8% | 2 | 3.88 | 51 | 27% | 0.59 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,043,619 | -1,793 | -1,428 | +18,422 | +43,619 | 1.3% | 2 | 1.65 | 7 | 71% | 10.47 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | +0 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,004,444 | -1,646 | +1,761 | -18,815 | +4,444 | 2.3% | 5 | 2.02 | 656 | 48% | 1.02 |
| v12_carry_timed | REJECTED | 1,019,383 | +1,231 | -32 | +19,383 | +19,383 | 0.9% | 5 | 2.21 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,008,124 | +67 | -3,004 | +8,124 | +8,124 | 0.7% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,027,353 | -1,839 | -12,384 | +27,353 | +27,353 | 2.0% | 5 | 2.30 | 1 | 0% | 0.00 |
| v14_term | REJECTED | 993,149 | -140 | -2,402 | -6,851 | -6,851 | 1.0% | 3 | 1.31 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,019,892 | -851 | -1,374 | +19,892 | +19,892 | 0.7% | 2 | 0.94 | 0 | — | — |
| v16_equity_rebal | REJECTED | 970,125 | +0 | -2,787 | -29,875 | -29,875 | 3.4% | 0 | 0.00 | 3 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 988,650 | +1,408 | +3,864 | -11,350 | -11,350 | 1.8% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,006,371 | -1,827 | -2,234 | +6,371 | +6,371 | 0.6% | 4 | 0.77 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,005,276 | -666 | -2,569 | +3,888 | +5,276 | 1.5% | 4 | 2.64 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 991,763 | +0 | -113 | -6,060 | -8,237 | 1.0% | 0 | 0.00 | 10 | 20% | 0.57 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 987,796 | -708 | -8,671 | +7,460 | -12,204 | 2.1% | 1 | 1.94 | 20 | 25% | 0.76 |
| v2_trend_carry | CHALLENGER | 1,008,891 | -511 | +308 | +8,226 | +8,891 | 0.2% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,010,371 | -670 | -1,162 | +7,891 | +10,371 | 0.4% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,011,787 | +2,015 | +7,064 | +14,363 | +11,787 | 0.5% | 4 | 2.45 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,004,551 | +111 | +1,691 | +3,886 | +4,551 | 0.1% | 4 | 0.65 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,347 | +198 | +928 | +372 | +1,347 | 0.1% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,008,281 | +111 | +1,691 | +7,173 | +8,281 | 0.1% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,004,642 | +111 | +1,693 | +5,189 | +4,642 | 0.1% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,004,597 | -916 | -414 | +3,490 | +4,597 | 0.4% | 4 | 0.65 | 3 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 996,956 | -900 | -2,098 | -5,388 | -3,044 | 0.9% | 4 | 0.65 | 32 | 34% | 0.43 |
| v5_carry_trend_daily_10p | REJECTED | 1,004,359 | -76 | -838 | +5,906 | +4,359 | 0.4% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,000,574 | +58 | -395 | +4,825 | +574 | 0.5% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,001,340 | -421 | -848 | +1,364 | +1,340 | 0.4% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,008,780 | -575 | -519 | +8,385 | +8,780 | 0.3% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,008,780 | -575 | -519 | +8,385 | +8,780 | 0.3% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,018,000 | +1,850 | -2,953 | +18,000 | +18,000 | 0.9% | 5 | 2.18 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 992,155 | +1,433 | +1,981 | -7,845 | -7,845 | 1.1% | 4 | 1.64 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,011,658 | +600 | -161 | +11,658 | +11,658 | 0.6% | 4 | 1.61 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,033,055 | -1,862 | -3,655 | +33,055 | +33,055 | 1.0% | 7 | 1.37 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,033,055 | -1,862 | -3,655 | +33,055 | +33,055 | 1.0% | 7 | 1.37 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 982,372 | -1,434 | -8,351 | -2,770 | -17,628 | 3.4% | 6 | 2.34 | 20 | 20% | 0.12 |

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
