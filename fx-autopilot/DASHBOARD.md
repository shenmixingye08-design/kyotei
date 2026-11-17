# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-17T04:03 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | -17,021 | -88,857 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +4,645 | +8,143 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 992,931 | +0 | -4,856 | -40,791 | -7,069 | 4.5% | 0 | 0.00 | 36 | 50% | 0.92 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,020,641 | -7,337 | -25,212 | -11,252 | +20,641 | 3.0% | 1 | 1.72 | 42 | 52% | 1.21 |
| mtf_pullback_v1 | RESEARCH_ONLY | 994,881 | +0 | +0 | +4,579 | -5,119 | 0.9% | 0 | 0.00 | 8 | 38% | 0.79 |
| regime_switch_v1 | RESEARCH_ONLY | 971,214 | +6,663 | +1,513 | -33,208 | -28,786 | 4.6% | 3 | 2.94 | 51 | 25% | 0.59 |
| trend_donchian_v1 | RESEARCH_ONLY | 984,960 | +672 | +26,768 | +219 | -15,040 | 3.7% | 3 | 2.86 | 19 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 960,354 | +1,634 | +11,684 | +1,135 | -39,646 | 4.0% | 1 | 1.10 | 46 | 28% | 0.57 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,030,398 | +5,203 | +14,897 | +14,252 | +30,398 | 0.2% | 3 | 2.09 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -3,414 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,007,500 | -1,945 | +1,268 | -4,529 | +7,500 | 2.0% | 5 | 1.75 | 531 | 49% | 1.06 |
| v12_carry_timed | REJECTED | 1,022,911 | +119 | +21,049 | +22,911 | +22,911 | 0.1% | 6 | 2.53 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,009,028 | -935 | +12,611 | +9,028 | +9,028 | 0.1% | 3 | 1.17 | 0 | — | — |
| v13_ratemom | REJECTED | 1,026,650 | +3,233 | +25,218 | +26,650 | +26,650 | 0.2% | 6 | 2.65 | 0 | — | — |
| v14_term | REJECTED | 996,832 | +862 | +1,047 | -3,168 | -3,168 | 0.6% | 4 | 1.64 | 2 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,016,220 | +1,465 | +18,496 | +16,220 | +16,220 | 0.1% | 2 | 0.94 | 0 | — | — |
| v16_equity_rebal | REJECTED | 973,924 | -4,163 | -22,728 | -26,076 | -26,076 | 3.0% | 2 | 0.70 | 1 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 991,355 | -4,130 | -7,156 | -8,645 | -8,645 | 1.6% | 3 | 1.08 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,005,189 | +1,108 | +7,047 | +5,189 | +5,189 | 0.0% | 2 | 0.39 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 997,767 | +2,550 | +17,747 | +12,361 | -2,233 | 0.7% | 3 | 2.24 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 988,853 | +3,473 | +5,231 | -11,147 | -11,147 | 1.3% | 2 | 1.36 | 8 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 988,806 | +4,844 | +14,625 | +13,245 | -11,194 | 2.0% | 2 | 1.99 | 15 | 13% | 0.39 |
| v2_trend_carry | CHALLENGER | 1,007,070 | +363 | +7,758 | +7,720 | +7,070 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,008,211 | +1,305 | +8,163 | +9,217 | +8,211 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,011,554 | -3,369 | +13,158 | +14,126 | +11,554 | 0.6% | 4 | 2.45 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,004,062 | -281 | +5,883 | +4,712 | +4,062 | 0.0% | 4 | 0.55 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,000,870 | -695 | +3,034 | +1,652 | +870 | 0.1% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,007,512 | +363 | +7,758 | +8,163 | +7,512 | 0.0% | 3 | 0.44 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,004,237 | -282 | +5,888 | +5,011 | +4,237 | 0.0% | 4 | 0.55 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,004,174 | +381 | +5,927 | +4,824 | +4,174 | 0.0% | 4 | 0.65 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 1,000,106 | +373 | +2,050 | -2,245 | +106 | 0.6% | 3 | 0.44 | 29 | 34% | 0.60 |
| v5_carry_trend_daily_10p | REJECTED | 1,004,539 | +600 | +11,197 | +7,377 | +4,539 | 0.2% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,000,558 | +811 | +8,571 | +4,648 | +558 | 0.5% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 999,252 | -184 | +4,776 | +3,026 | -748 | 0.3% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,006,488 | +990 | +10,257 | +8,810 | +6,488 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,006,488 | +990 | +10,257 | +8,810 | +6,488 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,023,262 | -1,903 | +19,431 | +23,262 | +23,262 | 0.3% | 6 | 2.49 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 991,955 | -2,068 | +703 | -8,045 | -8,045 | 1.1% | 5 | 1.97 | 1 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,014,283 | -275 | +17,675 | +14,283 | +14,283 | 0.1% | 5 | 1.93 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,031,506 | +2,913 | +27,369 | +31,506 | +31,506 | 0.0% | 7 | 1.38 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,031,506 | +2,913 | +27,369 | +31,506 | +31,506 | 0.0% | 7 | 1.38 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 985,791 | +4,705 | +13,625 | -6,548 | -14,209 | 3.1% | 6 | 2.23 | 19 | 21% | 0.13 |

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
