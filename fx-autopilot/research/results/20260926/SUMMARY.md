# FX AUTOPILOT 研究結果（2026-09-26 05:22 UTC）

**PAPER / BACKTEST のみ。利益を保証するものではありません。LIVE は本人の明示承認まで開始しません。**

## データ

Dukascopy 公開ヒストリカル（bid / ask 別 H1 足。Mid ではなく bid/ask で約定判定）

| pair | rows | first | last | spread_pips_median | spread_pips_p95 | weekday_gaps_gt_3h | crossed_quotes | abs_ret_gt_2pct |
|---|---|---|---|---|---|---|---|---|
| AUDUSD | 104339 | 2010-01-01 00:00:00+00:00 | 2026-09-25 20:00:00+00:00 | 1.0 | 2.4 | 16 | 20 | 7 |
| EURJPY | 104379 | 2010-01-01 00:00:00+00:00 | 2026-09-25 20:00:00+00:00 | 0.9 | 3.3 | 15 | 0 | 12 |
| EURUSD | 104382 | 2010-01-01 00:00:00+00:00 | 2026-09-25 20:00:00+00:00 | 0.4 | 1.4 | 15 | 0 | 1 |
| GBPUSD | 104371 | 2010-01-01 00:00:00+00:00 | 2026-09-25 20:00:00+00:00 | 1.0 | 3.2 | 16 | 0 | 5 |
| USDJPY | 104379 | 2010-01-01 00:00:00+00:00 | 2026-09-25 20:00:00+00:00 | 0.5 | 1.8 | 15 | 0 | 10 |

## データ分割（事前登録 `config/research_plan.yaml`）

- TRAIN 2010-01-01〜2018-12-31 ／ VALIDATION 2019-01-01〜2021-12-31（Stage 1 はこの 2 区間だけに切り詰めたデータで実行）
- TEST 2022-01-01〜2025-06-30 ／ FORWARD 2025-07-01〜最新（LOCK 後に 1 回だけ評価）
- Walk-Forward: 学習 4 年 → 検証 1 年を 2014〜2021 で繰り返し
- コスト（既定 retail_jp）: 実効スプレッド = max(実測, 国内業者の原則固定) + スリッページ （成行 0.2 pip / 逆指値 0.5 pip）+ スワップ（政策金利差 − 年1%）+ 1 本の執行遅延
- Risk: 1 トレード 0.5%、最大レバレッジ 5.0 倍、日次 2% / 週次 4% 損失で新規停止、DD 15% で全決済 + Kill Switch

## LOCK した仕様

| spec_id | trade_pairs | research_only | locked_at | spec_hash |
|---|---|---|---|---|
| ml_lgbm_v1 | USDJPY EURUSD EURJPY GBPUSD AUDUSD | True | 2026-09-25T12:17 | c5cce5bbf1cc |
| ml_logit_v1 | USDJPY EURUSD EURJPY GBPUSD AUDUSD | True | 2026-09-25T12:17 | 69ea55c68335 |
| mr_rsi_bb_v1 | USDJPY EURUSD EURJPY GBPUSD AUDUSD | True | 2026-09-25T12:17 | 4d6c83db42b9 |
| mr_zscore_v1 | USDJPY EURUSD EURJPY GBPUSD AUDUSD | True | 2026-09-25T12:17 | 633e1d300848 |
| mtf_pullback_v1 | USDJPY EURUSD EURJPY GBPUSD AUDUSD | True | 2026-09-25T12:17 | 14a8d8273c9e |
| regime_switch_v1 | USDJPY EURUSD EURJPY GBPUSD AUDUSD | True | 2026-09-25T12:17 | acd1486f9282 |
| trend_donchian_v1 | USDJPY EURUSD EURJPY GBPUSD AUDUSD | True | 2026-09-25T12:17 | f0784445d365 |
| trend_ema_adx_v1 | USDJPY EURUSD EURJPY GBPUSD AUDUSD | True | 2026-09-25T12:17 | 8fcf2bce96b7 |
| trend_tsmom_v1 | USDJPY EURUSD EURJPY GBPUSD AUDUSD | True | 2026-09-25T12:17 | 12e018ee5dcd |

## Stage 2: TEST / FORWARD（LOCK 後・1 回だけ）ポートフォリオ

