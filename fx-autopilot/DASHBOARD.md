# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-04T20:05 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 874,398 | -5,285 | -10,939 | -116,310 | -125,602 | 14.0% | 1 | 1.14 | 155 | 39% | 0.59 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,002,618 | -6,674 | -16,036 | -9,487 | +2,618 | 3.6% | 0 | 0.00 | 32 | 53% | 1.04 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,034,648 | +12,821 | +12,607 | +31,640 | +34,648 | 0.6% | 3 | 4.19 | 29 | 55% | 1.44 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,000,002 | +7,122 | +14,378 | +328 | +2 | 0.4% | 0 | 0.00 | 7 | 43% | 1.00 |
| regime_switch_v1 | RESEARCH_ONLY | 971,141 | -4,841 | -4,285 | -33,323 | -28,859 | 4.6% | 1 | 2.62 | 43 | 28% | 0.69 |
| trend_donchian_v1 | RESEARCH_ONLY | 963,586 | -1,034 | -9,195 | -46,123 | -36,414 | 5.8% | 2 | 1.61 | 17 | 12% | 0.17 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 950,496 | -3,065 | -14,583 | -30,339 | -49,504 | 5.0% | 1 | 1.30 | 36 | 28% | 0.40 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,017,176 | +0 | -5,560 | +3,679 | +17,176 | 0.9% | 0 | 0.00 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -13,475 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,003,812 | -11,518 | -21,727 | -319 | +3,812 | 2.3% | 5 | 1.98 | 406 | 49% | 1.06 |
| v12_carry_timed | REJECTED | 1,003,164 | -1,037 | +3,164 | +3,164 | +3,164 | 0.3% | 6 | 2.58 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 999,972 | -1,195 | -28 | -28 | -28 | 0.1% | 3 | 1.18 | 0 | — | — |
| v13_ratemom | REJECTED | 991,177 | -4,334 | -8,823 | -8,823 | -8,823 | 0.9% | 6 | 2.74 | 0 | — | — |
| v14_term | REJECTED | 1,002,307 | +3,003 | +2,307 | +2,307 | +2,307 | 0.0% | 6 | 2.39 | 0 | — | — |
| v14_term_ratemom | REJECTED | 997,097 | -2,376 | -2,903 | -2,903 | -2,903 | 0.4% | 2 | 0.96 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,001,822 | +2,707 | +1,822 | +1,822 | +1,822 | 0.2% | 3 | 1.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,005,494 | +1,427 | +5,494 | +5,494 | +5,494 | 0.2% | 3 | 1.06 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 989,657 | +550 | -11,512 | -9,005 | -10,343 | 1.5% | 4 | 3.03 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 994,154 | -1,855 | -4,863 | -5,846 | -5,846 | 0.8% | 1 | 0.71 | 3 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 977,800 | +7,431 | +3,300 | -23,855 | -22,200 | 3.1% | 0 | 0.00 | 14 | 14% | 0.43 |
| v2_trend_carry | CHALLENGER | 998,281 | -1,371 | -2,060 | -1,719 | -1,719 | 0.3% | 3 | 0.45 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 998,385 | -1,167 | -3,274 | -1,615 | -1,615 | 0.5% | 3 | 0.47 | 0 | — | — |
| v3_carry_only | REJECTED | 1,002,252 | -2,099 | +3,606 | +2,252 | +2,252 | 0.3% | 4 | 2.47 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 998,730 | -922 | -1,612 | -1,270 | -1,270 | 0.3% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 999,730 | -231 | -921 | -7 | -270 | 0.1% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 998,723 | -1,371 | -2,060 | -1,277 | -1,277 | 0.3% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 998,902 | -754 | -227 | -1,098 | -1,098 | 0.2% | 4 | 0.56 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,000,752 | -182 | -32 | +752 | +752 | 0.1% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,001,288 | -576 | -1,203 | -2,790 | +1,288 | 0.5% | 4 | 0.66 | 17 | 41% | 0.79 |
| v5_carry_trend_daily_10p | REJECTED | 993,303 | -1,317 | -4,138 | -9,371 | -6,697 | 1.3% | 4 | 0.59 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 990,566 | -1,975 | -4,330 | -10,246 | -9,434 | 1.5% | 3 | 0.43 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 996,251 | -1,347 | -2,904 | -3,080 | -3,749 | 0.6% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 995,903 | -1,596 | -3,671 | -3,845 | -4,097 | 0.7% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 995,903 | -1,596 | -3,671 | -3,845 | -4,097 | 0.7% | 4 | 0.73 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,002,976 | -2,213 | +2,976 | +2,976 | +2,976 | 0.3% | 6 | 2.54 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,002,990 | +2,408 | +2,990 | +2,990 | +2,990 | 0.0% | 6 | 2.39 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,002,708 | -704 | +2,708 | +2,708 | +2,708 | 0.2% | 5 | 1.95 | 0 | — | — |
| v8_dollar_carry | REJECTED | 998,082 | -3,746 | -1,918 | -1,918 | -1,918 | 0.5% | 7 | 1.42 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 998,082 | -3,746 | -1,918 | -1,918 | -1,918 | 0.5% | 7 | 1.42 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 980,070 | +720 | -4,748 | -27,696 | -19,930 | 3.6% | 3 | 1.15 | 10 | 10% | 0.02 |

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
