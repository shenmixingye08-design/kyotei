# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-11T17:31 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | -3,319 | -12,029 | -93,761 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +8,143 | +8,271 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 997,555 | +6,520 | -5,063 | -25,570 | -2,445 | 4.1% | 0 | 0.00 | 35 | 51% | 0.97 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,035,966 | -6,565 | +522 | +27,143 | +35,966 | 1.5% | 2 | 2.90 | 36 | 58% | 1.55 |
| mtf_pullback_v1 | RESEARCH_ONLY | 994,881 | +0 | -5,120 | -4,792 | -5,119 | 0.9% | 0 | 0.00 | 8 | 38% | 0.79 |
| regime_switch_v1 | RESEARCH_ONLY | 954,597 | -17,922 | -15,777 | -25,635 | -45,403 | 6.3% | 2 | 2.33 | 49 | 27% | 0.61 |
| trend_donchian_v1 | RESEARCH_ONLY | 977,195 | +10,829 | +13,972 | -37,276 | -22,805 | 4.4% | 3 | 3.25 | 18 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 960,656 | +15,474 | +9,964 | -8,768 | -39,344 | 3.9% | 2 | 2.92 | 44 | 27% | 0.51 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,019,896 | -177 | +2,720 | +2,028 | +19,896 | 0.6% | 1 | 0.43 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -16,792 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,011,696 | +4,848 | +8,067 | -4,222 | +11,696 | 1.6% | 5 | 1.94 | 481 | 49% | 1.10 |
| v12_carry_timed | REJECTED | 1,021,893 | +12,836 | +18,389 | +21,893 | +21,893 | 0.0% | 6 | 2.53 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,008,106 | +7,857 | +7,657 | +8,106 | +8,106 | 0.0% | 3 | 1.17 | 0 | — | — |
| v13_ratemom | REJECTED | 1,013,946 | +2,464 | +22,295 | +13,946 | +13,946 | 0.2% | 6 | 2.68 | 0 | — | — |
| v14_term | REJECTED | 1,000,429 | +5,908 | -2,300 | +429 | +429 | 0.2% | 6 | 2.39 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,008,982 | +4,211 | +11,572 | +8,982 | +8,982 | 0.1% | 2 | 0.95 | 0 | — | — |
| v16_equity_rebal | REJECTED | 987,494 | -1,864 | -14,458 | -12,506 | -12,506 | 1.7% | 3 | 1.01 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,002,394 | +6,209 | -3,330 | +2,394 | +2,394 | 0.5% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,328 | -96 | +328 | +328 | +328 | 0.0% | 1 | 0.22 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 989,475 | +8,248 | -725 | -8,081 | -10,525 | 1.5% | 4 | 3.03 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 983,804 | +1,178 | -10,462 | -16,196 | -16,196 | 1.8% | 2 | 1.37 | 7 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 974,181 | +0 | -3,619 | -16,651 | -25,819 | 3.5% | 0 | 0.00 | 15 | 13% | 0.39 |
| v2_trend_carry | CHALLENGER | 1,004,280 | +2,021 | +5,977 | +4,280 | +4,280 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,003,138 | +627 | +4,808 | +3,138 | +3,138 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,015,671 | +11,641 | +13,130 | +15,671 | +15,671 | 0.0% | 4 | 2.44 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,003,315 | +2,826 | +4,480 | +3,315 | +3,315 | 0.0% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,861 | +2,862 | +1,975 | +1,994 | +1,861 | 0.0% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,004,723 | +2,021 | +5,977 | +4,723 | +4,723 | 0.0% | 3 | 0.44 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,003,491 | +2,829 | +4,485 | +3,759 | +3,491 | 0.0% | 4 | 0.55 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,002,104 | +2,058 | +1,196 | +2,104 | +2,104 | 0.0% | 2 | 0.33 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 998,738 | +2,226 | -2,589 | -7,293 | -1,262 | 0.7% | 3 | 0.44 | 25 | 28% | 0.46 |
| v5_carry_trend_daily_10p | REJECTED | 1,000,907 | +3,771 | +7,462 | -3,092 | +907 | 0.6% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 997,589 | +2,953 | +6,988 | -5,160 | -2,411 | 0.8% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 998,462 | +2,576 | +2,049 | -1,042 | -1,538 | 0.3% | 4 | 0.62 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,001,808 | +1,606 | +5,743 | +1,927 | +1,808 | 0.1% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,001,808 | +1,606 | +5,743 | +1,927 | +1,808 | 0.1% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,024,487 | +13,767 | +20,982 | +24,487 | +24,487 | 0.0% | 6 | 2.49 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 996,649 | +8,630 | -6,783 | -3,351 | -3,351 | 0.7% | 6 | 2.40 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,012,506 | +11,103 | +9,470 | +12,506 | +12,506 | 0.0% | 5 | 1.93 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,020,426 | +5,836 | +22,160 | +20,426 | +20,426 | 0.0% | 7 | 1.39 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,020,426 | +5,836 | +22,160 | +20,426 | +20,426 | 0.0% | 7 | 1.39 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 972,220 | -442 | -7,892 | -39,283 | -27,780 | 4.4% | 0 | 0.00 | 18 | 17% | 0.11 |

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
