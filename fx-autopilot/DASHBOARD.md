# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-10-27T00:35 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 906,374 | +1,147 | -37,643 | -96,086 | -93,626 | 10.8% | 0 | 0.00 | 119 | 40% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,023,089 | -789 | -10,633 | +23,089 | +23,089 | 1.6% | 1 | 2.87 | 24 | 62% | 1.57 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,027,431 | +5,789 | -12,222 | +27,431 | +27,431 | 1.2% | 0 | 0.00 | 24 | 58% | 1.57 |
| mtf_pullback_v1 | RESEARCH_ONLY | 985,623 | -3,991 | -4,679 | -12,486 | -14,377 | 1.8% | 0 | 0.00 | 5 | 20% | 0.25 |
| regime_switch_v1 | RESEARCH_ONLY | 996,005 | -889 | -10,062 | -2,483 | -3,995 | 2.2% | 3 | 3.92 | 29 | 34% | 0.95 |
| trend_donchian_v1 | RESEARCH_ONLY | 975,119 | -5,380 | -4,699 | -24,873 | -24,881 | 4.6% | 3 | 2.23 | 11 | 9% | 0.22 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 959,176 | -4,100 | +3,797 | -39,830 | -40,824 | 4.1% | 1 | 2.19 | 27 | 26% | 0.43 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,022,337 | +1,738 | +6,957 | +22,337 | +22,337 | 0.1% | 2 | 1.04 | 4 | 75% | 6.25 |
| v10_carry_vix | REJECTED | 993,074 | +0 | -5,673 | -6,926 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,021,633 | +3,905 | +9,557 | +21,633 | +21,633 | 0.2% | 0 | 0.00 | 306 | 56% | 1.34 |
| v12_carry_timed | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v13_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 996,183 | +2,317 | +2,500 | -3,817 | -3,817 | 0.9% | 2 | 1.66 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 996,328 | -3,943 | -3,672 | -3,672 | -3,672 | 0.6% | 1 | 0.67 | 1 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 975,561 | +0 | +0 | -24,439 | -24,439 | 3.3% | 0 | 0.00 | 11 | 9% | 0.26 |
| v2_trend_carry | CHALLENGER | 1,000,116 | +844 | +347 | +116 | +116 | 0.1% | 2 | 0.29 | 0 | — | — |
| v2_xpair_strength | REJECTED | 1,001,527 | +578 | +2,321 | +1,527 | +1,527 | 0.0% | 2 | 0.35 | 0 | — | — |
| v3_carry_only | REJECTED | 995,577 | +4,601 | -4,672 | -4,423 | -4,423 | 0.9% | 3 | 1.85 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,000,116 | +844 | +347 | +116 | +116 | 0.1% | 2 | 0.29 | 0 | — | — |
| v3_carry_trend_mh | REJECTED | 1,000,285 | +688 | +648 | +285 | +285 | 0.1% | 1 | 0.18 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,000,418 | +689 | +648 | +418 | +418 | 0.1% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 998,903 | +605 | -191 | -1,097 | -1,097 | 0.2% | 2 | 0.29 | 2 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,000,418 | +689 | +648 | +418 | +418 | 0.1% | 1 | 0.18 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,000,759 | +1,753 | -1,988 | +759 | +759 | 0.5% | 3 | 0.45 | 13 | 31% | 0.28 |
| v5_carry_trend_daily_10p | REJECTED | 995,688 | +1,638 | -1,557 | -4,312 | -4,312 | 1.1% | 4 | 0.74 | 1 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 993,674 | +1,648 | -2,314 | -6,326 | -6,326 | 1.2% | 3 | 0.43 | 1 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 999,017 | +585 | +2,359 | -983 | -983 | 0.3% | 2 | 0.35 | 2 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 999,436 | +585 | +1,226 | -564 | -564 | 0.4% | 2 | 0.35 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 999,436 | +585 | +1,226 | -564 | -564 | 0.4% | 2 | 0.35 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 986,209 | +501 | -4,536 | -13,791 | -13,791 | 3.0% | 2 | 0.82 | 5 | 0% | 0.00 |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.95 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -3.2% | 0.83 | -0.59 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -5.6% | 0.91 | -0.60 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.74 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -8.5% | 0.73 | -1.24 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.23 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.65 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.17 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -7.2% | 0.68 | -0.96 | 1.09 |
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
