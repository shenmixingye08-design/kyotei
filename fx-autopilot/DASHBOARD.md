# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-24T10:17 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -43,153 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +0 | +8,143 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 975,576 | -7,626 | -17,354 | -48,301 | -24,424 | 6.2% | 0 | 0.00 | 40 | 45% | 0.76 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,017,984 | +5,706 | +913 | -1,726 | +17,984 | 3.3% | 3 | 2.84 | 48 | 50% | 1.12 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,014,303 | +7,293 | +19,422 | +24,001 | +14,303 | 0.0% | 0 | 0.00 | 11 | 55% | 1.59 |
| regime_switch_v1 | RESEARCH_ONLY | 1,011,434 | +10,679 | +39,389 | +13,406 | +11,434 | 0.7% | 3 | 2.97 | 55 | 29% | 0.74 |
| trend_donchian_v1 | RESEARCH_ONLY | 990,575 | +5,148 | +7,885 | +10,277 | -9,425 | 3.1% | 3 | 1.87 | 21 | 10% | 0.14 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 951,983 | +0 | -10,668 | -17,384 | -48,017 | 4.8% | 0 | 0.00 | 50 | 28% | 0.61 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,052,603 | +12,254 | +21,907 | +30,769 | +52,603 | 0.5% | 2 | 1.64 | 7 | 71% | 10.47 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | +0 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,004,947 | +1,834 | -1,462 | -12,781 | +4,947 | 2.2% | 5 | 2.17 | 611 | 49% | 1.06 |
| v12_carry_timed | REJECTED | 1,026,975 | +5,187 | +8,333 | +26,975 | +26,975 | 0.1% | 5 | 2.20 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,013,096 | +3,755 | +5,703 | +13,096 | +13,096 | 0.2% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,040,357 | +5,692 | +11,764 | +40,357 | +40,357 | 0.7% | 5 | 2.27 | 1 | 0% | 0.00 |
| v14_term | REJECTED | 1,000,042 | +2,782 | +6,719 | +42 | +42 | 0.3% | 3 | 1.30 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,024,696 | +4,678 | +8,738 | +24,696 | +24,696 | 0.3% | 2 | 0.93 | 0 | — | — |
| v16_equity_rebal | REJECTED | 970,125 | -1,579 | -3,701 | -29,875 | -29,875 | 3.4% | 0 | 0.00 | 3 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 986,888 | +138 | -1,717 | -13,112 | -13,112 | 2.0% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,010,715 | +4,214 | +5,325 | +10,715 | +10,715 | 0.2% | 4 | 0.77 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,015,015 | +13,142 | +16,938 | +19,573 | +15,015 | 0.6% | 4 | 2.61 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 993,902 | +3,869 | +3,759 | -6,516 | -6,098 | 0.8% | 1 | 0.64 | 9 | 11% | 0.12 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 993,813 | +6,679 | +3,429 | +18,252 | -6,187 | 1.5% | 1 | 1.23 | 19 | 26% | 0.80 |
| v2_trend_carry | CHALLENGER | 1,010,290 | +1,788 | +3,417 | +10,917 | +10,290 | 0.1% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,012,755 | +2,536 | +4,084 | +11,395 | +12,755 | 0.1% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,011,111 | +3,263 | +3,450 | +19,936 | +11,111 | 0.6% | 4 | 2.45 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,005,095 | +1,284 | +1,613 | +5,721 | +5,095 | 0.0% | 4 | 0.65 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,002,169 | +1,469 | +1,984 | +2,350 | +2,169 | 0.0% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,008,824 | +1,284 | +1,613 | +8,873 | +8,824 | 0.0% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,005,186 | +1,285 | +1,614 | +6,665 | +5,186 | 0.0% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,007,375 | +2,397 | +3,903 | +7,424 | +7,375 | 0.1% | 4 | 0.65 | 2 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 999,645 | -351 | -172 | +321 | -355 | 0.6% | 4 | 0.65 | 30 | 33% | 0.46 |
| v5_carry_trend_daily_10p | REJECTED | 1,006,996 | +1,992 | +3,409 | +12,852 | +6,996 | 0.1% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,003,044 | +1,728 | +3,283 | +10,631 | +3,044 | 0.2% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,004,163 | +2,760 | +4,976 | +5,319 | +4,163 | 0.2% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,011,068 | +2,085 | +4,389 | +11,806 | +11,068 | 0.1% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,011,068 | +2,742 | +4,418 | +11,806 | +11,068 | 0.1% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,025,929 | +4,885 | +6,543 | +25,929 | +25,929 | 0.1% | 5 | 2.16 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 994,470 | +4,171 | +4,237 | -5,530 | -5,530 | 0.9% | 4 | 1.63 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,017,311 | +4,734 | +6,469 | +17,311 | +17,311 | 0.1% | 4 | 1.60 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,041,249 | +5,613 | +10,603 | +41,249 | +41,249 | 0.3% | 7 | 1.36 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,041,249 | +5,613 | +10,603 | +41,249 | +41,249 | 0.3% | 7 | 1.36 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 996,196 | +8,514 | +11,909 | +10,265 | -3,804 | 2.1% | 6 | 2.30 | 20 | 20% | 0.12 |

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
