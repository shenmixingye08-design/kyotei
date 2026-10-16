# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-10-16T11:33 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 948,082 | -13,537 | -24,362 | -51,918 | -51,918 | 6.7% | 0 | 0.00 | 79 | 41% | 0.68 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | -426 | +128 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,033,721 | -5,262 | +10,977 | +33,721 | +33,721 | 0.6% | 0 | 0.00 | 22 | 68% | 2.06 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,029,881 | -4,533 | +21,362 | +29,881 | +29,881 | 0.8% | 1 | 1.20 | 16 | 62% | 2.17 |
| mtf_pullback_v1 | RESEARCH_ONLY | 990,302 | -5,107 | -9,371 | -9,698 | -9,698 | 1.3% | 0 | 0.00 | 4 | 25% | 0.33 |
| regime_switch_v1 | RESEARCH_ONLY | 998,753 | -5,136 | +20,199 | -1,247 | -1,247 | 1.6% | 2 | 3.00 | 22 | 27% | 1.02 |
| trend_donchian_v1 | RESEARCH_ONLY | 986,568 | -3,524 | -22,844 | -13,432 | -13,432 | 3.5% | 2 | 1.75 | 9 | 11% | 0.32 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 962,478 | +5,737 | -2,096 | -37,522 | -37,522 | 3.8% | 2 | 2.81 | 18 | 17% | 0.15 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,015,802 | +463 | +1,412 | +15,802 | +15,802 | 0.3% | 1 | 0.47 | 3 | 67% | 5.81 |
| v10_carry_vix | REJECTED | 997,584 | -2,666 | -8,501 | -2,416 | -2,416 | 1.4% | 6 | 2.31 | 0 | — | — |
| v11_intraday_region | REJECTED | 1,010,451 | -6,843 | +1,842 | +10,451 | +10,451 | 0.9% | 5 | 1.81 | 210 | 56% | 1.33 |
| v12_carry_timed | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 986,201 | -2,003 | -12,202 | -13,799 | -13,799 | 1.9% | 4 | 3.06 | 0 | — | — |
| v2_h4_ema | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 975,561 | -6,733 | -13,411 | -24,439 | -24,439 | 3.3% | 0 | 0.00 | 11 | 9% | 0.26 |
| v2_trend_carry | CHALLENGER | 999,063 | -701 | -937 | -937 | -937 | 0.2% | 1 | 0.18 | 0 | — | — |
| v2_xpair_strength | REJECTED | 998,505 | -1,581 | -1,495 | -1,495 | -1,495 | 0.3% | 2 | 0.36 | 0 | — | — |
| v3_carry_only | REJECTED | 996,728 | -905 | -3,272 | -3,272 | -3,272 | 0.8% | 2 | 1.42 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,063 | -701 | -937 | -937 | -937 | 0.2% | 1 | 0.18 | 0 | — | — |
| v3_carry_trend_mh | REJECTED | 998,931 | -701 | -937 | -1,069 | -1,069 | 0.2% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 999,063 | -701 | -937 | -937 | -937 | 0.2% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 998,713 | -1,349 | -1,018 | -1,287 | -1,287 | 0.2% | 2 | 0.29 | 1 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 999,063 | -701 | -937 | -937 | -937 | 0.2% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,001,716 | -657 | -2,693 | +1,716 | +1,716 | 0.4% | 4 | 0.56 | 4 | 25% | 0.18 |
| v5_carry_trend_daily_10p | REJECTED | 996,755 | -4,042 | -5,558 | -3,245 | -3,245 | 1.0% | 4 | 0.74 | 1 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 995,503 | -4,048 | -5,295 | -4,497 | -4,497 | 1.0% | 4 | 0.74 | 0 | — | — |
| v6_carry_trend_daily_mkt_7p | REJECTED | 995,610 | -2,969 | -3,646 | -4,390 | -4,390 | 0.6% | 3 | 0.57 | 1 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 997,061 | -2,968 | -2,819 | -2,939 | -2,939 | 0.6% | 3 | 0.57 | 1 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 997,061 | -2,968 | -2,819 | -2,939 | -2,939 | 0.6% | 3 | 0.57 | 1 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 991,193 | -12,040 | -15,168 | -8,807 | -8,807 | 2.6% | 5 | 1.91 | 0 | — | — |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.96 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -3.2% | 0.83 | -0.60 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -5.6% | 0.90 | -0.63 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.75 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -7.6% | 0.75 | -1.13 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.25 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.67 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.18 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -7.7% | 0.65 | -1.06 | 1.09 |
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
