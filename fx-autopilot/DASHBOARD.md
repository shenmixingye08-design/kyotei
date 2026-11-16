# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-16T06:39 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | -14,420 | -88,857 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +8,143 | +8,143 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 992,931 | -1,208 | -4,856 | -40,791 | -7,069 | 4.5% | 0 | 0.00 | 36 | 50% | 0.92 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,031,073 | +3,576 | -6,806 | -819 | +31,073 | 2.0% | 1 | 1.86 | 39 | 54% | 1.32 |
| mtf_pullback_v1 | RESEARCH_ONLY | 994,881 | +0 | -5,120 | +4,579 | -5,119 | 0.9% | 0 | 0.00 | 8 | 38% | 0.79 |
| regime_switch_v1 | RESEARCH_ONLY | 966,497 | +3,407 | -3,204 | -37,925 | -33,503 | 5.1% | 3 | 2.95 | 51 | 25% | 0.59 |
| trend_donchian_v1 | RESEARCH_ONLY | 983,385 | +338 | +23,940 | -1,356 | -16,615 | 3.8% | 3 | 2.87 | 19 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 958,819 | +579 | +1,331 | -399 | -41,181 | 4.1% | 1 | 1.10 | 46 | 28% | 0.57 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,026,082 | +1,244 | +8,906 | +9,935 | +26,082 | 0.0% | 1 | 0.42 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -3,414 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,008,347 | -1,212 | +4,169 | -3,681 | +8,347 | 1.9% | 5 | 1.76 | 516 | 48% | 1.08 |
| v12_carry_timed | REJECTED | 1,020,135 | -1,864 | +15,983 | +20,135 | +20,135 | 0.3% | 6 | 2.54 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,008,412 | -1,321 | +10,319 | +8,412 | +8,412 | 0.2% | 3 | 1.17 | 0 | — | — |
| v13_ratemom | REJECTED | 1,024,480 | +2,081 | +18,347 | +24,480 | +24,480 | 0.0% | 6 | 2.65 | 0 | — | — |
| v14_term | REJECTED | 994,131 | -1,234 | -479 | -5,869 | -5,869 | 0.9% | 4 | 1.64 | 2 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,014,728 | +322 | +12,185 | +14,728 | +14,728 | 0.0% | 2 | 0.94 | 0 | — | — |
| v16_equity_rebal | REJECTED | 976,833 | -1,331 | -16,304 | -23,167 | -23,167 | 2.7% | 2 | 0.70 | 1 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 992,995 | -2,558 | -3,281 | -7,005 | -7,005 | 1.4% | 3 | 1.08 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,004,508 | +658 | +5,321 | +4,508 | +4,508 | 0.0% | 2 | 0.39 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 995,142 | +393 | +10,277 | +9,736 | -4,858 | 1.0% | 3 | 2.24 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 986,528 | +1,471 | -1,892 | -13,472 | -13,472 | 1.5% | 2 | 1.36 | 8 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 986,194 | +3,127 | +5,937 | +10,634 | -13,806 | 2.3% | 1 | 1.11 | 15 | 13% | 0.39 |
| v2_trend_carry | CHALLENGER | 1,006,642 | +120 | +5,667 | +7,292 | +6,642 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,007,376 | +621 | +5,109 | +8,381 | +7,376 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,012,193 | -2,234 | +11,959 | +14,766 | +12,193 | 0.5% | 4 | 2.45 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,003,875 | -344 | +4,424 | +4,525 | +3,875 | 0.1% | 4 | 0.55 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,000,878 | -654 | +2,293 | +1,660 | +878 | 0.1% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,007,085 | +120 | +5,667 | +7,735 | +7,085 | 0.0% | 3 | 0.44 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,004,050 | -345 | +4,428 | +4,824 | +4,050 | 0.1% | 4 | 0.55 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,003,733 | +124 | +4,347 | +4,383 | +3,733 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 999,676 | +127 | +1,913 | -2,674 | -324 | 0.6% | 3 | 0.44 | 29 | 34% | 0.60 |
| v5_carry_trend_daily_10p | REJECTED | 1,003,527 | -136 | +8,453 | +6,365 | +3,527 | 0.3% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 999,438 | -39 | +6,082 | +3,528 | -562 | 0.6% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 999,020 | -374 | +3,055 | +2,794 | -980 | 0.3% | 4 | 0.62 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,005,708 | +402 | +6,613 | +8,030 | +5,708 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,005,708 | +402 | +6,613 | +8,030 | +5,708 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,022,185 | -2,139 | +18,450 | +22,185 | +22,185 | 0.4% | 6 | 2.49 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 992,011 | -1,904 | +753 | -7,989 | -7,989 | 1.1% | 5 | 1.97 | 1 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,012,297 | -1,793 | +13,077 | +12,297 | +12,297 | 0.3% | 5 | 1.93 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,028,574 | +829 | +20,419 | +28,574 | +28,574 | 0.0% | 7 | 1.38 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,028,574 | +829 | +20,419 | +28,574 | +28,574 | 0.0% | 7 | 1.38 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 980,862 | +748 | +1,992 | -11,477 | -19,138 | 3.6% | 6 | 2.24 | 19 | 21% | 0.13 |

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