| spec_id | period | variant | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | win_rate | payoff_ratio | expectancy_jpy | max_consecutive_losses | recovery_factor | exposure_time | avg_leverage | turnover_annual | total_cost_jpy | cost_ratio | halted_at |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ml_lgbm_v1 | FORWARD | portfolio | 453 | -9.7% | -7.9% | 0.87 | -0.98 | -1.22 | -15.0% | 47% | 0.98 | -214 | 12 | -0.61 | 21% | 2.87 | 1244 | 85,878 | — | 2025-10-17 01:00:00+00:00 |
| ml_lgbm_v1 | FORWARD | portfolio_ibkr | 316 | -14.7% | -12.1% | 0.72 | -2.14 | -2.38 | -15.1% | 47% | 0.81 | -466 | 12 | -0.97 | 14% | 2.85 | 828 | 227,724 | 2.69 | 2025-09-08 18:00:00+00:00 |
| ml_lgbm_v1 | FORWARD | portfolio_stress_2x | 419 | -13.5% | -11.1% | 0.81 | -1.52 | -1.88 | -15.0% | 45% | 0.99 | -322 | 12 | -0.88 | 20% | 2.86 | 1166 | 162,311 | 4.41 | 2025-10-08 05:00:00+00:00 |
| ml_lgbm_v1 | TEST | portfolio | 1165 | -12.5% | -3.8% | 0.94 | -0.49 | -0.64 | -15.1% | 48% | 1.00 | -107 | 8 | -0.81 | 17% | 2.45 | 903 | 182,009 | 2.31 | 2022-09-06 13:00:00+00:00 |
| ml_lgbm_v1 | TEST | portfolio_ibkr | 253 | -14.3% | -4.3% | 0.70 | -1.21 | -1.36 | -15.0% | 46% | 0.82 | -565 | 6 | -0.94 | 4% | 2.73 | 244 | 150,823 | 9.97 | 2022-03-04 15:00:00+00:00 |
| ml_lgbm_v1 | TEST | portfolio_stress_2x | 572 | -12.9% | -3.9% | 0.88 | -0.73 | -0.93 | -15.1% | 47% | 1.00 | -225 | 8 | -0.83 | 9% | 2.62 | 493 | 182,054 | 2.52 | 2022-05-06 17:00:00+00:00 |
| ml_logit_v1 | FORWARD | portfolio | 103 | -3.2% | -2.6% | 0.83 | -0.61 | -0.73 | -8.0% | 48% | 0.91 | -314 | 7 | -0.40 | 9% | 2.05 | 305 | 14,533 | — | — |
| ml_logit_v1 | FORWARD | portfolio_ibkr | 101 | -8.8% | -7.2% | 0.57 | -1.84 | -2.03 | -10.9% | 42% | 0.81 | -867 | 7 | -0.80 | 9% | 2.04 | 297 | 73,927 | — | — |
| ml_logit_v1 | FORWARD | portfolio_stress_2x | 102 | -5.2% | -4.2% | 0.74 | -0.96 | -1.12 | -9.2% | 45% | 0.90 | -510 | 7 | -0.56 | 9% | 2.07 | 304 | 30,920 | — | — |
| ml_logit_v1 | TEST | portfolio | 514 | +1.5% | +0.4% | 1.02 | 0.11 | 0.15 | -12.7% | 53% | 0.90 | 29 | 9 | 0.10 | 14% | 1.19 | 311 | 69,926 | 0.86 | — |
| ml_logit_v1 | TEST | portfolio_ibkr | 323 | -11.7% | -3.5% | 0.81 | -0.84 | -1.01 | -15.1% | 51% | 0.77 | -362 | 7 | -0.75 | 9% | 1.18 | 201 | 214,242 | 2.20 | 2024-08-02 13:00:00+00:00 |
| ml_logit_v1 | TEST | portfolio_stress_2x | 476 | -8.2% | -2.4% | 0.91 | -0.48 | -0.60 | -15.1% | 51% | 0.89 | -173 | 10 | -0.51 | 13% | 1.21 | 292 | 130,661 | 2.63 | 2025-04-06 22:00:00+00:00 |
| mr_rsi_bb_v1 | FORWARD | portfolio | 276 | -7.7% | -6.3% | 0.86 | -0.91 | -1.24 | -11.2% | 50% | 0.87 | -278 | 7 | -0.67 | 26% | 2.23 | 834 | 56,071 | — | — |
| mr_rsi_bb_v1 | FORWARD | portfolio_ibkr | 135 | -14.3% | -11.8% | 0.56 | -2.45 | -2.79 | -15.1% | 41% | 0.79 | -1,060 | 8 | -0.94 | 13% | 2.16 | 405 | 99,720 | — | 2026-02-17 12:00:00+00:00 |
| mr_rsi_bb_v1 | FORWARD | portfolio_stress_2x | 270 | -14.0% | -11.5% | 0.75 | -1.82 | -2.35 | -15.2% | 47% | 0.84 | -517 | 7 | -0.90 | 25% | 2.20 | 820 | 115,794 | — | 2026-09-16 20:00:00+00:00 |
| mr_rsi_bb_v1 | TEST | portfolio | 387 | -13.9% | -4.2% | 0.84 | -0.75 | -1.00 | -15.4% | 44% | 1.05 | -360 | 9 | -0.89 | 12% | 1.52 | 294 | 63,803 | — | 2023-06-27 14:00:00+00:00 |
| mr_rsi_bb_v1 | TEST | portfolio_ibkr | 116 | -14.2% | -4.3% | 0.55 | -1.41 | -1.67 | -15.4% | 41% | 0.81 | -1,225 | 9 | -0.91 | 4% | 1.64 | 106 | 71,261 | — | 2022-06-10 14:00:00+00:00 |
| mr_rsi_bb_v1 | TEST | portfolio_stress_2x | 281 | -13.9% | -4.2% | 0.79 | -0.85 | -1.15 | -15.2% | 43% | 1.05 | -493 | 9 | -0.90 | 8% | 1.47 | 209 | 88,821 | — | 2023-02-07 15:00:00+00:00 |
| mr_zscore_v1 | FORWARD | portfolio | 291 | -8.8% | -7.2% | 0.88 | -0.77 | -0.99 | -15.1% | 41% | 1.30 | -303 | 15 | -0.54 | 53% | 1.98 | 639 | 47,578 | — | 2026-09-16 11:00:00+00:00 |
| mr_zscore_v1 | FORWARD | portfolio_ibkr | 165 | -11.2% | -9.2% | 0.76 | -1.24 | -1.52 | -15.2% | 41% | 1.08 | -678 | 16 | -0.71 | 29% | 1.96 | 360 | 120,468 | 5.73 | 2026-02-12 02:00:00+00:00 |
| mr_zscore_v1 | FORWARD | portfolio_stress_2x | 283 | -10.2% | -8.3% | 0.86 | -0.91 | -1.16 | -15.0% | 41% | 1.22 | -360 | 15 | -0.64 | 50% | 1.99 | 629 | 93,171 | 5.24 | 2026-09-02 13:00:00+00:00 |
| mr_zscore_v1 | TEST | portfolio | 250 | -11.3% | -3.4% | 0.83 | -0.61 | -0.81 | -15.4% | 40% | 1.27 | -454 | 12 | -0.70 | 15% | 1.44 | 144 | 29,979 | — | 2022-10-26 07:00:00+00:00 |
| mr_zscore_v1 | TEST | portfolio_ibkr | 137 | -11.6% | -3.5% | 0.71 | -0.87 | -1.07 | -15.2% | 40% | 1.05 | -846 | 9 | -0.73 | 8% | 1.53 | 89 | 79,895 | — | 2022-06-10 12:00:00+00:00 |
| mr_zscore_v1 | TEST | portfolio_stress_2x | 208 | -12.1% | -3.6% | 0.78 | -0.74 | -0.94 | -15.0% | 38% | 1.26 | -584 | 12 | -0.78 | 12% | 1.46 | 125 | 50,232 | — | 2022-09-06 14:00:00+00:00 |
| mtf_pullback_v1 | FORWARD | portfolio | 104 | -8.5% | -6.9% | 0.72 | -1.30 | -1.69 | -10.0% | 37% | 1.25 | -818 | 9 | -0.84 | 20% | 2.03 | 321 | 31,593 | — | — |
| mtf_pullback_v1 | FORWARD | portfolio_ibkr | 102 | -14.2% | -11.7% | 0.57 | -2.22 | -2.68 | -15.1% | 37% | 0.95 | -1,393 | 9 | -0.93 | 20% | 2.03 | 313 | 89,116 | — | 2026-09-14 08:00:00+00:00 |
| mtf_pullback_v1 | FORWARD | portfolio_stress_2x | 102 | -13.7% | -11.2% | 0.57 | -2.25 | -2.74 | -15.0% | 31% | 1.24 | -1,341 | 9 | -0.90 | 17% | 1.99 | 312 | 60,128 | — | 2026-09-10 16:00:00+00:00 |
| mtf_pullback_v1 | TEST | portfolio | 134 | -10.7% | -3.2% | 0.74 | -0.92 | -1.23 | -15.0% | 34% | 1.42 | -801 | 19 | -0.68 | 8% | 1.43 | 100 | 26,354 | — | 2023-05-29 11:00:00+00:00 |
| mtf_pullback_v1 | TEST | portfolio_ibkr | 121 | -13.4% | -4.0% | 0.66 | -1.23 | -1.56 | -15.0% | 36% | 1.16 | -1,108 | 12 | -0.88 | 7% | 1.40 | 89 | 83,843 | — | 2023-04-28 01:00:00+00:00 |
| mtf_pullback_v1 | TEST | portfolio_stress_2x | 135 | -12.4% | -3.7% | 0.71 | -1.09 | -1.43 | -15.0% | 34% | 1.37 | -917 | 16 | -0.80 | 7% | 1.43 | 101 | 53,399 | — | 2023-05-29 13:00:00+00:00 |
| regime_switch_v1 | FORWARD | portfolio | 195 | -13.8% | -11.3% | 0.72 | -1.27 | -1.71 | -15.1% | 30% | 1.70 | -707 | 17 | -0.90 | 39% | 2.23 | 510 | 34,702 | — | 2026-02-23 09:00:00+00:00 |
| regime_switch_v1 | FORWARD | portfolio_ibkr | 80 | -14.9% | -12.3% | 0.42 | -2.06 | -2.38 | -15.3% | 22% | 1.46 | -1,864 | 17 | -0.97 | 16% | 2.20 | 217 | 59,424 | — | 2025-09-30 04:00:00+00:00 |
| regime_switch_v1 | FORWARD | portfolio_stress_2x | 152 | -14.8% | -12.1% | 0.63 | -1.65 | -2.07 | -15.1% | 30% | 1.50 | -971 | 12 | -0.97 | 31% | 2.25 | 408 | 62,224 | — | 2025-12-29 08:00:00+00:00 |
| regime_switch_v1 | TEST | portfolio | 410 | -6.5% | -1.9% | 0.94 | -0.19 | -0.27 | -15.1% | 36% | 1.68 | -159 | 10 | -0.39 | 23% | 1.66 | 284 | 68,278 | 4.68 | 2023-03-29 12:00:00+00:00 |
| regime_switch_v1 | TEST | portfolio_ibkr | 261 | -10.5% | -3.1% | 0.85 | -0.40 | -0.57 | -15.4% | 36% | 1.52 | -404 | 10 | -0.65 | 15% | 1.66 | 191 | 170,201 | 2.29 | 2022-11-10 14:00:00+00:00 |
| regime_switch_v1 | TEST | portfolio_stress_2x | 382 | -8.5% | -2.5% | 0.92 | -0.27 | -0.38 | -15.0% | 36% | 1.64 | -221 | 10 | -0.52 | 21% | 1.65 | 265 | 125,316 | 1.98 | 2023-03-01 07:00:00+00:00 |
| trend_donchian_v1 | FORWARD | portfolio | 52 | -13.6% | -11.2% | 0.16 | -1.70 | -2.05 | -15.0% | 17% | 0.76 | -2,616 | 14 | -0.89 | 23% | 1.82 | 84 | 6,821 | — | 2025-10-28 00:00:00+00:00 |
| trend_donchian_v1 | FORWARD | portfolio_ibkr | 41 | -14.0% | -11.5% | 0.07 | -1.88 | -2.21 | -15.1% | 10% | 0.60 | -3,410 | 26 | -0.91 | 18% | 1.87 | 68 | 28,341 | — | 2025-09-30 07:00:00+00:00 |
| trend_donchian_v1 | FORWARD | portfolio_stress_2x | 48 | -13.7% | -11.2% | 0.13 | -1.69 | -2.04 | -15.0% | 12% | 0.88 | -2,849 | 26 | -0.90 | 22% | 1.87 | 77 | 12,404 | — | 2025-10-19 22:00:00+00:00 |
| trend_donchian_v1 | TEST | portfolio | 112 | +16.8% | +4.5% | 1.48 | 0.56 | 0.83 | -15.1% | 34% | 2.89 | 1,496 | 15 | 0.81 | 30% | 1.66 | 44 | 12,359 | 0.06 | 2023-02-02 10:00:00+00:00 |
| trend_donchian_v1 | TEST | portfolio_ibkr | 103 | +12.8% | +3.5% | 1.38 | 0.46 | 0.67 | -15.1% | 33% | 2.81 | 1,247 | 9 | 0.64 | 28% | 1.68 | 41 | 63,232 | 0.30 | 2023-01-06 15:00:00+00:00 |
| trend_donchian_v1 | TEST | portfolio_stress_2x | 106 | +13.5% | +3.7% | 1.41 | 0.48 | 0.70 | -15.0% | 33% | 2.86 | 1,270 | 9 | 0.67 | 28% | 1.68 | 42 | 28,079 | 0.15 | 2023-01-06 15:00:00+00:00 |
| trend_ema_adx_v1 | FORWARD | portfolio | 303 | -3.5% | -2.8% | 0.95 | -0.18 | -0.30 | -15.0% | 30% | 2.18 | -114 | 10 | -0.20 | 68% | 2.50 | 735 | 64,506 | 1.58 | 2026-07-14 07:00:00+00:00 |
| trend_ema_adx_v1 | FORWARD | portfolio_ibkr | 244 | -13.3% | -10.9% | 0.79 | -0.94 | -1.45 | -15.9% | 31% | 1.77 | -545 | 11 | -0.81 | 57% | 2.48 | 578 | 187,664 | 2.59 | 2026-05-10 21:00:00+00:00 |
| trend_ema_adx_v1 | FORWARD | portfolio_stress_2x | 275 | -10.7% | -8.7% | 0.83 | -0.76 | -1.21 | -15.1% | 29% | 2.06 | -387 | 10 | -0.67 | 61% | 2.43 | 656 | 132,833 | 2.50 | 2026-06-05 12:00:00+00:00 |
| trend_ema_adx_v1 | TEST | portfolio | 279 | -5.9% | -1.7% | 0.91 | -0.21 | -0.33 | -15.2% | 29% | 2.20 | -210 | 18 | -0.35 | 22% | 1.66 | 170 | 42,417 | — | 2022-12-19 16:00:00+00:00 |
| trend_ema_adx_v1 | TEST | portfolio_ibkr | 203 | -12.1% | -3.6% | 0.78 | -0.57 | -0.84 | -15.4% | 26% | 2.27 | -595 | 16 | -0.76 | 16% | 1.76 | 136 | 129,475 | 6.15 | 2022-09-20 11:00:00+00:00 |
| trend_ema_adx_v1 | TEST | portfolio_stress_2x | 240 | -7.8% | -2.3% | 0.87 | -0.32 | -0.47 | -15.0% | 28% | 2.20 | -327 | 21 | -0.48 | 18% | 1.67 | 153 | 74,666 | 5.19 | 2022-11-01 21:00:00+00:00 |
| trend_tsmom_v1 | FORWARD | portfolio | 83 | -8.9% | -7.2% | 0.59 | -1.27 | -1.63 | -10.4% | 31% | 1.30 | -1,069 | 10 | -0.84 | 76% | 1.27 | 85 | 4,917 | — | — |
| trend_tsmom_v1 | FORWARD | portfolio_ibkr | 81 | -14.3% | -11.8% | 0.41 | -2.09 | -2.55 | -15.2% | 31% | 0.93 | -1,769 | 8 | -0.94 | 74% | 1.28 | 84 | 54,138 | — | 2026-09-17 23:00:00+00:00 |
| trend_tsmom_v1 | FORWARD | portfolio_stress_2x | 83 | -10.3% | -8.4% | 0.54 | -1.49 | -1.89 | -11.7% | 31% | 1.19 | -1,238 | 10 | -0.87 | 76% | 1.27 | 85 | 9,474 | — | — |
| trend_tsmom_v1 | TEST | portfolio | 255 | +10.3% | +2.9% | 1.15 | 0.51 | 0.77 | -7.0% | 38% | 1.91 | 405 | 16 | 1.29 | 83% | 0.96 | 73 | 14,987 | 0.12 | — |
| trend_tsmom_v1 | TEST | portfolio_ibkr | 254 | -3.9% | -1.1% | 0.94 | -0.12 | -0.17 | -8.3% | 36% | 1.69 | -154 | 16 | -0.45 | 83% | 0.96 | 73 | 154,856 | 1.14 | — |
| trend_tsmom_v1 | TEST | portfolio_stress_2x | 255 | +5.9% | +1.6% | 1.09 | 0.32 | 0.48 | -7.2% | 37% | 1.86 | 230 | 16 | 0.73 | 83% | 0.96 | 73 | 32,353 | 0.26 | — |

