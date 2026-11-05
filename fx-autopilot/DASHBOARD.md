# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-05T01:41 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 874,346 | -4,405 | -8,681 | -115,587 | -125,654 | 14.0% | 0 | 0.00 | 156 | 40% | 0.59 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,002,618 | -4,751 | -16,036 | -9,487 | +2,618 | 3.6% | 0 | 0.00 | 32 | 53% | 1.04 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,027,030 | +6,878 | +4,989 | +24,480 | +27,030 | 1.3% | 3 | 4.22 | 29 | 55% | 1.44 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,000,002 | +7,122 | +14,378 | +328 | +2 | 0.4% | 0 | 0.00 | 7 | 43% | 1.00 |
| regime_switch_v1 | RESEARCH_ONLY | 969,701 | -6,602 | -5,725 | -34,072 | -30,299 | 4.8% | 0 | 0.00 | 44 | 30% | 0.72 |
| trend_donchian_v1 | RESEARCH_ONLY | 965,585 | -909 | -8,710 | -43,108 | -34,415 | 5.6% | 2 | 1.61 | 17 | 12% | 0.17 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 951,569 | -1,904 | -12,203 | -29,266 | -48,431 | 4.8% | 1 | 1.30 | 36 | 28% | 0.40 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,017,176 | +0 | -6,838 | +4,613 | +17,176 | 0.9% | 0 | 0.00 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -13,214 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,001,683 | -12,584 | -26,136 | -1,651 | +1,683 | 2.5% | 5 | 1.90 | 411 | 48% | 1.04 |
| v12_carry_timed | REJECTED | 999,663 | -4,389 | -337 | -337 | -337 | 0.7% | 6 | 2.59 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 998,012 | -1,055 | -1,988 | -1,988 | -1,988 | 0.3% | 3 | 1.18 | 0 | — | — |
| v13_ratemom | REJECTED | 989,056 | -2,858 | -10,944 | -10,944 | -10,944 | 1.1% | 6 | 2.75 | 0 | — | — |
| v14_term | REJECTED | 1,001,037 | +451 | +1,037 | +1,037 | +1,037 | 0.2% | 6 | 2.39 | 0 | — | — |
| v14_term_ratemom | REJECTED | 995,066 | -3,044 | -4,934 | -4,934 | -4,934 | 0.6% | 2 | 0.96 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,003,110 | +5,351 | +3,110 | +3,110 | +3,110 | 0.1% | 3 | 1.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,004,883 | +1,478 | +4,883 | +4,883 | +4,883 | 0.2% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 986,608 | +872 | -15,806 | -11,529 | -13,392 | 1.8% | 4 | 3.04 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 995,304 | -936 | -3,989 | -4,696 | -4,696 | 0.7% | 2 | 1.25 | 3 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 977,800 | +5,998 | +3,300 | -22,673 | -22,200 | 3.1% | 0 | 0.00 | 14 | 14% | 0.43 |
| v2_trend_carry | CHALLENGER | 997,471 | -1,574 | -3,056 | -2,529 | -2,529 | 0.4% | 3 | 0.45 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 997,635 | -1,361 | -4,451 | -2,365 | -2,365 | 0.5% | 3 | 0.47 | 0 | — | — |
| v3_carry_only | REJECTED | 999,649 | -2,785 | +1,104 | -351 | -351 | 0.5% | 4 | 2.48 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 997,875 | -1,065 | -2,652 | -2,125 | -2,125 | 0.3% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 999,010 | -313 | -1,827 | -702 | -990 | 0.2% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 997,913 | -1,574 | -3,056 | -2,087 | -2,087 | 0.3% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 998,046 | -1,066 | -1,268 | -1,954 | -1,954 | 0.3% | 4 | 0.56 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,000,031 | -313 | -938 | +31 | +31 | 0.1% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,001,502 | +334 | -1,121 | -2,195 | +1,502 | 0.5% | 4 | 0.66 | 17 | 41% | 0.79 |
| v5_carry_trend_daily_10p | REJECTED | 992,106 | -2,099 | -4,925 | -10,647 | -7,894 | 1.4% | 4 | 0.59 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 989,731 | -2,483 | -5,082 | -11,262 | -10,269 | 1.6% | 3 | 0.43 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 995,140 | -1,631 | -4,461 | -4,132 | -4,860 | 0.7% | 4 | 0.63 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 994,685 | -1,737 | -5,335 | -5,040 | -5,315 | 0.9% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 994,685 | -1,737 | -5,335 | -5,040 | -5,315 | 0.9% | 4 | 0.73 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 999,948 | -2,723 | -52 | -52 | -52 | 0.6% | 6 | 2.55 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,001,245 | +2,780 | +1,245 | +1,245 | +1,245 | 0.2% | 6 | 2.39 | 0 | — | — |
| v7_cm_monthly | REJECTED | 999,772 | -3,208 | -228 | -228 | -228 | 0.5% | 5 | 1.96 | 0 | — | — |
| v8_dollar_carry | REJECTED | 995,683 | -5,926 | -4,317 | -4,317 | -4,317 | 0.8% | 7 | 1.42 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 995,683 | -5,926 | -4,317 | -4,317 | -4,317 | 0.8% | 7 | 1.42 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 979,532 | +259 | -5,234 | -28,026 | -20,468 | 3.7% | 4 | 1.08 | 11 | 18% | 0.07 |

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
