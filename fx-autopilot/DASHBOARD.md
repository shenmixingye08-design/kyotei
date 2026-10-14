# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-10-14T09:04 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 952,846 | +3,693 | -37,760 | -47,154 | -47,154 | 6.2% | 2 | 4.91 | 62 | 39% | 0.63 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,025,735 | +0 | +10,708 | +25,735 | +25,735 | 0.0% | 0 | 0.00 | 20 | 70% | 1.97 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,015,635 | +1,393 | +10,020 | +15,635 | +15,635 | 0.0% | 0 | 0.00 | 12 | 58% | 1.68 |
| mtf_pullback_v1 | RESEARCH_ONLY | 995,410 | -2,662 | -4,264 | -4,590 | -4,590 | 0.8% | 0 | 0.00 | 3 | 33% | 0.51 |
| regime_switch_v1 | RESEARCH_ONLY | 975,478 | +2,072 | -20,380 | -24,522 | -24,522 | 3.9% | 2 | 2.91 | 14 | 21% | 0.33 |
| trend_donchian_v1 | RESEARCH_ONLY | 1,002,677 | -3,719 | -10,416 | +2,677 | +2,677 | 2.0% | 2 | 3.49 | 6 | 0% | 0.00 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 963,362 | -1,579 | -12,990 | -36,638 | -36,638 | 3.7% | 3 | 4.97 | 11 | 9% | 0.05 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,016,984 | +397 | +328 | +16,984 | +16,984 | 0.2% | 1 | 0.47 | 3 | 67% | 5.81 |
| v10_carry_vix | REJECTED | 1,008,268 | +362 | +2,653 | +8,268 | +8,268 | 0.2% | 6 | 2.28 | 0 | — | — |
| v11_intraday_region | REJECTED | 1,010,762 | -1,034 | +9,654 | +10,762 | +10,762 | 0.5% | 5 | 2.02 | 183 | 55% | 1.24 |
| v12_carry_timed | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 999,539 | +2,764 | +2,698 | -461 | -461 | 0.1% | 4 | 3.02 | 0 | — | — |
| v2_h4_ema | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 979,422 | -7,142 | -18,004 | -20,578 | -20,578 | 2.9% | 0 | 0.00 | 10 | 10% | 0.30 |
| v2_trend_carry | CHALLENGER | 999,980 | -20 | -20 | -20 | -20 | 0.0% | 1 | 0.18 | 0 | — | — |
| v2_xpair_strength | REJECTED | 999,918 | -82 | -82 | -82 | -82 | 0.0% | 2 | 0.35 | 0 | — | — |
| v3_carry_only | REJECTED | 999,962 | -38 | -38 | -38 | -38 | 0.0% | 2 | 1.42 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,980 | -20 | -20 | -20 | -20 | 0.0% | 1 | 0.18 | 0 | — | — |
| v3_carry_trend_mh | REJECTED | 999,848 | -20 | -20 | -152 | -152 | 0.0% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 999,980 | -20 | -20 | -20 | -20 | 0.0% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 998,931 | -669 | -1,069 | -1,069 | -1,069 | 0.1% | 2 | 0.29 | 1 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 999,980 | -20 | -20 | -20 | -20 | 0.0% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,003,543 | -1,038 | -801 | +3,543 | +3,543 | 0.3% | 4 | 0.56 | 3 | 33% | 0.41 |
| v5_carry_trend_daily_10p | REJECTED | 1,001,631 | -1,440 | -667 | +1,631 | +1,631 | 0.3% | 4 | 0.74 | 1 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,000,381 | -1,443 | -451 | +381 | +381 | 0.3% | 4 | 0.74 | 0 | — | — |
| v6_carry_trend_daily_mkt_7p | REJECTED | 998,255 | -754 | -785 | -1,745 | -1,745 | 0.2% | 3 | 0.56 | 1 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 999,708 | -173 | -173 | -292 | -292 | 0.0% | 3 | 0.56 | 1 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 999,708 | -173 | -173 | -292 | -292 | 0.0% | 3 | 0.56 | 1 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 1,004,006 | -4,277 | -1,985 | +4,006 | +4,006 | 0.8% | 5 | 1.89 | 0 | — | — |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.96 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -3.2% | 0.83 | -0.60 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -5.6% | 0.90 | -0.63 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.75 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -7.6% | 0.75 | -1.13 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.25 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.67 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.18 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -7.7% | 0.65 | -1.06 | 1.09 |
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
