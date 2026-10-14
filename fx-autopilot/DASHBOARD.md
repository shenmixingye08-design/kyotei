# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-10-14T00:32 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 953,615 | +564 | -38,188 | -46,385 | -46,385 | 6.2% | 2 | 4.94 | 59 | 37% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,025,735 | +2,659 | +12,150 | +25,735 | +25,735 | 0.0% | 0 | 0.00 | 20 | 70% | 1.97 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,015,635 | +6,851 | +10,020 | +15,635 | +15,635 | 0.0% | 0 | 0.00 | 12 | 58% | 1.68 |
| mtf_pullback_v1 | RESEARCH_ONLY | 995,410 | -4,264 | -4,264 | -4,590 | -4,590 | 0.8% | 0 | 0.00 | 3 | 33% | 0.51 |
| regime_switch_v1 | RESEARCH_ONLY | 973,406 | -5,761 | -24,773 | -26,594 | -26,594 | 4.1% | 0 | 0.00 | 14 | 21% | 0.33 |
| trend_donchian_v1 | RESEARCH_ONLY | 1,000,232 | -13,259 | -1,831 | +232 | +232 | 2.2% | 1 | 1.61 | 6 | 0% | 0.00 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 964,547 | -4,102 | -16,875 | -35,453 | -35,453 | 3.5% | 2 | 2.94 | 11 | 9% | 0.05 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,016,936 | -602 | +8,298 | +16,936 | +16,936 | 0.2% | 1 | 0.47 | 3 | 67% | 5.81 |
| v10_carry_vix | REJECTED | 1,007,276 | -1,944 | +1,834 | +7,276 | +7,276 | 0.3% | 6 | 2.29 | 0 | — | — |
| v11_intraday_region | REJECTED | 1,010,929 | -4,537 | +14,976 | +10,929 | +10,929 | 0.5% | 0 | 0.00 | 178 | 55% | 1.28 |
| v12_carry_timed | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 997,011 | -111 | +497 | -2,989 | -2,989 | 0.3% | 4 | 3.03 | 0 | — | — |
| v2_h4_ema | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 979,422 | -10,312 | -18,004 | -20,578 | -20,578 | 2.9% | 0 | 0.00 | 10 | 10% | 0.30 |
| v2_trend_carry | CHALLENGER | 999,951 | -49 | -49 | -49 | -49 | 0.0% | 1 | 0.18 | 0 | — | — |
| v2_xpair_strength | REJECTED | 999,879 | -121 | -121 | -121 | -121 | 0.0% | 2 | 0.35 | 0 | — | — |
| v3_carry_only | REJECTED | 999,830 | -170 | -170 | -170 | -170 | 0.0% | 2 | 1.42 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,951 | -49 | -49 | -49 | -49 | 0.0% | 1 | 0.18 | 0 | — | — |
| v3_carry_trend_mh | REJECTED | 999,818 | -49 | -49 | -182 | -182 | 0.0% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 999,951 | -49 | -49 | -49 | -49 | 0.0% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 999,263 | -499 | -737 | -737 | -737 | 0.1% | 2 | 0.29 | 1 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 999,951 | -49 | -49 | -49 | -49 | 0.0% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,003,823 | -2,068 | +928 | +3,823 | +3,823 | 0.2% | 4 | 0.65 | 2 | 50% | 1.22 |
| v5_carry_trend_daily_10p | REJECTED | 1,001,753 | -2,137 | +102 | +1,753 | +1,753 | 0.2% | 4 | 0.74 | 1 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,000,504 | -2,137 | +320 | +504 | +504 | 0.2% | 4 | 0.74 | 0 | — | — |
| v6_carry_trend_daily_mkt_7p | REJECTED | 998,248 | -1,233 | -342 | -1,752 | -1,752 | 0.2% | 3 | 0.56 | 1 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 999,701 | -180 | -180 | -299 | -299 | 0.0% | 3 | 0.56 | 1 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 999,701 | -180 | -180 | -299 | -299 | 0.0% | 3 | 0.56 | 1 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 1,004,546 | -6,605 | +1,185 | +4,546 | +4,546 | 0.7% | 5 | 1.89 | 0 | — | — |

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
