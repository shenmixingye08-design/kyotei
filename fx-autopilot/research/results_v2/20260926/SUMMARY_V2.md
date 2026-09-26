# FX AUTOPILOT V2 研究結果（2026-09-26 07:26 UTC、データ〜2026-09-25 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v2.yaml`

> **検証汚染の申告**: 設計者は v1 の 2010〜2026 の結果（Stage1 WF 2014〜2021、TEST 2022〜2025-06、FORWARD 2025-07〜）を既に見ている。 V2 の候補選び（中期トレンド・キャリー・通貨強弱を優先したこと）はその知見の影響を受けている。 したがって V2 の Walk-Forward 成績は、どの年も「完全な未知データ」ではない（"汚染あり WF OOS" と表記する）。 V2 の最終判断は、LOCK 後に新しく到着する足での PAPER Forward のみで行う。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v2_trend_carry | CHALLENGER | 157 | +19.7% | +1.4% | 2.08 | 0.44 | 0.62 | -7.8% | 1,406 | 32 | 0.03 | 8 | 77% | 26% | +9.4% | +9.4% | 1.78 | 5 | 50% | 0.53 | 1 |  |
| v2_h4_ema | REJECTED | 896 | +4.7% | +0.4% | 1.03 | 0.10 | 0.16 | -13.4% | 52 | 82 | 0.41 | 16 | 46% | 44% | +7.7% | -2.8% | 0.92 | 2 | 72% | 0.14 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_d1_tsmom | REJECTED | 199 | -12.0% | -1.0% | 0.93 | -0.06 | -0.09 | -27.8% | -305 | 119 | 0.27 | 18 | 46% | 43% | -3.1% | -9.1% | 0.87 | 3 | 99% | 0.04 | 4 | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, single_regime_dependence, deflated_sharpe |
| v2_xpair_strength | REJECTED | 330 | -3.9% | -0.3% | 0.88 | -0.17 | -0.24 | -9.1% | -114 | 30 | — | 13 | 38% | 50% | +0.8% | -4.7% | 0.79 | 1 | 100% | 0.02 | 2 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_session_breakout | REJECTED | 2624 | -32.0% | -3.0% | 0.95 | -0.23 | -0.36 | -46.6% | -129 | 132 | 3.39 | 22 | 38% | 37% | -37.9% | +9.5% | 0.86 | 2 | 100% | 0.01 | 4 | profit_factor, sharpe, positive_years, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_d1_donchian | REJECTED | 164 | -10.0% | -0.8% | 0.74 | -0.26 | -0.37 | -16.8% | -640 | 42 | — | 12 | 31% | 41% | -2.5% | -7.7% | 0.65 | 0 | 100% | 0.01 | 3 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_ml_d1_logit | REJECTED | 155 | -6.0% | -0.5% | 0.60 | -0.65 | -0.79 | -6.5% | -384 | 30 | — | 6 | 23% | 45% | -4.6% | -1.4% | 0.54 | 0 | 100% | 0.00 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, ml_not_better_than_simple |
| trend_tsmom | REFERENCE_V1 | 973 | -18.7% | -1.6% | 0.93 | -0.19 | -0.28 | -28.0% | -189 | 63 | — | 20 | 54% | 34% | -16.1% | -3.0% | 0.87 | 2 | 100% | 0.01 | 3 | reference_v1 |
| ml_logit | REFERENCE_V1 | 3223 | -17.6% | -1.5% | 0.96 | -0.20 | -0.28 | -19.5% | -63 | 127 | 1.68 | 12 | 31% | 41% | -15.9% | -2.0% | 0.86 | 2 | 79% | 0.01 | 2 | reference_v1 |
| mr_zscore | REFERENCE_V1 | 3241 | -36.5% | -3.5% | 0.93 | -0.37 | -0.51 | -50.5% | -73 | 59 | 19.13 | 17 | 31% | 59% | -42.9% | +11.2% | 0.85 | 2 | 100% | 0.00 | 2 | reference_v1 |
| trend_ema_adx | REFERENCE_V1 | 3674 | -50.3% | -5.3% | 0.91 | -0.43 | -0.67 | -55.3% | -143 | 115 | 22.96 | 28 | 15% | 55% | -32.3% | -26.6% | 0.81 | 1 | 100% | 0.00 | 4 | reference_v1 |
| trend_donchian | REFERENCE_V1 | 2393 | -72.0% | -9.5% | 0.82 | -0.62 | -0.90 | -76.0% | -400 | 93 | — | 27 | 23% | 64% | -56.2% | -36.0% | 0.74 | 1 | 100% | 0.00 | 3 | reference_v1 |
| ml_lgbm | REFERENCE_V1 | 13972 | -65.2% | -8.0% | 0.95 | -0.64 | -0.87 | -68.4% | -48 | 100 | 1.62 | 13 | 15% | 95% | -50.5% | -29.7% | 0.85 | 1 | 100% | 0.00 | 2 | reference_v1 |
| mr_rsi_bb | REFERENCE_V1 | 2654 | -47.7% | -5.0% | 0.88 | -0.76 | -1.04 | -49.0% | -140 | 93 | — | 9 | 8% | 100% | -26.4% | -28.9% | 0.79 | 0 | 100% | 0.00 | 1 | reference_v1 |
| regime_switch | REFERENCE_V1 | 3756 | -68.1% | -8.6% | 0.88 | -0.87 | -1.25 | -71.6% | -137 | 75 | — | 15 | 23% | 63% | -55.4% | -28.6% | 0.80 | 0 | 100% | 0.00 | 2 | reference_v1 |
| mtf_pullback | REFERENCE_V1 | 765 | -40.5% | -4.0% | 0.74 | -1.08 | -1.39 | -42.4% | -532 | 140 | — | 15 | 23% | 44% | -38.0% | -4.0% | 0.66 | 0 | 99% | 0.00 | 2 | reference_v1 |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v2_d1_donchian | REJECTED | 164 | — | — | -237,498 | 0.41 | — | -6.7% |
| v2_d1_tsmom | REJECTED | 199 | — | — | -553,585 | 0.40 | — | -11.2% |
| v2_h4_ema | REJECTED | 896 | 77% | 319% | -101,959 | 0.94 | -125% | -1.8% |
| v2_trend_carry | CHALLENGER | 157 | 55% | 117% | -38,181 | 0.81 | 12% | +0.9% |
| v2_xpair_strength | REJECTED | 330 | — | — | -99,088 | 0.68 | — | -2.8% |
| v2_session_breakout | REJECTED | 2624 | — | — | -564,595 | 0.91 | — | +3.2% |
| v2_ml_d1_logit | REJECTED | 155 | — | — | -80,085 | 0.46 | — | -1.1% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v2_d1_donchian | v2_d1_tsmom | v2_h4_ema | v2_trend_carry | v2_xpair_strength | v2_session_breakout | v2_ml_d1_logit | trend_ema_adx | trend_donchian | trend_tsmom | mr_rsi_bb | mr_zscore | regime_switch | mtf_pullback | ml_logit | ml_lgbm |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2014.0 | +1.4% | +3.8% | -3.8% | +4.3% | +3.7% | -4.5% | -4.0% | -2.4% | -9.9% | +1.2% | -5.4% | +1.3% | -8.4% | -1.6% | -6.2% | -7.1% |
| 2015.0 | +1.9% | -4.9% | +10.5% | +2.3% | +1.1% | -6.4% | -0.4% | -11.1% | +11.7% | -2.9% | -2.5% | -8.0% | +4.6% | -4.5% | -8.1% | -12.6% |
| 2016.0 | +0.0% | +3.7% | +2.3% | +1.6% | -0.9% | -15.0% | +0.3% | -4.3% | -5.2% | +1.0% | -10.2% | -15.8% | +1.3% | -2.4% | -2.5% | +21.0% |
| 2017.0 | -0.6% | +0.2% | -0.8% | -1.1% | -1.5% | -13.5% | +0.0% | -11.2% | -0.5% | +6.6% | +1.3% | -5.7% | -19.6% | -6.1% | -0.2% | -10.4% |
| 2018.0 | -0.6% | -1.9% | +3.3% | -0.9% | +0.1% | -6.4% | -1.0% | +2.5% | -14.6% | -4.6% | -6.3% | -6.2% | -13.2% | -0.7% | +2.0% | -10.5% |
| 2019.0 | -2.8% | -1.7% | +2.4% | +0.2% | -1.3% | +1.8% | +0.0% | -0.9% | -23.4% | -14.5% | -0.7% | -0.8% | -10.8% | -3.6% | -1.7% | -23.4% |
| 2020.0 | -0.9% | -2.5% | -4.3% | +1.9% | +1.3% | +8.9% | +0.1% | -2.0% | -18.5% | -5.1% | -3.6% | -14.2% | -19.4% | -6.9% | -1.0% | -7.1% |
| 2021.0 | -0.9% | +0.4% | -1.2% | +0.8% | -1.7% | -9.0% | +0.4% | -7.8% | -13.4% | +2.3% | -2.2% | -3.4% | -8.4% | -19.2% | +1.0% | -11.8% |
| 2022.0 | +1.2% | +6.6% | +3.8% | +5.8% | -0.9% | +4.8% | +0.0% | +2.1% | +1.2% | +4.6% | -9.3% | -8.2% | +1.4% | +1.5% | +5.2% | +1.2% |
| 2023.0 | -2.3% | -4.0% | -4.6% | +2.5% | -1.0% | +1.2% | -0.3% | -7.7% | -20.9% | +3.4% | -7.3% | +20.1% | -2.1% | -7.5% | +4.5% | -7.7% |
| 2024.0 | -4.2% | -7.6% | +1.9% | +2.8% | -0.5% | -2.2% | -0.5% | -15.2% | +5.2% | +0.4% | -0.6% | +5.7% | -5.4% | +2.1% | -7.0% | -6.1% |
| 2025.0 | -1.7% | +0.7% | -3.5% | -2.0% | +1.2% | +7.5% | -0.7% | -1.9% | -20.9% | -5.6% | -10.6% | +7.0% | -20.6% | -2.5% | -2.1% | -16.5% |
| 2026.0 | -1.0% | -4.5% | -0.1% | +0.2% | -3.4% | -1.8% | +0.0% | -6.3% | -3.9% | -5.3% | -4.9% | -10.8% | -4.2% | +2.8% | -2.0% | -4.0% |