## Stage 2: 通貨ペア別（retail_jp コスト）

| spec_id | variant | period | n_trades | net_return | profit_factor | sharpe | max_drawdown | cost_ratio |
|---|---|---|---|---|---|---|---|---|
| ml_lgbm_v1 | AUDUSD | FORWARD | 348 | -11.7% | 0.83 | -1.35 | -15.1% | 5.25 |
| ml_lgbm_v1 | AUDUSD | TEST | 185 | -13.4% | 0.67 | -1.56 | -15.0% | — |
| ml_lgbm_v1 | EURJPY | FORWARD | 283 | -13.5% | 0.75 | -1.85 | -15.1% | — |
| ml_lgbm_v1 | EURJPY | TEST | 439 | -8.8% | 0.90 | -0.50 | -15.1% | — |
| ml_lgbm_v1 | EURUSD | FORWARD | 677 | -6.2% | 0.95 | -0.46 | -13.6% | 1.58 |
| ml_lgbm_v1 | EURUSD | TEST | 1110 | +2.3% | 1.01 | 0.15 | -15.1% | 0.73 |
| ml_lgbm_v1 | GBPUSD | FORWARD | 192 | +1.2% | 1.03 | 0.21 | -7.1% | 0.76 |
| ml_lgbm_v1 | GBPUSD | TEST | 529 | -14.5% | 0.85 | -0.86 | -15.0% | — |
| ml_lgbm_v1 | USDJPY | FORWARD | 320 | -2.3% | 0.96 | -0.18 | -10.4% | 4.64 |
| ml_lgbm_v1 | USDJPY | TEST | 892 | +0.4% | 1.00 | 0.05 | -12.4% | 0.93 |
| ml_logit_v1 | AUDUSD | FORWARD | 12 | -2.6% | 0.35 | -1.36 | -3.3% | — |
| ml_logit_v1 | AUDUSD | TEST | 24 | -1.1% | 0.77 | -0.30 | -3.2% | — |
| ml_logit_v1 | EURJPY | FORWARD | 26 | +0.9% | 1.29 | 0.53 | -1.2% | 0.28 |
| ml_logit_v1 | EURJPY | TEST | 275 | +10.7% | 1.23 | 0.92 | -7.5% | 0.27 |
| ml_logit_v1 | EURUSD | FORWARD | 21 | -1.1% | 0.74 | -0.54 | -2.9% | — |
| ml_logit_v1 | EURUSD | TEST | 77 | -3.3% | 0.79 | -0.50 | -6.2% | — |
| ml_logit_v1 | GBPUSD | FORWARD | 10 | -0.5% | 0.77 | -0.34 | -1.2% | — |
| ml_logit_v1 | GBPUSD | TEST | 31 | -2.4% | 0.63 | -0.65 | -4.4% | — |
| ml_logit_v1 | USDJPY | FORWARD | 39 | -1.0% | 0.86 | -0.38 | -3.3% | — |
| ml_logit_v1 | USDJPY | TEST | 114 | -0.4% | 0.98 | -0.05 | -4.8% | 2.31 |
| mr_rsi_bb_v1 | AUDUSD | FORWARD | 65 | +1.4% | 1.11 | 0.35 | -2.6% | 0.60 |
| mr_rsi_bb_v1 | AUDUSD | TEST | 224 | +10.2% | 1.21 | 0.73 | -5.2% | 0.41 |
| mr_rsi_bb_v1 | EURJPY | FORWARD | 52 | +1.1% | 1.10 | 0.15 | -2.7% | 0.49 |
| mr_rsi_bb_v1 | EURJPY | TEST | 157 | -14.5% | 0.65 | -1.30 | -15.1% | — |
| mr_rsi_bb_v1 | EURUSD | FORWARD | 69 | +5.2% | 1.34 | 1.04 | -3.8% | 0.21 |
| mr_rsi_bb_v1 | EURUSD | TEST | 210 | -2.6% | 0.95 | -0.18 | -7.2% | 2.35 |
| mr_rsi_bb_v1 | GBPUSD | FORWARD | 54 | -2.3% | 0.82 | -0.54 | -7.1% | — |
| mr_rsi_bb_v1 | GBPUSD | TEST | 172 | +3.4% | 1.09 | 0.25 | -4.0% | 0.50 |
| mr_rsi_bb_v1 | USDJPY | FORWARD | 56 | -6.5% | 0.55 | -1.67 | -7.7% | — |
| mr_rsi_bb_v1 | USDJPY | TEST | 97 | -15.1% | 0.49 | -1.63 | -15.1% | — |
| mr_zscore_v1 | AUDUSD | FORWARD | 64 | -6.8% | 0.65 | -1.47 | -8.0% | — |
| mr_zscore_v1 | AUDUSD | TEST | 207 | +6.6% | 1.12 | 0.46 | -5.5% | 0.40 |
| mr_zscore_v1 | EURJPY | FORWARD | 65 | +0.6% | 1.03 | 0.14 | -4.7% | 0.50 |
| mr_zscore_v1 | EURJPY | TEST | 202 | +8.9% | 1.17 | 0.56 | -7.3% | 0.21 |
| mr_zscore_v1 | EURUSD | FORWARD | 62 | -5.1% | 0.72 | -1.07 | -7.8% | — |
| mr_zscore_v1 | EURUSD | TEST | 209 | +13.1% | 1.24 | 0.76 | -6.7% | 0.15 |
| mr_zscore_v1 | GBPUSD | FORWARD | 69 | -2.6% | 0.86 | -0.49 | -6.1% | — |
| mr_zscore_v1 | GBPUSD | TEST | 206 | -0.6% | 0.99 | -0.02 | -5.5% | 0.97 |
| mr_zscore_v1 | USDJPY | FORWARD | 62 | +0.3% | 1.02 | 0.03 | -3.7% | 0.46 |
| mr_zscore_v1 | USDJPY | TEST | 208 | +0.0% | 1.00 | 0.02 | -9.6% | 0.58 |
| mtf_pullback_v1 | AUDUSD | FORWARD | 33 | -6.0% | 0.49 | -1.57 | -7.7% | — |
| mtf_pullback_v1 | AUDUSD | TEST | 111 | -9.2% | 0.73 | -0.77 | -13.7% | — |
| mtf_pullback_v1 | EURJPY | FORWARD | 34 | -0.7% | 0.93 | -0.19 | -2.3% | 1.92 |
| mtf_pullback_v1 | EURJPY | TEST | 102 | +3.8% | 1.13 | 0.36 | -6.0% | 0.40 |
| mtf_pullback_v1 | EURUSD | FORWARD | 15 | -1.4% | 0.71 | -0.51 | -3.0% | — |
| mtf_pullback_v1 | EURUSD | TEST | 40 | -7.0% | 0.50 | -1.13 | -8.7% | — |
| mtf_pullback_v1 | GBPUSD | FORWARD | 10 | -0.6% | 0.76 | -0.37 | -1.7% | — |
| mtf_pullback_v1 | GBPUSD | TEST | 44 | -4.1% | 0.67 | -0.68 | -5.8% | — |
| mtf_pullback_v1 | USDJPY | FORWARD | 13 | +0.5% | 1.14 | 0.18 | -2.6% | 0.18 |
| mtf_pullback_v1 | USDJPY | TEST | 42 | +3.6% | 1.34 | 0.49 | -3.8% | 0.14 |
| regime_switch_v1 | AUDUSD | FORWARD | 89 | +0.8% | 1.04 | 0.14 | -8.1% | 0.73 |
| regime_switch_v1 | AUDUSD | TEST | 256 | -8.5% | 0.88 | -0.46 | -14.9% | — |
| regime_switch_v1 | EURJPY | FORWARD | 98 | -7.2% | 0.76 | -0.90 | -11.4% | — |
| regime_switch_v1 | EURJPY | TEST | 273 | -10.8% | 0.85 | -0.54 | -12.5% | — |
| regime_switch_v1 | EURUSD | FORWARD | 93 | -2.8% | 0.89 | -0.38 | -6.1% | — |
| regime_switch_v1 | EURUSD | TEST | 258 | +3.7% | 1.05 | 0.21 | -9.4% | 0.44 |
| regime_switch_v1 | GBPUSD | FORWARD | 73 | -4.0% | 0.82 | -0.49 | -10.1% | — |
| regime_switch_v1 | GBPUSD | TEST | 212 | -5.1% | 0.91 | -0.29 | -7.1% | 7.65 |
| regime_switch_v1 | USDJPY | FORWARD | 89 | -13.6% | 0.48 | -2.08 | -15.3% | — |
| regime_switch_v1 | USDJPY | TEST | 273 | -3.6% | 0.96 | -0.12 | -13.0% | 272.55 |
| trend_donchian_v1 | AUDUSD | FORWARD | 49 | -11.9% | 0.36 | -1.71 | -12.6% | — |
| trend_donchian_v1 | AUDUSD | TEST | 75 | -14.6% | 0.43 | -0.96 | -15.1% | — |
| trend_donchian_v1 | EURJPY | FORWARD | 50 | -1.8% | 0.85 | -0.26 | -8.1% | — |
| trend_donchian_v1 | EURJPY | TEST | 137 | +0.3% | 1.01 | 0.04 | -10.0% | 0.64 |
| trend_donchian_v1 | EURUSD | FORWARD | 40 | -7.8% | 0.45 | -1.09 | -11.3% | — |
| trend_donchian_v1 | EURUSD | TEST | 80 | -10.4% | 0.63 | -0.57 | -15.0% | — |
| trend_donchian_v1 | GBPUSD | FORWARD | 29 | -2.7% | 0.60 | -0.59 | -5.5% | — |
| trend_donchian_v1 | GBPUSD | TEST | 80 | -1.0% | 0.95 | -0.06 | -8.9% | 0.77 |
| trend_donchian_v1 | USDJPY | FORWARD | 33 | -1.4% | 0.87 | -0.17 | -6.3% | — |
| trend_donchian_v1 | USDJPY | TEST | 101 | +13.4% | 1.34 | 0.48 | -11.9% | 0.10 |
| trend_ema_adx_v1 | AUDUSD | FORWARD | 81 | +5.6% | 1.28 | 0.71 | -4.2% | 0.32 |
| trend_ema_adx_v1 | AUDUSD | TEST | 146 | -10.1% | 0.72 | -0.70 | -15.0% | — |
| trend_ema_adx_v1 | EURJPY | FORWARD | 100 | -1.4% | 0.94 | -0.12 | -11.0% | 1.74 |
| trend_ema_adx_v1 | EURJPY | TEST | 245 | -14.9% | 0.73 | -0.83 | -15.0% | — |
| trend_ema_adx_v1 | EURUSD | FORWARD | 70 | -2.7% | 0.84 | -0.39 | -6.8% | — |
| trend_ema_adx_v1 | EURUSD | TEST | 184 | -7.7% | 0.83 | -0.43 | -10.2% | — |
| trend_ema_adx_v1 | GBPUSD | FORWARD | 50 | +3.5% | 1.32 | 0.59 | -5.4% | 0.22 |
| trend_ema_adx_v1 | GBPUSD | TEST | 153 | -5.6% | 0.84 | -0.34 | -10.9% | — |
| trend_ema_adx_v1 | USDJPY | FORWARD | 88 | -0.3% | 0.99 | -0.01 | -6.3% | 1.16 |
| trend_ema_adx_v1 | USDJPY | TEST | 245 | +17.9% | 1.29 | 0.77 | -8.1% | 0.16 |
| trend_tsmom_v1 | AUDUSD | FORWARD | 9 | -0.3% | 0.83 | -0.16 | -1.8% | — |
| trend_tsmom_v1 | AUDUSD | TEST | 47 | +1.8% | 1.17 | 0.24 | -3.4% | 0.18 |
| trend_tsmom_v1 | EURJPY | FORWARD | 21 | -3.2% | 0.44 | -1.13 | -4.4% | — |
| trend_tsmom_v1 | EURJPY | TEST | 59 | -2.9% | 0.82 | -0.29 | -4.7% | — |
| trend_tsmom_v1 | EURUSD | FORWARD | 25 | -1.4% | 0.78 | -0.47 | -2.6% | — |
| trend_tsmom_v1 | EURUSD | TEST | 71 | +4.8% | 1.26 | 0.45 | -4.8% | 0.06 |
| trend_tsmom_v1 | GBPUSD | FORWARD | 16 | +1.1% | 1.39 | 0.39 | -1.5% | 0.09 |
| trend_tsmom_v1 | GBPUSD | TEST | 46 | +0.2% | 1.02 | 0.09 | -5.0% | 0.31 |
| trend_tsmom_v1 | USDJPY | FORWARD | 24 | -4.4% | 0.41 | -1.38 | -4.9% | — |
| trend_tsmom_v1 | USDJPY | TEST | 74 | +5.6% | 1.27 | 0.50 | -4.4% | 0.06 |

