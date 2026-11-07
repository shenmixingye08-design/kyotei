# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-07T01:01 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 869,651 | -4,333 | -3,857 | -120,868 | -130,349 | 14.4% | 2 | 2.91 | 165 | 40% | 0.60 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 997,787 | -4,831 | -16,032 | -14,799 | -2,213 | 4.0% | 0 | 0.00 | 33 | 52% | 0.97 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,031,197 | -2,542 | +6,623 | +25,135 | +31,197 | 0.9% | 2 | 2.98 | 33 | 58% | 1.49 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,000,002 | +0 | +7,122 | +328 | +2 | 0.4% | 0 | 0.00 | 7 | 43% | 1.00 |
| regime_switch_v1 | RESEARCH_ONLY | 969,701 | +0 | -8,940 | -16,624 | -30,299 | 4.8% | 0 | 0.00 | 44 | 30% | 0.72 |
| trend_donchian_v1 | RESEARCH_ONLY | 961,749 | +846 | +2,283 | -50,415 | -38,251 | 6.0% | 2 | 1.65 | 18 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 962,164 | +9,017 | +12,572 | -12,572 | -37,836 | 3.8% | 3 | 4.09 | 39 | 28% | 0.44 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,017,176 | +0 | -6,096 | +1,701 | +17,176 | 0.9% | 0 | 0.00 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -13,123 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,007,587 | +3,682 | -12,158 | +4,724 | +7,587 | 2.0% | 0 | 0.00 | 441 | 48% | 1.07 |
| v12_carry_timed | REJECTED | 1,008,566 | +10,654 | +8,566 | +8,566 | +8,566 | 0.1% | 6 | 2.57 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 998,270 | +3,586 | -1,730 | -1,730 | -1,730 | 0.3% | 3 | 1.18 | 0 | — | — |
| v13_ratemom | REJECTED | 1,005,083 | +9,498 | +5,083 | +5,083 | +5,083 | 0.1% | 6 | 2.70 | 0 | — | — |
| v14_term | REJECTED | 996,615 | +2,161 | -3,385 | -3,385 | -3,385 | 0.6% | 6 | 2.40 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,004,041 | +6,567 | +4,041 | +4,041 | +4,041 | 0.0% | 2 | 0.95 | 0 | — | — |
| v16_equity_rebal | REJECTED | 988,643 | -6,250 | -11,357 | -11,357 | -11,357 | 1.6% | 3 | 1.01 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 995,876 | -680 | -4,124 | -4,124 | -4,124 | 1.1% | 3 | 1.08 | 0 | — | — |
| v2_d1_donchian | REJECTED | 999,788 | -212 | -212 | -212 | -212 | 0.0% | 1 | 0.22 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 983,710 | +2,626 | -14,722 | -13,442 | -16,290 | 2.1% | 4 | 3.05 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 989,306 | -1,748 | -8,053 | -10,694 | -10,694 | 1.3% | 1 | 0.53 | 5 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 981,848 | +4,048 | +10,403 | -14,012 | -18,152 | 2.7% | 1 | 1.26 | 14 | 14% | 0.43 |
| v2_trend_carry | CHALLENGER | 1,001,714 | +2,945 | +1,531 | +1,714 | +1,714 | 0.0% | 3 | 0.45 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,002,740 | +2,451 | +901 | +2,740 | +2,740 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,001,885 | +7,169 | +4,193 | +1,885 | +1,885 | 0.3% | 4 | 2.47 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,996 | +2,502 | -187 | -4 | -4 | 0.1% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 998,827 | +1,518 | -1,667 | -1,041 | -1,173 | 0.2% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,002,157 | +2,945 | +1,531 | +2,157 | +2,157 | 0.0% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,000,169 | +2,505 | +1,197 | +169 | +169 | 0.1% | 4 | 0.56 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 999,822 | +1,492 | -804 | -178 | -178 | 0.2% | 2 | 0.34 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 998,199 | -564 | -3,206 | -6,286 | -1,801 | 0.8% | 2 | 0.33 | 20 | 35% | 0.55 |
| v5_carry_trend_daily_10p | REJECTED | 996,312 | +3,369 | +1,299 | -6,681 | -3,688 | 1.0% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 994,617 | +3,130 | +1,270 | -6,912 | -5,383 | 1.1% | 3 | 0.43 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 996,150 | +1,806 | -3,211 | -3,183 | -3,850 | 0.6% | 4 | 0.63 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 999,883 | +3,758 | +104 | +2 | -117 | 0.3% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 999,883 | +3,758 | +104 | +2 | -117 | 0.3% | 4 | 0.73 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,005,168 | +9,132 | +5,168 | +5,168 | +5,168 | 0.1% | 6 | 2.54 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 989,767 | -856 | -10,233 | -10,233 | -10,233 | 1.4% | 6 | 2.42 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,002,217 | +5,572 | +2,217 | +2,217 | +2,217 | 0.3% | 5 | 1.95 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,011,710 | +10,013 | +11,710 | +11,710 | +11,710 | 0.1% | 7 | 1.40 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,011,710 | +10,013 | +11,710 | +11,710 | +11,710 | 0.1% | 7 | 1.40 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 982,489 | +2,584 | -902 | -25,595 | -17,511 | 3.4% | 3 | 1.26 | 15 | 20% | 0.14 |

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