## 年別 Profit Factor（WF OOS）

| year | v2_d1_donchian | v2_d1_tsmom | v2_h4_ema | v2_trend_carry | v2_xpair_strength | v2_session_breakout | v2_ml_d1_logit | trend_ema_adx | trend_donchian | trend_tsmom | mr_rsi_bb | mr_zscore | regime_switch | mtf_pullback | ml_logit | ml_lgbm |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2014.0 | 2.07 | 3.66 | 0.82 | 5.63 | 6.31 | 0.98 | 0.58 | 1.09 | 0.97 | 1.29 | 0.86 | 1.02 | 0.86 | 0.85 | 0.97 | 0.97 |
| 2015.0 | 0.18 | 0.33 | 2.03 | 1.02 | 1.36 | 0.91 | 1.05 | 0.68 | 1.16 | 0.72 | 0.95 | 0.87 | 1.05 | 0.66 | 0.83 | 0.94 |
| 2016.0 | 0.50 | 0.12 | 1.21 | 0.76 | 0.56 | 0.66 | — | 0.93 | 0.82 | 1.11 | 0.77 | 0.77 | 1.02 | 0.81 | 0.95 | 1.12 |
| 2017.0 | 1.57 | 2.44 | 0.95 | 1.29 | 0.58 | 0.77 | — | 0.84 | 1.03 | 1.62 | 1.02 | 0.90 | 0.75 | 0.54 | 0.97 | 0.92 |
| 2018.0 | 0.60 | 0.48 | 1.31 | 0.75 | 0.99 | 0.95 | 0.25 | 1.07 | 0.56 | 0.79 | 0.84 | 0.90 | 0.84 | 0.93 | 1.13 | 0.91 |
| 2019.0 | 0.10 | 0.14 | 1.11 | 1.11 | 0.26 | 0.96 | — | 0.93 | 0.27 | 0.20 | 0.98 | 0.99 | 0.78 | 0.69 | 0.79 | 0.78 |
| 2020.0 | 1.05 | 0.44 | 0.72 | 2.81 | 2.33 | 1.20 | — | 0.96 | 0.73 | 0.78 | 0.90 | 0.76 | 0.69 | 0.53 | 0.97 | 0.95 |
| 2021.0 | 0.83 | 11.88 | 0.82 | 163.68 | 0.31 | 0.79 | 1.43 | 0.87 | 0.82 | 1.15 | 0.94 | 0.97 | 0.85 | 0.54 | 2.32 | 0.90 |
| 2022.0 | 1.66 | 0.00 | 1.47 | 3.28 | 0.29 | 1.10 | — | 1.03 | 1.00 | 1.13 | 0.80 | 0.88 | 1.02 | 1.15 | 1.29 | 1.00 |
| 2023.0 | 0.20 | 0.09 | 0.61 | 1.48 | 0.46 | 1.01 | 0.22 | 0.87 | 0.75 | 1.15 | 0.83 | 1.37 | 0.96 | 0.61 | 1.21 | 0.95 |
| 2024.0 | 0.27 | 0.13 | 1.19 | 0.22 | 0.97 | 0.96 | 0.00 | 0.74 | 1.15 | 1.08 | 0.99 | 1.08 | 0.90 | 1.19 | 0.80 | 0.96 |
| 2025.0 | 0.72 | 3.38 | 0.74 | 0.50 | 2.03 | 1.25 | 0.24 | 0.95 | 0.46 | 0.70 | 0.71 | 1.16 | 0.64 | 0.80 | 0.88 | 0.88 |
| 2026.0 | 0.00 | 0.08 | 0.99 | 0.67 | 0.14 | 0.89 | — | 0.78 | 0.84 | 0.72 | 0.78 | 0.70 | 0.89 | 1.55 | 0.83 | 0.96 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v2_d1_donchian | AUDUSD | 37 | -36,518 | 0.64 | 30% | 62 | -10,084 |
| v2_d1_donchian | EURJPY | 26 | -4,906 | 0.90 | 38% | 42 | -2,062 |
| v2_d1_donchian | EURUSD | 33 | -14,740 | 0.82 | 27% | 28 | -10,868 |
| v2_d1_donchian | GBPUSD | 35 | -27,108 | 0.66 | 29% | 43 | -9,411 |
| v2_d1_donchian | USDJPY | 33 | -21,719 | 0.75 | 33% | 34 | -110 |
| v2_d1_tsmom | AUDUSD | 55 | +21,208 | 1.14 | 35% | 156 | -28,753 |
| v2_d1_tsmom | EURJPY | 35 | -115,402 | 0.37 | 20% | 141 | -7,410 |
| v2_d1_tsmom | EURUSD | 33 | +129,752 | 1.64 | 30% | 61 | -42,774 |
| v2_d1_tsmom | GBPUSD | 35 | +9,553 | 1.04 | 43% | 179 | -41,316 |
| v2_d1_tsmom | USDJPY | 41 | -105,835 | 0.36 | 24% | 45 | -5,677 |
| v2_h4_ema | AUDUSD | 156 | -1,358 | 1.00 | 35% | 122 | -8,241 |
| v2_h4_ema | EURJPY | 185 | -22,309 | 0.94 | 36% | 71 | -13,282 |
| v2_h4_ema | EURUSD | 186 | +9,330 | 1.03 | 32% | 69 | -13,868 |
| v2_h4_ema | GBPUSD | 179 | -489 | 1.00 | 33% | 92 | -10,835 |
| v2_h4_ema | USDJPY | 190 | +61,451 | 1.18 | 36% | 63 | -12,049 |
| v2_trend_carry | AUDUSD | 42 | +4,319 | 1.12 | 36% | 48 | -3,299 |
| v2_trend_carry | EURJPY | 25 | +12,170 | 1.31 | 36% | 27 | +2,606 |
| v2_trend_carry | EURUSD | 34 | +59,758 | 2.16 | 35% | 22 | +840 |
| v2_trend_carry | GBPUSD | 33 | +4,801 | 1.11 | 45% | 36 | -6,337 |
| v2_trend_carry | USDJPY | 23 | +139,770 | 5.06 | 39% | 21 | +33,379 |
| v2_xpair_strength | AUDUSD | 94 | -22,166 | 0.70 | 41% | 40 | -4,627 |
| v2_xpair_strength | EURJPY | 53 | -8,873 | 0.84 | 42% | 32 | -813 |
| v2_xpair_strength | EURUSD | 71 | -10,584 | 0.85 | 42% | 20 | -7,162 |
| v2_xpair_strength | GBPUSD | 60 | -5,199 | 0.91 | 45% | 34 | -6,094 |
| v2_xpair_strength | USDJPY | 52 | +9,318 | 1.18 | 44% | 22 | +2,163 |
| v2_session_breakout | AUDUSD | 516 | -280,635 | 0.78 | 32% | 184 | -23,190 |
| v2_session_breakout | EURJPY | 566 | -218,671 | 0.86 | 33% | 136 | -11,265 |
| v2_session_breakout | EURUSD | 535 | +101,863 | 1.08 | 35% | 95 | -30,573 |
| v2_session_breakout | GBPUSD | 503 | -126,135 | 0.91 | 32% | 140 | -29,536 |
| v2_session_breakout | USDJPY | 504 | +184,319 | 1.15 | 37% | 106 | -328 |
| v2_ml_d1_logit | AUDUSD | 15 | -2,070 | 0.85 | 60% | 40 | -701 |
| v2_ml_d1_logit | EURJPY | 27 | -8,416 | 0.70 | 44% | 33 | -777 |
| v2_ml_d1_logit | EURUSD | 33 | -21,065 | 0.41 | 33% | 22 | -2,001 |
| v2_ml_d1_logit | GBPUSD | 41 | -18,845 | 0.52 | 41% | 34 | -1,185 |
| v2_ml_d1_logit | USDJPY | 39 | -9,114 | 0.70 | 51% | 25 | -486 |
| trend_ema_adx | AUDUSD | 824 | -232,485 | 0.83 | 31% | 168 | -23,832 |
| trend_ema_adx | EURJPY | 799 | -142,109 | 0.89 | 30% | 113 | -28,988 |
| trend_ema_adx | EURUSD | 717 | -32,491 | 0.97 | 33% | 78 | -23,575 |
| trend_ema_adx | GBPUSD | 649 | -170,451 | 0.83 | 31% | 116 | -23,138 |
| trend_ema_adx | USDJPY | 685 | +50,616 | 1.05 | 32% | 93 | -22,231 |
| trend_donchian | AUDUSD | 534 | -516,891 | 0.57 | 23% | 133 | -29,930 |
| trend_donchian | EURJPY | 517 | -34,465 | 0.97 | 25% | 89 | -40,305 |
| trend_donchian | EURUSD | 441 | -221,336 | 0.75 | 23% | 62 | -31,442 |
| trend_donchian | GBPUSD | 438 | -245,051 | 0.75 | 24% | 96 | -39,003 |
| trend_donchian | USDJPY | 463 | +60,701 | 1.06 | 27% | 77 | -19,462 |
| trend_tsmom | AUDUSD | 183 | +6,526 | 1.01 | 39% | 95 | -15,539 |
| trend_tsmom | EURJPY | 187 | -111,082 | 0.77 | 33% | 57 | -8,774 |
| trend_tsmom | EURUSD | 205 | -52,879 | 0.91 | 36% | 53 | -25,384 |
| trend_tsmom | GBPUSD | 190 | +12,135 | 1.03 | 33% | 67 | -21,807 |
| trend_tsmom | USDJPY | 208 | -38,952 | 0.93 | 31% | 49 | -4,832 |
| mr_rsi_bb | AUDUSD | 445 | -5,373 | 0.99 | 51% | 138 | -3,909 |
| mr_rsi_bb | EURJPY | 496 | -79,768 | 0.87 | 48% | 89 | -7,446 |
| mr_rsi_bb | EURUSD | 553 | -31,772 | 0.95 | 49% | 68 | -7,932 |
| mr_rsi_bb | GBPUSD | 560 | -42,137 | 0.93 | 49% | 104 | -7,427 |
| mr_rsi_bb | USDJPY | 600 | -211,807 | 0.72 | 43% | 76 | -11,861 |
| mr_zscore | AUDUSD | 663 | -88,649 | 0.88 | 42% | 88 | -8,724 |
| mr_zscore | EURJPY | 656 | +26,073 | 1.04 | 46% | 53 | -11,102 |
| mr_zscore | EURUSD | 632 | +4,567 | 1.01 | 44% | 44 | -12,055 |
| mr_zscore | GBPUSD | 601 | -77,989 | 0.88 | 41% | 63 | -9,803 |
| mr_zscore | USDJPY | 689 | -101,175 | 0.88 | 41% | 46 | -15,208 |
| regime_switch | AUDUSD | 782 | -75,672 | 0.91 | 36% | 115 | -12,168 |
| regime_switch | EURJPY | 724 | -161,077 | 0.81 | 35% | 66 | -12,739 |
| regime_switch | EURUSD | 723 | -11,531 | 0.98 | 35% | 52 | -11,566 |
| regime_switch | GBPUSD | 706 | -65,140 | 0.92 | 36% | 78 | -12,208 |
| regime_switch | USDJPY | 821 | -201,245 | 0.79 | 32% | 61 | -13,269 |
| mtf_pullback | AUDUSD | 156 | -80,671 | 0.76 | 43% | 214 | -2,897 |
| mtf_pullback | EURJPY | 141 | -63,280 | 0.78 | 43% | 131 | -2,000 |
| mtf_pullback | EURUSD | 149 | -94,138 | 0.67 | 39% | 100 | -3,002 |
| mtf_pullback | GBPUSD | 165 | -152,530 | 0.60 | 36% | 154 | -2,957 |
| mtf_pullback | USDJPY | 154 | -16,176 | 0.94 | 46% | 96 | -604 |
| ml_logit | AUDUSD | 576 | +44,983 | 1.05 | 51% | 193 | -13,772 |
| ml_logit | EURJPY | 751 | +101,659 | 1.09 | 54% | 123 | -2,435 |
| ml_logit | EURUSD | 671 | -139,041 | 0.85 | 46% | 93 | -10,186 |
| ml_logit | GBPUSD | 365 | -140,493 | 0.75 | 45% | 133 | -4,134 |
| ml_logit | USDJPY | 860 | -71,734 | 0.95 | 50% | 111 | -7,587 |
| ml_lgbm | AUDUSD | 2800 | -363,259 | 0.88 | 48% | 158 | -27,883 |
| ml_lgbm | EURJPY | 2656 | -8,979 | 1.00 | 50% | 97 | -20,538 |
| ml_lgbm | EURUSD | 2857 | -191,314 | 0.93 | 49% | 66 | -37,500 |
| ml_lgbm | GBPUSD | 2475 | -225,873 | 0.91 | 49% | 109 | -21,785 |
| ml_lgbm | USDJPY | 3184 | +123,078 | 1.04 | 51% | 76 | -19,959 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v2_d1_donchian | regime4h | NEUTRAL | 39 | -42,862 | 33% | 0.48 |
| v2_d1_donchian | regime4h | RANGE | 28 | -24,701 | 29% | 0.68 |
| v2_d1_donchian | regime4h | TREND | 179 | -42,396 | 32% | 0.90 |
| v2_d1_donchian | month_dir | DOWN | 48 | +41,824 | 42% | 1.47 |
| v2_d1_donchian | month_dir | FLAT | 133 | -144,638 | 25% | 0.61 |
| v2_d1_donchian | month_dir | UP | 65 | -7,145 | 38% | 0.95 |
| v2_d1_donchian | month_vol | HIGH_VOL | 50 | -11,458 | 32% | 0.90 |
| v2_d1_donchian | month_vol | LOW_VOL | 196 | -98,502 | 32% | 0.79 |
| v2_d1_tsmom | regime4h | HIGH_VOL | 16 | -45,989 | 25% | 0.49 |
| v2_d1_tsmom | regime4h | NEUTRAL | 76 | -229,536 | 28% | 0.38 |
| v2_d1_tsmom | regime4h | RANGE | 85 | +3,496 | 34% | 1.01 |
| v2_d1_tsmom | regime4h | TREND | 186 | +240,057 | 34% | 1.26 |
| v2_d1_tsmom | month_dir | DOWN | 67 | -8,626 | 24% | 0.98 |
| v2_d1_tsmom | month_dir | FLAT | 214 | -145,399 | 33% | 0.86 |
| v2_d1_tsmom | month_dir | UP | 82 | +122,055 | 38% | 1.35 |
| v2_d1_tsmom | month_vol | HIGH_VOL | 104 | -252,954 | 28% | 0.46 |
| v2_d1_tsmom | month_vol | LOW_VOL | 259 | +220,984 | 34% | 1.17 |
| v2_h4_ema | regime4h | HIGH_VOL | 76 | +71,678 | 42% | 1.63 |
| v2_h4_ema | regime4h | NEUTRAL | 351 | -53,333 | 33% | 0.92 |
| v2_h4_ema | regime4h | TREND | 469 | +28,279 | 34% | 1.03 |
| v2_h4_ema | month_dir | DOWN | 156 | +304,443 | 42% | 2.26 |
| v2_h4_ema | month_dir | FLAT | 614 | -417,099 | 31% | 0.64 |
| v2_h4_ema | month_dir | UP | 126 | +159,280 | 41% | 1.71 |
| v2_h4_ema | month_vol | HIGH_VOL | 283 | +167,735 | 40% | 1.37 |
| v2_h4_ema | month_vol | LOW_VOL | 613 | -121,111 | 32% | 0.90 |
| v2_trend_carry | regime4h | HIGH_VOL | 10 | +17,524 | 50% | 2.83 |
| v2_trend_carry | regime4h | NEUTRAL | 36 | +19,842 | 36% | 1.48 |
| v2_trend_carry | regime4h | RANGE | 33 | +111,420 | 45% | 3.67 |
| v2_trend_carry | regime4h | TREND | 78 | +72,031 | 35% | 1.64 |
| v2_trend_carry | month_dir | DOWN | 31 | +19,757 | 45% | 1.46 |
| v2_trend_carry | month_dir | FLAT | 95 | +187,762 | 35% | 2.48 |
| v2_trend_carry | month_dir | UP | 31 | +13,299 | 42% | 1.37 |
| v2_trend_carry | month_vol | HIGH_VOL | 35 | +6,010 | 40% | 1.15 |
| v2_trend_carry | month_vol | LOW_VOL | 122 | +214,807 | 38% | 2.31 |
| v2_xpair_strength | regime4h | HIGH_VOL | 33 | -4,677 | 48% | 0.89 |
| v2_xpair_strength | regime4h | NEUTRAL | 88 | -35,758 | 39% | 0.60 |
| v2_xpair_strength | regime4h | RANGE | 134 | +10,741 | 47% | 1.10 |
| v2_xpair_strength | regime4h | TREND | 219 | -46,791 | 42% | 0.80 |
| v2_xpair_strength | month_dir | DOWN | 92 | +23,881 | 50% | 1.29 |
| v2_xpair_strength | month_dir | FLAT | 269 | -124,931 | 37% | 0.57 |
| v2_xpair_strength | month_dir | UP | 113 | +24,566 | 51% | 1.23 |
| v2_xpair_strength | month_vol | HIGH_VOL | 123 | -37,958 | 40% | 0.74 |
| v2_xpair_strength | month_vol | LOW_VOL | 351 | -38,526 | 44% | 0.88 |
| v2_session_breakout | regime4h | HIGH_VOL | 260 | +30,949 | 35% | 1.04 |
| v2_session_breakout | regime4h | NEUTRAL | 787 | -112,870 | 33% | 0.95 |
| v2_session_breakout | regime4h | RANGE | 1353 | -27,345 | 34% | 0.99 |
| v2_session_breakout | regime4h | TREND | 1460 | -315,674 | 33% | 0.92 |
| v2_session_breakout | month_dir | DOWN | 761 | +408,912 | 40% | 1.23 |
| v2_session_breakout | month_dir | FLAT | 2254 | -1,252,042 | 30% | 0.79 |
| v2_session_breakout | month_dir | UP | 845 | +418,190 | 37% | 1.20 |
| v2_session_breakout | month_vol | HIGH_VOL | 1460 | -2,171 | 35% | 1.00 |
| v2_session_breakout | month_vol | LOW_VOL | 2400 | -422,769 | 33% | 0.93 |
| v2_ml_d1_logit | regime4h | HIGH_VOL | 15 | -9,447 | 40% | 0.45 |
| v2_ml_d1_logit | regime4h | NEUTRAL | 45 | -28,587 | 40% | 0.46 |
| v2_ml_d1_logit | regime4h | RANGE | 34 | +4,552 | 59% | 1.21 |
| v2_ml_d1_logit | regime4h | TREND | 61 | -26,028 | 41% | 0.53 |
| v2_ml_d1_logit | month_dir | DOWN | 40 | -40,389 | 30% | 0.26 |
| v2_ml_d1_logit | month_dir | FLAT | 99 | -27,636 | 45% | 0.67 |
| v2_ml_d1_logit | month_dir | UP | 16 | +8,516 | 75% | 2.05 |
| v2_ml_d1_logit | month_vol | HIGH_VOL | 22 | -11,198 | 41% | 0.55 |
| v2_ml_d1_logit | month_vol | LOW_VOL | 133 | -48,311 | 45% | 0.61 |
| trend_ema_adx | regime4h | HIGH_VOL | 274 | -88,138 | 30% | 0.81 |
| trend_ema_adx | regime4h | NEUTRAL | 981 | -135,619 | 33% | 0.91 |
| trend_ema_adx | regime4h | RANGE | 2171 | -89,210 | 31% | 0.97 |
| trend_ema_adx | regime4h | TREND | 776 | -231,132 | 30% | 0.82 |
| trend_ema_adx | month_dir | DOWN | 812 | +243,634 | 32% | 1.19 |
| trend_ema_adx | month_dir | FLAT | 2640 | -815,183 | 30% | 0.81 |
| trend_ema_adx | month_dir | UP | 750 | +27,451 | 34% | 1.02 |
| trend_ema_adx | month_vol | HIGH_VOL | 1449 | -421,973 | 31% | 0.83 |
| trend_ema_adx | month_vol | LOW_VOL | 2753 | -122,126 | 31% | 0.97 |
| trend_donchian | regime4h | HIGH_VOL | 200 | -52,157 | 22% | 0.90 |
| trend_donchian | regime4h | NEUTRAL | 714 | -733,352 | 20% | 0.60 |
| trend_donchian | regime4h | RANGE | 1123 | -141,771 | 25% | 0.94 |
| trend_donchian | regime4h | TREND | 806 | -61,536 | 26% | 0.97 |
| trend_donchian | month_dir | DOWN | 542 | +206,782 | 30% | 1.18 |
| trend_donchian | month_dir | FLAT | 1773 | -1,791,771 | 20% | 0.59 |
| trend_donchian | month_dir | UP | 528 | +596,173 | 31% | 1.55 |
| trend_donchian | month_vol | HIGH_VOL | 899 | -273,621 | 25% | 0.87 |
| trend_donchian | month_vol | LOW_VOL | 1944 | -715,195 | 24% | 0.84 |
| trend_tsmom | regime4h | HIGH_VOL | 86 | -11,139 | 36% | 0.94 |
| trend_tsmom | regime4h | NEUTRAL | 170 | -59,617 | 34% | 0.87 |
| trend_tsmom | regime4h | RANGE | 215 | +159,215 | 39% | 1.31 |
| trend_tsmom | regime4h | TREND | 580 | -145,773 | 33% | 0.91 |
| trend_tsmom | month_dir | DOWN | 242 | +296,834 | 47% | 1.59 |
| trend_tsmom | month_dir | FLAT | 575 | -893,806 | 23% | 0.49 |
| trend_tsmom | month_dir | UP | 234 | +539,659 | 50% | 2.16 |
| trend_tsmom | month_vol | HIGH_VOL | 382 | +88,133 | 36% | 1.09 |
| trend_tsmom | month_vol | LOW_VOL | 669 | -145,446 | 34% | 0.92 |
| mr_rsi_bb | regime4h | HIGH_VOL | 132 | -1,357 | 53% | 0.99 |
| mr_rsi_bb | regime4h | NEUTRAL | 535 | -27,413 | 49% | 0.95 |
| mr_rsi_bb | regime4h | RANGE | 1149 | -222,073 | 47% | 0.83 |
| mr_rsi_bb | regime4h | TREND | 838 | -120,014 | 48% | 0.88 |
| mr_rsi_bb | month_dir | DOWN | 550 | -120,959 | 47% | 0.82 |
| mr_rsi_bb | month_dir | FLAT | 1534 | -106,969 | 49% | 0.94 |
| mr_rsi_bb | month_dir | UP | 570 | -142,929 | 45% | 0.79 |
| mr_rsi_bb | month_vol | HIGH_VOL | 923 | -221,152 | 45% | 0.81 |
| mr_rsi_bb | month_vol | LOW_VOL | 1731 | -149,705 | 49% | 0.92 |
| mr_zscore | regime4h | HIGH_VOL | 335 | -55,352 | 42% | 0.85 |
| mr_zscore | regime4h | NEUTRAL | 619 | +21,250 | 46% | 1.03 |
| mr_zscore | regime4h | RANGE | 756 | -141,807 | 42% | 0.83 |
| mr_zscore | regime4h | TREND | 1531 | -61,265 | 42% | 0.96 |
| mr_zscore | month_dir | DOWN | 789 | -266,369 | 37% | 0.73 |
| mr_zscore | month_dir | FLAT | 1794 | +251,778 | 47% | 1.14 |
| mr_zscore | month_dir | UP | 658 | -222,583 | 37% | 0.71 |
| mr_zscore | month_vol | HIGH_VOL | 1202 | -138,232 | 41% | 0.90 |
| mr_zscore | month_vol | LOW_VOL | 2039 | -98,942 | 44% | 0.96 |
| regime_switch | regime4h | HIGH_VOL | 28 | -8,624 | 39% | 0.48 |
| regime_switch | regime4h | NEUTRAL | 126 | -51,343 | 33% | 0.65 |
| regime_switch | regime4h | RANGE | 2847 | -411,282 | 36% | 0.87 |
| regime_switch | regime4h | TREND | 1171 | -124,031 | 32% | 0.91 |
| regime_switch | month_dir | DOWN | 828 | +10,046 | 37% | 1.01 |
| regime_switch | month_dir | FLAT | 2499 | -505,025 | 34% | 0.82 |
| regime_switch | month_dir | UP | 845 | -100,302 | 34% | 0.89 |
| regime_switch | month_vol | HIGH_VOL | 1301 | +64,123 | 37% | 1.04 |
| regime_switch | month_vol | LOW_VOL | 2871 | -659,403 | 33% | 0.80 |
| mtf_pullback | regime4h | HIGH_VOL | 4 | +181 | 50% | 1.02 |
| mtf_pullback | regime4h | NEUTRAL | 143 | +21,945 | 50% | 1.09 |
| mtf_pullback | regime4h | RANGE | 213 | -171,411 | 38% | 0.63 |
| mtf_pullback | regime4h | TREND | 405 | -257,511 | 40% | 0.70 |
| mtf_pullback | month_dir | DOWN | 123 | -72,272 | 41% | 0.71 |
| mtf_pullback | month_dir | FLAT | 478 | -357,848 | 38% | 0.65 |
| mtf_pullback | month_dir | UP | 164 | +23,324 | 52% | 1.08 |
| mtf_pullback | month_vol | HIGH_VOL | 214 | -145,044 | 43% | 0.70 |
| mtf_pullback | month_vol | LOW_VOL | 551 | -261,752 | 41% | 0.76 |
| ml_logit | regime4h | HIGH_VOL | 1236 | +108,129 | 52% | 1.06 |
| ml_logit | regime4h | NEUTRAL | 948 | -80,156 | 49% | 0.94 |
| ml_logit | regime4h | RANGE | 1088 | +27,933 | 52% | 1.02 |
| ml_logit | regime4h | TREND | 2695 | -383,162 | 48% | 0.91 |
| ml_logit | month_dir | DOWN | 1569 | -260,902 | 48% | 0.90 |
| ml_logit | month_dir | FLAT | 3118 | -102,138 | 50% | 0.98 |
| ml_logit | month_dir | UP | 1280 | +35,782 | 51% | 1.02 |
| ml_logit | month_vol | HIGH_VOL | 2389 | +78,771 | 52% | 1.02 |
| ml_logit | month_vol | LOW_VOL | 3578 | -406,028 | 49% | 0.93 |
| ml_lgbm | regime4h | HIGH_VOL | 1960 | +52,005 | 52% | 1.03 |
| ml_lgbm | regime4h | NEUTRAL | 2906 | -413,731 | 48% | 0.87 |
| ml_lgbm | regime4h | RANGE | 4505 | -146,460 | 49% | 0.97 |
| ml_lgbm | regime4h | TREND | 6883 | -198,926 | 51% | 0.97 |
| ml_lgbm | month_dir | DOWN | 3747 | -185,312 | 49% | 0.96 |
| ml_lgbm | month_dir | FLAT | 9109 | -366,071 | 50% | 0.96 |
| ml_lgbm | month_dir | UP | 3398 | -155,729 | 50% | 0.96 |
| ml_lgbm | month_vol | HIGH_VOL | 6408 | +133,129 | 51% | 1.02 |
| ml_lgbm | month_vol | LOW_VOL | 9846 | -840,241 | 49% | 0.92 |