## レバレッジ比較（同一シグナル・TEST 開始〜最新）

| spec_id | leverage_profile | risk_per_trade | max_leverage | n_trades | net_return | cagr | sharpe | max_drawdown | avg_leverage | halted_at |
|---|---|---|---|---|---|---|---|---|---|---|
| ml_lgbm_v1 | none | 0.005 | 1.005516 | 2755 | -15.3% | -3.5% | -0.57 | -15.4% | 0.89 | 2024-08-02 12:00:00+00:00 |
| ml_lgbm_v1 | low | 0.005 | 3.009476 | 755 | -13.6% | -3.1% | -0.56 | -15.2% | 2.21 | 2022-06-13 12:00:00+00:00 |
| ml_lgbm_v1 | medium | 0.01 | 9.978764 | 471 | -13.2% | -3.0% | -0.44 | -15.0% | 4.11 | 2022-05-05 13:00:00+00:00 |
| ml_logit_v1 | none | 0.005 | 0.999535 | 566 | +5.7% | +1.2% | 0.37 | -8.9% | 0.82 | — |
| ml_logit_v1 | low | 0.005 | 3.009394 | 553 | -3.8% | -0.8% | -0.16 | -15.2% | 1.23 | 2026-01-27 16:00:00+00:00 |
| ml_logit_v1 | medium | 0.01 | 5.178212 | 281 | +0.9% | +0.2% | 0.06 | -15.2% | 2.15 | 2024-07-31 06:00:00+00:00 |
| mr_rsi_bb_v1 | none | 0.005 | 1.003965 | 763 | -14.6% | -3.3% | -0.85 | -15.0% | 0.89 | 2025-10-23 06:00:00+00:00 |
| mr_rsi_bb_v1 | low | 0.005 | 2.996777 | 381 | -13.8% | -3.1% | -0.65 | -15.1% | 1.48 | 2023-06-27 12:00:00+00:00 |
| mr_rsi_bb_v1 | medium | 0.01 | 6.755715 | 76 | -13.4% | -3.0% | -0.89 | -15.2% | 2.75 | 2022-04-25 14:00:00+00:00 |
| mr_zscore_v1 | none | 0.005 | 1.005718 | 882 | -2.6% | -0.6% | -0.07 | -12.6% | 0.85 | — |
| mr_zscore_v1 | low | 0.005 | 2.987962 | 244 | -11.3% | -2.5% | -0.54 | -15.2% | 1.41 | 2022-10-21 10:00:00+00:00 |
| mr_zscore_v1 | medium | 0.01 | 8.107955 | 93 | -6.6% | -1.4% | -0.30 | -15.2% | 2.62 | 2022-04-27 14:00:00+00:00 |
| mtf_pullback_v1 | none | 0.005 | 1.007518 | 375 | -7.1% | -1.6% | -0.44 | -12.4% | 0.91 | — |
| mtf_pullback_v1 | low | 0.005 | 2.998631 | 128 | -10.8% | -2.4% | -0.83 | -15.1% | 1.40 | 2023-05-16 14:00:00+00:00 |
| mtf_pullback_v1 | medium | 0.01 | 6.60056 | 110 | -5.1% | -1.1% | -0.16 | -15.3% | 2.57 | 2023-04-10 12:00:00+00:00 |
| regime_switch_v1 | none | 0.005 | 1.007785 | 705 | -8.3% | -1.8% | -0.31 | -15.1% | 0.87 | 2025-05-05 05:00:00+00:00 |
| regime_switch_v1 | low | 0.005 | 3.018153 | 416 | -6.5% | -1.4% | -0.17 | -15.1% | 1.58 | 2023-04-12 13:00:00+00:00 |
| regime_switch_v1 | medium | 0.01 | 9.325208 | 235 | -3.1% | -0.7% | -0.01 | -15.1% | 2.86 | 2022-11-21 08:00:00+00:00 |
| trend_donchian_v1 | none | 0.005 | 1.04737 | 122 | +2.4% | +0.5% | 0.14 | -15.0% | 0.81 | 2023-05-03 20:00:00+00:00 |
| trend_donchian_v1 | low | 0.005 | 3.117194 | 112 | +16.8% | +3.3% | 0.49 | -15.1% | 1.64 | 2023-02-02 10:00:00+00:00 |
| trend_donchian_v1 | medium | 0.01 | 6.742134 | 93 | +20.9% | +4.1% | 0.42 | -15.4% | 2.56 | 2022-12-15 17:00:00+00:00 |
| trend_ema_adx_v1 | none | 0.005 | 1.034141 | 329 | -8.1% | -1.8% | -0.41 | -15.1% | 0.82 | 2023-09-22 08:00:00+00:00 |
| trend_ema_adx_v1 | low | 0.005 | 3.024721 | 277 | -5.3% | -1.2% | -0.17 | -15.1% | 1.57 | 2022-12-19 11:00:00+00:00 |
| trend_ema_adx_v1 | medium | 0.01 | 8.111146 | 183 | -6.2% | -1.3% | -0.12 | -15.1% | 2.89 | 2022-09-19 01:00:00+00:00 |
| trend_tsmom_v1 | none | 0.005 | 1.011968 | 294 | -3.8% | -0.8% | -0.16 | -10.1% | 0.68 | — |
| trend_tsmom_v1 | low | 0.005 | 2.971962 | 337 | -0.7% | -0.1% | 0.03 | -13.5% | 1.04 | — |
| trend_tsmom_v1 | medium | 0.01 | 5.424095 | 260 | +12.6% | +2.6% | 0.30 | -15.0% | 1.94 | 2025-08-07 04:00:00+00:00 |

