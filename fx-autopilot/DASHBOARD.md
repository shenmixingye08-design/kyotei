# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-10T21:28 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 868,415 | -11,449 | -11,171 | -96,525 | -131,585 | 14.5% | 3 | 4.94 | 176 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +4,601 | +8,143 | +8,271 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 994,293 | -3,494 | -13,075 | -28,451 | -5,707 | 4.4% | 1 | 1.31 | 34 | 50% | 0.91 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,048,206 | +2,353 | +26,581 | +39,688 | +48,206 | 0.0% | 2 | 2.65 | 35 | 60% | 1.67 |
| mtf_pullback_v1 | RESEARCH_ONLY | 994,881 | +0 | +2,001 | -4,792 | -5,119 | 0.9% | 0 | 0.00 | 8 | 38% | 0.79 |
| regime_switch_v1 | RESEARCH_ONLY | 969,593 | -108 | -4,681 | -7,593 | -30,407 | 4.8% | 2 | 3.30 | 44 | 30% | 0.72 |
| trend_donchian_v1 | RESEARCH_ONLY | 965,098 | +8,239 | +6 | -43,195 | -34,902 | 5.6% | 2 | 1.64 | 18 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 943,746 | -6,472 | -10,802 | -19,686 | -56,254 | 5.6% | 2 | 2.97 | 44 | 27% | 0.51 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,019,000 | +3,921 | +1,824 | +3,920 | +19,000 | 0.7% | 1 | 0.43 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -13,457 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,009,922 | +3,701 | -4,030 | -58 | +9,922 | 1.7% | 0 | 0.00 | 471 | 49% | 1.08 |
| v12_carry_timed | REJECTED | 1,009,131 | +7,944 | +3,982 | +9,131 | +9,131 | 0.0% | 6 | 2.56 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,222 | +4,053 | -1,097 | +222 | +222 | 0.1% | 3 | 1.18 | 0 | — | — |
| v13_ratemom | REJECTED | 1,009,404 | +7,534 | +13,562 | +9,404 | +9,404 | 0.2% | 6 | 2.69 | 0 | — | — |
| v14_term | REJECTED | 995,747 | -514 | -3,890 | -4,253 | -4,253 | 0.7% | 6 | 2.40 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,003,503 | +5,860 | +3,586 | +3,503 | +3,503 | 0.1% | 2 | 0.95 | 0 | — | — |
| v16_equity_rebal | REJECTED | 991,470 | -5,301 | -6,921 | -8,530 | -8,530 | 1.3% | 3 | 1.01 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 997,997 | +134 | -6,024 | -2,003 | -2,003 | 0.9% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 999,887 | +1,955 | -113 | -113 | -113 | 0.1% | 1 | 0.22 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 981,522 | +910 | -7,154 | -16,432 | -18,478 | 2.3% | 4 | 3.06 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 983,502 | -488 | -12,999 | -16,498 | -16,498 | 1.8% | 1 | 0.72 | 7 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 974,181 | +0 | +4,800 | -14,791 | -25,819 | 3.5% | 0 | 0.00 | 15 | 13% | 0.39 |
| v2_trend_carry | CHALLENGER | 1,001,852 | +2,827 | +2,147 | +1,852 | +1,852 | 0.0% | 3 | 0.45 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,001,849 | +1,807 | +2,279 | +1,849 | +1,849 | 0.1% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,004,804 | +7,937 | +141 | +4,804 | +4,804 | 0.0% | 4 | 2.46 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,000,379 | +2,477 | +674 | +379 | +379 | 0.1% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 999,157 | +1,491 | -859 | -711 | -843 | 0.2% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,002,295 | +2,827 | +2,147 | +2,295 | +2,295 | 0.0% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,000,552 | +2,480 | +709 | +1,272 | +552 | 0.1% | 4 | 0.56 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 999,907 | +1,841 | -1,116 | -93 | -93 | 0.1% | 2 | 0.34 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 996,552 | -1,363 | -5,275 | -7,446 | -3,448 | 1.0% | 2 | 0.27 | 23 | 30% | 0.47 |
| v5_carry_trend_daily_10p | REJECTED | 996,591 | +3,483 | +1,658 | -5,520 | -3,409 | 1.0% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 994,156 | +2,183 | +1,291 | -6,702 | -5,844 | 1.1% | 3 | 0.43 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 995,826 | +1,389 | -2,011 | -3,168 | -4,174 | 0.6% | 4 | 0.63 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 999,475 | +3,281 | +1,958 | -405 | -525 | 0.4% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 999,475 | +3,281 | +1,958 | -405 | -525 | 0.4% | 4 | 0.73 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,011,241 | +8,385 | +5,446 | +11,241 | +11,241 | 0.0% | 6 | 2.52 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 989,952 | -1,261 | -10,273 | -10,048 | -10,048 | 1.3% | 6 | 2.42 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,001,389 | +5,299 | -2,570 | +1,389 | +1,389 | 0.4% | 5 | 1.95 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,012,747 | +9,034 | +9,970 | +12,747 | +12,747 | 0.2% | 7 | 1.40 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,012,747 | +9,034 | +9,970 | +12,747 | +12,747 | 0.2% | 7 | 1.40 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 972,226 | -222 | -7,359 | -33,592 | -27,774 | 4.4% | 1 | 0.36 | 17 | 18% | 0.11 |

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