## 比較: session（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | session | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v2_session_breakout | all | 5261 | -3.1% | 1.00 | 0.05 | -0.15 | 0.27 | -42.6% |
| v2_session_breakout | london | 4151 | +23.6% | 1.02 | 0.17 | 0.02 | 0.48 | -40.9% |
| v2_session_breakout | london_ny | 2976 | -11.3% | 0.98 | -0.02 | -0.14 | 0.01 | -37.0% |
| v2_session_breakout | ny | 3720 | -0.5% | 1.00 | 0.05 | -0.08 | 0.08 | -37.2% |
| v2_session_breakout | tokyo | 3081 | -15.6% | 0.98 | -0.05 | -0.37 | 0.45 | -37.5% |
| v2_session_breakout | tokyo_london | 2256 | +23.8% | 1.04 | 0.19 | 0.15 | 0.45 | -26.9% |

## 比較: sizing（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | sizing | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v2_d1_donchian | fixed_notional | 248 | -43.4% | 0.80 | -0.17 | -0.21 | -0.33 | -55.2% |
| v2_d1_donchian | risk_stop | 256 | -0.5% | 1.02 | -0.01 | 0.03 | -0.40 | -16.5% |
| v2_d1_donchian | vol_target | 259 | -18.9% | 0.90 | -0.09 | -0.17 | -0.35 | -40.3% |
| v2_d1_tsmom | fixed_notional | 275 | -31.1% | 0.87 | -0.05 | -0.08 | -0.29 | -56.1% |
| v2_d1_tsmom | risk_stop | 271 | +5.9% | 1.17 | 0.12 | 0.14 | -0.01 | -12.7% |
| v2_d1_tsmom | vol_target | 277 | +9.8% | 1.07 | 0.10 | 0.08 | -0.14 | -41.8% |
| v2_trend_carry | risk_stop | 125 | +4.6% | 1.02 | 0.01 | 0.00 | -0.01 | -7.4% |
| v2_trend_carry | vol_target | 139 | +9.8% | 0.93 | 0.02 | 0.02 | 0.06 | -26.8% |
| v2_xpair_strength | fixed_notional | 432 | -30.0% | 0.87 | -0.10 | -0.13 | -0.30 | -52.4% |
| v2_xpair_strength | risk_stop | 368 | +0.1% | 1.00 | 0.01 | 0.03 | -0.46 | -8.4% |
| v2_xpair_strength | vol_target | 448 | -11.1% | 0.94 | -0.05 | -0.04 | -0.42 | -34.7% |

