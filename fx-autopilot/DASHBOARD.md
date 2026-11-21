# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-21T02:35 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -52,047 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +0 | +8,143 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 983,203 | +0 | -10,936 | -50,518 | -16,797 | 5.4% | 0 | 0.00 | 38 | 47% | 0.82 |
| mr_zscore_v1 | RESEARCH_ONLY | 999,283 | -7,765 | -28,214 | -25,649 | -717 | 5.0% | 2 | 2.81 | 46 | 48% | 1.01 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,007,010 | +1,740 | +12,129 | +16,707 | +7,010 | 0.0% | 0 | 0.00 | 10 | 50% | 1.29 |
| regime_switch_v1 | RESEARCH_ONLY | 1,001,925 | +10,628 | +38,834 | +39 | +1,925 | 1.6% | 3 | 2.88 | 54 | 28% | 0.71 |
| trend_donchian_v1 | RESEARCH_ONLY | 994,409 | -5,421 | +11,362 | +8,094 | -5,591 | 2.8% | 3 | 1.94 | 20 | 10% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 958,384 | +2,976 | +143 | +5,014 | -41,616 | 4.2% | 1 | 1.83 | 49 | 29% | 0.61 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,046,645 | +1,901 | +21,807 | +31,891 | +46,645 | 0.1% | 3 | 2.06 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -4,098 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 999,767 | -2,618 | -9,792 | -10,772 | -233 | 2.7% | 0 | 0.00 | 591 | 48% | 1.00 |
| v12_carry_timed | REJECTED | 1,018,669 | -4,930 | -3,330 | +18,669 | +18,669 | 0.6% | 5 | 2.21 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,009,626 | -1,788 | -107 | +9,626 | +9,626 | 0.2% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,039,756 | +4,206 | +17,357 | +39,756 | +39,756 | 0.1% | 6 | 2.61 | 0 | — | — |
| v14_term | REJECTED | 996,505 | -1,607 | +1,140 | -3,495 | -3,495 | 0.6% | 3 | 1.31 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,020,879 | -308 | +6,474 | +20,879 | +20,879 | 0.1% | 2 | 0.93 | 0 | — | — |
| v16_equity_rebal | REJECTED | 971,665 | -890 | -6,499 | -28,335 | -28,335 | 3.3% | 1 | 0.37 | 2 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 983,020 | -5,466 | -12,533 | -16,980 | -16,980 | 2.4% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,009,494 | +973 | +5,644 | +9,494 | +9,494 | 0.1% | 4 | 0.77 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,006,501 | -24 | +11,751 | +14,030 | +6,501 | 0.1% | 4 | 2.64 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 992,078 | -192 | +7,022 | -7,420 | -7,922 | 1.0% | 1 | 0.64 | 9 | 11% | 0.12 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 997,813 | +3,311 | +14,746 | +22,253 | -2,187 | 1.1% | 2 | 2.28 | 18 | 22% | 0.74 |
| v2_trend_carry | CHALLENGER | 1,008,659 | -634 | +2,136 | +9,632 | +8,659 | 0.1% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,012,042 | +1,755 | +5,287 | +13,043 | +12,042 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,001,039 | -11,752 | -13,389 | +2,664 | +1,039 | 1.6% | 4 | 2.47 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,002,356 | -2,207 | -1,863 | +3,329 | +2,356 | 0.3% | 4 | 0.66 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 999,726 | -1,999 | -1,805 | +378 | -274 | 0.2% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,006,085 | -2,207 | -880 | +6,605 | +6,085 | 0.3% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,002,444 | -2,211 | -1,951 | +4,395 | +2,444 | 0.3% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,005,163 | -660 | +1,554 | +5,683 | +5,163 | 0.1% | 4 | 0.65 | 2 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 998,558 | -2,174 | -991 | -3,215 | -1,442 | 0.8% | 4 | 0.65 | 29 | 34% | 0.60 |
| v5_carry_trend_daily_10p | REJECTED | 1,004,514 | -1,826 | +850 | +9,823 | +4,514 | 0.2% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,000,887 | -1,027 | +1,410 | +7,452 | +887 | 0.5% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,001,940 | -7 | +2,547 | +5,464 | +1,940 | 0.0% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,009,522 | +620 | +4,216 | +12,627 | +9,522 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,009,522 | +620 | +4,216 | +12,627 | +9,522 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,018,101 | -7,335 | -6,223 | +18,101 | +18,101 | 0.9% | 5 | 2.18 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 988,179 | -3,133 | -5,735 | -11,821 | -11,821 | 1.5% | 4 | 1.64 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,010,267 | -4,174 | -3,823 | +10,267 | +10,267 | 0.5% | 4 | 1.61 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,037,674 | -615 | +9,930 | +37,674 | +37,674 | 0.1% | 7 | 1.37 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,037,674 | -615 | +9,930 | +37,674 | +37,674 | 0.1% | 7 | 1.37 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 990,475 | -353 | +10,361 | +4,085 | -9,525 | 2.6% | 6 | 2.32 | 20 | 20% | 0.12 |

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
