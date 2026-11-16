# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-16T01:27 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | -11,772 | -88,857 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +8,143 | +8,143 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 992,931 | -1,208 | -4,856 | -40,791 | -7,069 | 4.5% | 0 | 0.00 | 36 | 50% | 0.92 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,027,401 | -96 | -6,702 | -4,491 | +27,401 | 2.4% | 1 | 1.87 | 39 | 54% | 1.32 |
| mtf_pullback_v1 | RESEARCH_ONLY | 994,881 | +0 | -5,120 | +4,579 | -5,119 | 0.9% | 0 | 0.00 | 8 | 38% | 0.79 |
| regime_switch_v1 | RESEARCH_ONLY | 963,078 | -12 | -6,624 | -41,344 | -36,922 | 5.4% | 3 | 2.96 | 51 | 25% | 0.59 |
| trend_donchian_v1 | RESEARCH_ONLY | 983,846 | +799 | +24,548 | -895 | -16,154 | 3.8% | 3 | 2.86 | 19 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 958,347 | +107 | -2,102 | -871 | -41,653 | 4.2% | 1 | 1.10 | 46 | 28% | 0.57 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,024,792 | -46 | +7,616 | +8,646 | +24,792 | 0.2% | 1 | 0.43 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -3,414 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,009,533 | -26 | +3,953 | -2,496 | +9,533 | 1.8% | 5 | 1.76 | 516 | 48% | 1.08 |
| v12_carry_timed | REJECTED | 1,023,028 | +1,029 | +16,123 | +23,028 | +23,028 | 0.0% | 6 | 2.53 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 1,010,276 | +543 | +11,242 | +10,276 | +10,276 | 0.0% | 3 | 1.17 | 0 | — | — |
| v13_ratemom | REJECTED | 1,022,603 | +204 | +15,762 | +22,603 | +22,603 | 0.0% | 6 | 2.66 | 0 | — | — |
| v14_term | REJECTED | 996,090 | +724 | -614 | -3,910 | -3,910 | 0.7% | 4 | 1.64 | 2 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,014,464 | +58 | +10,754 | +14,464 | +14,464 | 0.0% | 2 | 0.94 | 0 | — | — |
| v16_equity_rebal | REJECTED | 978,636 | +472 | -12,408 | -21,364 | -21,364 | 2.6% | 2 | 0.70 | 1 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 996,231 | +678 | +225 | -3,769 | -3,769 | 1.1% | 3 | 1.07 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,003,831 | -19 | +4,562 | +3,831 | +3,831 | 0.0% | 2 | 0.39 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 994,762 | +12 | +8,480 | +9,356 | -5,238 | 1.0% | 3 | 2.24 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 984,756 | -301 | -4,448 | -15,244 | -15,244 | 1.7% | 2 | 1.36 | 8 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 982,950 | -117 | +1,345 | +7,389 | -17,050 | 2.6% | 1 | 1.11 | 15 | 13% | 0.39 |
| v2_trend_carry | CHALLENGER | 1,006,604 | +82 | +5,330 | +7,254 | +6,604 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,006,658 | -97 | +4,041 | +7,663 | +6,658 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,015,424 | +996 | +14,745 | +17,996 | +15,424 | 0.2% | 4 | 2.44 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,004,372 | +152 | +4,615 | +5,022 | +4,372 | 0.0% | 4 | 0.55 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,695 | +163 | +2,847 | +2,477 | +1,695 | 0.0% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,007,047 | +82 | +5,330 | +7,697 | +7,047 | 0.0% | 3 | 0.44 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,004,548 | +152 | +4,620 | +5,322 | +4,548 | 0.0% | 4 | 0.55 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,003,690 | +81 | +4,047 | +4,340 | +3,690 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 999,629 | +80 | +1,609 | -2,721 | -371 | 0.7% | 3 | 0.44 | 29 | 34% | 0.60 |
| v5_carry_trend_daily_10p | REJECTED | 1,003,929 | +266 | +7,981 | +6,767 | +3,929 | 0.3% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 999,654 | +177 | +5,493 | +3,744 | -346 | 0.6% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 999,466 | +72 | +3,122 | +3,240 | -534 | 0.2% | 4 | 0.62 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,005,296 | -10 | +5,532 | +7,618 | +5,296 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,005,296 | -10 | +5,532 | +7,618 | +5,296 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,025,617 | +1,292 | +20,550 | +25,617 | +25,617 | 0.0% | 6 | 2.48 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 994,424 | +510 | +2,782 | -5,576 | -5,576 | 0.9% | 5 | 1.97 | 1 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,014,975 | +885 | +13,466 | +14,975 | +14,975 | 0.0% | 5 | 1.93 | 0 | — | — |
| v8_dollar_carry | REJECTED | 1,028,164 | +419 | +17,978 | +28,164 | +28,164 | 0.0% | 7 | 1.38 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,028,164 | +419 | +17,978 | +28,164 | +28,164 | 0.0% | 7 | 1.38 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 980,544 | +430 | -901 | -11,795 | -19,456 | 3.6% | 6 | 2.24 | 19 | 21% | 0.13 |

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
