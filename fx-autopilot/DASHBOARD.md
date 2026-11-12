# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-12T11:26 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | -8,444 | -88,159 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +8,143 | +8,271 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 997,555 | +0 | -5,063 | -28,180 | -2,445 | 4.1% | 0 | 0.00 | 35 | 51% | 0.97 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,033,044 | -12,449 | +825 | +19,385 | +33,044 | 1.8% | 1 | 1.86 | 38 | 55% | 1.37 |
| mtf_pullback_v1 | RESEARCH_ONLY | 994,881 | +0 | -5,120 | -528 | -5,119 | 0.9% | 0 | 0.00 | 8 | 38% | 0.79 |
| regime_switch_v1 | RESEARCH_ONLY | 957,362 | -8,474 | -12,339 | -16,044 | -42,638 | 6.0% | 2 | 2.32 | 49 | 27% | 0.61 |
| trend_donchian_v1 | RESEARCH_ONLY | 976,470 | +10,221 | +12,475 | -28,534 | -23,530 | 4.5% | 3 | 3.25 | 18 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 956,575 | +8,007 | +5,913 | -7,086 | -43,425 | 4.3% | 3 | 4.97 | 44 | 27% | 0.51 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,021,044 | +2,260 | +3,868 | +4,762 | +21,044 | 0.5% | 1 | 0.43 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -13,789 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,008,239 | -3,104 | +3,565 | -4,314 | +8,239 | 1.9% | 5 | 2.19 | 491 | 49% | 1.09 |
| v12_carry_timed | REJECTED | 1,018,998 | +5,404 | +17,565 | +18,998 | +18,998 | 0.4% | 6 | 2.54 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,006,125 | +2,622 | +6,156 | +6,125 | +6,125 | 0.3% | 3 | 1.17 | 0 | — | — |
| v13_ratemom | REJECTED | 1,015,019 | +2,815 | +24,386 | +15,019 | +15,019 | 0.3% | 6 | 2.68 | 0 | — | — |
| v14_term | REJECTED | 997,015 | -882 | -4,156 | -2,985 | -2,985 | 0.6% | 5 | 1.96 | 1 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,008,951 | +3,499 | +12,239 | +8,951 | +8,951 | 0.2% | 2 | 0.95 | 0 | — | — |
| v16_equity_rebal | REJECTED | 986,625 | -3,251 | -16,107 | -13,375 | -13,375 | 1.8% | 3 | 1.02 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 999,809 | +724 | -5,902 | -191 | -191 | 0.7% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,764 | +987 | +764 | +764 | +764 | 0.0% | 2 | 0.39 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 986,853 | +1,685 | -2,039 | -10,177 | -13,147 | 1.8% | 4 | 3.04 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 983,156 | +32 | -11,162 | -16,844 | -16,844 | 1.9% | 2 | 1.37 | 7 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 973,590 | -591 | -4,210 | -7,423 | -26,410 | 3.5% | 1 | 1.12 | 15 | 13% | 0.39 |
| v2_trend_carry | CHALLENGER | 1,004,290 | +1,842 | +6,231 | +4,290 | +4,290 | 0.1% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,003,537 | +1,267 | +5,545 | +3,537 | +3,537 | 0.1% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,013,177 | +5,778 | +11,178 | +13,177 | +13,177 | 0.3% | 4 | 2.44 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,002,875 | +1,673 | +4,277 | +2,875 | +2,875 | 0.1% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,137 | +1,104 | +1,443 | +1,269 | +1,137 | 0.1% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,004,732 | +1,842 | +6,231 | +4,732 | +4,732 | 0.1% | 3 | 0.44 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,003,051 | +1,674 | +4,281 | +3,557 | +3,051 | 0.1% | 4 | 0.55 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,001,828 | +1,273 | +1,114 | +1,828 | +1,828 | 0.1% | 2 | 0.33 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 998,316 | +1,253 | -3,182 | -6,036 | -1,684 | 0.8% | 4 | 0.55 | 27 | 33% | 0.59 |
| v5_carry_trend_daily_10p | REJECTED | 1,000,359 | +2,193 | +7,342 | -2,442 | +359 | 0.6% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 997,274 | +1,923 | +7,233 | -4,281 | -2,726 | 0.8% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 997,915 | +1,123 | +2,073 | -1,305 | -2,085 | 0.4% | 4 | 0.62 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,001,993 | +1,851 | +6,366 | +2,113 | +1,993 | 0.1% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,001,993 | +1,851 | +6,366 | +2,113 | +1,993 | 0.1% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,021,239 | +4,904 | +18,987 | +21,239 | +21,239 | 0.4% | 6 | 2.50 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 992,413 | -161 | -10,427 | -7,587 | -7,587 | 1.1% | 5 | 1.97 | 1 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,009,629 | +4,268 | +7,853 | +9,629 | +9,629 | 0.3% | 5 | 1.94 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,020,449 | +4,944 | +23,407 | +20,449 | +20,449 | 0.2% | 7 | 1.39 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,020,449 | +4,944 | +23,407 | +20,449 | +20,449 | 0.2% | 7 | 1.39 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 970,680 | -1,541 | -9,649 | -36,675 | -29,320 | 4.6% | 6 | 2.27 | 18 | 17% | 0.11 |

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