## 年別（全期間・研究用設定）

| year | ml_lgbm_v1 | ml_logit_v1 | mr_rsi_bb_v1 | mr_zscore_v1 | mtf_pullback_v1 | regime_switch_v1 | trend_donchian_v1 | trend_ema_adx_v1 | trend_tsmom_v1 |
|---|---|---|---|---|---|---|---|---|---|
| 2010.0 | +0.0% | +0.0% | -2.4% | -9.7% | +2.8% | -2.2% | +5.1% | +13.3% | +11.8% |
| 2011.0 | +0.0% | +0.0% | +0.9% | -4.9% | +0.8% | -22.1% | -9.4% | -22.8% | -3.7% |
| 2012.0 | +0.0% | +0.0% | -17.1% | -21.9% | -1.7% | +1.1% | +8.2% | -2.7% | +11.7% |
| 2013.0 | +0.0% | +0.0% | -13.0% | -6.9% | -2.5% | -4.0% | +0.3% | +2.9% | -1.3% |
| 2014.0 | -1.3% | +11.0% | -5.2% | +10.5% | +4.6% | -6.8% | +10.7% | +8.5% | -1.9% |
| 2015.0 | -26.3% | -8.3% | -0.5% | -9.3% | -1.7% | +7.5% | +9.9% | +2.6% | +5.0% |
| 2016.0 | +17.4% | -3.8% | -10.3% | -16.9% | -7.3% | +1.6% | -5.6% | -6.8% | +3.5% |
| 2017.0 | -17.9% | +0.2% | +0.7% | -4.3% | +3.5% | -18.2% | -4.1% | +9.0% | +1.5% |
| 2018.0 | -0.8% | +2.7% | -11.9% | -11.0% | +6.8% | -11.5% | -6.5% | -0.7% | +5.3% |
| 2019.0 | -48.1% | -1.4% | -2.5% | -5.9% | -4.7% | -20.0% | -20.3% | +2.6% | -5.4% |
| 2020.0 | -30.3% | -1.6% | -9.0% | -16.3% | -6.9% | -20.6% | -14.6% | +0.0% | -9.8% |
| 2021.0 | -30.3% | +1.0% | -7.0% | -0.7% | -14.1% | -16.9% | -9.8% | -10.9% | -1.2% |
| 2022.0 | -22.4% | +5.8% | -6.8% | -11.4% | +1.2% | +1.6% | +23.1% | -4.7% | +2.6% |
| 2023.0 | -13.4% | +5.9% | -9.4% | +18.6% | -14.5% | -6.4% | -12.4% | -8.9% | +10.5% |
| 2024.0 | -28.1% | -8.2% | -0.8% | +10.2% | +2.9% | -2.8% | -4.8% | -11.3% | +0.6% |
| 2025.0 | -11.9% | -2.2% | -10.2% | +8.7% | +1.1% | -22.5% | -21.6% | -5.2% | -2.8% |
| 2026.0 | -14.9% | -2.5% | -2.7% | -14.1% | -8.1% | -5.1% | -0.3% | +1.5% | -8.5% |

