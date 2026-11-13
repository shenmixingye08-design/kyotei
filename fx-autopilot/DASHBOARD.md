# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-13T11:20 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | -12,352 | -93,497 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +8,143 | +8,271 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 997,555 | +0 | -3,211 | -28,180 | -2,445 | 4.1% | 0 | 0.00 | 35 | 51% | 0.97 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,027,431 | -5,613 | -6,308 | +11,796 | +27,431 | 2.4% | 2 | 2.90 | 38 | 55% | 1.37 |
| mtf_pullback_v1 | RESEARCH_ONLY | 994,881 | +0 | -5,120 | -528 | -5,119 | 0.9% | 0 | 0.00 | 8 | 38% | 0.79 |
| regime_switch_v1 | RESEARCH_ONLY | 961,695 | +4,333 | -8,007 | -12,875 | -38,305 | 5.6% | 3 | 4.14 | 50 | 26% | 0.59 |
| trend_donchian_v1 | RESEARCH_ONLY | 982,389 | +5,918 | +17,206 | -21,771 | -17,611 | 3.9% | 3 | 2.87 | 19 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 957,504 | +929 | +448 | -6,299 | -42,496 | 4.2% | 1 | 1.10 | 46 | 28% | 0.57 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,023,842 | +2,798 | +6,666 | +6,539 | +23,842 | 0.3% | 1 | 0.43 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -15,903 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,011,423 | +3,184 | +1,482 | +265 | +11,423 | 1.6% | 5 | 2.18 | 506 | 48% | 1.07 |
| v12_carry_timed | REJECTED | 1,022,988 | +3,990 | +17,930 | +22,988 | +22,988 | 0.0% | 6 | 2.53 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,009,202 | +3,077 | +13,343 | +9,202 | +9,202 | 0.0% | 3 | 1.17 | 0 | — | — |
| v13_ratemom | REJECTED | 1,019,404 | +4,385 | +20,320 | +19,404 | +19,404 | 0.1% | 6 | 2.67 | 0 | — | — |
| v14_term | REJECTED | 997,209 | +193 | +2,012 | -2,791 | -2,791 | 0.6% | 5 | 1.96 | 1 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,012,837 | +3,886 | +11,375 | +12,837 | +12,837 | 0.0% | 2 | 0.94 | 0 | — | — |
| v16_equity_rebal | REJECTED | 980,705 | -5,920 | -8,966 | -19,295 | -19,295 | 2.4% | 3 | 1.02 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 998,195 | -1,614 | +2,177 | -1,805 | -1,805 | 0.9% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,002,927 | +2,162 | +2,927 | +2,927 | +2,927 | 0.0% | 2 | 0.39 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 990,879 | +4,026 | +9,988 | -9,077 | -9,121 | 1.4% | 3 | 2.25 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 983,584 | +428 | -5,761 | -16,416 | -16,416 | 1.8% | 1 | 0.65 | 8 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 980,564 | +6,974 | +1,795 | +1,142 | -19,436 | 2.8% | 1 | 1.11 | 15 | 13% | 0.39 |
| v2_trend_carry | CHALLENGER | 1,006,070 | +1,781 | +4,978 | +5,936 | +6,070 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,005,427 | +1,890 | +3,302 | +5,322 | +5,427 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,016,238 | +3,061 | +15,714 | +15,624 | +16,238 | 0.0% | 4 | 2.44 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,004,167 | +1,292 | +4,881 | +4,033 | +4,167 | 0.0% | 4 | 0.55 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,727 | +590 | +3,613 | +1,725 | +1,727 | 0.0% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,006,513 | +1,781 | +4,978 | +6,378 | +6,513 | 0.0% | 3 | 0.44 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,004,344 | +1,293 | +4,886 | +5,264 | +4,344 | 0.0% | 4 | 0.55 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,003,154 | +1,326 | +4,019 | +3,019 | +3,154 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 999,316 | +1,000 | +1,287 | -4,563 | -684 | 0.7% | 4 | 0.55 | 28 | 36% | 0.65 |
| v5_carry_trend_daily_10p | REJECTED | 1,003,116 | +2,757 | +7,758 | +1,109 | +3,116 | 0.4% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 999,176 | +1,902 | +5,583 | -1,580 | -824 | 0.6% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 998,928 | +1,013 | +3,671 | +554 | -1,072 | 0.3% | 4 | 0.62 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,004,192 | +2,199 | +5,741 | +4,365 | +4,192 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,004,192 | +2,199 | +5,741 | +4,365 | +4,192 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,025,278 | +4,039 | +24,784 | +25,278 | +25,278 | 0.0% | 6 | 2.49 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 993,959 | +1,546 | +5,273 | -6,041 | -6,041 | 0.9% | 5 | 1.97 | 1 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,014,130 | +4,502 | +13,212 | +14,130 | +14,130 | 0.0% | 5 | 1.93 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,026,480 | +6,031 | +17,586 | +26,480 | +26,480 | 0.0% | 7 | 1.38 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,026,480 | +6,031 | +17,586 | +26,480 | +26,480 | 0.0% | 7 | 1.38 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 978,418 | +7,738 | -4,716 | -26,172 | -21,582 | 3.8% | 5 | 1.89 | 19 | 21% | 0.13 |

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