## 比較: regime（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | regime | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v2_d1_donchian | no_high_vol | 242 | -17.3% | 0.93 | -0.06 | -0.08 | -0.44 | -36.2% |
| v2_d1_donchian | none | 268 | -24.7% | 0.88 | -0.12 | -0.14 | -0.42 | -39.5% |
| v2_d1_donchian | trend_only | 253 | -20.8% | 0.90 | -0.09 | -0.12 | -0.21 | -36.3% |
| v2_h4_ema | no_high_vol | 961 | -5.8% | 0.94 | -0.10 | -0.12 | -0.25 | -17.4% |
| v2_h4_ema | none | 1088 | -0.2% | 0.97 | -0.03 | 0.02 | -0.28 | -16.9% |
| v2_h4_ema | trend_only | 896 | +0.6% | 0.98 | -0.01 | 0.04 | -0.35 | -16.0% |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v2_d1_donchian | REJECTED | {"n": 100, "regime": "no_high_vol", "sizing": "risk_stop"} | risk_stop | 2026-09-25T13:17 | ac202f04df06 |
| v2_d1_tsmom | REJECTED | {"lookback": 252, "sizing": "vol_target"} | vol_target | 2026-09-25T13:17 | d0edd4216f33 |
| v2_h4_ema | REJECTED | {"adx_min": 20, "fast_slow": "20_100", "regime": "trend_only"} | risk_stop | 2026-09-25T13:17 | 5c35b7e9b450 |
| v2_trend_carry | CHALLENGER | {"mode": "composite", "sizing": "risk_stop"} | risk_stop | 2026-09-25T13:17 | e239210bb725 |
| v2_xpair_strength | REJECTED | {"lookback": 60, "sizing": "risk_stop", "top_k": 3} | risk_stop | 2026-09-25T13:17 | c6eeaa6cc6e6 |
| v2_session_breakout | REJECTED | {"session": "tokyo_london"} | risk_stop | 2026-09-25T13:17 | 427b10450f14 |
| v2_ml_d1_logit | REJECTED | {"th": 0.55} | risk_stop | 2026-09-25T13:17 | d3bf47a9d351 |

