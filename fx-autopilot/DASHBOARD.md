# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-10-20T14:28 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 932,311 | -9,200 | -16,494 | -67,689 | -67,689 | 8.3% | 2 | 2.33 | 95 | 42% | 0.67 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +128 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,033,721 | +0 | +7,986 | +33,721 | +33,721 | 0.6% | 0 | 0.00 | 22 | 68% | 2.06 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,027,868 | -9,419 | +12,233 | +27,868 | +27,868 | 1.2% | 1 | 1.85 | 18 | 61% | 1.95 |
| mtf_pullback_v1 | RESEARCH_ONLY | 990,302 | +0 | -5,107 | -9,698 | -9,698 | 1.3% | 0 | 0.00 | 4 | 25% | 0.33 |
| regime_switch_v1 | RESEARCH_ONLY | 1,001,254 | -4,827 | +27,848 | +1,254 | +1,254 | 1.7% | 0 | 0.00 | 27 | 33% | 1.02 |
| trend_donchian_v1 | RESEARCH_ONLY | 985,027 | +3,983 | -17,208 | -14,973 | -14,973 | 3.7% | 1 | 0.85 | 10 | 10% | 0.26 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 948,405 | -8,968 | -12,938 | -51,595 | -51,595 | 5.2% | 1 | 1.40 | 23 | 17% | 0.20 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,015,152 | -12 | -1,964 | +15,152 | +15,152 | 0.4% | 2 | 1.05 | 4 | 75% | 6.25 |
| v10_carry_vix | REJECTED | 995,392 | -2,277 | -11,947 | -4,608 | -4,608 | 1.6% | 5 | 1.96 | 1 | 100% | — |
| v11_intraday_region | REJECTED | 1,010,700 | -1,775 | -388 | +10,700 | +10,700 | 0.9% | 0 | 0.00 | 245 | 53% | 1.19 |
| v12_carry_timed | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 988,016 | -4,341 | -9,276 | -11,984 | -11,984 | 1.7% | 4 | 3.06 | 0 | — | — |
| v2_h4_ema | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 975,561 | +0 | -3,861 | -24,439 | -24,439 | 3.3% | 0 | 0.00 | 11 | 9% | 0.26 |
| v2_trend_carry | CHALLENGER | 999,435 | -187 | -565 | -565 | -565 | 0.2% | 1 | 0.18 | 0 | — | — |
| v2_xpair_strength | REJECTED | 999,131 | -3 | -869 | -869 | -869 | 0.3% | 2 | 0.35 | 0 | — | — |
| v3_carry_only | REJECTED | 997,804 | -1,517 | -2,196 | -2,196 | -2,196 | 0.7% | 2 | 1.42 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,435 | -187 | -565 | -565 | -565 | 0.2% | 1 | 0.18 | 0 | — | — |
| v3_carry_trend_mh | REJECTED | 999,303 | -187 | -565 | -697 | -697 | 0.2% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 999,435 | -187 | -565 | -565 | -565 | 0.2% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 998,481 | -363 | -967 | -1,519 | -1,519 | 0.3% | 2 | 0.29 | 1 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 999,435 | -187 | -565 | -565 | -565 | 0.2% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,001,347 | -971 | -3,153 | +1,347 | +1,347 | 0.5% | 3 | 0.45 | 8 | 38% | 0.38 |
| v5_carry_trend_daily_10p | REJECTED | 994,678 | -1,789 | -7,573 | -5,322 | -5,322 | 1.2% | 4 | 0.74 | 1 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 993,423 | -1,788 | -7,578 | -6,577 | -6,577 | 1.2% | 4 | 0.74 | 0 | — | — |
| v6_carry_trend_daily_mkt_7p | REJECTED | 996,583 | +3 | -2,122 | -3,417 | -3,417 | 0.5% | 2 | 0.36 | 2 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 996,835 | -999 | -3,046 | -3,165 | -3,165 | 0.6% | 3 | 0.57 | 1 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 996,835 | -999 | -3,046 | -3,165 | -3,165 | 0.6% | 3 | 0.57 | 1 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 986,541 | -3,288 | -19,622 | -13,459 | -13,459 | 3.0% | 3 | 1.18 | 2 | 0% | 0.00 |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.96 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -3.2% | 0.83 | -0.59 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -4.6% | 0.92 | -0.50 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.75 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -8.5% | 0.73 | -1.25 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.24 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.66 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.17 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -7.7% | 0.65 | -1.05 | 1.09 |
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
