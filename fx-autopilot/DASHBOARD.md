# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-05T20:07 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 875,120 | +936 | -3,502 | -117,947 | -124,880 | 13.9% | 1 | 2.03 | 160 | 40% | 0.60 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,002,618 | +0 | -17,111 | -9,503 | +2,618 | 3.6% | 0 | 0.00 | 32 | 53% | 1.04 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,035,434 | +3,311 | +13,394 | +29,819 | +35,434 | 0.5% | 2 | 2.50 | 31 | 58% | 1.56 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,000,002 | +0 | +7,122 | +328 | +2 | 0.4% | 0 | 0.00 | 7 | 43% | 1.00 |
| regime_switch_v1 | RESEARCH_ONLY | 969,701 | -16 | -5,725 | -28,477 | -30,299 | 4.8% | 0 | 0.00 | 44 | 30% | 0.72 |
| trend_donchian_v1 | RESEARCH_ONLY | 960,960 | -3,636 | -5,775 | -39,726 | -39,040 | 6.0% | 3 | 2.53 | 17 | 12% | 0.17 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 950,069 | -1,666 | -13,703 | -30,934 | -49,931 | 5.0% | 1 | 1.16 | 38 | 29% | 0.46 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,017,176 | +0 | -4,722 | +9,345 | +17,176 | 0.9% | 0 | 0.00 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -11,951 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,003,975 | -280 | -19,759 | +7,985 | +3,975 | 2.3% | 5 | 1.97 | 421 | 48% | 1.06 |
| v12_carry_timed | REJECTED | 998,377 | -5,113 | -1,623 | -1,623 | -1,623 | 0.8% | 6 | 2.59 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 995,565 | -4,485 | -4,435 | -4,435 | -4,435 | 0.6% | 3 | 1.18 | 0 | — | — |
| v13_ratemom | REJECTED | 993,662 | +3,475 | -6,338 | -6,338 | -6,338 | 0.7% | 6 | 2.73 | 0 | — | — |
| v14_term | REJECTED | 995,580 | -6,934 | -4,420 | -4,420 | -4,420 | 0.7% | 6 | 2.40 | 0 | — | — |
| v14_term_ratemom | REJECTED | 996,967 | +250 | -3,033 | -3,033 | -3,033 | 0.4% | 2 | 0.96 | 0 | — | — |
| v16_equity_rebal | REJECTED | 996,840 | -5,378 | -3,160 | -3,160 | -3,160 | 0.8% | 3 | 1.01 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 998,815 | -7,502 | -1,185 | -1,185 | -1,185 | 0.8% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 982,216 | -6,891 | -16,456 | -14,030 | -17,784 | 2.3% | 4 | 3.06 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 991,395 | -3,467 | -6,210 | -8,605 | -8,605 | 1.1% | 1 | 0.54 | 4 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 977,800 | +0 | +3,300 | -19,626 | -22,200 | 3.1% | 0 | 0.00 | 14 | 14% | 0.43 |
| v2_trend_carry | CHALLENGER | 998,626 | +355 | -1,546 | -1,374 | -1,374 | 0.3% | 3 | 0.45 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 999,741 | +1,630 | -1,639 | -259 | -259 | 0.3% | 3 | 0.47 | 0 | — | — |
| v3_carry_only | REJECTED | 996,617 | -6,533 | -2,780 | -3,383 | -3,383 | 0.8% | 4 | 2.48 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 997,739 | -1,065 | -2,433 | -2,261 | -2,261 | 0.4% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 997,780 | -2,049 | -2,702 | -2,136 | -2,220 | 0.3% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 999,069 | +355 | -1,546 | -931 | -931 | 0.2% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 997,909 | -1,067 | -1,051 | -2,091 | -2,091 | 0.3% | 4 | 0.56 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 998,801 | -2,049 | -1,813 | -1,199 | -1,199 | 0.3% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 999,483 | -2,233 | -2,496 | -2,971 | -517 | 0.7% | 3 | 0.48 | 18 | 39% | 0.77 |
| v5_carry_trend_daily_10p | REJECTED | 992,871 | -422 | -3,167 | -8,537 | -7,129 | 1.4% | 4 | 0.59 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 991,016 | +594 | -2,810 | -8,978 | -8,984 | 1.4% | 3 | 0.43 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 994,577 | -1,439 | -4,319 | -3,865 | -5,423 | 0.7% | 4 | 0.63 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 995,845 | +178 | -3,469 | -4,083 | -4,155 | 0.7% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 995,845 | +178 | -3,469 | -4,083 | -4,155 | 0.7% | 4 | 0.73 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 997,046 | -6,506 | -2,954 | -2,954 | -2,954 | 0.9% | 6 | 2.56 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 993,176 | -10,156 | -6,824 | -6,824 | -6,824 | 1.0% | 6 | 2.41 | 0 | — | — |
| v7_cm_monthly | REJECTED | 997,706 | -5,272 | -2,294 | -2,294 | -2,294 | 0.7% | 5 | 1.96 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,431 | +2,567 | +431 | +431 | +431 | 0.3% | 7 | 1.42 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,431 | +2,567 | +431 | +431 | +431 | 0.3% | 7 | 1.42 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 979,830 | -406 | -2,416 | -22,678 | -20,170 | 3.7% | 4 | 1.08 | 11 | 18% | 0.07 |

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
