# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-19T02:50 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY / KILL | 861,913 | +0 | +0 | -83,868 | -138,087 | 15.2% | 0 | 0.00 | 182 | 41% | 0.61 |
| ml_logit_v1 | RESEARCH_ONLY | 1,008,271 | +0 | +0 | +8,143 | +8,271 | 0.0% | 0 | 0.00 | 3 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 990,143 | -2,788 | -7,412 | -43,579 | -9,857 | 4.8% | 1 | 2.54 | 36 | 50% | 0.92 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,010,719 | -9,170 | -23,579 | -27,888 | +10,719 | 3.9% | 0 | 0.00 | 44 | 50% | 1.10 |
| mtf_pullback_v1 | RESEARCH_ONLY | 999,639 | +2,661 | +4,758 | +9,336 | -361 | 0.4% | 0 | 0.00 | 9 | 44% | 0.99 |
| regime_switch_v1 | RESEARCH_ONLY | 985,820 | +12,134 | +30,626 | -20,246 | -14,180 | 3.2% | 3 | 2.89 | 51 | 25% | 0.59 |
| trend_donchian_v1 | RESEARCH_ONLY | 994,194 | +6,397 | +18,899 | +13,853 | -5,806 | 2.8% | 3 | 2.83 | 19 | 11% | 0.15 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 954,183 | +0 | -4,546 | -99 | -45,817 | 4.6% | 0 | 0.00 | 48 | 29% | 0.62 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,039,821 | +8,855 | +19,695 | +25,013 | +39,821 | 0.0% | 3 | 2.08 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -4,604 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,010,656 | +3,156 | -419 | -1,698 | +10,656 | 1.7% | 5 | 1.74 | 561 | 48% | 1.07 |
| v12_carry_timed | REJECTED | 1,023,216 | +871 | +2,548 | +23,216 | +23,216 | 0.0% | 5 | 2.21 | 1 | 0% | 0.00 |
| v13_carry_ratemom | REJECTED | 1,010,944 | +2,436 | +3,717 | +10,944 | +10,944 | 0.0% | 2 | 0.84 | 1 | 0% | 0.00 |
| v13_ratemom | REJECTED | 1,033,723 | +7,215 | +18,823 | +33,723 | +33,723 | 0.0% | 6 | 2.63 | 0 | — | — |
| v14_term | REJECTED | 996,924 | +1,717 | -2,785 | -3,076 | -3,076 | 0.6% | 3 | 1.31 | 3 | 0% | 0.00 |
| v14_term_ratemom | REJECTED | 1,019,332 | +3,289 | +10,469 | +19,332 | +19,332 | 0.0% | 2 | 0.94 | 0 | — | — |
| v16_equity_rebal | REJECTED | 973,056 | -349 | -14,029 | -26,944 | -26,944 | 3.1% | 1 | 0.36 | 2 | 0% | 0.00 |
| v16_equity_rebal_carry | REJECTED | 988,898 | -2,105 | -12,076 | -11,102 | -11,102 | 1.8% | 2 | 0.75 | 1 | 0% | 0.00 |
| v2_d1_donchian | REJECTED | 1,007,657 | +1,797 | +7,340 | +7,657 | +7,657 | 0.0% | 2 | 0.39 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 1,004,605 | +5,619 | +16,020 | +11,851 | +4,605 | 0.1% | 4 | 2.64 | 3 | 33% | 0.04 |
| v2_h4_ema | REJECTED | 992,880 | +4,573 | +9,758 | -7,120 | -7,120 | 0.9% | 2 | 1.35 | 8 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 995,873 | +6,676 | +21,692 | +20,312 | -4,127 | 1.3% | 3 | 2.99 | 16 | 19% | 0.76 |
| v2_trend_carry | CHALLENGER | 1,008,618 | +1,105 | +4,494 | +8,942 | +8,618 | 0.0% | 3 | 0.44 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 1,010,184 | +1,489 | +6,903 | +11,168 | +10,184 | 0.0% | 3 | 0.46 | 0 | — | — |
| v3_carry_only | REJECTED | 1,011,548 | -1,229 | -2,283 | +11,466 | +11,548 | 0.6% | 4 | 2.45 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 1,004,367 | +84 | +1,392 | +4,691 | +4,367 | 0.0% | 4 | 0.65 | 2 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 1,001,207 | +401 | -259 | +1,663 | +1,207 | 0.1% | 4 | 0.55 | 2 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 1,008,096 | +84 | +3,530 | +8,420 | +8,096 | 0.0% | 4 | 0.65 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 1,004,457 | +84 | +1,307 | +5,422 | +4,457 | 0.0% | 4 | 0.65 | 4 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,005,008 | +54 | +3,117 | +5,333 | +5,008 | 0.0% | 3 | 0.44 | 2 | 0% | 0.00 |
| v4_carry_trend_h4 | REJECTED | 1,000,544 | +85 | +1,741 | -2,110 | +544 | 0.6% | 4 | 0.65 | 29 | 34% | 0.60 |
| v5_carry_trend_daily_10p | REJECTED | 1,005,734 | +1,084 | +5,159 | +9,120 | +5,734 | 0.1% | 4 | 0.58 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 1,001,421 | +843 | +3,967 | +6,064 | +1,421 | 0.4% | 4 | 0.58 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 1,001,056 | +1,835 | +2,852 | +4,588 | +1,056 | 0.1% | 4 | 0.72 | 4 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 1,008,515 | +1,501 | +6,728 | +10,627 | +8,515 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v6_trend_carry_mkt_5p | REJECTED | 1,008,515 | +1,501 | +6,728 | +10,627 | +8,515 | 0.0% | 4 | 0.62 | 3 | 33% | 0.48 |
| v7_carry_monthly | REJECTED | 1,025,227 | +1,769 | +2,127 | +25,227 | +25,227 | 0.1% | 5 | 2.16 | 1 | 0% | 0.00 |
| v7_ccv_monthly | REJECTED | 992,122 | -52 | -3,009 | -7,878 | -7,878 | 1.1% | 4 | 1.64 | 2 | 0% | 0.00 |
| v7_cm_monthly | REJECTED | 1,014,468 | +635 | +3,395 | +14,468 | +14,468 | 0.1% | 4 | 1.60 | 1 | 0% | 0.00 |
| v8_dollar_carry | REJECTED | 1,035,972 | +4,265 | +15,616 | +35,972 | +35,972 | 0.0% | 7 | 1.37 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 1,035,972 | +4,265 | +15,616 | +35,972 | +35,972 | 0.0% | 7 | 1.37 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 989,954 | +4,039 | +18,713 | -12 | -10,046 | 2.7% | 6 | 2.22 | 19 | 21% | 0.13 |

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
