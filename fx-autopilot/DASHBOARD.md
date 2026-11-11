# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-11T06:34 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 867,056 | -11,330 | -14,326 | -96,763 | -132,944 | 14.7% | 2 | 2.83 | 179 | 42% | 0.62 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +4,645 | +8,143 | +8,271 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 997,555 | -232 | -10,430 | -25,189 | -2,445 | 4.1% | 0 | 0.00 | 35 | 51% | 0.97 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,049,630 | +3,777 | +21,033 | +41,112 | +49,630 | 0.2% | 2 | 2.65 | 35 | 60% | 1.67 |
| mtf_pullback_v1 | RESEARCH_ONLY | 994,881 | +0 | -59 | -4,792 | -5,119 | 0.9% | 0 | 0.00 | 8 | 38% | 0.79 |
| regime_switch_v1 | RESEARCH_ONLY | 967,655 | -2,047 | -14,104 | -10,054 | -32,345 | 5.0% | 2 | 3.31 | 44 | 30% | 0.72 |
| trend_donchian_v1 | RESEARCH_ONLY | 963,161 | +5,090 | -2,063 | -44,525 | -36,839 | 5.8% | 3 | 3.29 | 18 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 944,029 | -5,513 | -5,585 | -19,982 | -55,971 | 5.6% | 2 | 2.97 | 44 | 27% | 0.51 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,018,334 | +3,117 | +1,158 | +3,286 | +18,334 | 0.8% | 1 | 0.43 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -14,284 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,009,531 | +3,092 | -1,083 | -2,430 | +9,531 | 1.8% | 5 | 1.76 | 471 | 49% | 1.08 |
| v12_carry_timed | REJECTED | 1,010,344 | +8,267 | +11,176 | +10,344 | +10,344 | 0.0% | 6 | 2.56 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,001,292 | +4,829 | +4,131 | +1,292 | +1,292 | 0.0% | 3 | 1.18 | 0 | — | — |
| v13_ratemom | REJECTED | 1,010,720 | +10,024 | +20,296 | +10,720 | +10,720 | 0.1% | 6 | 2.69 | 0 | — | — |
| v14_term | REJECTED | 997,056 | +725 | -1,643 | -2,944 | -2,944 | 0.6% | 6 | 2.40 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,003,705 | +6,310 | +7,308 | +3,705 | +3,705 | 0.1% | 2 | 0.95 | 0 | — | — |
| v16_equity_rebal | REJECTED | 991,901 | -5,161 | -7,034 | -8,099 | -8,099 | 1.2% | 3 | 1.01 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 998,553 | -536 | -3,184 | -1,447 | -1,447 | 0.9% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 999,554 | +1,554 | -446 | -446 | -446 | 0.1% | 1 | 0.22 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 983,124 | +3,254 | -1,446 | -14,312 | -16,876 | 2.2% | 4 | 3.05 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 983,356 | -714 | -12,720 | -16,644 | -16,644 | 1.9% | 1 | 0.72 | 7 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 974,181 | +0 | -192 | -14,791 | -25,819 | 3.5% | 0 | 0.00 | 15 | 13% | 0.39 |
| v2_trend_carry | CHALLENGER | 1,001,763 | +2,558 | +3,724 | +1,763 | +1,763 | 0.0% | 3 | 0.45 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,001,768 | +1,976 | +3,142 | +1,768 | +1,768 | 0.1% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,005,068 | +6,340 | +7,107 | +5,068 | +5,068 | 0.1% | 4 | 2.46 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,000,466 | +2,297 | +2,626 | +466 | +466 | 0.1% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 999,410 | +1,512 | +963 | -457 | -590 | 0.2% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,002,206 | +2,558 | +3,724 | +2,206 | +2,206 | 0.0% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,000,639 | +2,299 | +2,629 | +1,202 | +639 | 0.0% | 4 | 0.56 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 999,984 | +1,773 | +516 | -16 | -16 | 0.1% | 2 | 0.34 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 996,535 | -1,711 | -3,991 | -7,642 | -3,465 | 1.0% | 3 | 0.45 | 24 | 29% | 0.47 |
| v5_carry_trend_daily_10p | REJECTED | 996,777 | +3,507 | +3,880 | -5,629 | -3,223 | 1.0% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 994,348 | +2,470 | +3,910 | -6,808 | -5,652 | 1.1% | 4 | 0.59 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 996,111 | +1,687 | +309 | -2,846 | -3,889 | 0.6% | 4 | 0.63 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 999,401 | +3,374 | +3,947 | -480 | -599 | 0.4% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 999,401 | +3,374 | +3,947 | -480 | -599 | 0.4% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,013,133 | +9,027 | +15,180 | +13,133 | +13,133 | 0.0% | 6 | 2.52 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 991,397 | -284 | -5,680 | -8,603 | -8,603 | 1.2% | 6 | 2.42 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,002,142 | +5,366 | +2,352 | +2,142 | +2,142 | 0.3% | 5 | 1.95 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,012,927 | +9,110 | +14,360 | +12,927 | +12,927 | 0.2% | 7 | 1.40 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,012,927 | +9,110 | +14,360 | +12,927 | +12,927 | 0.2% | 7 | 1.40 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 972,220 | +280 | -7,235 | -34,371 | -27,780 | 4.4% | 0 | 0.00 | 18 | 17% | 0.11 |

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
