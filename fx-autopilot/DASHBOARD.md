# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-26T03:56 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -41,565 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,009,588 | +0 | +1,318 | +9,460 | +9,588 | 0.1% | 0 | 0.00 | 4 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 980,723 | +5,147 | -7,512 | -41,415 | -19,277 | 5.7% | 1 | 1.95 | 41 | 46% | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,030,801 | +2,142 | +21,901 | +3,371 | +30,801 | 2.0% | 0 | 0.00 | 53 | 53% | 1.25 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,013,577 | +4,180 | +13,938 | +27,953 | +13,577 | 0.1% | 2 | 2.96 | 12 | 50% | 1.32 |
| regime_switch_v1 | RESEARCH_ONLY | 1,001,353 | -1,200 | +12,601 | +6,972 | +1,353 | 1.7% | 0 | 0.00 | 59 | 31% | 1.01 |
| trend_donchian_v1 | RESEARCH_ONLY | 983,704 | -4,965 | -13,391 | +10,113 | -16,296 | 3.8% | 2 | 1.25 | 22 | 9% | 0.13 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 949,121 | -2,862 | -5,062 | -11,001 | -50,879 | 5.1% | 2 | 2.88 | 50 | 28% | 0.61 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,045,132 | -1,247 | +3,334 | +23,078 | +45,132 | 1.2% | 2 | 1.65 | 7 | 71% | 10.47 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | +0 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,006,157 | +6,650 | -5,559 | -15,304 | +6,157 | 2.1% | 5 | 1.74 | 636 | 49% | 1.05 |
| v12_carry_timed | REJECTED | 1,016,598 | -3,446 | -8,290 | +16,598 | +16,598 | 1.1% | 5 | 2.22 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,007,032 | -2,031 | -4,615 | +7,032 | +7,032 | 0.8% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,028,903 | -3,712 | -5,960 | +28,903 | +28,903 | 1.8% | 5 | 2.30 | 1 | 0% | 0.00 |
| v14_term | REJECTED | 991,656 | -3,271 | -6,523 | -8,344 | -8,344 | 1.1% | 3 | 1.31 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,020,618 | -657 | +561 | +20,618 | +20,618 | 0.7% | 2 | 0.93 | 0 | — | — |
| v16_equity_rebal | REJECTED | 970,125 | +0 | -2,659 | -29,875 | -29,875 | 3.4% | 0 | 0.00 | 3 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 986,896 | +443 | -2,272 | -13,104 | -13,104 | 2.0% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,007,941 | -1,427 | -188 | +7,941 | +7,941 | 0.5% | 4 | 0.77 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,006,190 | -1,816 | +137 | +9,159 | +6,190 | 1.4% | 4 | 2.64 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 991,763 | +0 | -1,551 | -5,080 | -8,237 | 1.0% | 0 | 0.00 | 10 | 20% | 0.57 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 988,504 | +0 | -8,749 | +12,943 | -11,496 | 2.0% | 0 | 0.00 | 20 | 25% | 0.76 |
| v2_trend_carry | CHALLENGER | 1,009,130 | -539 | +81 | +9,052 | +9,130 | 0.2% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,011,104 | -881 | +627 | +9,672 | +11,104 | 0.3% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,008,806 | +531 | -3,967 | +12,226 | +8,806 | 0.8% | 4 | 2.45 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,004,130 | -358 | -676 | +4,052 | +4,130 | 0.1% | 4 | 0.65 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,000,975 | -50 | -577 | +641 | +975 | 0.1% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,007,859 | -358 | -676 | +7,393 | +7,859 | 0.1% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,004,220 | -358 | -678 | +5,354 | +4,220 | 0.1% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,005,243 | -539 | -195 | +4,777 | +5,243 | 0.3% | 3 | 0.44 | 3 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 997,587 | -437 | -3,392 | -3,600 | -2,413 | 0.9% | 3 | 0.44 | 32 | 34% | 0.43 |
| v5_carry_trend_daily_10p | REJECTED | 1,003,575 | -1,193 | -2,640 | +7,910 | +3,575 | 0.4% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,000,092 | -949 | -1,841 | +6,480 | +92 | 0.5% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,001,741 | -434 | +277 | +2,819 | +1,741 | 0.4% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,009,284 | -799 | +351 | +9,943 | +9,284 | 0.3% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,009,284 | -799 | +351 | +9,943 | +9,284 | 0.3% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,014,128 | -3,760 | -12,803 | +14,128 | +14,128 | 1.3% | 5 | 2.19 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 990,934 | -546 | -1,835 | -9,066 | -9,066 | 1.2% | 4 | 1.64 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,009,245 | -2,949 | -6,214 | +9,245 | +9,245 | 0.9% | 4 | 1.61 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,033,043 | -3,556 | -4,348 | +33,043 | +33,043 | 1.0% | 7 | 1.37 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,033,043 | -3,556 | -4,348 | +33,043 | +33,043 | 1.0% | 7 | 1.37 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 982,300 | -4,845 | -9,253 | -3,879 | -17,700 | 3.4% | 6 | 2.34 | 20 | 20% | 0.12 |

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
