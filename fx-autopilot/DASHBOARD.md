# FX AUTOPILOT ダッシュボード（PAPER ONLY）

更新: 2026-11-05T11:13 UTC ／ モード: **PAPER** ／ LIVE: **無効**（本人の明示承認まで開始しない）

**Champion:** CASH（取引しない） — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
**LIVE 候補:** なし

## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）

| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ml_lgbm_v1 | RESEARCH_ONLY | 870,357 | -10,535 | -7,801 | -122,394 | -129,643 | 14.4% | 1 | 1.78 | 157 | 39% | 0.58 |
| ml_logit_v1 | RESEARCH_ONLY | 1,000,128 | +0 | +0 | +128 | +128 | 0.2% | 0 | 0.00 | 1 | 100% | — |
| mr_rsi_bb_v1 | RESEARCH_ONLY | 1,002,618 | -3,387 | -16,036 | -9,487 | +2,618 | 3.6% | 0 | 0.00 | 32 | 53% | 1.04 |
| mr_zscore_v1 | RESEARCH_ONLY | 1,032,219 | +8,317 | +10,178 | +26,603 | +32,219 | 0.8% | 3 | 4.20 | 29 | 55% | 1.44 |
| mtf_pullback_v1 | RESEARCH_ONLY | 1,000,002 | +0 | +14,378 | +328 | +2 | 0.4% | 0 | 0.00 | 7 | 43% | 1.00 |
| regime_switch_v1 | RESEARCH_ONLY | 969,701 | -1,587 | -5,725 | -28,477 | -30,299 | 4.8% | 0 | 0.00 | 44 | 30% | 0.72 |
| trend_donchian_v1 | RESEARCH_ONLY | 963,996 | -3,189 | -6,606 | -41,824 | -36,004 | 5.7% | 2 | 1.61 | 17 | 12% | 0.17 |
| trend_ema_adx_v1 | RESEARCH_ONLY | 950,662 | -4,230 | -13,110 | -30,173 | -49,338 | 4.9% | 2 | 2.70 | 36 | 28% | 0.40 |
| trend_tsmom_v1 | RESEARCH_ONLY | 1,017,176 | +0 | -5,817 | +7,206 | +17,176 | 0.9% | 0 | 0.00 | 6 | 67% | 5.83 |
| v10_carry_vix | REJECTED | 993,074 | +0 | +0 | -14,668 | -6,926 | 1.9% | 0 | 0.00 | 7 | 57% | 0.45 |
| v11_intraday_region | REJECTED | 1,004,675 | -1,024 | -19,876 | +4,695 | +4,675 | 2.3% | 5 | 2.05 | 416 | 48% | 1.01 |
| v12_carry_timed | REJECTED | 1,001,433 | -604 | +1,433 | +1,433 | +1,433 | 0.5% | 6 | 2.58 | 0 | — | — |
| v13_carry_ratemom | REJECTED | 999,969 | +841 | -31 | -31 | -31 | 0.1% | 3 | 1.18 | 0 | — | — |
| v13_ratemom | REJECTED | 990,633 | +3,455 | -9,367 | -9,367 | -9,367 | 1.0% | 6 | 2.74 | 0 | — | — |
| v14_term | REJECTED | 1,001,171 | -699 | +1,171 | +1,171 | +1,171 | 0.2% | 6 | 2.39 | 0 | — | — |
| v14_term_ratemom | REJECTED | 996,711 | +1,586 | -3,289 | -3,289 | -3,289 | 0.4% | 2 | 0.96 | 0 | — | — |
| v16_equity_rebal | REJECTED | 1,002,733 | -259 | +2,733 | +2,733 | +2,733 | 0.2% | 3 | 1.00 | 0 | — | — |
| v16_equity_rebal_carry | REJECTED | 1,005,710 | -1,469 | +5,710 | +5,710 | +5,710 | 0.1% | 3 | 1.06 | 0 | — | — |
| v2_d1_donchian | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_d1_tsmom | REJECTED | 988,892 | +3,114 | -11,119 | -7,626 | -11,108 | 1.6% | 4 | 3.03 | 2 | 50% | 0.12 |
| v2_h4_ema | REJECTED | 994,318 | -2,349 | -3,525 | -5,682 | -5,682 | 0.8% | 2 | 1.25 | 3 | 0% | 0.00 |
| v2_ml_d1_logit | REJECTED | 1,000,000 | +0 | +0 | +0 | +0 | 0.0% | 0 | 0.00 | 0 | — | — |
| v2_session_breakout | REJECTED | 977,800 | +0 | +3,300 | -19,626 | -22,200 | 3.1% | 0 | 0.00 | 14 | 14% | 0.43 |
| v2_trend_carry | CHALLENGER | 998,059 | +182 | -2,325 | -1,941 | -1,941 | 0.3% | 3 | 0.45 | 1 | 0% | 0.00 |
| v2_xpair_strength | REJECTED | 997,992 | +781 | -3,753 | -2,008 | -2,008 | 0.5% | 3 | 0.47 | 0 | — | — |
| v3_carry_only | REJECTED | 1,001,999 | -1,228 | +3,176 | +1,999 | +1,999 | 0.3% | 4 | 2.47 | 0 | — | — |
| v3_carry_trend_7p | REJECTED | 998,598 | +108 | -1,786 | -1,402 | -1,402 | 0.3% | 4 | 0.56 | 1 | 0% | 0.00 |
| v3_carry_trend_mh | REJECTED | 999,693 | +135 | -1,001 | +6 | -307 | 0.2% | 3 | 0.45 | 1 | 0% | 0.00 |
| v3_carry_trend_xs | REJECTED | 998,501 | +182 | -2,325 | -1,499 | -1,499 | 0.3% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_daily | REJECTED | 998,770 | +108 | -402 | -1,230 | -1,230 | 0.2% | 4 | 0.56 | 3 | 0% | 0.00 |
| v4_carry_trend_daily_fast | REJECTED | 1,000,715 | +135 | -112 | +715 | +715 | 0.1% | 3 | 0.45 | 0 | — | — |
| v4_carry_trend_h4 | REJECTED | 1,001,498 | -672 | -826 | -1,951 | +1,498 | 0.5% | 3 | 0.48 | 18 | 39% | 0.77 |
| v5_carry_trend_daily_10p | REJECTED | 993,017 | +198 | -3,775 | -10,089 | -6,983 | 1.4% | 4 | 0.59 | 2 | 0% | 0.00 |
| v5_carry_trend_weekly_10p | REJECTED | 990,041 | +298 | -4,583 | -11,321 | -9,959 | 1.5% | 3 | 0.43 | 2 | 0% | 0.00 |
| v6_carry_trend_daily_mkt_7p | REJECTED | 995,842 | +830 | -3,418 | -3,068 | -4,158 | 0.6% | 4 | 0.63 | 3 | 0% | 0.00 |
| v6_carry_trend_mkt_7p | REJECTED | 995,628 | +964 | -4,051 | -4,072 | -4,372 | 0.8% | 4 | 0.73 | 2 | 0% | 0.00 |
| v6_trend_carry_mkt_5p | REJECTED | 995,628 | +964 | -4,051 | -4,072 | -4,372 | 0.8% | 4 | 0.73 | 2 | 0% | 0.00 |
| v7_carry_monthly | REJECTED | 1,002,251 | -456 | +2,251 | +2,251 | +2,251 | 0.4% | 6 | 2.54 | 0 | — | — |
| v7_ccv_monthly | REJECTED | 1,002,841 | +588 | +2,841 | +2,841 | +2,841 | 0.1% | 6 | 2.39 | 0 | — | — |
| v7_cm_monthly | REJECTED | 1,001,776 | -235 | +1,776 | +1,776 | +1,776 | 0.3% | 5 | 1.95 | 0 | — | — |
| v8_dollar_carry | REJECTED | 997,042 | +350 | -2,958 | -2,958 | -2,958 | 0.7% | 7 | 1.42 | 0 | — | — |
| v8_dollar_carry_trend | REJECTED | 997,042 | +350 | -2,958 | -2,958 | -2,958 | 0.7% | 7 | 1.42 | 0 | — | — |
| v9_tsmom_multi | REJECTED | 980,329 | -161 | -3,687 | -27,178 | -19,671 | 3.6% | 4 | 1.08 | 11 | 18% | 0.07 |

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
