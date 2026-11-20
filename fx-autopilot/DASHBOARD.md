# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-20T12:00 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -52,404 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +0 | +8,143 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 983,203 | +0 | -14,352 | -50,518 | -16,797 | 5.4% | 0 | 0.00 | 38 | 47% | 0.82 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,007,215 | -8,757 | -20,216 | -17,058 | +7,215 | 4.3% | 1 | 1.58 | 45 | 49% | 1.05 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,007,010 | +7,371 | +12,129 | +16,707 | +7,010 | 0.0% | 0 | 0.00 | 10 | 50% | 1.29 |
| regime_switch_v1 | RESEARCH_ONLY | 998,500 | +22,829 | +36,805 | -2,010 | -1,500 | 1.9% | 3 | 2.89 | 54 | 28% | 0.71 |
| trend_donchian_v1 | RESEARCH_ONLY | 989,954 | -4,112 | +7,565 | +1,947 | -10,046 | 3.2% | 2 | 1.24 | 20 | 10% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 955,677 | -2,860 | -1,827 | -462 | -44,323 | 4.4% | 1 | 1.83 | 49 | 29% | 0.61 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,044,175 | +11,176 | +20,334 | +29,053 | +44,175 | 0.2% | 3 | 2.07 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -4,252 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,001,806 | -937 | -9,617 | -6,423 | +1,806 | 2.5% | 5 | 2.02 | 581 | 48% | 0.98 |
| v12_carry_timed | REJECTED | 1,019,160 | -1,932 | -3,828 | +19,160 | +19,160 | 0.6% | 5 | 2.21 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,010,925 | +2,081 | +1,723 | +10,925 | +10,925 | 0.1% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,039,042 | +11,651 | +19,638 | +39,042 | +39,042 | 0.0% | 6 | 2.62 | 0 | — | — |
| v14_term | REJECTED | 995,101 | +844 | -2,107 | -4,899 | -4,899 | 0.8% | 3 | 1.31 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,020,969 | +4,238 | +8,132 | +20,969 | +20,969 | 0.1% | 2 | 0.93 | 0 | — | — |
| v16_equity_rebal | REJECTED | 973,218 | -2,133 | -7,487 | -26,782 | -26,782 | 3.1% | 1 | 0.36 | 2 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 985,176 | -7,048 | -13,019 | -14,824 | -14,824 | 2.2% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,008,319 | +2,305 | +5,393 | +8,319 | +8,319 | 0.1% | 3 | 0.60 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,007,314 | +9,056 | +16,435 | +14,074 | +7,314 | 0.0% | 4 | 2.63 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 991,592 | +3,151 | +8,009 | -8,408 | -8,408 | 1.0% | 1 | 0.64 | 9 | 11% | 0.12 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 995,411 | +7,304 | +14,847 | +19,850 | -4,589 | 1.4% | 2 | 2.28 | 18 | 22% | 0.74 |
| v2_trend_carry | CHALLENGER | 1,008,514 | +473 | +2,443 | +9,595 | +8,514 | 0.1% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,011,336 | +3,423 | +5,909 | +12,215 | +11,336 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,005,269 | -11,266 | -10,968 | +7,240 | +5,269 | 1.2% | 4 | 2.46 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,002,943 | -1,985 | -1,224 | +4,024 | +2,943 | 0.2% | 4 | 0.66 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,000,452 | -1,056 | -1,275 | +1,129 | +452 | 0.2% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,006,672 | -1,985 | +159 | +7,216 | +6,672 | 0.2% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,003,032 | -1,988 | -1,312 | +5,085 | +3,032 | 0.2% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,004,845 | +422 | +1,691 | +5,390 | +4,845 | 0.1% | 4 | 0.65 | 2 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 999,136 | -1,953 | -181 | -2,605 | -864 | 0.7% | 4 | 0.65 | 29 | 34% | 0.60 |
| v5_carry_trend_daily_10p | REJECTED | 1,005,078 | +163 | +1,962 | +10,507 | +5,078 | 0.2% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,000,841 | +405 | +1,665 | +7,526 | +841 | 0.5% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,002,016 | +2,626 | +3,088 | +5,437 | +2,016 | 0.0% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,009,146 | +2,381 | +4,953 | +12,148 | +9,146 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,009,146 | +2,381 | +4,953 | +12,148 | +9,146 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,020,910 | -4,122 | -4,369 | +20,910 | +20,910 | 0.6% | 5 | 2.17 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 990,289 | -1,091 | -3,671 | -9,711 | -9,711 | 1.3% | 4 | 1.64 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,011,613 | -736 | -2,518 | +11,613 | +11,613 | 0.4% | 4 | 1.61 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,036,155 | +3,757 | +9,675 | +36,155 | +36,155 | 0.3% | 7 | 1.37 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,036,155 | +3,757 | +9,675 | +36,155 | +36,155 | 0.3% | 7 | 1.37 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 989,999 | +6,698 | +11,581 | +3,558 | -10,001 | 2.7% | 6 | 2.22 | 19 | 21% | 0.13 |

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
