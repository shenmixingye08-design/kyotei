# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-19T11:56 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -74,815 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +0 | +8,143 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 983,203 | -13,380 | -14,352 | -50,518 | -16,797 | 5.4% | 0 | 0.00 | 38 | 47% | 0.82 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,015,972 | +5,254 | -17,072 | -19,846 | +15,972 | 3.4% | 1 | 1.05 | 44 | 50% | 1.10 |
| mtf_pullback_v1 | RESEARCH_ONLY | 999,639 | +0 | +4,758 | +9,336 | -361 | 0.4% | 0 | 0.00 | 9 | 44% | 0.99 |
| regime_switch_v1 | RESEARCH_ONLY | 975,671 | -940 | +18,309 | -30,395 | -24,329 | 4.2% | 2 | 1.66 | 52 | 27% | 0.62 |
| trend_donchian_v1 | RESEARCH_ONLY | 994,066 | +7,542 | +17,596 | +12,336 | -5,934 | 2.8% | 3 | 2.83 | 19 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 958,538 | +4,355 | +1,963 | +12,785 | -41,462 | 4.1% | 1 | 2.16 | 48 | 29% | 0.62 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,032,999 | -1,322 | +11,955 | +15,774 | +32,999 | 0.9% | 3 | 2.09 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -1,634 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,002,744 | -5,115 | -5,496 | -8,655 | +2,744 | 2.4% | 5 | 2.19 | 566 | 49% | 1.08 |
| v12_carry_timed | REJECTED | 1,021,092 | -912 | +2,094 | +21,092 | +21,092 | 0.4% | 5 | 2.21 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,008,844 | -1,424 | +2,719 | +8,844 | +8,844 | 0.3% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,027,391 | -3,717 | +12,372 | +27,391 | +27,391 | 0.8% | 6 | 2.65 | 0 | — | — |
| v14_term | REJECTED | 994,257 | -751 | -2,758 | -5,743 | -5,743 | 0.8% | 3 | 1.31 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,016,731 | -1,437 | +7,781 | +16,731 | +16,731 | 0.4% | 2 | 0.94 | 0 | — | — |
| v16_equity_rebal | REJECTED | 975,351 | +1,817 | -11,274 | -24,649 | -24,649 | 2.9% | 1 | 0.36 | 2 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 992,224 | +2,669 | -7,585 | -7,776 | -7,776 | 1.5% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,006,014 | +49 | +5,250 | +6,014 | +6,014 | 0.2% | 2 | 0.39 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 998,258 | -5,142 | +11,405 | +7,100 | -1,742 | 0.8% | 4 | 2.66 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 988,441 | -3,297 | +5,286 | -11,559 | -11,559 | 1.3% | 1 | 0.64 | 9 | 11% | 0.12 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 988,107 | -5,632 | +14,517 | +12,546 | -11,893 | 2.1% | 1 | 1.06 | 18 | 22% | 0.74 |
| v2_trend_carry | CHALLENGER | 1,008,041 | +385 | +3,751 | +8,173 | +8,041 | 0.1% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,007,914 | -1,497 | +4,377 | +8,092 | +7,914 | 0.3% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,016,535 | +4,959 | +3,358 | +17,332 | +16,535 | 0.1% | 4 | 2.44 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,004,927 | +1,132 | +2,052 | +5,060 | +4,927 | 0.0% | 4 | 0.65 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,508 | +489 | +371 | +1,772 | +1,508 | 0.0% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,008,657 | +1,132 | +3,924 | +8,789 | +8,657 | 0.0% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,005,020 | +1,134 | +1,969 | +5,886 | +5,020 | 0.0% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,004,423 | -47 | +2,594 | +4,555 | +4,423 | 0.1% | 3 | 0.44 | 2 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 1,001,089 | +1,114 | +2,773 | -1,108 | +1,089 | 0.5% | 4 | 0.65 | 29 | 34% | 0.60 |
| v5_carry_trend_daily_10p | REJECTED | 1,004,915 | -310 | +4,556 | +9,474 | +4,915 | 0.2% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,000,436 | -418 | +3,162 | +6,251 | +436 | 0.5% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 999,390 | -1,095 | +1,475 | +2,116 | -610 | 0.2% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,006,764 | -873 | +4,771 | +8,416 | +6,764 | 0.2% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,006,764 | -873 | +4,771 | +8,416 | +6,764 | 0.2% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,025,032 | +1,145 | +3,793 | +25,032 | +25,032 | 0.2% | 5 | 2.16 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 991,379 | -1,422 | -1,034 | -8,621 | -8,621 | 1.2% | 4 | 1.64 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,012,349 | -1,856 | +2,720 | +12,349 | +12,349 | 0.3% | 4 | 1.60 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,032,398 | -136 | +11,948 | +32,398 | +32,398 | 0.5% | 7 | 1.37 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,032,398 | -136 | +11,948 | +32,398 | +32,398 | 0.5% | 7 | 1.37 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 983,301 | -4,803 | +12,621 | -4,232 | -16,699 | 3.3% | 6 | 2.24 | 19 | 21% | 0.13 |

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