## 相場局面別（エントリー時点の状態・全期間）

| spec_id | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| ml_lgbm_v1 | regime4h | HIGH_VOL | 1410 | -171,254 | 49% | 0.87 |
| ml_lgbm_v1 | regime4h | NEUTRAL | 3545 | -286,479 | 48% | 0.90 |
| ml_lgbm_v1 | regime4h | RANGE | 5775 | -176,355 | 48% | 0.96 |
| ml_lgbm_v1 | regime4h | TREND | 7713 | -302,623 | 49% | 0.95 |
| ml_lgbm_v1 | month_dir | DOWN | 4074 | -405,152 | 47% | 0.89 |
| ml_lgbm_v1 | month_dir | FLAT | 10471 | -370,046 | 49% | 0.96 |
| ml_lgbm_v1 | month_dir | UP | 3898 | -161,514 | 49% | 0.95 |
| ml_lgbm_v1 | month_vol | HIGH_VOL | 6293 | -113,704 | 50% | 0.98 |
| ml_lgbm_v1 | month_vol | LOW_VOL | 12150 | -823,007 | 48% | 0.92 |
| ml_logit_v1 | regime4h | HIGH_VOL | 507 | +69,395 | 54% | 1.08 |
| ml_logit_v1 | regime4h | NEUTRAL | 223 | -50,036 | 48% | 0.89 |
| ml_logit_v1 | regime4h | RANGE | 236 | +60,759 | 52% | 1.15 |
| ml_logit_v1 | regime4h | TREND | 885 | -112,704 | 49% | 0.94 |
| ml_logit_v1 | month_dir | DOWN | 544 | -178,276 | 47% | 0.84 |
| ml_logit_v1 | month_dir | FLAT | 787 | +110,244 | 53% | 1.08 |
| ml_logit_v1 | month_dir | UP | 520 | +35,445 | 51% | 1.04 |
| ml_logit_v1 | month_vol | HIGH_VOL | 1097 | -24,117 | 52% | 0.99 |
| ml_logit_v1 | month_vol | LOW_VOL | 754 | -8,470 | 49% | 0.99 |
| mr_rsi_bb_v1 | regime4h | HIGH_VOL | 195 | -34,582 | 51% | 0.85 |
| mr_rsi_bb_v1 | regime4h | NEUTRAL | 801 | -53,895 | 48% | 0.95 |
| mr_rsi_bb_v1 | regime4h | RANGE | 1725 | -253,761 | 47% | 0.89 |
| mr_rsi_bb_v1 | regime4h | TREND | 1311 | -326,770 | 47% | 0.82 |
| mr_rsi_bb_v1 | regime4h | UNKNOWN | 2 | -9,873 | 0% | 0.00 |
| mr_rsi_bb_v1 | month_dir | DOWN | 862 | -321,667 | 46% | 0.73 |
| mr_rsi_bb_v1 | month_dir | FLAT | 2201 | -122,155 | 49% | 0.95 |
| mr_rsi_bb_v1 | month_dir | UP | 971 | -235,059 | 45% | 0.83 |
| mr_rsi_bb_v1 | month_vol | HIGH_VOL | 1284 | -296,890 | 46% | 0.82 |
| mr_rsi_bb_v1 | month_vol | LOW_VOL | 2750 | -381,991 | 48% | 0.89 |
| mr_zscore_v1 | regime4h | HIGH_VOL | 419 | -12,765 | 44% | 0.97 |
| mr_zscore_v1 | regime4h | NEUTRAL | 889 | -212,056 | 43% | 0.83 |
| mr_zscore_v1 | regime4h | RANGE | 1045 | -221,761 | 42% | 0.85 |
| mr_zscore_v1 | regime4h | TREND | 2208 | -178,576 | 42% | 0.94 |
| mr_zscore_v1 | month_dir | DOWN | 1153 | -616,357 | 36% | 0.68 |
| mr_zscore_v1 | month_dir | FLAT | 2409 | +386,668 | 48% | 1.14 |
| mr_zscore_v1 | month_dir | UP | 999 | -395,469 | 37% | 0.75 |
| mr_zscore_v1 | month_vol | HIGH_VOL | 1457 | -192,756 | 41% | 0.90 |
| mr_zscore_v1 | month_vol | LOW_VOL | 3104 | -432,403 | 43% | 0.90 |
| mtf_pullback_v1 | regime4h | HIGH_VOL | 5 | +22,682 | 80% | 5.72 |
| mtf_pullback_v1 | regime4h | NEUTRAL | 308 | -92,742 | 38% | 0.89 |
| mtf_pullback_v1 | regime4h | RANGE | 461 | -119,345 | 39% | 0.90 |
| mtf_pullback_v1 | regime4h | TREND | 832 | -151,289 | 41% | 0.93 |
| mtf_pullback_v1 | month_dir | DOWN | 314 | +112,479 | 45% | 1.15 |
| mtf_pullback_v1 | month_dir | FLAT | 901 | -572,616 | 36% | 0.77 |
| mtf_pullback_v1 | month_dir | UP | 391 | +119,443 | 45% | 1.13 |
| mtf_pullback_v1 | month_vol | HIGH_VOL | 416 | -230,800 | 37% | 0.79 |
| mtf_pullback_v1 | month_vol | LOW_VOL | 1190 | -109,894 | 41% | 0.96 |
| regime_switch_v1 | regime4h | HIGH_VOL | 34 | -13,795 | 47% | 0.43 |
| regime_switch_v1 | regime4h | NEUTRAL | 152 | -96,920 | 30% | 0.59 |
| regime_switch_v1 | regime4h | RANGE | 3393 | -583,259 | 36% | 0.88 |
| regime_switch_v1 | regime4h | TREND | 1831 | -110,839 | 33% | 0.96 |
| regime_switch_v1 | month_dir | DOWN | 1069 | -82,625 | 36% | 0.95 |
| regime_switch_v1 | month_dir | FLAT | 3096 | -698,697 | 34% | 0.84 |
| regime_switch_v1 | month_dir | UP | 1245 | -23,490 | 35% | 0.99 |
| regime_switch_v1 | month_vol | HIGH_VOL | 1572 | -88,177 | 37% | 0.96 |
| regime_switch_v1 | month_vol | LOW_VOL | 3838 | -716,635 | 34% | 0.87 |
| trend_donchian_v1 | regime4h | HIGH_VOL | 110 | +5,709 | 27% | 1.02 |
| trend_donchian_v1 | regime4h | NEUTRAL | 476 | +157,707 | 30% | 1.13 |
| trend_donchian_v1 | regime4h | RANGE | 742 | -429,352 | 26% | 0.79 |
| trend_donchian_v1 | regime4h | TREND | 653 | -208,421 | 24% | 0.89 |
| trend_donchian_v1 | month_dir | DOWN | 385 | +538,526 | 36% | 1.60 |
| trend_donchian_v1 | month_dir | FLAT | 1186 | -2,106,210 | 19% | 0.41 |
| trend_donchian_v1 | month_dir | UP | 410 | +1,093,327 | 40% | 2.19 |
| trend_donchian_v1 | month_vol | HIGH_VOL | 573 | +83,884 | 28% | 1.05 |
| trend_donchian_v1 | month_vol | LOW_VOL | 1408 | -558,241 | 26% | 0.86 |
| trend_ema_adx_v1 | regime4h | HIGH_VOL | 313 | -204,964 | 27% | 0.69 |
| trend_ema_adx_v1 | regime4h | NEUTRAL | 1140 | -11,026 | 32% | 1.00 |
| trend_ema_adx_v1 | regime4h | RANGE | 2436 | +21,427 | 31% | 1.00 |
| trend_ema_adx_v1 | regime4h | TREND | 887 | -138,357 | 31% | 0.93 |
| trend_ema_adx_v1 | month_dir | DOWN | 879 | +637,378 | 35% | 1.35 |
| trend_ema_adx_v1 | month_dir | FLAT | 2941 | -1,096,328 | 30% | 0.83 |
| trend_ema_adx_v1 | month_dir | UP | 956 | +126,031 | 32% | 1.06 |
| trend_ema_adx_v1 | month_vol | HIGH_VOL | 1511 | -395,844 | 30% | 0.88 |
| trend_ema_adx_v1 | month_vol | LOW_VOL | 3265 | +62,924 | 32% | 1.01 |
| trend_tsmom_v1 | regime4h | HIGH_VOL | 77 | -32,499 | 36% | 0.83 |
| trend_tsmom_v1 | regime4h | NEUTRAL | 196 | -62,151 | 37% | 0.90 |
| trend_tsmom_v1 | regime4h | RANGE | 237 | +152,852 | 38% | 1.21 |
| trend_tsmom_v1 | regime4h | TREND | 617 | +99,143 | 38% | 1.05 |
| trend_tsmom_v1 | month_dir | DOWN | 260 | +601,542 | 50% | 2.01 |
| trend_tsmom_v1 | month_dir | FLAT | 591 | -1,151,684 | 27% | 0.48 |
| trend_tsmom_v1 | month_dir | UP | 276 | +707,487 | 48% | 2.00 |
| trend_tsmom_v1 | month_vol | HIGH_VOL | 357 | +107,718 | 37% | 1.10 |
| trend_tsmom_v1 | month_vol | LOW_VOL | 770 | +49,627 | 38% | 1.02 |

