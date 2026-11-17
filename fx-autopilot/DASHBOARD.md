# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-17T16:15 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | -4,124 | -88,857 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +0 | +8,143 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 992,931 | +0 | +143 | -40,791 | -7,069 | 4.5% | 0 | 0.00 | 36 | 50% | 0.92 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,019,356 | -9,168 | -26,497 | -12,536 | +19,356 | 3.1% | 1 | 1.89 | 43 | 51% | 1.15 |
| mtf_pullback_v1 | RESEARCH_ONLY | 994,881 | +0 | +0 | +4,579 | -5,119 | 0.9% | 0 | 0.00 | 8 | 38% | 0.79 |
| regime_switch_v1 | RESEARCH_ONLY | 971,207 | +1,412 | -1,344 | -33,215 | -28,793 | 4.6% | 3 | 2.94 | 51 | 25% | 0.59 |
| trend_donchian_v1 | RESEARCH_ONLY | 984,320 | -1,104 | +18,846 | -421 | -15,680 | 3.7% | 3 | 2.86 | 19 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 959,778 | -779 | +16,425 | +559 | -40,222 | 4.0% | 2 | 2.93 | 46 | 28% | 0.57 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,029,701 | -57 | +10,131 | +13,554 | +29,701 | 0.3% | 3 | 2.10 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -3,414 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,007,119 | -1,790 | -1,505 | -4,909 | +7,119 | 2.0% | 0 | 0.00 | 541 | 48% | 1.05 |
| v12_carry_timed | REJECTED | 1,020,051 | -2,712 | +11,210 | +20,051 | +20,051 | 0.3% | 5 | 2.21 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,007,608 | -1,684 | +7,606 | +7,608 | +7,608 | 0.3% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,026,267 | -873 | +15,499 | +26,267 | +26,267 | 0.3% | 6 | 2.65 | 0 | — | — |
| v14_term | REJECTED | 993,848 | -2,635 | -1,218 | -6,152 | -6,152 | 0.9% | 3 | 1.31 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,015,675 | -446 | +11,674 | +15,675 | +15,675 | 0.1% | 2 | 0.94 | 0 | — | — |
| v16_equity_rebal | REJECTED | 973,663 | -2,374 | -16,275 | -26,337 | -26,337 | 3.1% | 1 | 0.36 | 2 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 990,151 | -2,616 | -6,314 | -9,849 | -9,849 | 1.7% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,005,362 | +480 | +5,189 | +5,362 | +5,362 | 0.0% | 2 | 0.39 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 997,738 | +534 | +16,608 | +12,332 | -2,262 | 0.7% | 3 | 2.24 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 988,647 | +579 | +5,905 | -11,353 | -11,353 | 1.3% | 2 | 1.36 | 8 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 988,851 | +1,596 | +14,671 | +13,291 | -11,149 | 2.0% | 2 | 1.95 | 16 | 19% | 0.76 |
| v2_trend_carry | CHALLENGER | 1,007,015 | -32 | +5,075 | +7,665 | +7,015 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,008,430 | +625 | +6,190 | +9,436 | +8,430 | 0.1% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,010,699 | -2,272 | +7,248 | +13,272 | +10,699 | 0.6% | 4 | 2.45 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,003,728 | -549 | +3,486 | +4,378 | +3,728 | 0.1% | 3 | 0.44 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,000,446 | -761 | +1,568 | +1,229 | +446 | 0.2% | 2 | 0.34 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,007,457 | -32 | +5,075 | +8,107 | +7,457 | 0.0% | 3 | 0.44 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,003,818 | -635 | +3,403 | +4,592 | +3,818 | 0.1% | 3 | 0.44 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,004,198 | +62 | +4,344 | +4,848 | +4,198 | 0.0% | 4 | 0.65 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 1,000,054 | -23 | +3,618 | -2,296 | +54 | 0.6% | 3 | 0.44 | 29 | 34% | 0.60 |
| v5_carry_trend_daily_10p | REJECTED | 1,004,037 | -115 | +7,215 | +6,874 | +4,037 | 0.3% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,000,007 | -304 | +5,524 | +4,097 | +7 | 0.5% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 998,993 | -284 | +3,257 | +2,767 | -1,007 | 0.3% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,006,574 | +338 | +6,809 | +8,896 | +6,574 | 0.1% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,006,574 | +338 | +6,809 | +8,896 | +6,574 | 0.1% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,020,931 | -3,283 | +10,302 | +20,931 | +20,931 | 0.5% | 5 | 2.17 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 991,000 | -1,729 | +2,585 | -9,000 | -9,000 | 1.2% | 4 | 1.64 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,012,188 | -1,356 | +11,057 | +12,188 | +12,188 | 0.3% | 4 | 1.60 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,030,320 | -254 | +16,525 | +30,320 | +30,320 | 0.2% | 7 | 1.38 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,030,320 | -254 | +16,525 | +30,320 | +30,320 | 0.2% | 7 | 1.38 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 984,199 | +271 | +11,597 | -8,140 | -15,801 | 3.2% | 6 | 2.23 | 19 | 21% | 0.13 |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.93 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -2.4% | 0.87 | -0.43 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -9.1% | 0.86 | -0.96 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.73 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -8.0% | 0.75 | -1.12 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.20 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.61 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.17 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -7.1% | 0.68 | -0.91 | 1.09 |
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
