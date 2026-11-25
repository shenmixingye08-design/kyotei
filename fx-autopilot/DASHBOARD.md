# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-25T09:02 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -48,291 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,009,588 | +1,318 | +1,318 | +9,460 | +9,588 | 0.1% | 0 | 0.00 | 4 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 973,331 | -2,245 | -19,599 | -50,547 | -26,669 | 6.4% | 1 | 1.08 | 40 | 45% | 0.76 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,024,685 | +8,738 | +9,471 | -127 | +24,685 | 2.6% | 1 | 0.82 | 51 | 53% | 1.24 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,009,397 | -4,906 | +9,758 | +20,951 | +9,397 | 0.5% | 0 | 0.00 | 12 | 50% | 1.32 |
| regime_switch_v1 | RESEARCH_ONLY | 1,007,880 | -5,771 | +29,934 | +11,862 | +7,880 | 1.0% | 1 | 0.73 | 58 | 31% | 1.02 |
| trend_donchian_v1 | RESEARCH_ONLY | 997,178 | +5,452 | +9,175 | +19,656 | -2,822 | 2.5% | 3 | 1.86 | 21 | 10% | 0.14 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 951,983 | +0 | -2,199 | -8,610 | -48,017 | 4.8% | 0 | 0.00 | 50 | 28% | 0.61 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,050,172 | -4,260 | +15,246 | +29,444 | +50,172 | 0.7% | 2 | 1.64 | 7 | 71% | 10.47 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | +0 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,001,901 | -6,076 | -5,723 | -18,997 | +1,901 | 2.5% | 5 | 1.81 | 626 | 48% | 1.01 |
| v12_carry_timed | REJECTED | 1,022,649 | -3,965 | -433 | +22,649 | +22,649 | 0.5% | 5 | 2.21 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,009,826 | -3,903 | -303 | +9,826 | +9,826 | 0.5% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,037,102 | -6,490 | +5,899 | +37,102 | +37,102 | 1.0% | 5 | 2.28 | 1 | 0% | 0.00 |
| v14_term | REJECTED | 997,360 | -3,271 | +1,241 | -2,640 | -2,640 | 0.5% | 3 | 1.31 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,023,345 | -2,352 | +5,200 | +23,345 | +23,345 | 0.4% | 2 | 0.93 | 0 | — | — |
| v16_equity_rebal | REJECTED | 970,125 | +0 | -3,003 | -29,875 | -29,875 | 3.4% | 0 | 0.00 | 3 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 985,834 | +445 | -3,803 | -14,166 | -14,166 | 2.1% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,012,014 | +676 | +5,753 | +12,014 | +12,014 | 0.1% | 4 | 0.77 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,012,011 | -5,065 | +8,787 | +17,588 | +12,011 | 0.9% | 4 | 2.62 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 991,763 | -2,851 | +171 | -6,976 | -8,237 | 1.0% | 0 | 0.00 | 10 | 20% | 0.57 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 988,504 | -6,632 | -5,015 | +12,943 | -11,496 | 2.0% | 0 | 0.00 | 20 | 25% | 0.76 |
| v2_trend_carry | CHALLENGER | 1,010,878 | +413 | +3,060 | +11,362 | +10,878 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,013,317 | +186 | +3,820 | +12,325 | +13,317 | 0.1% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,008,846 | -1,060 | -2,906 | +16,278 | +8,846 | 0.8% | 4 | 2.45 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,005,288 | +757 | +1,314 | +5,772 | +5,288 | 0.0% | 4 | 0.65 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,521 | -646 | +480 | +1,736 | +1,521 | 0.1% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,009,018 | +757 | +1,314 | +9,100 | +9,018 | 0.0% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,005,378 | +757 | +1,314 | +6,892 | +5,378 | 0.0% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,006,990 | -797 | +2,343 | +7,072 | +6,990 | 0.2% | 3 | 0.44 | 3 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 999,230 | -827 | -922 | -430 | -770 | 0.7% | 3 | 0.44 | 31 | 32% | 0.42 |
| v5_carry_trend_daily_10p | REJECTED | 1,005,352 | -1,922 | +61 | +10,601 | +5,352 | 0.3% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,002,029 | -1,332 | +906 | +9,419 | +2,029 | 0.3% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,003,363 | -1,390 | +2,907 | +4,888 | +3,363 | 0.2% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,011,512 | +80 | +3,764 | +12,618 | +11,512 | 0.1% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,011,512 | +80 | +3,764 | +12,618 | +11,512 | 0.1% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,019,185 | -6,248 | -5,301 | +19,185 | +19,185 | 0.8% | 5 | 2.18 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 992,292 | -1,583 | -422 | -7,708 | -7,708 | 1.1% | 4 | 1.64 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,013,223 | -3,487 | -1,281 | +13,223 | +13,223 | 0.5% | 4 | 1.60 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,040,133 | -1,897 | +6,764 | +40,133 | +40,133 | 0.4% | 7 | 1.36 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,040,133 | -1,897 | +6,764 | +40,133 | +40,133 | 0.4% | 7 | 1.36 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 991,485 | -6,671 | +2,635 | +5,589 | -8,515 | 2.5% | 6 | 2.31 | 20 | 20% | 0.12 |

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
