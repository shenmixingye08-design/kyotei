# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-06T01:42 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 874,062 | -284 | -10,120 | -117,059 | -125,938 | 14.0% | 1 | 2.03 | 160 | 40% | 0.60 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,002,618 | +0 | -13,172 | -11,594 | +2,618 | 3.6% | 0 | 0.00 | 32 | 53% | 1.04 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,033,739 | +6,709 | +11,698 | +28,123 | +33,739 | 0.6% | 0 | 0.00 | 33 | 58% | 1.49 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,000,002 | +0 | +7,122 | +328 | +2 | 0.4% | 0 | 0.00 | 7 | 43% | 1.00 |
| regime_switch_v1 | RESEARCH_ONLY | 969,701 | +0 | -5,725 | -29,605 | -30,299 | 4.8% | 0 | 0.00 | 44 | 30% | 0.72 |
| trend_donchian_v1 | RESEARCH_ONLY | 961,234 | -4,351 | -3,805 | -41,624 | -38,766 | 6.0% | 3 | 2.53 | 17 | 12% | 0.17 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 952,048 | +479 | -10,666 | -29,847 | -47,952 | 4.8% | 2 | 2.49 | 38 | 29% | 0.46 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,017,176 | +0 | -3,320 | +8,035 | +17,176 | 0.9% | 0 | 0.00 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -12,761 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,004,860 | +3,178 | -16,758 | +8,450 | +4,860 | 2.2% | 5 | 1.87 | 426 | 48% | 1.04 |
| v12_carry_timed | REJECTED | 998,835 | -828 | -1,165 | -1,165 | -1,165 | 0.7% | 6 | 2.59 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 995,182 | -2,830 | -4,818 | -4,818 | -4,818 | 0.6% | 3 | 1.18 | 0 | — | — |
| v13_ratemom | REJECTED | 995,023 | +5,967 | -4,977 | -4,977 | -4,977 | 0.5% | 6 | 2.73 | 0 | — | — |
| v14_term | REJECTED | 995,428 | -5,609 | -4,572 | -4,572 | -4,572 | 0.7% | 6 | 2.40 | 0 | — | — |
| v14_term_ratemom | REJECTED | 997,402 | +2,336 | -2,598 | -2,598 | -2,598 | 0.3% | 2 | 0.96 | 0 | — | — |
| v16_equity_rebal | REJECTED | 995,737 | -7,373 | -4,263 | -4,263 | -4,263 | 0.9% | 3 | 1.01 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 997,722 | -7,161 | -2,278 | -2,278 | -2,278 | 0.9% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 981,857 | -4,752 | -13,125 | -14,771 | -18,143 | 2.3% | 4 | 3.06 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 991,078 | -4,226 | -5,781 | -8,922 | -8,922 | 1.1% | 1 | 0.54 | 4 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 977,800 | +0 | +3,300 | -19,626 | -22,200 | 3.1% | 0 | 0.00 | 14 | 14% | 0.43 |
| v2_trend_carry | CHALLENGER | 998,821 | +1,351 | -791 | -1,179 | -1,179 | 0.2% | 3 | 0.45 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,000,148 | +2,513 | -766 | +148 | +148 | 0.3% | 3 | 0.47 | 0 | — | — |
| v3_carry_only | REJECTED | 996,015 | -3,635 | +356 | -3,985 | -3,985 | 0.9% | 4 | 2.49 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 997,724 | -151 | -1,888 | -2,276 | -2,276 | 0.4% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 997,604 | -1,406 | -2,318 | -2,263 | -2,396 | 0.4% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 999,264 | +1,351 | -791 | -736 | -736 | 0.2% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 997,894 | -152 | -506 | -2,106 | -2,106 | 0.3% | 4 | 0.56 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 998,626 | -1,406 | -1,429 | -1,374 | -1,374 | 0.3% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 999,130 | -2,372 | -1,403 | -4,027 | -870 | 0.7% | 3 | 0.48 | 18 | 39% | 0.77 |
| v5_carry_trend_daily_10p | REJECTED | 993,005 | +899 | -1,108 | -8,765 | -6,995 | 1.4% | 4 | 0.59 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 991,427 | +1,696 | -699 | -8,874 | -8,573 | 1.4% | 3 | 0.43 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 994,556 | -583 | -3,879 | -4,096 | -5,444 | 0.7% | 4 | 0.63 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 996,111 | +1,427 | -2,743 | -3,769 | -3,889 | 0.7% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 996,111 | +1,427 | -2,743 | -3,769 | -3,889 | 0.7% | 4 | 0.73 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 997,001 | -2,947 | -2,999 | -2,999 | -2,999 | 0.9% | 6 | 2.56 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 992,004 | -9,241 | -7,996 | -7,996 | -7,996 | 1.1% | 6 | 2.42 | 0 | — | — |
| v7_cm_monthly | REJECTED | 997,455 | -2,318 | -2,545 | -2,545 | -2,545 | 0.8% | 5 | 1.96 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,001,473 | +5,790 | +1,473 | +1,473 | +1,473 | 0.2% | 7 | 1.42 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,001,473 | +5,790 | +1,473 | +1,473 | +1,473 | 0.2% | 7 | 1.42 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 979,804 | +273 | -2,206 | -24,062 | -20,196 | 3.7% | 1 | 0.36 | 15 | 20% | 0.14 |

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
