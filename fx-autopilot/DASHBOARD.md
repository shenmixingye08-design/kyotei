# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-10-26T04:55 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 905,456 | +390 | -36,561 | -97,003 | -94,544 | 10.9% | 3 | 5.00 | 115 | 40% | 0.60 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,023,878 | +0 | -9,843 | +23,878 | +23,878 | 1.5% | 0 | 0.00 | 24 | 62% | 1.57 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,022,741 | +3,031 | -14,482 | +22,741 | +22,741 | 1.7% | 2 | 2.28 | 22 | 55% | 1.44 |
| mtf_pullback_v1 | RESEARCH_ONLY | 988,702 | -1,600 | -1,600 | -9,407 | -11,298 | 1.5% | 1 | 1.42 | 4 | 25% | 0.33 |
| regime_switch_v1 | RESEARCH_ONLY | 996,210 | -1,818 | -9,428 | -2,278 | -3,790 | 2.2% | 1 | 1.06 | 29 | 34% | 0.95 |
| trend_donchian_v1 | RESEARCH_ONLY | 980,113 | -185 | -961 | -19,879 | -19,887 | 4.2% | 3 | 2.22 | 11 | 9% | 0.22 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 962,952 | -6,416 | +7,502 | -36,054 | -37,048 | 3.7% | 1 | 1.48 | 26 | 23% | 0.33 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,020,040 | -1,794 | +3,704 | +20,040 | +20,040 | 0.3% | 2 | 1.04 | 4 | 75% | 6.25 |
| v10_carry_vix | REJECTED | 993,074 | +0 | -4,718 | -6,926 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,017,995 | +267 | +4,878 | +17,995 | +17,995 | 0.2% | 5 | 1.94 | 291 | 55% | 1.28 |
| v12_carry_timed | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 993,435 | -2,007 | +3,513 | -6,565 | -6,565 | 1.1% | 2 | 1.67 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 1,000,066 | -352 | +66 | +66 | +66 | 0.2% | 2 | 1.29 | 0 | — | — |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 975,561 | +0 | +0 | -24,439 | -24,439 | 3.3% | 0 | 0.00 | 11 | 9% | 0.26 |
| v2_trend_carry | CHALLENGER | 999,210 | -164 | -291 | -790 | -790 | 0.2% | 2 | 0.29 | 0 | — | — |
| v2_xpair_strength | REJECTED | 1,000,762 | -598 | +1,583 | +762 | +762 | 0.1% | 2 | 0.35 | 0 | — | — |
| v3_carry_only | REJECTED | 991,169 | -6 | -7,039 | -8,831 | -8,831 | 1.3% | 3 | 1.86 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,210 | -164 | -291 | -790 | -790 | 0.2% | 2 | 0.29 | 0 | — | — |
| v3_carry_trend_mh | REJECTED | 999,525 | -295 | +156 | -475 | -475 | 0.2% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 999,657 | -295 | +156 | -343 | -343 | 0.2% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 998,226 | -295 | -682 | -1,774 | -1,774 | 0.3% | 1 | 0.18 | 2 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 999,657 | -295 | +156 | -343 | -343 | 0.2% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 998,992 | -332 | -3,105 | -1,008 | -1,008 | 0.7% | 3 | 0.45 | 13 | 31% | 0.28 |
| v5_carry_trend_daily_10p | REJECTED | 993,814 | -330 | -3,035 | -6,186 | -6,186 | 1.3% | 4 | 0.74 | 1 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 991,944 | -469 | -3,651 | -8,056 | -8,056 | 1.3% | 3 | 0.43 | 1 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 998,246 | -598 | +1,622 | -1,754 | -1,754 | 0.4% | 2 | 0.35 | 2 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 998,665 | -598 | +793 | -1,335 | -1,335 | 0.5% | 2 | 0.36 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 998,665 | -598 | +793 | -1,335 | -1,335 | 0.5% | 2 | 0.36 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 985,636 | -295 | -5,919 | -14,364 | -14,364 | 3.1% | 1 | 0.18 | 5 | 0% | 0.00 |

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