## イベント期間（金融危機・急変相場）

| spec_id | event | return | max_drawdown | trades | pnl_jpy |
|---|---|---|---|---|---|
| ml_lgbm_v1 | EUR_debt_crisis_2011 | +0.0% | 0.0% | 0 | +0 |
| ml_lgbm_v1 | abenomics_2012_2013 | +0.0% | 0.0% | 0 | +0 |
| ml_lgbm_v1 | SNB_shock_2015 | -0.1% | -4.7% | 115 | -254 |
| ml_lgbm_v1 | brexit_vote_2016 | +6.9% | -4.4% | 164 | +49,802 |
| ml_lgbm_v1 | covid_crash_2020 | -2.6% | -8.4% | 389 | -7,236 |
| ml_lgbm_v1 | usd_jpy_surge_2022 | -19.7% | -24.0% | 1157 | -33,191 |
| ml_lgbm_v1 | yen_carry_unwind_2024 | -2.6% | -2.9% | 121 | -2,671 |
| ml_logit_v1 | EUR_debt_crisis_2011 | +0.0% | 0.0% | 0 | +0 |
| ml_logit_v1 | abenomics_2012_2013 | +0.0% | 0.0% | 0 | +0 |
| ml_logit_v1 | SNB_shock_2015 | -1.3% | -3.1% | 20 | -14,096 |
| ml_logit_v1 | brexit_vote_2016 | -1.0% | -3.8% | 69 | -12,518 |
| ml_logit_v1 | covid_crash_2020 | +2.4% | -4.1% | 97 | +23,380 |
| ml_logit_v1 | usd_jpy_surge_2022 | +6.3% | -2.3% | 81 | +62,487 |
| ml_logit_v1 | yen_carry_unwind_2024 | -9.1% | -10.2% | 64 | -99,417 |
| mr_rsi_bb_v1 | EUR_debt_crisis_2011 | +4.1% | -5.3% | 136 | +38,346 |
| mr_rsi_bb_v1 | abenomics_2012_2013 | -13.0% | -15.9% | 145 | -110,726 |
| mr_rsi_bb_v1 | SNB_shock_2015 | +1.4% | -1.1% | 14 | +6,808 |
| mr_rsi_bb_v1 | brexit_vote_2016 | -0.3% | -2.4% | 21 | -7,197 |
| mr_rsi_bb_v1 | covid_crash_2020 | +3.1% | -2.8% | 36 | +18,777 |
| mr_rsi_bb_v1 | usd_jpy_surge_2022 | -5.0% | -8.3% | 176 | -17,304 |
| mr_rsi_bb_v1 | yen_carry_unwind_2024 | -3.0% | -3.3% | 33 | -10,391 |
| mr_zscore_v1 | EUR_debt_crisis_2011 | -4.7% | -6.9% | 144 | -35,429 |
| mr_zscore_v1 | abenomics_2012_2013 | -9.9% | -16.2% | 177 | -74,753 |
| mr_zscore_v1 | SNB_shock_2015 | -0.8% | -1.6% | 14 | -5,162 |
| mr_zscore_v1 | brexit_vote_2016 | -0.7% | -2.7% | 15 | -2,530 |
| mr_zscore_v1 | covid_crash_2020 | -6.3% | -9.0% | 60 | -22,592 |
| mr_zscore_v1 | usd_jpy_surge_2022 | -15.5% | -15.5% | 202 | -55,285 |
| mr_zscore_v1 | yen_carry_unwind_2024 | +0.9% | -5.6% | 43 | +3,617 |
| mtf_pullback_v1 | EUR_debt_crisis_2011 | +6.2% | -2.1% | 46 | +53,921 |
| mtf_pullback_v1 | abenomics_2012_2013 | -1.7% | -5.0% | 57 | -16,475 |
| mtf_pullback_v1 | SNB_shock_2015 | +0.2% | -0.8% | 2 | +2,127 |
| mtf_pullback_v1 | brexit_vote_2016 | +0.8% | -1.0% | 6 | +7,751 |
| mtf_pullback_v1 | covid_crash_2020 | -0.3% | -1.9% | 13 | -2,574 |
| mtf_pullback_v1 | usd_jpy_surge_2022 | +6.1% | -2.5% | 53 | +47,269 |
| mtf_pullback_v1 | yen_carry_unwind_2024 | +1.1% | -1.2% | 8 | +13,810 |
| regime_switch_v1 | EUR_debt_crisis_2011 | -6.2% | -12.2% | 154 | -47,822 |
| regime_switch_v1 | abenomics_2012_2013 | +6.3% | -6.1% | 195 | +53,917 |
| regime_switch_v1 | SNB_shock_2015 | +0.7% | -0.8% | 4 | -3,787 |
| regime_switch_v1 | brexit_vote_2016 | +10.4% | -2.4% | 17 | +55,152 |
| regime_switch_v1 | covid_crash_2020 | -5.5% | -5.6% | 35 | -22,859 |
| regime_switch_v1 | usd_jpy_surge_2022 | +4.1% | -7.9% | 209 | +12,732 |
| regime_switch_v1 | yen_carry_unwind_2024 | -0.4% | -3.3% | 28 | +616 |
| trend_donchian_v1 | EUR_debt_crisis_2011 | +0.5% | -8.6% | 54 | +17,684 |
| trend_donchian_v1 | abenomics_2012_2013 | +11.2% | -9.8% | 68 | +117,197 |
| trend_donchian_v1 | SNB_shock_2015 | +4.0% | -2.7% | 5 | -18,772 |
| trend_donchian_v1 | brexit_vote_2016 | -2.0% | -4.8% | 9 | -24,751 |
| trend_donchian_v1 | covid_crash_2020 | -0.9% | -8.1% | 23 | +973 |
| trend_donchian_v1 | usd_jpy_surge_2022 | +30.8% | -6.9% | 57 | +176,224 |
| trend_donchian_v1 | yen_carry_unwind_2024 | +5.4% | -7.3% | 9 | +57,058 |
| trend_ema_adx_v1 | EUR_debt_crisis_2011 | -13.3% | -17.7% | 147 | -135,614 |
| trend_ema_adx_v1 | abenomics_2012_2013 | +5.0% | -10.9% | 160 | +42,060 |
| trend_ema_adx_v1 | SNB_shock_2015 | +1.2% | -3.3% | 19 | -7,057 |
| trend_ema_adx_v1 | brexit_vote_2016 | +1.6% | -5.0% | 28 | +22,196 |
| trend_ema_adx_v1 | covid_crash_2020 | +0.3% | -6.9% | 60 | -17,305 |
| trend_ema_adx_v1 | usd_jpy_surge_2022 | +3.2% | -12.2% | 185 | +17,725 |
| trend_ema_adx_v1 | yen_carry_unwind_2024 | +1.5% | -4.1% | 16 | +6,583 |
| trend_tsmom_v1 | EUR_debt_crisis_2011 | +3.4% | -3.4% | 28 | +47,141 |
| trend_tsmom_v1 | abenomics_2012_2013 | +6.7% | -4.1% | 40 | +78,966 |
| trend_tsmom_v1 | SNB_shock_2015 | +2.4% | -0.7% | 3 | +6,096 |
| trend_tsmom_v1 | brexit_vote_2016 | +1.1% | -2.2% | 3 | -3,619 |
| trend_tsmom_v1 | covid_crash_2020 | -5.7% | -5.8% | 20 | -63,151 |
| trend_tsmom_v1 | usd_jpy_surge_2022 | +6.3% | -4.9% | 53 | +50,721 |
| trend_tsmom_v1 | yen_carry_unwind_2024 | +1.5% | -2.5% | 9 | +34,832 |


