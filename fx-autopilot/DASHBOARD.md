# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-10-13T01:00 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 953,052 | -8,879 | -37,677 | -46,948 | -46,948 | 6.2% | 1 | 1.86 | 54 | 35% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,023,076 | +332 | +10,971 | +23,076 | +23,076 | 0.0% | 1 | 2.60 | 19 | 68% | 1.86 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,008,785 | +266 | +5,889 | +8,785 | +8,785 | 0.2% | 1 | 2.11 | 11 | 55% | 1.37 |
| mtf_pullback_v1 | RESEARCH_ONLY | 999,673 | +0 | +0 | -327 | -327 | 0.4% | 0 | 0.00 | 2 | 50% | 0.93 |
| regime_switch_v1 | RESEARCH_ONLY | 979,167 | +2,781 | -25,144 | -20,833 | -20,833 | 3.5% | 2 | 2.90 | 12 | 25% | 0.38 |
| trend_donchian_v1 | RESEARCH_ONLY | 1,013,490 | +5,075 | +3,244 | +13,490 | +13,490 | 0.9% | 2 | 2.84 | 4 | 0% | 0.00 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 968,650 | +6,108 | -12,185 | -31,350 | -31,350 | 3.1% | 2 | 2.89 | 9 | 0% | 0.00 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,017,539 | +2,694 | +4,235 | +17,539 | +17,539 | 0.1% | 1 | 0.47 | 3 | 67% | 5.81 |
| v10_carry_vix | REJECTED | 1,009,221 | +2,376 | +2,509 | +9,221 | +9,221 | 0.1% | 6 | 2.28 | 0 | — | — |
| v11_intraday_region | REJECTED | 1,015,466 | +5,486 | +10,856 | +15,466 | +15,466 | 0.0% | 0 | 0.00 | 163 | 59% | 1.45 |
| v12_carry_timed | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 997,121 | -1,344 | -998 | -2,879 | -2,879 | 0.3% | 2 | 1.61 | 0 | — | — |
| v2_h4_ema | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 989,734 | +762 | -11,721 | -10,266 | -10,266 | 1.9% | 1 | 1.60 | 8 | 12% | 0.44 |
| v2_trend_carry | CHALLENGER | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_xpair_strength | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v3_carry_only | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v3_carry_trend_mh | REJECTED | 999,868 | +0 | +210 | -132 | -132 | 0.0% | 0 | 0.00 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 999,761 | +438 | -239 | -239 | -239 | 0.0% | 1 | 0.11 | 1 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,005,891 | +1,955 | +1,795 | +5,891 | +5,891 | 0.0% | 4 | 0.65 | 2 | 50% | 1.22 |
| v5_carry_trend_daily_10p | REJECTED | 1,003,890 | +1,712 | +946 | +3,890 | +3,890 | 0.0% | 3 | 0.56 | 1 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,002,641 | +1,711 | +1,531 | +2,641 | +2,641 | 0.0% | 3 | 0.56 | 0 | — | — |
| v6_carry_trend_daily_mkt_7p | REJECTED | 999,480 | +466 | +118 | -520 | -520 | 0.1% | 2 | 0.39 | 1 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 999,881 | +0 | +210 | -119 | -119 | 0.0% | 0 | 0.00 | 1 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 999,881 | +0 | +210 | -119 | -119 | 0.0% | 0 | 0.00 | 1 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 1,011,151 | +5,171 | +2,883 | +11,151 | +11,151 | 0.1% | 4 | 1.70 | 0 | — | — |

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
