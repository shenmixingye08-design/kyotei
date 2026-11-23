# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-23T21:42 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -43,153 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +0 | +8,143 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 975,576 | -7,626 | -17,354 | -48,301 | -24,424 | 6.2% | 0 | 0.00 | 40 | 45% | 0.76 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,014,926 | +15,643 | -6,340 | -4,783 | +14,926 | 3.5% | 3 | 2.85 | 48 | 50% | 1.12 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,014,303 | +7,293 | +19,422 | +24,001 | +14,303 | 0.0% | 0 | 0.00 | 11 | 55% | 1.59 |
| regime_switch_v1 | RESEARCH_ONLY | 1,014,742 | +12,818 | +41,221 | +16,714 | +14,742 | 0.4% | 3 | 2.97 | 55 | 29% | 0.74 |
| trend_donchian_v1 | RESEARCH_ONLY | 992,335 | -2,074 | +5,402 | +12,037 | -7,665 | 3.0% | 3 | 1.87 | 21 | 10% | 0.14 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 951,983 | -6,401 | -9,062 | -17,384 | -48,017 | 4.8% | 0 | 0.00 | 50 | 28% | 0.61 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,055,086 | +8,441 | +23,089 | +33,253 | +55,086 | 0.2% | 2 | 1.63 | 7 | 71% | 10.47 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | +0 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,007,497 | +7,730 | -195 | -10,231 | +7,497 | 2.0% | 0 | 0.00 | 606 | 49% | 1.05 |
| v12_carry_timed | REJECTED | 1,025,557 | +6,888 | +3,319 | +25,557 | +25,557 | 0.3% | 5 | 2.20 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,013,639 | +4,013 | +4,328 | +13,639 | +13,639 | 0.1% | 2 | 0.83 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,046,740 | +6,984 | +18,908 | +46,740 | +46,740 | 0.1% | 5 | 2.26 | 1 | 0% | 0.00 |
| v14_term | REJECTED | 1,000,560 | +4,054 | +4,677 | +560 | +560 | 0.2% | 3 | 1.30 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,026,010 | +5,130 | +9,190 | +26,010 | +26,010 | 0.1% | 2 | 0.93 | 0 | — | — |
| v16_equity_rebal | REJECTED | 970,125 | -1,539 | -4,272 | -29,875 | -29,875 | 3.4% | 0 | 0.00 | 3 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 983,438 | +418 | -7,810 | -16,562 | -16,562 | 2.4% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,012,060 | +2,566 | +6,510 | +12,060 | +12,060 | 0.1% | 4 | 0.77 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,018,021 | +11,520 | +19,272 | +22,579 | +18,021 | 0.3% | 4 | 2.61 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 994,833 | +2,755 | +5,438 | -5,585 | -5,167 | 0.7% | 1 | 0.64 | 9 | 11% | 0.12 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 998,712 | +898 | +8,110 | +23,151 | -1,288 | 1.0% | 1 | 1.22 | 19 | 26% | 0.80 |
| v2_trend_carry | CHALLENGER | 1,010,164 | +1,505 | +2,782 | +10,790 | +10,164 | 0.1% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,013,732 | +1,691 | +5,252 | +12,372 | +13,732 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,005,959 | +4,920 | -6,319 | +14,784 | +5,959 | 1.1% | 4 | 2.46 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,003,636 | +1,280 | -667 | +4,262 | +3,636 | 0.1% | 4 | 0.65 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,576 | +1,850 | +591 | +1,756 | +1,576 | 0.1% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,007,365 | +1,280 | -459 | +7,413 | +7,365 | 0.1% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,003,725 | +1,281 | -753 | +5,204 | +3,725 | 0.1% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,007,572 | +2,410 | +3,101 | +7,621 | +7,572 | 0.1% | 4 | 0.65 | 2 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 999,843 | +1,285 | -572 | +519 | -157 | 0.6% | 3 | 0.44 | 30 | 33% | 0.46 |
| v5_carry_trend_daily_10p | REJECTED | 1,006,831 | +2,318 | +2,189 | +12,687 | +6,831 | 0.1% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,003,212 | +2,325 | +2,692 | +10,799 | +3,212 | 0.2% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,005,003 | +3,063 | +5,382 | +6,159 | +5,003 | 0.1% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,011,643 | +2,121 | +4,813 | +12,380 | +11,643 | 0.1% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,011,643 | +2,121 | +4,813 | +12,380 | +11,643 | 0.1% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,024,023 | +5,922 | +608 | +24,023 | +24,023 | 0.3% | 5 | 2.17 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 993,121 | +4,941 | +890 | -6,879 | -6,879 | 1.0% | 4 | 1.63 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,015,525 | +5,258 | +1,676 | +15,525 | +15,525 | 0.2% | 4 | 1.60 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,042,039 | +4,364 | +10,320 | +42,039 | +42,039 | 0.2% | 7 | 1.36 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,042,039 | +4,364 | +10,320 | +42,039 | +42,039 | 0.2% | 7 | 1.36 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 999,973 | +9,497 | +14,411 | +14,042 | -27 | 1.7% | 6 | 2.29 | 20 | 20% | 0.12 |

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
