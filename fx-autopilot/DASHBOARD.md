# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-03T19:50 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 879,683 | +450 | -13,986 | -125,195 | -120,317 | 13.4% | 2 | 3.92 | 148 | 39% | 0.59 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,009,292 | -11,537 | -9,362 | +9,406 | +9,292 | 2.9% | 1 | 2.51 | 30 | 57% | 1.20 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,021,827 | -6,956 | -3,912 | +12,318 | +21,827 | 1.8% | 2 | 3.04 | 26 | 58% | 1.50 |
| mtf_pullback_v1 | RESEARCH_ONLY | 992,880 | +0 | +7,257 | -143 | -7,120 | 1.1% | 0 | 0.00 | 6 | 33% | 0.63 |
| regime_switch_v1 | RESEARCH_ONLY | 975,982 | -7,233 | -8,867 | -19,743 | -24,018 | 4.2% | 1 | 2.44 | 40 | 30% | 0.78 |
| trend_donchian_v1 | RESEARCH_ONLY | 964,621 | +3,430 | -8,993 | -40,717 | -35,379 | 5.7% | 3 | 2.64 | 16 | 12% | 0.19 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 953,561 | +10,556 | -11,799 | -27,274 | -46,439 | 4.6% | 2 | 2.79 | 35 | 26% | 0.37 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,017,176 | +0 | -7,505 | +9,181 | +17,176 | 0.9% | 0 | 0.00 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -9,298 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,015,330 | -1,349 | -6,689 | +8,079 | +15,330 | 1.2% | 5 | 1.99 | 391 | 51% | 1.18 |
| v12_carry_timed | REJECTED | 1,004,201 | +4,201 | +4,201 | +4,201 | +4,201 | 0.0% | 6 | 2.58 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,001,167 | +1,167 | +1,167 | +1,167 | +1,167 | 0.0% | 3 | 1.18 | 0 | — | — |
| v13_ratemom | REJECTED | 995,512 | -4,488 | -4,488 | -4,488 | -4,488 | 0.5% | 6 | 2.73 | 0 | — | — |
| v14_term | REJECTED | 999,304 | -696 | -696 | -696 | -696 | 0.1% | 6 | 2.39 | 0 | — | — |
| v14_term_ratemom | REJECTED | 999,473 | -527 | -527 | -527 | -527 | 0.1% | 2 | 0.95 | 0 | — | — |
| v16_equity_rebal | REJECTED | 999,114 | -886 | -886 | -886 | -886 | 0.1% | 3 | 1.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,004,067 | +4,067 | +4,067 | +4,067 | +4,067 | 0.0% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 989,107 | -3,403 | -11,078 | -5,668 | -10,893 | 1.6% | 2 | 1.67 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 996,010 | +500 | -1,073 | -3,990 | -3,990 | 0.6% | 1 | 0.56 | 2 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 970,369 | -3,075 | -9,283 | -24,477 | -29,631 | 3.8% | 1 | 1.52 | 13 | 8% | 0.22 |
| v2_trend_carry | CHALLENGER | 999,652 | +21 | -959 | -348 | -348 | 0.2% | 1 | 0.18 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 999,552 | -795 | -2,756 | -448 | -448 | 0.3% | 2 | 0.35 | 0 | — | — |
| v3_carry_only | REJECTED | 1,004,351 | +5,036 | +6,026 | +4,351 | +4,351 | 0.0% | 3 | 1.83 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,652 | +21 | -959 | -348 | -348 | 0.2% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 999,962 | +21 | -945 | +549 | -38 | 0.1% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,000,094 | +21 | -945 | +94 | +94 | 0.1% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 999,656 | +1,237 | +257 | -344 | -344 | 0.1% | 4 | 0.56 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,000,934 | +860 | -106 | +934 | +934 | 0.0% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,001,864 | +803 | -350 | -1,164 | +1,864 | 0.4% | 4 | 0.65 | 15 | 40% | 0.86 |
| v5_carry_trend_daily_10p | REJECTED | 994,620 | +1,183 | -2,817 | -7,033 | -5,380 | 1.2% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 992,541 | +658 | -1,992 | -7,668 | -7,459 | 1.3% | 4 | 0.59 | 1 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 997,598 | -270 | -2,200 | -1,734 | -2,402 | 0.4% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 997,499 | -788 | -2,717 | -1,925 | -2,501 | 0.6% | 2 | 0.36 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 997,499 | -788 | -2,717 | -1,925 | -2,501 | 0.6% | 2 | 0.36 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,005,189 | +5,189 | +5,189 | +5,189 | +5,189 | 0.0% | 6 | 2.54 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,582 | +582 | +582 | +582 | +582 | 0.0% | 6 | 2.40 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,003,413 | +3,413 | +3,413 | +3,413 | +3,413 | 0.0% | 5 | 1.95 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,001,828 | +1,828 | +1,828 | +1,828 | +1,828 | 0.0% | 7 | 1.42 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,001,828 | +1,828 | +1,828 | +1,828 | +1,828 | 0.0% | 7 | 1.42 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 979,351 | -1,066 | -5,711 | -24,727 | -20,649 | 3.7% | 5 | 1.87 | 8 | 0% | 0.00 |

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
