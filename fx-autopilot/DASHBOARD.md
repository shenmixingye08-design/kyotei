# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-18T12:10 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -79,772 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +0 | +8,143 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 996,583 | +3,652 | -972 | -37,139 | -3,417 | 4.1% | 1 | 2.52 | 36 | 50% | 0.92 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,010,719 | -6,020 | -32,166 | -25,726 | +10,719 | 3.9% | 0 | 0.00 | 44 | 50% | 1.10 |
| mtf_pullback_v1 | RESEARCH_ONLY | 999,639 | +4,758 | +4,758 | +9,336 | -361 | 0.4% | 0 | 0.00 | 9 | 44% | 0.99 |
| regime_switch_v1 | RESEARCH_ONLY | 977,227 | +4,932 | +11,735 | -27,925 | -22,773 | 4.0% | 3 | 2.92 | 51 | 25% | 0.59 |
| trend_donchian_v1 | RESEARCH_ONLY | 987,072 | +3,537 | +19,156 | +5,608 | -12,928 | 3.5% | 3 | 2.85 | 19 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 954,183 | -7,061 | +4,124 | -3,579 | -45,817 | 4.6% | 0 | 0.00 | 48 | 29% | 0.62 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,034,595 | +3,484 | +15,292 | +19,625 | +34,595 | 0.2% | 3 | 2.09 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -3,501 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,007,858 | +710 | -4,309 | -4,639 | +7,858 | 1.9% | 5 | 2.02 | 551 | 48% | 1.04 |
| v12_carry_timed | REJECTED | 1,022,043 | +1,472 | +7,773 | +22,043 | +22,043 | 0.1% | 5 | 2.21 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,010,268 | +1,663 | +6,675 | +10,268 | +10,268 | 0.0% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,031,148 | +2,468 | +18,065 | +31,148 | +31,148 | 0.2% | 6 | 2.64 | 0 | — | — |
| v14_term | REJECTED | 995,047 | +740 | -2,819 | -4,953 | -4,953 | 0.8% | 3 | 1.31 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,018,168 | +1,494 | +12,201 | +18,168 | +18,168 | 0.1% | 2 | 0.94 | 0 | — | — |
| v16_equity_rebal | REJECTED | 973,534 | -74 | -15,633 | -26,466 | -26,466 | 3.1% | 1 | 0.36 | 2 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 989,554 | -5 | -9,229 | -10,446 | -10,446 | 1.7% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,006,102 | +747 | +6,066 | +6,102 | +6,102 | 0.0% | 2 | 0.39 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,003,400 | +3,895 | +18,617 | +12,239 | +3,400 | 0.2% | 4 | 2.64 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 991,739 | +1,513 | +8,598 | -8,261 | -8,261 | 1.0% | 2 | 1.35 | 8 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 993,739 | +2,494 | +19,558 | +18,178 | -6,261 | 1.5% | 3 | 3.00 | 16 | 19% | 0.76 |
| v2_trend_carry | CHALLENGER | 1,007,724 | +654 | +5,023 | +8,198 | +7,724 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,009,479 | +719 | +7,023 | +10,409 | +9,479 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,011,576 | +1,289 | +3,773 | +12,834 | +11,576 | 0.6% | 4 | 2.45 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,003,864 | +80 | +2,494 | +4,338 | +3,864 | 0.1% | 4 | 0.65 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,088 | +485 | +1,018 | +1,694 | +1,088 | 0.1% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,007,593 | +80 | +4,450 | +8,067 | +7,593 | 0.0% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,003,955 | +80 | +2,411 | +5,182 | +3,955 | 0.1% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,004,538 | +542 | +3,860 | +5,012 | +4,538 | 0.0% | 4 | 0.65 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 1,000,043 | -69 | +2,857 | -1,992 | +43 | 0.6% | 4 | 0.65 | 29 | 34% | 0.60 |
| v5_carry_trend_daily_10p | REJECTED | 1,005,224 | +805 | +6,782 | +9,358 | +5,224 | 0.1% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,000,864 | +566 | +5,191 | +6,254 | +864 | 0.5% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,000,485 | +888 | +3,662 | +3,969 | +485 | 0.1% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,007,706 | +838 | +7,318 | +10,041 | +7,706 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,007,706 | +838 | +7,318 | +10,041 | +7,706 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,023,927 | +2,115 | +7,040 | +23,927 | +23,927 | 0.2% | 5 | 2.17 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 992,802 | +1,339 | +877 | -7,198 | -7,198 | 1.1% | 4 | 1.63 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,014,205 | +1,483 | +8,630 | +14,205 | +14,205 | 0.1% | 4 | 1.60 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,032,690 | +1,731 | +16,160 | +32,690 | +32,690 | 0.1% | 7 | 1.37 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,032,690 | +1,731 | +16,160 | +32,690 | +32,690 | 0.1% | 7 | 1.37 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 988,134 | +2,317 | +15,913 | -706 | -11,866 | 2.9% | 6 | 2.23 | 19 | 21% | 0.13 |

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
