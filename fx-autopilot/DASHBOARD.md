# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-10-22T21:51 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 911,144 | -2,985 | -47,806 | -88,856 | -88,856 | 10.3% | 1 | 1.69 | 108 | 40% | 0.60 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,023,878 | -9,843 | -15,105 | +23,878 | +23,878 | 1.5% | 0 | 0.00 | 24 | 62% | 1.57 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,018,244 | -6,872 | -15,180 | +18,244 | +18,244 | 2.1% | 1 | 1.31 | 21 | 52% | 1.33 |
| mtf_pullback_v1 | RESEARCH_ONLY | 990,302 | +0 | -5,107 | -9,698 | -9,698 | 1.3% | 0 | 0.00 | 4 | 25% | 0.33 |
| regime_switch_v1 | RESEARCH_ONLY | 997,332 | -4,554 | -8,329 | -2,668 | -2,668 | 2.1% | 1 | 1.06 | 29 | 34% | 0.95 |
| trend_donchian_v1 | RESEARCH_ONLY | 982,508 | -4,053 | -6,508 | -17,492 | -17,492 | 3.9% | 3 | 2.21 | 11 | 9% | 0.22 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 969,483 | +15,757 | +14,212 | -30,517 | -30,517 | 3.1% | 2 | 3.29 | 25 | 20% | 0.25 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,020,846 | +5,992 | +4,847 | +20,846 | +20,846 | 0.1% | 2 | 1.04 | 4 | 75% | 6.25 |
| v10_carry_vix | REJECTED | 993,192 | -3,486 | -5,358 | -6,808 | -6,808 | 1.9% | 6 | 2.50 | 1 | 100% | — |
| v11_intraday_region | REJECTED | 1,013,548 | +3,010 | -5,782 | +13,548 | +13,548 | 0.6% | 0 | 0.00 | 276 | 54% | 1.22 |
| v12_carry_timed | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 992,793 | +264 | +6,042 | -7,207 | -7,207 | 1.2% | 2 | 1.67 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 999,630 | +57 | -370 | -370 | -370 | 0.1% | 2 | 1.29 | 0 | — | — |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 975,561 | +0 | -6,642 | -24,439 | -24,439 | 3.3% | 0 | 0.00 | 11 | 9% | 0.26 |
| v2_trend_carry | CHALLENGER | 999,406 | +385 | -237 | -594 | -594 | 0.2% | 2 | 0.29 | 0 | — | — |
| v2_xpair_strength | REJECTED | 1,001,031 | +1,999 | +1,460 | +1,031 | +1,031 | 0.1% | 2 | 0.35 | 0 | — | — |
| v3_carry_only | REJECTED | 991,151 | -7,428 | -6,841 | -8,849 | -8,849 | 1.3% | 3 | 1.86 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,406 | +385 | -237 | -594 | -594 | 0.2% | 2 | 0.29 | 0 | — | — |
| v3_carry_trend_mh | REJECTED | 999,606 | +265 | +96 | -394 | -394 | 0.2% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 999,739 | +265 | +96 | -261 | -261 | 0.2% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 998,308 | +260 | -1,625 | -1,692 | -1,692 | 0.3% | 1 | 0.18 | 2 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 999,739 | +265 | +96 | -261 | -261 | 0.2% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 999,432 | -2,356 | -2,940 | -568 | -568 | 0.7% | 2 | 0.39 | 12 | 33% | 0.30 |
| v5_carry_trend_daily_10p | REJECTED | 993,524 | -1,002 | -5,919 | -6,476 | -6,476 | 1.3% | 4 | 0.74 | 1 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 992,278 | -992 | -5,915 | -7,722 | -7,722 | 1.3% | 4 | 0.74 | 0 | — | — |
| v6_carry_trend_daily_mkt_7p | REJECTED | 998,509 | +2,018 | +875 | -1,491 | -1,491 | 0.3% | 2 | 0.35 | 2 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 998,927 | +2,018 | -159 | -1,073 | -1,073 | 0.4% | 2 | 0.35 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 998,927 | +2,018 | -159 | -1,073 | -1,073 | 0.4% | 2 | 0.35 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 985,740 | -85 | -13,537 | -14,260 | -14,260 | 3.1% | 3 | 0.86 | 3 | 0% | 0.00 |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.96 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -3.2% | 0.83 | -0.59 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -4.6% | 0.92 | -0.50 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.75 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -8.5% | 0.73 | -1.25 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.24 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.66 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.17 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -7.7% | 0.65 | -1.05 | 1.09 |
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
