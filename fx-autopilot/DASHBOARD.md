# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-04T11:07 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 880,891 | +490 | -2,324 | -110,179 | -119,109 | 13.3% | 2 | 2.95 | 153 | 40% | 0.60 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,006,005 | -15,049 | -12,649 | -1,360 | +6,005 | 3.2% | 1 | 1.76 | 31 | 55% | 1.11 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,023,902 | -4,749 | +1,861 | +22,618 | +23,902 | 1.6% | 3 | 4.23 | 29 | 55% | 1.44 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,000,002 | +7,122 | +14,378 | +328 | +2 | 0.4% | 0 | 0.00 | 7 | 43% | 1.00 |
| regime_switch_v1 | RESEARCH_ONLY | 971,288 | -12,292 | -9,248 | -37,072 | -28,712 | 4.6% | 2 | 3.89 | 42 | 29% | 0.71 |
| trend_donchian_v1 | RESEARCH_ONLY | 967,185 | +6,976 | -4,259 | -46,229 | -32,815 | 5.4% | 2 | 1.60 | 17 | 12% | 0.17 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 954,892 | +10,404 | -15,965 | -25,943 | -45,108 | 4.5% | 1 | 1.29 | 36 | 28% | 0.40 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,017,176 | +0 | -8,652 | +1,713 | +17,176 | 0.9% | 0 | 0.00 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -12,687 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,005,699 | -9,887 | -19,221 | +180 | +5,699 | 2.2% | 5 | 2.04 | 401 | 50% | 1.11 |
| v12_carry_timed | REJECTED | 1,002,037 | +2,724 | +2,037 | +2,037 | +2,037 | 0.4% | 6 | 2.58 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 999,128 | -1,097 | -872 | -872 | -872 | 0.2% | 3 | 1.18 | 0 | — | — |
| v13_ratemom | REJECTED | 987,178 | -10,871 | -12,822 | -12,822 | -12,822 | 1.3% | 6 | 2.75 | 0 | — | — |
| v14_term | REJECTED | 1,001,870 | +5,172 | +1,870 | +1,870 | +1,870 | 0.0% | 6 | 2.39 | 0 | — | — |
| v14_term_ratemom | REJECTED | 995,126 | -5,263 | -4,874 | -4,874 | -4,874 | 0.5% | 2 | 0.96 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,002,992 | +3,173 | +2,992 | +2,992 | +2,992 | 0.1% | 3 | 1.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,007,180 | +6,245 | +7,180 | +7,180 | +7,180 | 0.0% | 3 | 1.06 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 985,777 | -5,022 | -15,367 | -11,662 | -14,223 | 1.9% | 4 | 3.04 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 996,666 | +1,156 | -484 | -3,334 | -3,334 | 0.5% | 1 | 0.71 | 3 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 977,800 | +5,851 | -3,618 | -26,020 | -22,200 | 3.1% | 0 | 0.00 | 14 | 14% | 0.43 |
| v2_trend_carry | CHALLENGER | 997,877 | -1,966 | -2,896 | -2,123 | -2,123 | 0.3% | 3 | 0.45 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 997,211 | -3,241 | -5,479 | -2,789 | -2,789 | 0.6% | 3 | 0.47 | 0 | — | — |
| v3_carry_only | REJECTED | 1,003,227 | +1,603 | +5,881 | +3,227 | +3,227 | 0.2% | 4 | 2.47 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 998,490 | -1,353 | -2,283 | -1,510 | -1,510 | 0.3% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 999,558 | -595 | -1,525 | -22 | -442 | 0.2% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 998,319 | -1,966 | -2,896 | -1,681 | -1,681 | 0.3% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 998,662 | -407 | -898 | -1,338 | -1,338 | 0.2% | 4 | 0.56 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,000,579 | +129 | -636 | +579 | +579 | 0.1% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,002,171 | +920 | -184 | -2,183 | +2,171 | 0.4% | 3 | 0.48 | 17 | 41% | 0.79 |
| v5_carry_trend_daily_10p | REJECTED | 992,819 | -976 | -6,434 | -9,730 | -7,181 | 1.4% | 4 | 0.59 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 989,743 | -1,973 | -6,588 | -10,899 | -10,257 | 1.6% | 3 | 0.43 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 995,012 | -3,198 | -5,175 | -4,320 | -4,988 | 0.7% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 994,663 | -3,736 | -5,942 | -4,928 | -5,337 | 0.9% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 994,663 | -3,736 | -5,942 | -4,928 | -5,337 | 0.9% | 4 | 0.73 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,002,707 | +2,791 | +2,707 | +2,707 | +2,707 | 0.3% | 6 | 2.54 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,002,253 | +2,388 | +2,253 | +2,253 | +2,253 | 0.0% | 6 | 2.39 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,002,011 | +1,590 | +2,011 | +2,011 | +2,011 | 0.3% | 5 | 1.95 | 0 | — | — |
| v8_dollar_carry | REJECTED | 996,692 | -3,234 | -3,308 | -3,308 | -3,308 | 0.7% | 7 | 1.42 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 996,692 | -3,234 | -3,308 | -3,308 | -3,308 | 0.7% | 7 | 1.42 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 980,490 | -915 | -4,761 | -27,054 | -19,510 | 3.6% | 3 | 1.15 | 10 | 10% | 0.02 |

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
