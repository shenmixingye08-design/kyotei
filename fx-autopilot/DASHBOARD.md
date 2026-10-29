# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-10-29T10:15 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 877,929 | -6,333 | -29,126 | -130,992 | -122,071 | 13.6% | 1 | 0.20 | 134 | 38% | 0.56 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,018,654 | +0 | -5,224 | +21,654 | +18,654 | 2.0% | 0 | 0.00 | 25 | 60% | 1.40 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,022,041 | +0 | +2,818 | +23,116 | +22,041 | 1.8% | 0 | 0.00 | 25 | 56% | 1.41 |
| mtf_pullback_v1 | RESEARCH_ONLY | 985,623 | +0 | -4,679 | -9,357 | -14,377 | 1.8% | 0 | 0.00 | 5 | 20% | 0.25 |
| regime_switch_v1 | RESEARCH_ONLY | 975,427 | -4,983 | -21,479 | -17,275 | -24,573 | 4.2% | 0 | 0.00 | 36 | 28% | 0.71 |
| trend_donchian_v1 | RESEARCH_ONLY | 971,133 | -566 | -15,201 | -33,554 | -28,867 | 5.0% | 2 | 2.10 | 13 | 15% | 0.25 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 963,772 | -5,423 | -9,800 | -31,360 | -36,228 | 3.6% | 0 | 0.00 | 29 | 31% | 0.50 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,024,543 | -1,157 | +4,153 | +24,637 | +24,543 | 0.2% | 2 | 1.04 | 4 | 75% | 6.25 |
| v10_carry_vix | REJECTED | 993,074 | +0 | -156 | -9,221 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,027,080 | +2,873 | +16,059 | +23,333 | +27,080 | 0.1% | 5 | 2.19 | 341 | 55% | 1.39 |
| v12_carry_timed | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,000,783 | -193 | +8,620 | +783 | +783 | 0.4% | 2 | 1.65 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 997,529 | +280 | -928 | -2,471 | -2,471 | 0.4% | 1 | 0.67 | 1 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 974,500 | -6,355 | -1,061 | -19,390 | -25,500 | 3.4% | 0 | 0.00 | 12 | 8% | 0.25 |
| v2_trend_carry | CHALLENGER | 1,000,612 | -105 | +1,194 | +612 | +612 | 0.1% | 1 | 0.18 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,002,262 | -386 | +1,383 | +2,262 | +2,262 | 0.1% | 2 | 0.35 | 0 | — | — |
| v3_carry_only | REJECTED | 998,572 | +1,448 | +7,421 | -1,428 | -1,428 | 0.6% | 3 | 1.84 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,000,612 | -105 | +1,194 | +612 | +612 | 0.1% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,000,922 | -105 | +1,385 | +922 | +922 | 0.0% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,001,055 | -105 | +1,385 | +1,055 | +1,055 | 0.0% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 999,400 | -105 | +1,161 | -600 | -600 | 0.2% | 1 | 0.18 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,001,055 | -105 | +1,385 | +1,055 | +1,055 | 0.0% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,002,404 | +203 | +2,829 | +1,500 | +2,404 | 0.4% | 3 | 0.45 | 13 | 31% | 0.28 |
| v5_carry_trend_daily_10p | REJECTED | 997,379 | -1,994 | +3,669 | -3,548 | -2,621 | 0.9% | 4 | 0.74 | 1 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 995,124 | -1,251 | +2,660 | -4,876 | -4,876 | 1.0% | 4 | 0.58 | 1 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 999,777 | -367 | +1,421 | -223 | -223 | 0.2% | 2 | 0.35 | 2 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,000,196 | -367 | +1,421 | +196 | +196 | 0.3% | 2 | 0.35 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 1,000,196 | -367 | +1,421 | +196 | +196 | 0.3% | 2 | 0.35 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 984,589 | -605 | -972 | -17,484 | -15,411 | 3.2% | 5 | 1.99 | 6 | 0% | 0.00 |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.95 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -3.2% | 0.83 | -0.59 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -5.6% | 0.91 | -0.60 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.74 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -8.5% | 0.73 | -1.24 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.23 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.65 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.17 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -7.2% | 0.68 | -0.96 | 1.09 |
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
