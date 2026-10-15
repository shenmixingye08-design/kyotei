# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-10-15T04:53 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 958,635 | +2,979 | -34,138 | -41,365 | -41,365 | 5.7% | 1 | 1.66 | 71 | 42% | 0.70 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,660 | +660 | +660 | +660 | +660 | 0.0% | 1 | 1.88 | 0 | — | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,038,983 | +13,248 | +23,348 | +38,983 | +38,983 | 0.0% | 0 | 0.00 | 21 | 71% | 2.47 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,032,439 | +16,803 | +25,181 | +32,439 | +32,439 | 0.0% | 1 | 1.20 | 14 | 64% | 2.39 |
| mtf_pullback_v1 | RESEARCH_ONLY | 995,410 | +0 | -4,264 | -4,590 | -4,590 | 0.8% | 0 | 0.00 | 3 | 33% | 0.51 |
| regime_switch_v1 | RESEARCH_ONLY | 1,006,386 | +33,114 | +21,593 | +6,386 | +6,386 | 0.8% | 2 | 2.97 | 19 | 21% | 0.60 |
| trend_donchian_v1 | RESEARCH_ONLY | 987,985 | -10,453 | -24,748 | -12,015 | -12,015 | 3.4% | 1 | 1.63 | 8 | 0% | 0.00 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 952,036 | -13,519 | -22,617 | -47,964 | -47,964 | 4.8% | 2 | 3.00 | 16 | 12% | 0.03 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,015,102 | -1,552 | +281 | +15,102 | +15,102 | 0.4% | 1 | 0.47 | 3 | 67% | 5.81 |
| v10_carry_vix | REJECTED | 1,000,660 | -5,948 | -5,649 | +660 | +660 | 1.1% | 6 | 2.30 | 0 | — | — |
| v11_intraday_region | REJECTED | 1,017,996 | +8,618 | +14,993 | +17,996 | +17,996 | 0.0% | 2 | 0.78 | 193 | 56% | 1.40 |
| v12_carry_timed | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 991,011 | -5,883 | -6,134 | -8,989 | -8,989 | 1.4% | 4 | 3.05 | 0 | — | — |
| v2_h4_ema | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 979,422 | +0 | -15,209 | -20,578 | -20,578 | 2.9% | 0 | 0.00 | 10 | 10% | 0.30 |
| v2_trend_carry | CHALLENGER | 999,531 | -320 | -469 | -469 | -469 | 0.2% | 1 | 0.18 | 0 | — | — |
| v2_xpair_strength | REJECTED | 999,709 | -79 | -291 | -291 | -291 | 0.2% | 2 | 0.35 | 0 | — | — |
| v3_carry_only | REJECTED | 996,896 | -2,418 | -3,104 | -3,104 | -3,104 | 0.8% | 2 | 1.42 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,531 | -320 | -469 | -469 | -469 | 0.2% | 1 | 0.18 | 0 | — | — |
| v3_carry_trend_mh | REJECTED | 999,399 | -320 | -469 | -601 | -601 | 0.2% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 999,531 | -320 | -469 | -469 | -469 | 0.2% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 999,330 | +345 | -670 | -670 | -670 | 0.2% | 2 | 0.29 | 1 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 999,531 | -320 | -469 | -469 | -469 | 0.2% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,002,004 | -1,228 | -2,719 | +2,004 | +2,004 | 0.4% | 4 | 0.56 | 3 | 33% | 0.41 |
| v5_carry_trend_daily_10p | REJECTED | 999,969 | -1,077 | -3,132 | -31 | -31 | 0.7% | 4 | 0.74 | 1 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 998,724 | -1,073 | -2,913 | -1,276 | -1,276 | 0.7% | 4 | 0.74 | 0 | — | — |
| v6_carry_trend_daily_mkt_7p | REJECTED | 998,213 | +272 | -1,229 | -1,787 | -1,787 | 0.4% | 3 | 0.56 | 1 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 999,664 | +270 | -216 | -336 | -336 | 0.4% | 3 | 0.56 | 1 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 999,664 | +270 | -216 | -336 | -336 | 0.4% | 3 | 0.56 | 1 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 1,001,266 | -1,278 | -7,300 | +1,266 | +1,266 | 1.6% | 5 | 1.89 | 0 | — | — |

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
