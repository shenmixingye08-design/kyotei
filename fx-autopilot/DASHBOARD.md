# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-09T06:47 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 876,333 | +6,682 | +77 | -88,607 | -123,667 | 13.8% | 1 | 0.81 | 167 | 41% | 0.62 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 997,787 | +0 | -16,032 | -24,957 | -2,213 | 4.0% | 0 | 0.00 | 33 | 52% | 0.97 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,037,880 | +6,683 | +13,907 | +29,361 | +37,880 | 0.2% | 2 | 2.96 | 33 | 58% | 1.49 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,000,002 | +0 | +7,122 | +328 | +2 | 0.4% | 0 | 0.00 | 7 | 43% | 1.00 |
| regime_switch_v1 | RESEARCH_ONLY | 969,701 | +0 | -9,483 | -7,485 | -30,299 | 4.8% | 0 | 0.00 | 44 | 30% | 0.72 |
| trend_donchian_v1 | RESEARCH_ONLY | 959,445 | -2,304 | -648 | -48,848 | -40,555 | 6.2% | 2 | 1.65 | 18 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 957,488 | -4,676 | +14,009 | -5,944 | -42,512 | 4.3% | 3 | 4.11 | 39 | 28% | 0.44 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,017,176 | +0 | -3,295 | +2,096 | +17,176 | 0.9% | 0 | 0.00 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -13,457 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,004,178 | -3,409 | -18,421 | -5,802 | +4,178 | 2.3% | 5 | 1.87 | 441 | 48% | 1.07 |
| v12_carry_timed | REJECTED | 1,004,152 | -4,414 | +4,152 | +4,152 | +4,152 | 0.5% | 6 | 2.58 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 998,094 | -176 | -1,906 | -1,906 | -1,906 | 0.3% | 3 | 1.18 | 0 | — | — |
| v13_ratemom | REJECTED | 1,006,133 | +1,050 | +6,133 | +6,133 | +6,133 | 0.1% | 6 | 2.70 | 0 | — | — |
| v14_term | REJECTED | 994,610 | -2,005 | -5,390 | -5,390 | -5,390 | 0.8% | 6 | 2.40 | 0 | — | — |
| v14_term_ratemom | REJECTED | 1,002,543 | -1,498 | +2,543 | +2,543 | +2,543 | 0.2% | 2 | 0.95 | 0 | — | — |
| v16_equity_rebal | REJECTED | 993,138 | +4,495 | -6,862 | -6,862 | -6,862 | 1.1% | 3 | 1.01 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 996,276 | +400 | -3,724 | -3,724 | -3,724 | 1.1% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 999,187 | -601 | -813 | -813 | -813 | 0.1% | 1 | 0.22 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 984,865 | +1,155 | -10,785 | -13,089 | -15,135 | 2.0% | 4 | 3.05 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 988,420 | -886 | -7,992 | -11,580 | -11,580 | 1.4% | 2 | 1.07 | 5 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 980,258 | -1,590 | +7,713 | -8,715 | -19,742 | 2.9% | 1 | 1.26 | 14 | 14% | 0.43 |
| v2_trend_carry | CHALLENGER | 1,000,975 | -739 | +1,128 | +975 | +975 | 0.1% | 3 | 0.45 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,002,266 | -473 | +1,362 | +2,266 | +2,266 | 0.1% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,000,234 | -1,651 | +1,443 | +234 | +234 | 0.5% | 4 | 2.48 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 999,451 | -545 | -396 | -549 | -549 | 0.2% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 998,584 | -243 | -1,573 | -1,283 | -1,416 | 0.3% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,001,418 | -739 | +1,128 | +1,418 | +1,418 | 0.1% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 999,622 | -546 | +988 | +342 | -378 | 0.1% | 4 | 0.56 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 999,386 | -437 | -904 | -614 | -614 | 0.2% | 2 | 0.34 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 997,763 | -436 | -3,649 | -6,235 | -2,237 | 0.8% | 2 | 0.33 | 20 | 35% | 0.55 |
| v5_carry_trend_daily_10p | REJECTED | 995,074 | -1,237 | +429 | -7,036 | -4,926 | 1.2% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 993,356 | -1,261 | +260 | -7,502 | -6,644 | 1.2% | 3 | 0.43 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 995,964 | -186 | -2,462 | -3,030 | -4,036 | 0.6% | 4 | 0.63 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 999,095 | -788 | +250 | -786 | -905 | 0.4% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 999,095 | -788 | +250 | -786 | -905 | 0.4% | 4 | 0.73 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,003,735 | -1,433 | +3,735 | +3,735 | +3,735 | 0.2% | 6 | 2.54 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 991,257 | +1,490 | -8,743 | -8,743 | -8,743 | 1.2% | 6 | 2.42 | 0 | — | — |
| v7_cm_monthly | REJECTED | 999,219 | -2,997 | -781 | -781 | -781 | 0.6% | 5 | 1.96 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,008,154 | -3,556 | +8,154 | +8,154 | +8,154 | 0.4% | 7 | 1.41 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,008,154 | -3,556 | +8,154 | +8,154 | +8,154 | 0.4% | 7 | 1.41 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 978,870 | -3,620 | -2,446 | -26,949 | -21,130 | 3.8% | 3 | 1.26 | 15 | 20% | 0.14 |

## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）

| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 1,165 | -12.5% | 0.94 | -0.49 | -15.1% | -9.7% | 0.87 | -0.94 | 0.88 |
| ml_logit_v1 | RESEARCH_ONLY | 514 | +1.5% | 1.02 | 0.11 | -12.7% | -3.2% | 0.83 | -0.58 | 0.91 |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 387 | -13.9% | 0.84 | -0.75 | -15.4% | -8.0% | 0.87 | -0.85 | 0.79 |
| mr_zscore_v1 | RESEARCH_ONLY | 250 | -11.3% | 0.83 | -0.61 | -15.4% | -8.8% | 0.88 | -0.73 | 0.78 |
| mtf_pullback_v1 | RESEARCH_ONLY | 134 | -10.7% | 0.74 | -0.92 | -15.0% | -7.6% | 0.76 | -1.06 | 0.71 |
| regime_switch_v1 | RESEARCH_ONLY | 410 | -6.5% | 0.94 | -0.19 | -15.1% | -13.8% | 0.72 | -1.21 | 0.92 |
| trend_donchian_v1 | RESEARCH_ONLY | 112 | +16.8% | 1.48 | 0.56 | -15.1% | -13.6% | 0.16 | -1.62 | 1.41 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 279 | -5.9% | 0.91 | -0.21 | -15.2% | -3.5% | 0.95 | -0.17 | 0.87 |
| trend_tsmom_v1 | RESEARCH_ONLY | 255 | +10.3% | 1.15 | 0.51 | -7.0% | -7.6% | 0.66 | -1.00 | 1.09 |
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
