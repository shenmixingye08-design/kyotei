# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-20T02:33 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -63,374 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +0 | +8,143 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 983,203 | -6,940 | -14,352 | -50,518 | -16,797 | 5.4% | 0 | 0.00 | 38 | 47% | 0.82 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,005,745 | -4,973 | -23,498 | -21,216 | +5,745 | 4.4% | 0 | 0.00 | 45 | 49% | 1.05 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,006,284 | +6,645 | +11,403 | +15,981 | +6,284 | 0.0% | 1 | 2.45 | 9 | 44% | 0.99 |
| regime_switch_v1 | RESEARCH_ONLY | 998,791 | +12,970 | +39,878 | -5,083 | -1,209 | 1.9% | 3 | 4.50 | 52 | 27% | 0.62 |
| trend_donchian_v1 | RESEARCH_ONLY | 997,362 | +3,168 | +17,124 | +13,498 | -2,638 | 2.5% | 3 | 2.83 | 19 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 952,135 | -2,047 | -9,280 | +112 | -47,865 | 4.8% | 0 | 0.00 | 49 | 29% | 0.61 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,045,866 | +6,045 | +22,647 | +30,946 | +45,866 | 0.0% | 3 | 2.06 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -6,333 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 999,419 | -11,237 | -8,543 | -11,007 | -581 | 2.8% | 5 | 1.76 | 576 | 48% | 1.02 |
| v12_carry_timed | REJECTED | 1,022,251 | -965 | +329 | +22,251 | +22,251 | 0.3% | 5 | 2.21 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,011,477 | +533 | +3,074 | +11,477 | +11,477 | 0.0% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,037,800 | +4,078 | +19,031 | +37,800 | +37,800 | 0.0% | 6 | 2.62 | 0 | — | — |
| v14_term | REJECTED | 997,614 | +690 | +376 | -2,386 | -2,386 | 0.5% | 3 | 1.31 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,021,537 | +2,206 | +9,479 | +21,537 | +21,537 | 0.0% | 2 | 0.93 | 0 | — | — |
| v16_equity_rebal | REJECTED | 972,391 | -664 | -9,732 | -27,609 | -27,609 | 3.2% | 1 | 0.36 | 2 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 986,748 | -2,150 | -11,749 | -13,252 | -13,252 | 2.0% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,008,896 | +1,238 | +6,472 | +8,896 | +8,896 | 0.0% | 3 | 0.60 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,007,502 | +2,896 | +17,794 | +15,395 | +7,502 | 0.0% | 4 | 2.63 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 992,514 | -367 | +9,228 | -7,486 | -7,486 | 0.9% | 1 | 0.64 | 9 | 11% | 0.12 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 994,926 | -946 | +15,915 | +19,366 | -5,074 | 1.4% | 1 | 1.05 | 18 | 22% | 0.74 |
| v2_trend_carry | CHALLENGER | 1,009,118 | +500 | +3,449 | +9,833 | +9,118 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,010,924 | +740 | +5,846 | +11,870 | +10,924 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,009,322 | -2,225 | -5,784 | +10,101 | +9,322 | 0.8% | 4 | 2.45 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,003,866 | -501 | -19 | +4,580 | +3,866 | 0.1% | 4 | 0.65 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,220 | +13 | -380 | +1,777 | +1,220 | 0.1% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,007,595 | -501 | +1,482 | +8,020 | +7,595 | 0.1% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,003,956 | -501 | -105 | +5,644 | +3,956 | 0.1% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,005,741 | +733 | +2,987 | +6,166 | +5,741 | 0.0% | 4 | 0.65 | 2 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 1,000,044 | -499 | +894 | -2,032 | +44 | 0.6% | 4 | 0.65 | 29 | 34% | 0.60 |
| v5_carry_trend_daily_10p | REJECTED | 1,006,038 | +303 | +3,581 | +10,277 | +6,038 | 0.1% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,001,683 | +262 | +2,949 | +7,179 | +1,683 | 0.4% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,002,218 | +1,162 | +3,417 | +5,707 | +2,218 | 0.0% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,009,197 | +682 | +5,405 | +12,266 | +9,197 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,009,197 | +682 | +5,405 | +12,266 | +9,197 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,023,784 | -1,442 | -347 | +23,784 | +23,784 | 0.3% | 5 | 2.17 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 990,704 | -1,418 | -2,979 | -9,296 | -9,296 | 1.3% | 4 | 1.64 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,013,627 | -842 | +737 | +13,627 | +13,627 | 0.2% | 4 | 1.60 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,038,325 | +2,353 | +13,185 | +38,325 | +38,325 | 0.0% | 7 | 1.37 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,038,325 | +2,353 | +13,185 | +38,325 | +38,325 | 0.0% | 7 | 1.37 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 991,429 | +1,475 | +14,700 | +3,221 | -8,571 | 2.5% | 6 | 2.22 | 19 | 21% | 0.13 |

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
