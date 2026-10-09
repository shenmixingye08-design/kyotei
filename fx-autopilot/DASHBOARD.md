# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-10-09T01:28 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 981,598 | -10,261 | -28,185 | -18,402 | -18,402 | 3.4% | 2 | 2.95 | 41 | 41% | 0.79 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,022,744 | +11,860 | +31,049 | +22,744 | +22,744 | 0.0% | 0 | 0.00 | 19 | 68% | 1.86 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,008,519 | +2,146 | +11,882 | +8,519 | +8,519 | 0.2% | 0 | 0.00 | 11 | 55% | 1.37 |
| mtf_pullback_v1 | RESEARCH_ONLY | 999,673 | +0 | +4,693 | -327 | -327 | 0.4% | 0 | 0.00 | 2 | 50% | 0.93 |
| regime_switch_v1 | RESEARCH_ONLY | 980,845 | -6,489 | -24,594 | -19,155 | -19,155 | 3.3% | 1 | 1.08 | 11 | 27% | 0.44 |
| trend_donchian_v1 | RESEARCH_ONLY | 1,009,331 | -4,115 | -6,722 | +9,331 | +9,331 | 1.3% | 2 | 2.69 | 3 | 0% | 0.00 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 968,255 | -9,731 | -12,580 | -31,745 | -31,745 | 3.2% | 2 | 3.07 | 6 | 0% | 0.00 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,013,114 | -2,562 | +3,755 | +13,114 | +13,114 | 0.6% | 3 | 1.88 | 1 | 0% | 0.00 |
| v10_carry_vix | REJECTED | 1,004,497 | -2,045 | +1,968 | +4,497 | +4,497 | 0.4% | 5 | 1.94 | 0 | — | — |
| v11_intraday_region | REJECTED | 1,007,830 | +6,037 | +560 | +7,830 | +7,830 | 0.1% | 5 | 1.66 | 133 | 55% | 1.27 |
| v12_carry_timed | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 996,594 | -875 | +1,693 | -3,406 | -3,406 | 0.4% | 2 | 1.61 | 0 | — | — |
| v2_h4_ema | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 992,637 | -4,311 | -7,660 | -7,363 | -7,363 | 1.6% | 2 | 1.96 | 6 | 17% | 0.77 |
| v2_trend_carry | CHALLENGER | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_xpair_strength | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v3_carry_only | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v3_carry_trend_mh | REJECTED | 999,868 | +0 | +982 | -132 | -132 | 0.0% | 0 | 0.00 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 999,681 | -319 | -319 | -319 | -319 | 0.0% | 2 | 0.32 | 0 | — | — |
| v4_carry_trend_daily_fast | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,003,888 | -688 | -1,420 | +3,888 | +3,888 | 0.2% | 4 | 0.65 | 2 | 50% | 1.22 |
| v5_carry_trend_daily_10p | REJECTED | 1,001,675 | -1,633 | -624 | +1,675 | +1,675 | 0.2% | 4 | 0.77 | 0 | — | — |
| v5_carry_trend_weekly_10p | REJECTED | 1,000,361 | -1,485 | -6 | +361 | +361 | 0.2% | 3 | 0.56 | 0 | — | — |
| v6_carry_trend_daily_mkt_7p | REJECTED | 999,058 | -438 | -274 | -942 | -942 | 0.1% | 1 | 0.21 | 1 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 999,881 | +0 | +984 | -119 | -119 | 0.0% | 0 | 0.00 | 1 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 999,881 | +0 | +984 | -119 | -119 | 0.0% | 0 | 0.00 | 1 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 1,005,141 | -4,122 | -3,112 | +5,141 | +5,141 | 0.6% | 4 | 1.71 | 0 | — | — |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.97 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -3.2% | 0.83 | -0.61 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -7.7% | 0.87 | -0.91 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.76 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -8.2% | 0.73 | -1.24 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.26 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.69 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.18 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -8.3% | 0.62 | -1.16 | 1.09 |
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
