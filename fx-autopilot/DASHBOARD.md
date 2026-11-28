# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-28T05:13 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -20,808 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,009,588 | +0 | +1,318 | +9,460 | +9,588 | 0.1% | 0 | 0.00 | 4 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 986,405 | +4,772 | +3,202 | -32,249 | -13,595 | 5.1% | 0 | 0.00 | 43 | 49% | 0.87 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,030,801 | +0 | +31,518 | +8,760 | +30,801 | 2.0% | 0 | 0.00 | 53 | 53% | 1.25 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,018,926 | +4,405 | +11,916 | +33,303 | +18,926 | 0.1% | 1 | 1.23 | 13 | 54% | 1.59 |
| regime_switch_v1 | RESEARCH_ONLY | 1,001,353 | +0 | -572 | +25,926 | +1,353 | 1.7% | 0 | 0.00 | 59 | 31% | 1.01 |
| trend_donchian_v1 | RESEARCH_ONLY | 983,451 | -740 | -10,958 | +9,037 | -16,549 | 3.8% | 2 | 1.25 | 22 | 9% | 0.13 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 949,965 | +2,720 | -8,419 | -14,060 | -50,035 | 5.0% | 2 | 3.88 | 51 | 27% | 0.59 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,047,894 | +3,000 | +1,248 | +24,853 | +47,894 | 0.9% | 2 | 1.64 | 7 | 71% | 10.47 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | +0 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,004,124 | -2,026 | +4,358 | -23,244 | +4,124 | 2.3% | 0 | 0.00 | 666 | 48% | 1.02 |
| v12_carry_timed | REJECTED | 1,021,960 | +2,895 | +3,291 | +21,960 | +21,960 | 0.6% | 5 | 2.21 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,010,080 | +2,046 | +454 | +10,080 | +10,080 | 0.5% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,031,088 | +1,668 | -8,668 | +31,088 | +31,088 | 1.6% | 5 | 2.29 | 1 | 0% | 0.00 |
| v14_term | REJECTED | 995,021 | +899 | -1,484 | -4,979 | -4,979 | 0.8% | 3 | 1.31 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,022,292 | +1,794 | +1,413 | +22,292 | +22,292 | 0.5% | 2 | 0.93 | 0 | — | — |
| v16_equity_rebal | REJECTED | 970,125 | +0 | -1,539 | -29,875 | -29,875 | 3.4% | 0 | 0.00 | 3 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 988,250 | +1,052 | +5,230 | -11,750 | -11,750 | 1.9% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,008,204 | +338 | -1,290 | +8,204 | +8,204 | 0.4% | 4 | 0.77 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,010,220 | +4,611 | +3,719 | +8,719 | +10,220 | 1.0% | 4 | 2.63 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 991,763 | +0 | -316 | -7,764 | -8,237 | 1.0% | 0 | 0.00 | 10 | 20% | 0.57 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 989,659 | +1,155 | -8,154 | +15,160 | -10,341 | 1.9% | 1 | 1.93 | 20 | 25% | 0.76 |
| v2_trend_carry | CHALLENGER | 1,009,831 | +589 | +1,172 | +9,540 | +9,831 | 0.1% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,011,407 | +449 | -635 | +9,646 | +11,407 | 0.3% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,013,269 | +3,823 | +12,231 | +16,056 | +13,269 | 0.4% | 4 | 2.44 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,005,147 | +829 | +2,791 | +4,857 | +5,147 | 0.0% | 4 | 0.65 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,002,047 | +1,001 | +2,321 | +1,446 | +2,047 | 0.0% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,008,876 | +829 | +2,791 | +8,143 | +8,876 | 0.0% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,005,238 | +830 | +2,794 | +6,160 | +5,238 | 0.0% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,006,020 | +701 | +857 | +5,287 | +6,020 | 0.2% | 4 | 0.65 | 3 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 998,376 | +680 | -182 | -3,706 | -1,624 | 0.8% | 4 | 0.65 | 32 | 34% | 0.43 |
| v5_carry_trend_daily_10p | REJECTED | 1,005,559 | +1,126 | +1,046 | +8,969 | +5,559 | 0.2% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,001,588 | +883 | +701 | +7,225 | +1,588 | 0.4% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,002,711 | +1,094 | +771 | +3,434 | +2,711 | 0.3% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,009,972 | +747 | +450 | +10,277 | +9,972 | 0.2% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,009,972 | +747 | +450 | +10,277 | +9,972 | 0.2% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,019,912 | +3,157 | +1,811 | +19,912 | +19,912 | 0.7% | 5 | 2.17 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 993,681 | +2,913 | +5,501 | -6,319 | -6,319 | 1.0% | 4 | 1.63 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,014,119 | +2,756 | +3,853 | +14,119 | +14,119 | 0.4% | 4 | 1.60 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,035,858 | +908 | -1,816 | +35,858 | +35,858 | 0.8% | 7 | 1.37 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,035,858 | +908 | -1,816 | +35,858 | +35,858 | 0.8% | 7 | 1.37 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 987,018 | +2,619 | -3,457 | +2,800 | -12,982 | 3.0% | 6 | 2.32 | 20 | 20% | 0.12 |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.92 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -2.3% | 0.88 | -0.40 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -9.8% | 0.85 | -1.02 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.72 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -5.9% | 0.82 | -0.78 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.19 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.59 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.17 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -5.4% | 0.76 | -0.66 | 1.09 |
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
