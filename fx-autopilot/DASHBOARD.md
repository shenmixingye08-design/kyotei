# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-25T19:41 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -44,461 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,009,588 | -356 | +1,318 | +9,460 | +9,588 | 0.1% | 0 | 0.00 | 4 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 977,307 | +1,731 | -15,279 | -47,078 | -22,693 | 6.0% | 1 | 1.96 | 41 | 46% | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,030,830 | +2,170 | +20,111 | +3,399 | +30,830 | 2.0% | 1 | 0.91 | 52 | 52% | 1.20 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,011,443 | -1,853 | +11,804 | +25,820 | +11,443 | 0.3% | 1 | 1.73 | 12 | 50% | 1.32 |
| regime_switch_v1 | RESEARCH_ONLY | 1,001,353 | -1,200 | +22,575 | +2,923 | +1,353 | 1.7% | 0 | 0.00 | 59 | 31% | 1.01 |
| trend_donchian_v1 | RESEARCH_ONLY | 984,598 | +476 | -3,241 | +8,596 | -15,402 | 3.7% | 2 | 1.25 | 22 | 9% | 0.13 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 950,383 | -1,600 | -3,799 | -7,982 | -49,617 | 5.0% | 1 | 1.34 | 50 | 28% | 0.61 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,042,565 | -2,234 | +6,591 | +20,683 | +42,565 | 1.4% | 2 | 1.65 | 7 | 71% | 10.47 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | +0 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,008,443 | +9,458 | -3,123 | -14,197 | +8,443 | 1.9% | 5 | 1.90 | 631 | 48% | 1.00 |
| v12_carry_timed | REJECTED | 1,014,665 | -5,221 | -7,253 | +14,665 | +14,665 | 1.3% | 5 | 2.22 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,005,539 | -2,884 | -4,838 | +5,539 | +5,539 | 0.9% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,025,827 | -4,674 | -6,695 | +25,827 | +25,827 | 2.1% | 5 | 2.30 | 1 | 0% | 0.00 |
| v14_term | REJECTED | 990,330 | -4,136 | -5,540 | -9,670 | -9,670 | 1.2% | 3 | 1.32 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,019,127 | -1,273 | +584 | +19,127 | +19,127 | 0.8% | 2 | 0.94 | 0 | — | — |
| v16_equity_rebal | REJECTED | 970,125 | +0 | -3,240 | -29,875 | -29,875 | 3.4% | 0 | 0.00 | 3 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 987,079 | -496 | -1,770 | -12,921 | -12,921 | 2.0% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,007,559 | -205 | +1,277 | +7,559 | +7,559 | 0.5% | 4 | 0.77 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,002,965 | -3,124 | -260 | +7,197 | +2,965 | 1.7% | 4 | 2.65 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 991,763 | +0 | -621 | -4,840 | -8,237 | 1.0% | 0 | 0.00 | 10 | 20% | 0.57 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 988,504 | +0 | -5,918 | +12,943 | -11,496 | 2.0% | 0 | 0.00 | 20 | 25% | 0.76 |
| v2_trend_carry | CHALLENGER | 1,008,916 | -287 | +1,160 | +8,986 | +8,916 | 0.2% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,010,783 | -246 | +1,339 | +9,408 | +10,783 | 0.3% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,007,849 | -2,044 | -2,766 | +13,107 | +7,849 | 0.9% | 4 | 2.46 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,004,065 | -351 | +509 | +4,135 | +4,065 | 0.2% | 4 | 0.65 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,000,516 | -606 | -384 | +377 | +516 | 0.2% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,007,794 | -351 | +509 | +7,523 | +7,794 | 0.2% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,004,155 | -352 | +508 | +5,314 | +4,155 | 0.2% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,005,030 | -278 | +800 | +4,759 | +5,030 | 0.3% | 3 | 0.44 | 3 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 997,375 | -178 | -2,360 | -3,066 | -2,625 | 0.9% | 3 | 0.44 | 32 | 34% | 0.43 |
| v5_carry_trend_daily_10p | REJECTED | 1,002,832 | -1,607 | -2,522 | +7,199 | +2,832 | 0.5% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 999,399 | -1,437 | -1,575 | +5,936 | -601 | 0.6% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,000,859 | -776 | +235 | +1,999 | +859 | 0.5% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,008,864 | -413 | +1,206 | +9,586 | +8,864 | 0.3% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,008,864 | -413 | +1,206 | +9,586 | +8,864 | 0.3% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,011,949 | -6,643 | -12,067 | +11,949 | +11,949 | 1.5% | 5 | 2.19 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 989,732 | -1,686 | -1,935 | -10,268 | -10,268 | 1.4% | 4 | 1.64 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,007,808 | -3,553 | -5,987 | +7,808 | +7,808 | 1.0% | 4 | 1.61 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,031,915 | -3,124 | -1,876 | +31,915 | +31,915 | 1.1% | 7 | 1.37 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,031,915 | -3,124 | -1,876 | +31,915 | +31,915 | 1.1% | 7 | 1.37 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 979,163 | -5,496 | -9,396 | -7,087 | -20,837 | 3.7% | 6 | 2.34 | 20 | 20% | 0.12 |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.92 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -2.4% | 0.87 | -0.42 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -10.1% | 0.84 | -1.06 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.72 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -6.9% | 0.79 | -0.94 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.20 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.60 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.17 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -5.4% | 0.76 | -0.67 | 1.09 |
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
