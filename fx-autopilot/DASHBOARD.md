# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-10-28T05:50 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 884,053 | -15,667 | -37,361 | -128,454 | -115,947 | 13.0% | 2 | 3.25 | 126 | 39% | 0.57 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,018,654 | -3,099 | -15,067 | +18,654 | +18,654 | 2.0% | 0 | 0.00 | 25 | 60% | 1.40 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,022,701 | -4,729 | -4,082 | +22,701 | +22,701 | 1.7% | 1 | 2.41 | 24 | 58% | 1.57 |
| mtf_pullback_v1 | RESEARCH_ONLY | 985,623 | +0 | -4,679 | -14,530 | -14,377 | 1.8% | 0 | 0.00 | 5 | 20% | 0.25 |
| regime_switch_v1 | RESEARCH_ONLY | 982,168 | -12,649 | -21,481 | -18,096 | -17,832 | 3.6% | 0 | 0.00 | 34 | 29% | 0.77 |
| trend_donchian_v1 | RESEARCH_ONLY | 972,806 | -1,748 | -10,173 | -25,346 | -27,194 | 4.9% | 2 | 2.09 | 13 | 15% | 0.25 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 967,760 | +7,818 | +16,543 | -27,372 | -32,240 | 3.2% | 2 | 2.82 | 27 | 26% | 0.43 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,026,216 | +3,613 | +10,766 | +26,216 | +26,216 | 0.0% | 2 | 1.04 | 4 | 75% | 6.25 |
| v10_carry_vix | REJECTED | 993,074 | +0 | -5,563 | -6,926 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,026,114 | +5,145 | +16,068 | +26,298 | +26,114 | 0.1% | 5 | 1.93 | 321 | 56% | 1.34 |
| v12_carry_timed | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,001,858 | +5,171 | +10,293 | +1,858 | +1,858 | 0.3% | 2 | 1.65 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 997,633 | +1,206 | -2,367 | -2,367 | -2,367 | 0.4% | 1 | 0.67 | 1 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 981,723 | +6,162 | +6,162 | -18,277 | -18,277 | 2.7% | 1 | 1.79 | 11 | 9% | 0.26 |
| v2_trend_carry | CHALLENGER | 1,000,803 | +626 | +1,466 | +803 | +803 | 0.1% | 1 | 0.18 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,002,820 | +1,204 | +3,589 | +2,820 | +2,820 | 0.0% | 2 | 0.35 | 0 | — | — |
| v3_carry_only | REJECTED | 997,615 | +1,733 | -522 | -2,385 | -2,385 | 0.7% | 3 | 1.85 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,000,803 | +626 | +1,466 | +803 | +803 | 0.1% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,114 | +751 | +1,686 | +1,114 | +1,114 | 0.0% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,001,246 | +751 | +1,686 | +1,246 | +1,246 | 0.0% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 999,591 | +627 | +1,226 | -409 | -409 | 0.1% | 1 | 0.18 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,001,246 | +751 | +1,686 | +1,246 | +1,246 | 0.0% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,002,362 | +1,414 | +697 | +2,683 | +2,362 | 0.4% | 3 | 0.45 | 13 | 31% | 0.28 |
| v5_carry_trend_daily_10p | REJECTED | 999,367 | +3,603 | +3,747 | -633 | -633 | 0.7% | 4 | 0.74 | 1 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 996,316 | +2,647 | +1,951 | -3,684 | -3,684 | 0.9% | 4 | 0.58 | 1 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,000,316 | +1,210 | +3,627 | +316 | +316 | 0.2% | 2 | 0.35 | 2 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,000,735 | +1,210 | +3,627 | +735 | +735 | 0.3% | 2 | 0.35 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 1,000,735 | +1,210 | +3,627 | +735 | +735 | 0.3% | 2 | 0.35 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 985,281 | -839 | -2,711 | -14,719 | -14,719 | 3.1% | 1 | 0.18 | 6 | 0% | 0.00 |

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
