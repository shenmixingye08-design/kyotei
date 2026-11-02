# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-02T06:21 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 876,256 | +2,748 | -31,670 | -128,622 | -123,744 | 13.8% | 0 | 0.00 | 142 | 38% | 0.57 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,013,819 | +0 | -10,059 | +13,933 | +13,819 | 2.5% | 0 | 0.00 | 26 | 58% | 1.27 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,023,972 | -602 | -1,540 | +14,463 | +23,972 | 1.6% | 1 | 1.65 | 25 | 56% | 1.41 |
| mtf_pullback_v1 | RESEARCH_ONLY | 992,880 | +0 | +5,562 | -143 | -7,120 | 1.1% | 0 | 0.00 | 6 | 33% | 0.63 |
| regime_switch_v1 | RESEARCH_ONLY | 979,184 | +542 | -15,988 | -16,541 | -20,816 | 3.8% | 1 | 1.60 | 37 | 27% | 0.68 |
| trend_donchian_v1 | RESEARCH_ONLY | 960,093 | +627 | -17,992 | -45,244 | -39,907 | 6.1% | 1 | 0.88 | 16 | 12% | 0.19 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 943,479 | -6,113 | -17,448 | -37,357 | -56,521 | 5.7% | 1 | 1.49 | 33 | 27% | 0.41 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,020,471 | -2,801 | +713 | +12,476 | +20,471 | 0.6% | 2 | 1.04 | 4 | 75% | 6.25 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -9,298 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,022,599 | +2,854 | +3,187 | +15,348 | +22,599 | 0.5% | 5 | 1.93 | 366 | 52% | 1.24 |
| v12_carry_timed | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 995,650 | -2,782 | +2,051 | +875 | -4,350 | 0.9% | 2 | 1.66 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 996,412 | -947 | -2,550 | -3,588 | -3,588 | 0.6% | 1 | 0.67 | 1 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 972,545 | +1,100 | -3,016 | -22,301 | -27,455 | 3.6% | 1 | 1.52 | 12 | 8% | 0.25 |
| v2_trend_carry | CHALLENGER | 999,847 | -337 | +525 | -153 | -153 | 0.1% | 1 | 0.18 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,000,905 | -934 | +237 | +905 | +905 | 0.2% | 2 | 0.35 | 0 | — | — |
| v3_carry_only | REJECTED | 998,791 | +1,099 | +6,335 | -1,209 | -1,209 | 0.6% | 3 | 1.84 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,847 | -337 | +525 | -153 | -153 | 0.1% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,000,157 | -337 | +554 | +744 | +157 | 0.1% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,000,290 | -337 | +554 | +290 | +290 | 0.1% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 998,635 | -337 | +330 | -1,365 | -1,365 | 0.2% | 1 | 0.18 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,000,290 | -337 | +554 | +290 | +290 | 0.1% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,001,412 | +7 | +1,988 | -1,615 | +1,412 | 0.5% | 4 | 0.66 | 14 | 36% | 0.30 |
| v5_carry_trend_daily_10p | REJECTED | 994,645 | -367 | +623 | -7,007 | -5,355 | 1.2% | 3 | 0.43 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 993,096 | -251 | +979 | -7,114 | -6,904 | 1.2% | 4 | 0.59 | 1 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 998,427 | -934 | +275 | -905 | -1,573 | 0.3% | 2 | 0.35 | 2 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 998,845 | -934 | +275 | -579 | -1,155 | 0.4% | 2 | 0.36 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 998,845 | -934 | +275 | -579 | -1,155 | 0.4% | 2 | 0.36 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 981,316 | -2,075 | -4,398 | -22,762 | -18,684 | 3.5% | 3 | 1.18 | 8 | 0% | 0.00 |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.94 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -3.2% | 0.83 | -0.59 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -6.5% | 0.89 | -0.70 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.74 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -8.2% | 0.74 | -1.18 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.22 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.64 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.17 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -7.0% | 0.68 | -0.93 | 1.09 |
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
