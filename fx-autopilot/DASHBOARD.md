# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-24T22:46 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -44,101 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,009,597 | +1,327 | +1,327 | +9,469 | +9,597 | 0.1% | 1 | 1.56 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 975,576 | +0 | -17,354 | -48,301 | -24,424 | 6.2% | 0 | 0.00 | 40 | 45% | 0.76 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,028,659 | +13,176 | +8,969 | +4,008 | +28,659 | 2.2% | 0 | 0.00 | 51 | 53% | 1.24 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,013,431 | -872 | +16,954 | +23,129 | +13,431 | 0.2% | 1 | 1.15 | 11 | 55% | 1.59 |
| regime_switch_v1 | RESEARCH_ONLY | 1,002,553 | -11,203 | +31,274 | +7,435 | +2,553 | 1.5% | 0 | 0.00 | 58 | 31% | 1.02 |
| trend_donchian_v1 | RESEARCH_ONLY | 984,156 | -7,465 | -1,273 | +7,002 | -15,844 | 3.8% | 3 | 1.88 | 21 | 10% | 0.14 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 951,983 | +0 | -4,445 | -8,889 | -48,017 | 4.8% | 0 | 0.00 | 50 | 28% | 0.61 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,044,715 | -10,200 | +15,067 | +25,005 | +44,715 | 1.2% | 2 | 1.65 | 7 | 71% | 10.47 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | +0 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 999,236 | -8,260 | -7,802 | -18,492 | -764 | 2.8% | 0 | 0.00 | 621 | 48% | 1.00 |
| v12_carry_timed | REJECTED | 1,019,637 | -5,062 | -1,916 | +19,637 | +19,637 | 0.8% | 5 | 2.21 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,008,511 | -5,062 | +68 | +8,511 | +8,511 | 0.7% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,030,345 | -15,354 | +4,704 | +30,345 | +30,345 | 1.7% | 5 | 2.29 | 1 | 0% | 0.00 |
| v14_term | REJECTED | 994,288 | -5,442 | -432 | -5,712 | -5,712 | 0.8% | 3 | 1.31 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,020,370 | -5,559 | +4,625 | +20,370 | +20,370 | 0.7% | 2 | 0.93 | 0 | — | — |
| v16_equity_rebal | REJECTED | 970,125 | +0 | -3,078 | -29,875 | -29,875 | 3.4% | 0 | 0.00 | 3 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 987,453 | +3,864 | -3,322 | -12,547 | -12,547 | 2.0% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,007,758 | -3,980 | +2,365 | +7,758 | +7,758 | 0.5% | 4 | 0.77 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,005,908 | -11,647 | +7,617 | +11,355 | +5,908 | 1.5% | 4 | 2.64 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 991,763 | -3,061 | +3,605 | -8,024 | -8,237 | 1.0% | 0 | 0.00 | 10 | 20% | 0.57 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 988,504 | -9,327 | -340 | +12,943 | -11,496 | 2.0% | 0 | 0.00 | 20 | 25% | 0.76 |
| v2_trend_carry | CHALLENGER | 1,009,189 | -914 | +2,008 | +10,036 | +9,189 | 0.2% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,011,028 | -2,468 | +2,605 | +10,376 | +11,028 | 0.3% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,009,621 | +3,298 | -2,408 | +18,324 | +9,621 | 0.8% | 4 | 2.45 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,004,376 | +763 | +476 | +5,223 | +4,376 | 0.1% | 4 | 0.65 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,068 | -555 | +488 | +1,472 | +1,068 | 0.1% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,008,105 | +763 | +476 | +8,376 | +8,105 | 0.1% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,004,466 | +764 | +475 | +6,168 | +4,466 | 0.1% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,005,300 | -2,206 | +727 | +5,571 | +5,300 | 0.3% | 3 | 0.44 | 3 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 997,540 | -2,241 | -2,678 | -1,837 | -2,460 | 0.9% | 3 | 0.44 | 31 | 32% | 0.42 |
| v5_carry_trend_daily_10p | REJECTED | 1,004,455 | -2,305 | -147 | +9,911 | +4,455 | 0.3% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,000,779 | -2,220 | +423 | +8,674 | +779 | 0.5% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,001,591 | -3,311 | +2,549 | +3,455 | +1,591 | 0.4% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,009,256 | -2,202 | +2,576 | +10,702 | +9,256 | 0.3% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,009,256 | -2,202 | +2,576 | +10,702 | +9,256 | 0.3% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,018,440 | -5,136 | -4,322 | +18,440 | +18,440 | 0.9% | 5 | 2.18 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 991,287 | -1,659 | -449 | -8,713 | -8,713 | 1.2% | 4 | 1.64 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,011,370 | -3,754 | -2,338 | +11,370 | +11,370 | 0.6% | 4 | 1.61 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,034,998 | -6,445 | +3,981 | +34,998 | +34,998 | 0.9% | 7 | 1.37 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,034,998 | -6,445 | +3,981 | +34,998 | +34,998 | 0.9% | 7 | 1.37 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 984,571 | -14,282 | -821 | -1,136 | -15,429 | 3.2% | 6 | 2.33 | 20 | 20% | 0.12 |

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
