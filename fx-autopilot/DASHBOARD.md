# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-27T01:52 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -24,357 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,009,588 | +0 | +1,318 | +9,460 | +9,588 | 0.1% | 0 | 0.00 | 4 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 981,634 | +2,312 | -1,569 | -37,021 | -18,366 | 5.6% | 0 | 0.00 | 42 | 48% | 0.82 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,030,801 | +0 | +25,056 | +7,238 | +30,801 | 2.0% | 0 | 0.00 | 53 | 53% | 1.25 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,016,319 | +6,020 | +12,274 | +30,696 | +16,319 | 0.0% | 2 | 2.95 | 12 | 50% | 1.32 |
| regime_switch_v1 | RESEARCH_ONLY | 1,001,353 | +0 | +5,342 | +19,185 | +1,353 | 1.7% | 0 | 0.00 | 59 | 31% | 1.01 |
| trend_donchian_v1 | RESEARCH_ONLY | 984,767 | +1,078 | -12,759 | +10,202 | -15,233 | 3.7% | 2 | 1.25 | 22 | 9% | 0.13 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 947,137 | -3,926 | -4,998 | -19,064 | -52,863 | 5.3% | 2 | 3.90 | 51 | 27% | 0.59 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,046,125 | +2,346 | +1,942 | +20,295 | +46,125 | 1.1% | 2 | 1.65 | 7 | 71% | 10.47 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | +0 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,005,956 | +751 | +5,951 | -14,604 | +5,956 | 2.1% | 5 | 1.74 | 651 | 48% | 1.04 |
| v12_carry_timed | REJECTED | 1,020,050 | +5,037 | -1,739 | +20,050 | +20,050 | 0.8% | 5 | 2.21 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,008,516 | +1,960 | -2,332 | +8,516 | +8,516 | 0.7% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,030,796 | +2,590 | -5,394 | +30,796 | +30,796 | 1.6% | 5 | 2.29 | 1 | 0% | 0.00 |
| v14_term | REJECTED | 994,888 | +4,239 | -2,171 | -5,112 | -5,112 | 0.8% | 3 | 1.31 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,021,173 | +1,314 | +426 | +21,173 | +21,173 | 0.6% | 2 | 0.93 | 0 | — | — |
| v16_equity_rebal | REJECTED | 970,125 | +0 | -2,777 | -29,875 | -29,875 | 3.4% | 0 | 0.00 | 3 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 987,228 | +918 | -282 | -12,772 | -12,772 | 2.0% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,008,292 | +495 | -160 | +8,292 | +8,292 | 0.4% | 4 | 0.77 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,007,009 | +2,254 | +1,285 | +4,453 | +7,009 | 1.4% | 4 | 2.63 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 991,763 | +0 | -274 | -6,732 | -8,237 | 1.0% | 0 | 0.00 | 10 | 20% | 0.57 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 988,504 | +0 | -5,622 | +7,396 | -11,496 | 2.0% | 0 | 0.00 | 20 | 25% | 0.76 |
| v2_trend_carry | CHALLENGER | 1,009,466 | +639 | +469 | +8,724 | +9,466 | 0.2% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,011,170 | +70 | +728 | +8,479 | +11,170 | 0.3% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,010,105 | +3,230 | -182 | +12,300 | +10,105 | 0.7% | 4 | 2.45 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,004,488 | +753 | +460 | +3,746 | +4,488 | 0.1% | 4 | 0.65 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,293 | +793 | +69 | +241 | +1,293 | 0.1% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,008,217 | +753 | +460 | +7,033 | +8,217 | 0.1% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,004,578 | +754 | +460 | +5,049 | +4,578 | 0.1% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,005,714 | +771 | +257 | +4,529 | +5,714 | 0.3% | 4 | 0.65 | 3 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 998,073 | +784 | -2,131 | -4,372 | -1,927 | 0.8% | 4 | 0.65 | 32 | 34% | 0.43 |
| v5_carry_trend_daily_10p | REJECTED | 1,004,774 | +1,646 | -995 | +6,883 | +4,774 | 0.3% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,001,041 | +1,434 | -393 | +6,088 | +1,041 | 0.4% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,002,026 | +699 | +293 | +1,839 | +2,026 | 0.4% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,009,506 | +427 | +696 | +8,900 | +9,506 | 0.3% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,009,506 | +427 | +696 | +8,900 | +9,506 | 0.3% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,017,558 | +4,796 | -6,121 | +17,558 | +17,558 | 0.9% | 5 | 2.18 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 991,240 | +1,094 | +776 | -8,760 | -8,760 | 1.2% | 4 | 1.64 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,012,069 | +3,783 | -984 | +12,069 | +12,069 | 0.6% | 4 | 1.61 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,035,782 | +3,539 | -1,750 | +35,782 | +35,782 | 0.8% | 7 | 1.37 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,035,782 | +3,539 | -1,750 | +35,782 | +35,782 | 0.8% | 7 | 1.37 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 985,810 | +4,609 | -4,027 | +591 | -14,190 | 3.1% | 6 | 2.33 | 20 | 20% | 0.12 |

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
