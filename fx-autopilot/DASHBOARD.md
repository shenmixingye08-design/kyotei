# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-04T01:29 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 878,751 | -233 | -7,519 | -125,193 | -121,249 | 13.5% | 2 | 3.93 | 149 | 39% | 0.59 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,007,368 | -13,686 | -11,286 | +7,240 | +7,368 | 3.1% | 0 | 0.00 | 31 | 55% | 1.11 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,020,152 | -10,305 | -3,411 | +11,913 | +20,152 | 1.9% | 3 | 4.91 | 26 | 58% | 1.50 |
| mtf_pullback_v1 | RESEARCH_ONLY | 992,880 | +0 | +7,257 | -857 | -7,120 | 1.1% | 0 | 0.00 | 6 | 33% | 0.63 |
| regime_switch_v1 | RESEARCH_ONLY | 976,304 | -7,816 | -5,864 | -23,428 | -23,696 | 4.1% | 2 | 3.73 | 41 | 29% | 0.74 |
| trend_donchian_v1 | RESEARCH_ONLY | 966,494 | +5,786 | -8,071 | -41,470 | -33,506 | 5.5% | 3 | 2.63 | 16 | 12% | 0.19 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 953,473 | +13,465 | -12,727 | -27,362 | -46,527 | 4.7% | 2 | 2.79 | 35 | 26% | 0.37 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,017,176 | +0 | -8,654 | +6,412 | +17,176 | 0.9% | 0 | 0.00 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -10,664 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,014,267 | -1,896 | -6,294 | +7,532 | +14,267 | 1.3% | 5 | 1.95 | 396 | 50% | 1.15 |
| v12_carry_timed | REJECTED | 1,004,051 | +4,235 | +4,051 | +4,051 | +4,051 | 0.2% | 6 | 2.58 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 999,067 | -1,431 | -933 | -933 | -933 | 0.2% | 3 | 1.18 | 0 | — | — |
| v13_ratemom | REJECTED | 991,914 | -8,087 | -8,086 | -8,086 | -8,086 | 0.8% | 6 | 2.74 | 0 | — | — |
| v14_term | REJECTED | 1,000,586 | +895 | +586 | +586 | +586 | 0.0% | 6 | 2.39 | 0 | — | — |
| v14_term_ratemom | REJECTED | 998,110 | -2,131 | -1,890 | -1,890 | -1,890 | 0.3% | 2 | 0.96 | 0 | — | — |
| v16_equity_rebal | REJECTED | 997,760 | -1,840 | -2,240 | -2,240 | -2,240 | 0.3% | 3 | 1.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,003,406 | +3,549 | +3,406 | +3,406 | +3,406 | 0.1% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 985,736 | -7,140 | -16,820 | -9,808 | -14,264 | 1.9% | 4 | 3.04 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 996,240 | +730 | -2,255 | -3,760 | -3,760 | 0.6% | 1 | 0.55 | 2 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 971,802 | -1,888 | -9,306 | -25,485 | -28,198 | 3.7% | 1 | 1.52 | 13 | 8% | 0.22 |
| v2_trend_carry | CHALLENGER | 999,045 | -715 | -1,697 | -955 | -955 | 0.2% | 3 | 0.45 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 998,995 | -1,624 | -3,696 | -1,005 | -1,005 | 0.4% | 3 | 0.47 | 0 | — | — |
| v3_carry_only | REJECTED | 1,002,434 | +2,892 | +4,629 | +2,434 | +2,434 | 0.2% | 4 | 2.47 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 998,940 | -820 | -1,802 | -1,060 | -1,060 | 0.2% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 999,323 | -747 | -1,729 | -149 | -677 | 0.2% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 999,488 | -715 | -1,697 | -512 | -512 | 0.2% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 999,113 | +639 | -417 | -887 | -887 | 0.2% | 4 | 0.56 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,000,345 | +134 | -840 | +345 | +345 | 0.1% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,001,167 | +124 | -1,278 | -2,125 | +1,167 | 0.5% | 4 | 0.66 | 16 | 44% | 0.94 |
| v5_carry_trend_daily_10p | REJECTED | 994,205 | +605 | -3,685 | -7,854 | -5,795 | 1.2% | 4 | 0.59 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 992,214 | +71 | -2,739 | -8,244 | -7,786 | 1.3% | 4 | 0.59 | 1 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 996,771 | -1,355 | -3,417 | -2,561 | -3,229 | 0.5% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 996,422 | -2,144 | -4,184 | -3,061 | -3,578 | 0.7% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 996,422 | -2,144 | -4,184 | -3,061 | -3,578 | 0.7% | 4 | 0.73 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,002,671 | +2,727 | +2,671 | +2,671 | +2,671 | 0.3% | 6 | 2.54 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 998,465 | -1,995 | -1,535 | -1,535 | -1,535 | 0.2% | 6 | 2.40 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,002,981 | +2,634 | +2,981 | +2,981 | +2,981 | 0.2% | 5 | 1.95 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,001,609 | +1,773 | +1,609 | +1,609 | +1,609 | 0.2% | 7 | 1.42 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,001,609 | +1,773 | +1,609 | +1,609 | +1,609 | 0.2% | 7 | 1.42 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 979,272 | -1,234 | -5,947 | -26,115 | -20,728 | 3.7% | 3 | 1.15 | 10 | 10% | 0.02 |

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
