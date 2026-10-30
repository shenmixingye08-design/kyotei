# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-10-30T18:31 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 874,003 | -4,600 | -31,571 | -133,055 | -125,997 | 14.0% | 2 | 3.37 | 140 | 38% | 0.57 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,013,819 | -5,511 | -10,059 | +17,937 | +13,819 | 2.5% | 0 | 0.00 | 26 | 58% | 1.27 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,025,536 | +3,495 | +5,778 | +25,443 | +25,536 | 1.4% | 1 | 1.65 | 25 | 56% | 1.41 |
| mtf_pullback_v1 | RESEARCH_ONLY | 992,880 | +0 | +2,578 | -2,100 | -7,120 | 1.1% | 0 | 0.00 | 6 | 33% | 0.63 |
| regime_switch_v1 | RESEARCH_ONLY | 978,992 | +3,565 | -19,828 | -16,366 | -21,008 | 3.9% | 2 | 2.50 | 36 | 28% | 0.71 |
| trend_donchian_v1 | RESEARCH_ONLY | 959,313 | -7,230 | -21,796 | -45,246 | -40,687 | 6.2% | 1 | 0.88 | 16 | 12% | 0.19 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 953,407 | -10,366 | -17,443 | -38,692 | -46,593 | 4.7% | 3 | 3.90 | 31 | 29% | 0.45 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,024,543 | +3,129 | +1,857 | +22,362 | +24,543 | 0.2% | 2 | 1.04 | 4 | 75% | 6.25 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -9,777 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,018,409 | -5,921 | +1,110 | +18,695 | +18,409 | 0.9% | 5 | 1.97 | 361 | 52% | 1.25 |
| v12_carry_timed | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 999,022 | +906 | +2,664 | +5,575 | -978 | 0.6% | 2 | 1.66 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 997,208 | -406 | -3,414 | -2,792 | -2,792 | 0.5% | 1 | 0.67 | 1 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 971,177 | -3,323 | -4,384 | -23,051 | -28,823 | 3.8% | 1 | 1.52 | 12 | 8% | 0.25 |
| v2_trend_carry | CHALLENGER | 1,000,338 | +279 | +780 | +338 | +338 | 0.1% | 1 | 0.18 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,002,263 | +1,044 | +618 | +2,263 | +2,263 | 0.1% | 2 | 0.35 | 0 | — | — |
| v3_carry_only | REJECTED | 997,372 | -1,557 | +5,602 | -2,628 | -2,628 | 0.7% | 3 | 1.85 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,000,338 | +279 | +780 | +338 | +338 | 0.1% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,000,648 | +279 | +676 | +1,248 | +648 | 0.1% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,000,780 | +279 | +676 | +780 | +780 | 0.1% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 999,125 | +279 | +452 | -875 | -875 | 0.2% | 1 | 0.18 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,000,780 | +279 | +676 | +780 | +780 | 0.1% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,001,320 | -449 | +1,811 | -114 | +1,320 | 0.5% | 4 | 0.66 | 13 | 31% | 0.28 |
| v5_carry_trend_daily_10p | REJECTED | 995,049 | -530 | +613 | -7,085 | -4,951 | 1.2% | 3 | 0.43 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 993,244 | -291 | +524 | -7,645 | -6,756 | 1.2% | 4 | 0.59 | 1 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 999,784 | +1,050 | +656 | +382 | -216 | 0.2% | 2 | 0.35 | 2 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,000,203 | +1,050 | +656 | +801 | +203 | 0.3% | 2 | 0.35 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 1,000,203 | +1,050 | +656 | +801 | +203 | 0.3% | 2 | 0.35 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 984,739 | +2,005 | -1,344 | -19,263 | -15,261 | 3.2% | 4 | 1.63 | 7 | 0% | 0.00 |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.95 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -3.2% | 0.83 | -0.59 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -5.6% | 0.91 | -0.60 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.74 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -8.5% | 0.73 | -1.24 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.23 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.65 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.17 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -7.2% | 0.68 | -0.96 | 1.09 |
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
