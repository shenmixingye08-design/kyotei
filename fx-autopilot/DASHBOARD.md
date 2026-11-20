# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-20T20:43 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -52,471 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +0 | +8,143 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 983,203 | +0 | -12,185 | -50,518 | -16,797 | 5.4% | 0 | 0.00 | 38 | 47% | 0.82 |
| mr_zscore_v1 | RESEARCH_ONLY | 999,443 | -8,417 | -28,187 | -25,287 | -557 | 5.0% | 2 | 2.54 | 45 | 49% | 1.05 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,007,010 | +3,390 | +12,129 | +16,707 | +7,010 | 0.0% | 0 | 0.00 | 10 | 50% | 1.29 |
| regime_switch_v1 | RESEARCH_ONLY | 1,001,755 | +12,153 | +38,670 | -131 | +1,755 | 1.6% | 3 | 2.88 | 54 | 28% | 0.71 |
| trend_donchian_v1 | RESEARCH_ONLY | 994,750 | -4,838 | +11,143 | +7,414 | -5,250 | 2.7% | 2 | 1.24 | 20 | 10% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 960,022 | +4,020 | +1,328 | +6,057 | -39,978 | 4.0% | 1 | 1.82 | 49 | 29% | 0.61 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,046,817 | +3,639 | +22,089 | +32,267 | +46,817 | 0.0% | 3 | 2.06 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -3,786 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 999,815 | -2,618 | -9,784 | -10,781 | -185 | 2.7% | 5 | 1.92 | 586 | 48% | 1.02 |
| v12_carry_timed | REJECTED | 1,017,807 | -5,515 | -4,879 | +17,807 | +17,807 | 0.7% | 5 | 2.22 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,009,223 | -1,886 | -1,031 | +9,223 | +9,223 | 0.3% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,040,052 | +5,720 | +17,444 | +40,052 | +40,052 | 0.0% | 6 | 2.61 | 0 | — | — |
| v14_term | REJECTED | 995,707 | -1,934 | -217 | -4,293 | -4,293 | 0.7% | 3 | 1.31 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,020,896 | +445 | +6,328 | +20,896 | +20,896 | 0.1% | 2 | 0.93 | 0 | — | — |
| v16_equity_rebal | REJECTED | 972,052 | -939 | -6,594 | -27,948 | -27,948 | 3.2% | 1 | 0.37 | 2 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 982,914 | -6,222 | -13,196 | -17,086 | -17,086 | 2.4% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,009,664 | +1,520 | +5,873 | +9,664 | +9,664 | 0.0% | 3 | 0.60 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,006,448 | +1,273 | +11,730 | +13,584 | +6,448 | 0.1% | 4 | 2.64 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 992,227 | +514 | +7,231 | -7,706 | -7,773 | 1.0% | 1 | 0.64 | 9 | 11% | 0.12 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 998,409 | +4,839 | +15,622 | +22,848 | -1,591 | 1.1% | 2 | 2.27 | 18 | 22% | 0.74 |
| v2_trend_carry | CHALLENGER | 1,008,594 | -570 | +2,023 | +9,621 | +8,594 | 0.1% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,012,086 | +2,118 | +5,444 | +13,155 | +12,086 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,000,575 | -12,853 | -14,620 | +1,537 | +575 | 1.6% | 4 | 2.48 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,002,287 | -2,415 | -2,063 | +3,315 | +2,287 | 0.3% | 4 | 0.66 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 999,633 | -2,062 | -2,057 | +309 | -367 | 0.2% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,006,016 | -2,415 | -997 | +6,560 | +6,016 | 0.3% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,002,375 | -2,419 | -2,152 | +4,375 | +2,375 | 0.3% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,005,151 | -399 | +1,494 | +5,694 | +5,151 | 0.1% | 4 | 0.65 | 2 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 998,492 | -2,378 | -1,104 | -3,489 | -1,508 | 0.8% | 4 | 0.65 | 29 | 34% | 0.60 |
| v5_carry_trend_daily_10p | REJECTED | 1,004,198 | -1,995 | +290 | +9,713 | +4,198 | 0.2% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,000,634 | -1,067 | +1,046 | +7,406 | +634 | 0.5% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,001,949 | +412 | +2,482 | +5,560 | +1,949 | 0.0% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,009,504 | +879 | +4,235 | +12,697 | +9,504 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,009,504 | +879 | +4,235 | +12,697 | +9,504 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,017,175 | -8,447 | -8,022 | +17,175 | +17,175 | 1.0% | 5 | 2.18 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 988,088 | -3,217 | -6,193 | -11,912 | -11,912 | 1.5% | 4 | 1.64 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,009,605 | -4,671 | -5,248 | +9,605 | +9,605 | 0.6% | 4 | 1.61 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,037,167 | -493 | +9,094 | +37,167 | +37,167 | 0.2% | 7 | 1.37 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,037,167 | -493 | +9,094 | +37,167 | +37,167 | 0.2% | 7 | 1.37 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 990,043 | +286 | +9,722 | +4,336 | -9,957 | 2.7% | 6 | 2.22 | 19 | 21% | 0.13 |

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
