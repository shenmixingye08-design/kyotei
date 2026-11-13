# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-13T20:01 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | -8,969 | -90,456 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +8,143 | +8,271 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 995,355 | -2,200 | -2,432 | -43,664 | -4,645 | 4.3% | 1 | 1.95 | 35 | 51% | 0.97 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,028,422 | -345 | -4,692 | +7,936 | +28,422 | 2.3% | 1 | 1.86 | 39 | 54% | 1.32 |
| mtf_pullback_v1 | RESEARCH_ONLY | 994,881 | +0 | -5,120 | -528 | -5,119 | 0.9% | 0 | 0.00 | 8 | 38% | 0.79 |
| regime_switch_v1 | RESEARCH_ONLY | 962,137 | +3,241 | -7,564 | -26,324 | -37,863 | 5.5% | 3 | 2.96 | 51 | 25% | 0.59 |
| trend_donchian_v1 | RESEARCH_ONLY | 982,407 | +2,688 | +20,677 | -16,274 | -17,593 | 3.9% | 3 | 2.87 | 19 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 958,698 | -3,694 | -4,841 | +2,803 | -41,302 | 4.1% | 1 | 1.10 | 46 | 28% | 0.57 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,024,532 | +1,568 | +7,356 | +7,950 | +24,532 | 0.2% | 1 | 0.43 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -13,569 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,010,246 | +3,305 | +1,851 | -5,254 | +10,246 | 1.7% | 5 | 1.93 | 511 | 49% | 1.09 |
| v12_carry_timed | REJECTED | 1,022,027 | -9 | +13,495 | +22,027 | +22,027 | 0.1% | 6 | 2.53 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,010,083 | +1,151 | +11,828 | +10,083 | +10,083 | 0.0% | 3 | 1.17 | 0 | — | — |
| v13_ratemom | REJECTED | 1,022,740 | +3,039 | +16,814 | +22,740 | +22,740 | 0.0% | 6 | 2.66 | 0 | — | — |
| v14_term | REJECTED | 995,662 | -1,430 | -1,617 | -4,338 | -4,338 | 0.7% | 4 | 1.64 | 2 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,014,345 | +1,737 | +10,301 | +14,345 | +14,345 | 0.0% | 2 | 0.94 | 0 | — | — |
| v16_equity_rebal | REJECTED | 978,811 | -3,809 | -9,993 | -21,189 | -21,189 | 2.5% | 2 | 0.70 | 1 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 995,813 | -2,646 | +431 | -4,187 | -4,187 | 1.1% | 3 | 1.08 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,003,620 | +1,156 | +3,620 | +3,620 | +3,620 | 0.0% | 2 | 0.39 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 994,088 | +3,383 | +9,429 | -6,960 | -5,912 | 1.1% | 3 | 2.25 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 985,008 | +1,632 | -4,313 | -14,992 | -14,992 | 1.7% | 2 | 1.36 | 8 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 982,305 | +3,928 | +426 | +2,883 | -17,695 | 2.6% | 1 | 1.11 | 15 | 13% | 0.39 |
| v2_trend_carry | CHALLENGER | 1,006,381 | +642 | +4,719 | +5,667 | +6,381 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,006,520 | +1,263 | +3,596 | +4,981 | +6,520 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,014,375 | -1,117 | +13,194 | +13,407 | +14,375 | 0.3% | 4 | 2.44 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,004,164 | +166 | +4,262 | +3,450 | +4,164 | 0.0% | 4 | 0.55 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,552 | -225 | +2,845 | +970 | +1,552 | 0.0% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,006,824 | +642 | +4,719 | +6,109 | +6,824 | 0.0% | 3 | 0.44 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,004,340 | +165 | +4,266 | +4,036 | +4,340 | 0.0% | 4 | 0.55 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,003,468 | +672 | +3,740 | +2,754 | +3,468 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 999,408 | +80 | +1,286 | -4,636 | -592 | 0.7% | 3 | 0.44 | 29 | 34% | 0.60 |
| v5_carry_trend_daily_10p | REJECTED | 1,003,752 | +1,269 | +7,360 | -159 | +3,752 | 0.3% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 999,413 | +633 | +4,679 | -3,251 | -587 | 0.6% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 999,331 | +279 | +3,149 | -1,784 | -669 | 0.3% | 4 | 0.62 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,005,082 | +1,147 | +5,129 | +2,514 | +5,082 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,005,082 | +1,147 | +5,129 | +2,514 | +5,082 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,024,736 | +379 | +19,922 | +24,736 | +24,736 | 0.1% | 6 | 2.49 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 993,765 | -518 | +3,826 | -6,235 | -6,235 | 1.0% | 5 | 1.97 | 1 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,014,351 | +1,261 | +11,941 | +14,351 | +14,351 | 0.1% | 5 | 1.93 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,027,786 | +2,834 | +15,825 | +27,786 | +27,786 | 0.0% | 7 | 1.38 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,027,786 | +2,834 | +15,825 | +27,786 | +27,786 | 0.0% | 7 | 1.38 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 979,852 | +2,745 | -3,357 | -31,485 | -20,148 | 3.7% | 5 | 1.88 | 19 | 21% | 0.13 |

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