## ランダム売買（ベンチマーク・TRAIN+VALIDATION・10 シード）

| pair | sharpe_mean | sharpe_p95 | net_return_mean | trades | cost_ratio |
|---|---|---|---|---|---|
| AUDUSD | -0.58 | -0.07 | -22.4% | 700 | 4.76 |
| EURJPY | -0.47 | -0.02 | -18.1% | 680 | 1.93 |
| EURUSD | -0.30 | 0.01 | -12.1% | 695 | 10.71 |
| GBPUSD | -0.38 | 0.02 | -14.7% | 692 | 4.72 |
| USDJPY | -0.47 | -0.08 | -18.4% | 682 | 6.01 |


## Market Microstructure（直近 2 年・UTC 時間帯別の実測スプレッド）

| pair | spread_min_hour | spread_min | spread_max_hour | spread_max | best_spread_to_range | worst_spread_to_range |
|---|---|---|---|---|---|---|
| AUDUSD | 2.0 | 0.90 | 21.0 | 3.10 | 0.062 | 0.416 |
| EURJPY | 14.0 | 0.80 | 21.0 | 8.05 | 0.029 | 0.503 |
| EURUSD | 10.0 | 0.30 | 21.0 | 2.20 | 0.016 | 0.333 |
| GBPUSD | 10.0 | 0.60 | 21.0 | 6.60 | 0.030 | 0.606 |
| USDJPY | 15.0 | 0.40 | 21.0 | 4.90 | 0.016 | 0.400 |

スプレッド / 1 時間の値幅 が大きい時間帯（NY クローズ〜オセアニア早朝）はコスト負けしやすい。Risk Engine は実測スプレッドが直近中央値の 3 倍を超える足で新規を禁止する。

## Strategy Tournament

Champion: **CASH（取引しない）** — LOCK 後 PAPER Forward 合格の候補なし → Champion = CASH（取引しない）
LIVE 候補: **なし**（LIVE 開始には本人の明示承認が必須）

| spec_id | status | gate_b_fail | paper_gate_fail |
|---|---|---|---|
| ml_lgbm_v1 | RESEARCH_ONLY | gate_A_failed_all_pairs, test_profit_factor, test_sharpe, test_kill_switch, stress_2x_cost, forward_not_positive | paper_months<3, paper_trades, paper_not_positive |
| ml_logit_v1 | RESEARCH_ONLY | gate_A_failed_all_pairs, test_profit_factor, test_sharpe, stress_2x_cost, forward_not_positive | paper_months<3, paper_trades, paper_not_positive |
| mr_rsi_bb_v1 | RESEARCH_ONLY | gate_A_failed_all_pairs, test_profit_factor, test_sharpe, test_kill_switch, stress_2x_cost, forward_not_positive | paper_months<3, paper_trades, paper_not_positive |
| mr_zscore_v1 | RESEARCH_ONLY | gate_A_failed_all_pairs, test_profit_factor, test_sharpe, test_kill_switch, stress_2x_cost, forward_not_positive | paper_months<3, paper_trades, paper_not_positive |
| mtf_pullback_v1 | RESEARCH_ONLY | gate_A_failed_all_pairs, test_profit_factor, test_sharpe, test_kill_switch, stress_2x_cost, forward_not_positive | paper_months<3, paper_trades, paper_not_positive |
| regime_switch_v1 | RESEARCH_ONLY | gate_A_failed_all_pairs, test_profit_factor, test_sharpe, test_kill_switch, stress_2x_cost, forward_not_positive, test_forward_divergence | paper_months<3, paper_trades, paper_not_positive |
| trend_donchian_v1 | RESEARCH_ONLY | gate_A_failed_all_pairs, test_kill_switch, forward_not_positive, test_forward_divergence | paper_months<3, paper_trades, paper_not_positive |
| trend_ema_adx_v1 | RESEARCH_ONLY | gate_A_failed_all_pairs, test_profit_factor, test_sharpe, test_kill_switch, stress_2x_cost, forward_not_positive | paper_months<3, paper_trades, paper_not_positive |
| trend_tsmom_v1 | RESEARCH_ONLY | gate_A_failed_all_pairs, forward_not_positive, test_forward_divergence | paper_months<3, paper_trades, paper_not_positive |
| v2_d1_donchian | REJECTED | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe | paper_months<3, paper_trades, paper_not_positive |
| v2_d1_tsmom | REJECTED | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, single_regime_dependence, deflated_sharpe | paper_months<3, paper_trades, paper_not_positive |
| v2_h4_ema | REJECTED | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe | paper_months<3, paper_trades, paper_not_positive |
| v2_ml_d1_logit | REJECTED | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, ml_not_better_than_simple | paper_months<3, paper_trades, paper_not_positive |
| v2_session_breakout | REJECTED | profit_factor, sharpe, positive_years, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe | paper_months<3, paper_trades, paper_not_positive |
| v2_trend_carry | CHALLENGER |  | paper_months<3, paper_trades, paper_not_positive |
| v2_xpair_strength | REJECTED | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe | paper_months<3, paper_trades, paper_not_positive |
| v3_carry_only | REJECTED | trades, sharpe, subperiod_not_positive, single_regime_dependence, top5_trade_dependence, top1_trade_dependence | paper_months<3, paper_trades, paper_not_positive |
| v3_carry_trend_7p | REJECTED | top1_trade_dependence | paper_months<3, paper_trades, paper_not_positive |
| v3_carry_trend_mh | REJECTED | sharpe, top5_trade_dependence, top1_trade_dependence | paper_months<3, paper_trades, paper_not_positive |
| v3_carry_trend_xs | REJECTED | top5_trade_dependence, top1_trade_dependence | paper_months<3, paper_trades, paper_not_positive |
| v4_carry_trend_daily | REJECTED | single_regime_dependence, top1_trade_dependence | paper_months<3, paper_trades, paper_not_positive |
| v4_carry_trend_daily_fast | REJECTED | profit_factor, sharpe, positive_years, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence | paper_months<3, paper_trades, paper_not_positive |
| v4_carry_trend_h4 | REJECTED | profit_factor, sharpe, positive_years, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence | paper_months<3, paper_trades, paper_not_positive |
| v5_carry_trend_daily_10p | REJECTED | sharpe, positive_years, subperiod_not_positive, few_positive_pairs, single_regime_dependence, top5_trade_dependence, top1_trade_dependence | paper_months<3, paper_trades, paper_not_positive |
| v5_carry_trend_weekly_10p | REJECTED | sharpe, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, top5_trade_dependence, top1_trade_dependence | paper_months<3, paper_trades, paper_not_positive |

