# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-10-30T01:14 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 884,182 | +1,155 | -26,112 | -130,084 | -115,818 | 13.0% | 1 | 1.51 | 136 | 38% | 0.58 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,015,790 | -2,865 | -8,088 | +15,234 | +15,790 | 2.3% | 1 | 1.66 | 25 | 60% | 1.40 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,022,041 | +0 | +3,423 | +21,247 | +22,041 | 1.8% | 0 | 0.00 | 25 | 56% | 1.41 |
| mtf_pullback_v1 | RESEARCH_ONLY | 992,880 | +7,257 | +2,578 | -2,100 | -7,120 | 1.1% | 0 | 0.00 | 6 | 33% | 0.63 |
| regime_switch_v1 | RESEARCH_ONLY | 975,427 | +0 | -23,483 | -18,731 | -24,573 | 4.2% | 0 | 0.00 | 36 | 28% | 0.71 |
| trend_donchian_v1 | RESEARCH_ONLY | 965,039 | -9,256 | -19,690 | -39,953 | -34,961 | 5.6% | 1 | 0.73 | 15 | 13% | 0.20 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 962,714 | -1,058 | -11,679 | -32,418 | -37,286 | 3.7% | 1 | 1.65 | 29 | 31% | 0.50 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,020,496 | -3,518 | -998 | +17,601 | +20,496 | 0.6% | 2 | 1.04 | 4 | 75% | 6.25 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -10,125 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,021,618 | -6,200 | +8,889 | +18,464 | +21,618 | 0.6% | 5 | 1.94 | 351 | 53% | 1.31 |
| v12_carry_timed | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 994,982 | -7,432 | +2,394 | -5,225 | -5,018 | 1.0% | 2 | 1.66 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 996,859 | -2,433 | -3,815 | -3,141 | -3,141 | 0.5% | 1 | 0.67 | 1 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 974,500 | +0 | -1,061 | -23,031 | -25,500 | 3.4% | 0 | 0.00 | 12 | 8% | 0.25 |
| v2_trend_carry | CHALLENGER | 999,612 | -915 | +221 | -388 | -388 | 0.2% | 1 | 0.18 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,000,914 | -1,172 | -334 | +914 | +914 | 0.2% | 2 | 0.35 | 0 | — | — |
| v3_carry_only | REJECTED | 995,658 | -2,887 | +5,981 | -4,342 | -4,342 | 0.9% | 3 | 1.85 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,612 | -915 | +221 | -388 | -388 | 0.2% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 999,922 | -915 | +362 | -110 | -78 | 0.1% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,000,055 | -915 | +362 | +55 | +55 | 0.1% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 998,400 | -915 | +138 | -1,600 | -1,600 | 0.3% | 1 | 0.18 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,000,055 | -915 | +362 | +55 | +55 | 0.1% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,000,534 | -2,089 | +1,112 | -1,031 | +534 | 0.6% | 4 | 0.66 | 13 | 31% | 0.28 |
| v5_carry_trend_daily_10p | REJECTED | 994,113 | -2,919 | +822 | -7,032 | -5,887 | 1.2% | 4 | 0.74 | 1 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 992,126 | -2,688 | +79 | -7,876 | -7,874 | 1.3% | 4 | 0.59 | 1 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 998,436 | -1,165 | -296 | -1,599 | -1,564 | 0.3% | 2 | 0.35 | 2 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 998,854 | -1,165 | -296 | -1,180 | -1,146 | 0.4% | 2 | 0.36 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 998,854 | -1,165 | -296 | -1,180 | -1,146 | 0.4% | 2 | 0.36 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 982,010 | -2,755 | -3,661 | -20,976 | -17,990 | 3.5% | 4 | 1.64 | 7 | 0% | 0.00 |

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
