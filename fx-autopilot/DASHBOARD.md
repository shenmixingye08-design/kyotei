# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-03T11:03 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 880,226 | +3,971 | -12,440 | -124,651 | -119,774 | 13.4% | 1 | 1.38 | 146 | 38% | 0.58 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,021,054 | +5,188 | +2,400 | +21,169 | +21,054 | 1.8% | 0 | 0.00 | 28 | 61% | 1.41 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,026,663 | +5,254 | -768 | +17,154 | +26,663 | 1.3% | 3 | 4.23 | 25 | 56% | 1.41 |
| mtf_pullback_v1 | RESEARCH_ONLY | 992,880 | +0 | +7,257 | -143 | -7,120 | 1.1% | 0 | 0.00 | 6 | 33% | 0.63 |
| regime_switch_v1 | RESEARCH_ONLY | 983,581 | +2,383 | -4,832 | -12,144 | -16,419 | 3.4% | 0 | 0.00 | 39 | 31% | 0.82 |
| trend_donchian_v1 | RESEARCH_ONLY | 960,910 | -2,805 | -13,179 | -44,427 | -39,090 | 6.0% | 3 | 2.65 | 16 | 12% | 0.19 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 944,150 | -4,774 | -19,882 | -36,685 | -55,850 | 5.6% | 2 | 2.81 | 35 | 26% | 0.37 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,017,176 | +0 | -7,516 | +9,181 | +17,176 | 0.9% | 0 | 0.00 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -9,298 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,014,679 | -2,285 | -9,244 | +7,428 | +14,679 | 1.3% | 5 | 2.22 | 386 | 51% | 1.19 |
| v12_carry_timed | REJECTED | 999,169 | -831 | -831 | -831 | -831 | 0.1% | 6 | 2.59 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 999,509 | -491 | -491 | -491 | -491 | 0.1% | 3 | 1.18 | 0 | — | — |
| v13_ratemom | REJECTED | 997,778 | -2,222 | -2,222 | -2,222 | -2,222 | 0.3% | 6 | 2.72 | 0 | — | — |
| v14_term | REJECTED | 997,017 | -2,983 | -2,983 | -2,983 | -2,983 | 0.3% | 6 | 2.40 | 0 | — | — |
| v14_term_ratemom | REJECTED | 999,833 | -167 | -167 | -167 | -167 | 0.1% | 2 | 0.95 | 0 | — | — |
| v16_equity_rebal | REJECTED | 999,697 | -303 | -303 | -303 | -303 | 0.1% | 3 | 1.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,598 | +598 | +598 | +598 | +598 | 0.0% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 990,084 | -2,827 | -9,538 | -4,691 | -9,916 | 1.5% | 2 | 1.67 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 995,510 | -939 | -1,588 | -4,490 | -4,490 | 0.6% | 0 | 0.00 | 2 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 972,799 | -2,342 | -5,712 | -22,046 | -27,201 | 3.6% | 2 | 2.76 | 12 | 8% | 0.25 |
| v2_trend_carry | CHALLENGER | 999,722 | +432 | -772 | -278 | -278 | 0.2% | 1 | 0.18 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,000,285 | +673 | -2,026 | +285 | +285 | 0.3% | 2 | 0.35 | 0 | — | — |
| v3_carry_only | REJECTED | 1,001,145 | +1,763 | +4,198 | +1,145 | +1,145 | 0.3% | 3 | 1.84 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,722 | +432 | -772 | -278 | -278 | 0.2% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,000,032 | +432 | -760 | +619 | +32 | 0.1% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,000,164 | +432 | -760 | +164 | +164 | 0.1% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 998,829 | +751 | -453 | -1,171 | -1,171 | 0.2% | 4 | 0.56 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,000,193 | +461 | -731 | +193 | +193 | 0.1% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,001,211 | -299 | -534 | -1,817 | +1,211 | 0.5% | 3 | 0.48 | 15 | 40% | 0.86 |
| v5_carry_trend_daily_10p | REJECTED | 993,544 | +252 | -2,887 | -8,108 | -6,456 | 1.3% | 4 | 0.59 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 991,654 | +78 | -2,594 | -8,555 | -8,346 | 1.4% | 4 | 0.59 | 1 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 997,875 | +741 | -1,926 | -1,456 | -2,125 | 0.4% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 998,232 | +679 | -1,988 | -1,192 | -1,768 | 0.5% | 2 | 0.36 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 998,232 | +679 | -1,988 | -1,192 | -1,768 | 0.5% | 2 | 0.36 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 999,524 | -476 | -476 | -476 | -476 | 0.1% | 6 | 2.55 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 999,009 | -991 | -991 | -991 | -991 | 0.1% | 6 | 2.40 | 0 | — | — |
| v7_cm_monthly | REJECTED | 999,791 | -209 | -209 | -209 | -209 | 0.1% | 5 | 1.96 | 0 | — | — |
| v8_dollar_carry | REJECTED | 999,868 | -132 | -132 | -132 | -132 | 0.1% | 7 | 1.42 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 999,868 | -132 | -132 | -132 | -132 | 0.1% | 7 | 1.42 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 980,666 | +727 | -5,699 | -23,412 | -19,334 | 3.6% | 5 | 1.87 | 8 | 0% | 0.00 |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.94 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -3.2% | 0.83 | -0.59 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -6.5% | 0.89 | -0.70 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.74 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -8.2% | 0.74 | -1.18 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.22 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.64 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.17 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -7.0% | 0.68 | -0.93 | 1.09 |
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