CHALLENGER でも自動で Champion にはならない。Champion 昇格は LOCK 後 PAPER Forward（3 か月・20 取引・プラス・乖離）合格が必須。

## データ品質: 政策金利近似表（旧）と FRED 市場金利（3 か月物）の差（2010〜、%ポイント）

```
ccy  months market_last  mean_diff_pp  mean_abs_diff_pp  max_abs_diff_pp
USD     199     2026-08        -0.117             0.143            1.225
EUR     193     2026-01        -0.190             0.223            1.176
JPY     199     2026-07        -0.168             0.169            0.958
GBP     193     2026-01        -0.116             0.154            1.140
AUD     200     2026-08        -0.167             0.197            0.910
NZD     200     2026-08        -0.173             0.181            0.680
CAD     200     2026-08         0.052             0.084            0.422
CHF     200     2026-08         0.034             0.066            0.353
```

## データ品質: Dukascopy と米連銀 H.10 正午レートの突き合わせ（日次）

  pair  days  median_abs_diff_pct  p99_abs_diff_pct  max_abs_diff_pct  days_gt_0_5pct  days_gt_1pct  worst_day
USDJPY  4181               0.0219            0.2995             1.156               9             1 2013-06-06
EURUSD  4181               0.0253            0.3181             0.884               9             0 2011-10-07
GBPUSD  4181               0.0257            0.3184             1.817              11             1 2020-03-18
AUDUSD  4181               0.0303            0.3768             1.172              20             3 2020-03-12
NZDUSD  4181               0.0361            0.4023             1.450              23             2 2011-08-05
USDCAD  4181               0.0248            0.2948             0.895               9             0 2020-03-12
USDCHF  4181               0.0276            0.3103             1.041               8             1 2011-10-07
