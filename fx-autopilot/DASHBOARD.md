# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-09T01:18 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 873,685 | +4,034 | -2,207 | -91,256 | -126,315 | 14.0% | 2 | 2.89 | 165 | 40% | 0.60 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 997,787 | +0 | -16,032 | -24,957 | -2,213 | 4.0% | 0 | 0.00 | 33 | 52% | 0.97 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,034,104 | +2,907 | +9,077 | +25,585 | +34,104 | 0.6% | 2 | 2.97 | 33 | 58% | 1.49 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,000,002 | +0 | +7,122 | +328 | +2 | 0.4% | 0 | 0.00 | 7 | 43% | 1.00 |
| regime_switch_v1 | RESEARCH_ONLY | 969,701 | +0 | -9,543 | -7,485 | -30,299 | 4.8% | 0 | 0.00 | 44 | 30% | 0.72 |
| trend_donchian_v1 | RESEARCH_ONLY | 959,298 | -2,451 | -268 | -48,996 | -40,702 | 6.2% | 2 | 1.65 | 18 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 960,449 | -1,714 | +14,695 | -2,982 | -39,551 | 4.0% | 3 | 4.09 | 39 | 28% | 0.44 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,017,176 | +0 | -4,744 | +2,096 | +17,176 | 0.9% | 0 | 0.00 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -13,457 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,005,580 | -2,007 | -15,099 | -4,400 | +5,580 | 2.2% | 5 | 1.87 | 441 | 48% | 1.07 |
| v12_carry_timed | REJECTED | 1,006,905 | -1,661 | +6,905 | +6,905 | +6,905 | 0.3% | 6 | 2.57 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 999,034 | +764 | -966 | -966 | -966 | 0.2% | 3 | 1.18 | 0 | — | — |
| v13_ratemom | REJECTED | 1,006,841 | +1,758 | +6,841 | +6,841 | +6,841 | 0.0% | 6 | 2.70 | 0 | — | — |
| v14_term | REJECTED | 996,704 | +88 | -3,296 | -3,296 | -3,296 | 0.6% | 6 | 2.40 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,003,710 | -331 | +3,710 | +3,710 | +3,710 | 0.1% | 2 | 0.95 | 0 | — | — |
| v16_equity_rebal | REJECTED | 991,044 | +2,401 | -8,956 | -8,956 | -8,956 | 1.3% | 3 | 1.01 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 996,006 | +130 | -3,994 | -3,994 | -3,994 | 1.1% | 3 | 1.08 | 0 | — | — |
| v2_d1_donchian | REJECTED | 999,269 | -519 | -731 | -731 | -731 | 0.1% | 1 | 0.22 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 986,281 | +2,572 | -11,571 | -11,672 | -13,719 | 1.9% | 4 | 3.04 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 989,204 | -102 | -8,051 | -10,796 | -10,796 | 1.3% | 1 | 0.53 | 5 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 981,605 | -243 | +9,983 | -7,367 | -18,395 | 2.7% | 1 | 1.26 | 14 | 14% | 0.43 |
| v2_trend_carry | CHALLENGER | 1,001,274 | -440 | +1,183 | +1,274 | +1,274 | 0.1% | 3 | 0.45 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,002,617 | -123 | +1,229 | +2,617 | +2,617 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,000,679 | -1,206 | +1,627 | +679 | +679 | 0.4% | 4 | 2.47 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,756 | -240 | -335 | -244 | -244 | 0.2% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 998,848 | +21 | -1,553 | -1,020 | -1,152 | 0.2% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,001,717 | -440 | +1,183 | +1,717 | +1,717 | 0.1% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 999,928 | -241 | +1,049 | +648 | -72 | 0.1% | 4 | 0.56 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 999,643 | -179 | -890 | -357 | -357 | 0.2% | 2 | 0.34 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 998,020 | -179 | -3,632 | -5,978 | -1,980 | 0.8% | 2 | 0.33 | 20 | 35% | 0.55 |
| v5_carry_trend_daily_10p | REJECTED | 995,948 | -364 | +946 | -6,162 | -4,052 | 1.1% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 994,160 | -456 | +866 | -6,698 | -5,840 | 1.1% | 3 | 0.43 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 996,344 | +194 | -2,566 | -2,650 | -3,656 | 0.6% | 4 | 0.63 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 999,763 | -119 | +435 | -117 | -237 | 0.4% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 999,763 | -119 | +435 | -117 | -237 | 0.4% | 4 | 0.73 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,005,066 | -102 | +5,066 | +5,066 | +5,066 | 0.1% | 6 | 2.54 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 991,642 | +1,875 | -8,358 | -8,358 | -8,358 | 1.2% | 6 | 2.42 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,001,509 | -708 | +1,509 | +1,509 | +1,509 | 0.4% | 5 | 1.95 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,010,185 | -1,524 | +10,185 | +10,185 | +10,185 | 0.2% | 7 | 1.40 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,010,185 | -1,524 | +10,185 | +10,185 | +10,185 | 0.2% | 7 | 1.40 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 981,445 | -1,044 | -1,228 | -24,374 | -18,555 | 3.5% | 3 | 1.26 | 15 | 20% | 0.14 |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.94 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -3.2% | 0.83 | -0.58 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -8.0% | 0.87 | -0.85 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.73 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -7.6% | 0.76 | -1.06 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.21 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.62 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.17 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -7.6% | 0.66 | -1.00 | 1.09 |
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
