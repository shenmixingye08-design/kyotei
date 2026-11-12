# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-12T01:08 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | -7,006 | -12,433 | -91,123 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +8,143 | +8,271 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 997,555 | +2,022 | -5,063 | -25,498 | -2,445 | 4.1% | 0 | 0.00 | 35 | 51% | 0.97 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,033,705 | -16,039 | +6,675 | +24,940 | +33,705 | 1.8% | 1 | 1.05 | 37 | 57% | 1.46 |
| mtf_pullback_v1 | RESEARCH_ONLY | 994,881 | +0 | -5,120 | -4,792 | -5,119 | 0.9% | 0 | 0.00 | 8 | 38% | 0.79 |
| regime_switch_v1 | RESEARCH_ONLY | 955,458 | -12,894 | -14,244 | -23,405 | -44,542 | 6.2% | 2 | 2.33 | 49 | 27% | 0.61 |
| trend_donchian_v1 | RESEARCH_ONLY | 976,286 | +11,916 | +10,701 | -36,939 | -23,714 | 4.5% | 3 | 3.25 | 18 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 959,852 | +16,395 | +8,283 | -8,879 | -40,148 | 4.0% | 2 | 2.92 | 44 | 27% | 0.51 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,020,357 | +1,794 | +3,181 | +2,933 | +20,357 | 0.6% | 1 | 0.43 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -15,986 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,011,199 | +1,088 | +9,516 | -4,307 | +11,199 | 1.6% | 1 | 0.35 | 486 | 49% | 1.10 |
| v12_carry_timed | REJECTED | 1,021,103 | +11,736 | +21,441 | +21,103 | +21,103 | 0.1% | 6 | 2.53 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,007,394 | +6,824 | +9,382 | +7,394 | +7,394 | 0.1% | 3 | 1.17 | 0 | — | — |
| v13_ratemom | REJECTED | 1,014,915 | +5,841 | +25,859 | +14,915 | +14,915 | 0.1% | 6 | 2.68 | 0 | — | — |
| v14_term | REJECTED | 999,608 | +3,374 | -1,429 | -392 | -392 | 0.3% | 6 | 2.39 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,009,065 | +5,791 | +13,999 | +9,065 | +9,065 | 0.1% | 2 | 0.95 | 0 | — | — |
| v16_equity_rebal | REJECTED | 986,880 | -4,925 | -16,230 | -13,120 | -13,120 | 1.7% | 3 | 1.02 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,001,245 | +2,784 | -3,639 | +1,245 | +1,245 | 0.6% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,469 | +801 | +469 | +469 | +469 | 0.0% | 2 | 0.39 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 988,972 | +7,031 | +2,363 | -7,850 | -11,028 | 1.6% | 4 | 3.03 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 982,958 | -690 | -12,346 | -17,042 | -17,042 | 1.9% | 2 | 1.37 | 7 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 974,181 | +0 | -3,619 | -15,174 | -25,819 | 3.5% | 0 | 0.00 | 15 | 13% | 0.39 |
| v2_trend_carry | CHALLENGER | 1,004,302 | +2,581 | +6,831 | +4,302 | +4,302 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,003,450 | +1,787 | +5,816 | +3,450 | +3,450 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,014,243 | +9,305 | +14,594 | +14,243 | +14,243 | 0.2% | 4 | 2.44 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,003,149 | +2,793 | +5,274 | +3,149 | +3,149 | 0.0% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,581 | +2,338 | +2,571 | +1,714 | +1,581 | 0.0% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,004,744 | +2,581 | +6,831 | +4,744 | +4,744 | 0.0% | 3 | 0.44 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,003,325 | +2,796 | +5,279 | +3,522 | +3,325 | 0.0% | 4 | 0.55 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,002,011 | +2,126 | +1,980 | +2,011 | +2,011 | 0.0% | 2 | 0.33 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 998,762 | +2,208 | -2,740 | -7,135 | -1,238 | 0.7% | 3 | 0.44 | 25 | 28% | 0.46 |
| v5_carry_trend_daily_10p | REJECTED | 1,000,759 | +4,176 | +8,653 | -3,127 | +759 | 0.6% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 997,586 | +3,494 | +7,855 | -5,052 | -2,414 | 0.8% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 998,393 | +2,524 | +3,253 | -1,132 | -1,607 | 0.3% | 4 | 0.62 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,002,037 | +2,754 | +7,352 | +2,157 | +2,037 | 0.1% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,002,037 | +2,754 | +7,352 | +2,157 | +2,037 | 0.1% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,023,471 | +11,727 | +23,523 | +23,471 | +23,471 | 0.1% | 6 | 2.49 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 995,420 | +4,753 | -5,825 | -4,580 | -4,580 | 0.8% | 6 | 2.41 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,011,488 | +9,779 | +11,715 | +11,488 | +11,488 | 0.1% | 5 | 1.93 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,020,696 | +8,487 | +23,265 | +20,696 | +20,696 | 0.0% | 7 | 1.39 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,020,696 | +8,487 | +23,265 | +20,696 | +20,696 | 0.0% | 7 | 1.39 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 971,757 | -463 | -7,775 | -39,534 | -28,243 | 4.5% | 6 | 2.27 | 18 | 17% | 0.11 |

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
