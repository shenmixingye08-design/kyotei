# FX AUTOPILOT V2 研究結果（2026-11-28 05:06 UTC、データ〜2026-11-27 21:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v2.yaml`

> **検証汚染の申告**: 設計者は v1 の 2010〜2026 の結果（Stage1 WF 2014〜2021、TEST 2022〜2025-06、FORWARD 2025-07〜）を既に見ている。 V2 の候補選び（中期トレンド・キャリー・通貨強弱を優先したこと）はその知見の影響を受けている。 したがって V2 の Walk-Forward 成績は、どの年も「完全な未知データ」ではない（"汚染あり WF OOS" と表記する）。 V2 の最終判断は、LOCK 後に新しく到着する足での PAPER Forward のみで行う。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v2_trend_carry | CHALLENGER | 159 | +21.9% | +1.5% | 2.18 | 0.48 | 0.67 | -7.8% | 1,528 | 33 | 0.02 | 8 | 77% | 24% | +9.4% | +11.4% | 1.88 | 5 | 48% | 0.58 | 1 |  |
| v2_h4_ema | REJECTED | 906 | +3.9% | +0.3% | 1.02 | 0.09 | 0.14 | -13.4% | 41 | 82 | 0.44 | 16 | 46% | 44% | +7.7% | -3.6% | 0.91 | 3 | 73% | 0.12 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, single_regime_dependence, deflated_sharpe |
| v2_d1_tsmom | REJECTED | 203 | -13.9% | -1.2% | 0.90 | -0.08 | -0.11 | -27.8% | -441 | 119 | 0.39 | 18 | 46% | 43% | -3.1% | -11.1% | 0.84 | 1 | 100% | 0.03 | 4 | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_xpair_strength | REJECTED | 333 | -3.0% | -0.2% | 0.91 | -0.12 | -0.17 | -9.3% | -81 | 31 | 36.47 | 13 | 38% | 50% | +0.8% | -3.7% | 0.82 | 1 | 100% | 0.03 | 2 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_session_breakout | REJECTED | 2645 | -32.2% | -3.0% | 0.95 | -0.23 | -0.36 | -46.6% | -130 | 132 | 3.38 | 22 | 38% | 37% | -37.9% | +9.2% | 0.85 | 2 | 100% | 0.01 | 4 | profit_factor, sharpe, positive_years, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_d1_donchian | REJECTED | 168 | -9.3% | -0.8% | 0.76 | -0.24 | -0.33 | -16.9% | -576 | 42 | — | 12 | 31% | 41% | -2.5% | -7.0% | 0.66 | 0 | 100% | 0.01 | 3 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_ml_d1_logit | REJECTED | 155 | -6.0% | -0.5% | 0.60 | -0.64 | -0.78 | -6.5% | -384 | 30 | — | 6 | 23% | 45% | -4.6% | -1.4% | 0.54 | 0 | 100% | 0.00 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, ml_not_better_than_simple |
| trend_tsmom | REFERENCE_V1 | 986 | -17.4% | -1.5% | 0.93 | -0.17 | -0.25 | -28.0% | -172 | 63 | — | 20 | 54% | 34% | -16.1% | -1.5% | 0.88 | 2 | 100% | 0.02 | 3 | reference_v1 |
| ml_logit | REFERENCE_V1 | 3227 | -16.9% | -1.4% | 0.96 | -0.19 | -0.26 | -19.5% | -61 | 127 | 1.63 | 12 | 31% | 41% | -15.9% | -1.2% | 0.86 | 2 | 79% | 0.01 | 2 | reference_v1 |
| mr_zscore | REFERENCE_V1 | 3293 | -35.5% | -3.3% | 0.94 | -0.35 | -0.49 | -50.5% | -70 | 59 | 9.05 | 17 | 31% | 59% | -42.9% | +13.0% | 0.85 | 2 | 100% | 0.00 | 2 | reference_v1 |
| trend_ema_adx | REFERENCE_V1 | 3704 | -49.7% | -5.2% | 0.91 | -0.42 | -0.65 | -55.3% | -140 | 115 | 14.63 | 28 | 15% | 55% | -32.3% | -25.7% | 0.81 | 1 | 100% | 0.00 | 4 | reference_v1 |
| trend_donchian | REFERENCE_V1 | 2414 | -72.3% | -9.5% | 0.82 | -0.62 | -0.90 | -76.0% | -399 | 92 | — | 27 | 23% | 64% | -56.2% | -36.7% | 0.74 | 1 | 100% | 0.00 | 3 | reference_v1 |
| ml_lgbm | REFERENCE_V1 | 14126 | -68.4% | -8.5% | 0.95 | -0.70 | -0.94 | -70.7% | -50 | 100 | 1.68 | 13 | 15% | 95% | -50.5% | -36.2% | 0.85 | 1 | 100% | 0.00 | 2 | reference_v1 |
| mr_rsi_bb | REFERENCE_V1 | 2688 | -48.7% | -5.0% | 0.88 | -0.78 | -1.05 | -49.5% | -141 | 93 | — | 10 | 8% | 100% | -26.4% | -30.3% | 0.79 | 1 | 100% | 0.00 | 1 | reference_v1 |
| regime_switch | REFERENCE_V1 | 3804 | -68.6% | -8.6% | 0.88 | -0.87 | -1.25 | -71.9% | -136 | 74 | — | 15 | 23% | 63% | -55.4% | -29.5% | 0.80 | 0 | 100% | 0.00 | 2 | reference_v1 |
| mtf_pullback | REFERENCE_V1 | 774 | -39.6% | -3.8% | 0.75 | -1.04 | -1.33 | -42.4% | -510 | 140 | — | 15 | 23% | 55% | -38.0% | -2.5% | 0.67 | 0 | 99% | 0.00 | 2 | reference_v1 |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v2_d1_donchian | REJECTED | 168 | — | — | -229,308 | 0.43 | — | -6.0% |
| v2_d1_tsmom | REJECTED | 203 | — | — | -546,669 | 0.42 | — | -13.1% |
| v2_h4_ema | REJECTED | 906 | 96% | 398% | -111,254 | 0.93 | -158% | -2.6% |
| v2_trend_carry | CHALLENGER | 159 | 53% | 109% | -21,719 | 0.89 | 12% | +2.7% |
| v2_xpair_strength | REJECTED | 333 | — | — | -88,536 | 0.71 | — | -1.8% |
| v2_session_breakout | REJECTED | 2645 | — | — | -567,992 | 0.92 | — | +3.0% |
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
| 2026.0 | -0.2% | -6.6% | -0.9% | +2.0% | -2.5% | -2.1% | +0.0% | -5.2% | -5.1% | -3.8% | -6.7% | -9.4% | -5.5% | +4.4% | -1.2% | -13.0% |

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
| 2021.0 | 0.83 | 11.88 | 0.82 | 169.93 | 0.31 | 0.79 | 1.43 | 0.87 | 0.82 | 1.15 | 0.94 | 0.97 | 0.85 | 0.54 | 2.32 | 0.90 |
| 2022.0 | 1.66 | 0.00 | 1.47 | 3.28 | 0.29 | 1.10 | — | 1.03 | 1.00 | 1.13 | 0.80 | 0.88 | 1.02 | 1.15 | 1.29 | 1.00 |
| 2023.0 | 0.20 | 0.09 | 0.61 | 1.48 | 0.46 | 1.01 | 0.22 | 0.87 | 0.75 | 1.15 | 0.83 | 1.37 | 0.96 | 0.61 | 1.21 | 0.95 |
| 2024.0 | 0.27 | 0.13 | 1.19 | 0.22 | 0.97 | 0.96 | 0.00 | 0.74 | 1.15 | 1.08 | 0.99 | 1.08 | 0.90 | 1.19 | 0.80 | 0.96 |
| 2025.0 | 0.72 | 2.11 | 0.74 | 0.50 | 2.03 | 1.25 | 0.24 | 0.95 | 0.46 | 0.70 | 0.71 | 1.16 | 0.64 | 0.80 | 0.88 | 0.88 |
| 2026.0 | 1.11 | 0.71 | 0.91 | 2.16 | 0.40 | 0.90 | — | 0.84 | 0.83 | 0.83 | 0.77 | 0.79 | 0.88 | 1.71 | 0.90 | 0.90 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v2_d1_donchian | AUDUSD | 38 | -29,849 | 0.71 | 32% | 61 | -10,210 |
| v2_d1_donchian | EURJPY | 27 | -5,742 | 0.89 | 37% | 41 | -2,158 |
| v2_d1_donchian | EURUSD | 34 | -12,296 | 0.85 | 29% | 27 | -10,811 |
| v2_d1_donchian | GBPUSD | 36 | -27,195 | 0.66 | 28% | 42 | -9,482 |
| v2_d1_donchian | USDJPY | 33 | -21,719 | 0.75 | 33% | 34 | -110 |
| v2_d1_tsmom | AUDUSD | 55 | -33,223 | 0.77 | 35% | 156 | -30,354 |
| v2_d1_tsmom | EURJPY | 36 | -109,677 | 0.40 | 22% | 142 | -8,760 |
| v2_d1_tsmom | EURUSD | 34 | +159,689 | 1.79 | 32% | 62 | -41,823 |
| v2_d1_tsmom | GBPUSD | 36 | -5,703 | 0.98 | 42% | 183 | -42,167 |
| v2_d1_tsmom | USDJPY | 42 | -100,545 | 0.39 | 26% | 44 | -4,427 |
| v2_h4_ema | AUDUSD | 158 | -6,868 | 0.98 | 35% | 122 | -8,446 |
| v2_h4_ema | EURJPY | 189 | -26,543 | 0.93 | 36% | 74 | -13,502 |
| v2_h4_ema | EURUSD | 188 | +4,295 | 1.01 | 31% | 69 | -13,873 |
| v2_h4_ema | GBPUSD | 180 | +7,931 | 1.02 | 33% | 91 | -11,144 |
| v2_h4_ema | USDJPY | 191 | +58,514 | 1.17 | 36% | 63 | -12,137 |
| v2_trend_carry | AUDUSD | 44 | +13,296 | 1.35 | 36% | 50 | -3,491 |
| v2_trend_carry | EURJPY | 25 | +12,170 | 1.31 | 36% | 27 | +2,606 |
| v2_trend_carry | EURUSD | 34 | +67,242 | 2.30 | 35% | 22 | +1,016 |
| v2_trend_carry | GBPUSD | 33 | +4,801 | 1.11 | 45% | 36 | -6,337 |
| v2_trend_carry | USDJPY | 23 | +145,454 | 5.23 | 39% | 21 | +34,449 |
| v2_xpair_strength | AUDUSD | 95 | -17,980 | 0.76 | 42% | 39 | -4,707 |
| v2_xpair_strength | EURJPY | 54 | -6,784 | 0.88 | 43% | 34 | -1,356 |
| v2_xpair_strength | EURUSD | 72 | -6,308 | 0.91 | 43% | 20 | -7,026 |
| v2_xpair_strength | GBPUSD | 60 | -5,199 | 0.91 | 45% | 34 | -6,094 |
| v2_xpair_strength | USDJPY | 52 | +9,318 | 1.18 | 44% | 22 | +2,163 |
| v2_session_breakout | AUDUSD | 520 | -273,771 | 0.79 | 32% | 185 | -23,338 |
| v2_session_breakout | EURJPY | 571 | -242,013 | 0.84 | 33% | 136 | -12,642 |
| v2_session_breakout | EURUSD | 541 | +104,448 | 1.09 | 35% | 95 | -30,232 |
| v2_session_breakout | GBPUSD | 506 | -111,363 | 0.92 | 32% | 140 | -29,853 |
| v2_session_breakout | USDJPY | 507 | +180,042 | 1.14 | 37% | 106 | -323 |
| v2_ml_d1_logit | AUDUSD | 15 | -2,070 | 0.85 | 60% | 40 | -701 |
| v2_ml_d1_logit | EURJPY | 27 | -8,416 | 0.70 | 44% | 33 | -777 |
| v2_ml_d1_logit | EURUSD | 33 | -21,065 | 0.41 | 33% | 22 | -2,001 |
| v2_ml_d1_logit | GBPUSD | 41 | -18,845 | 0.52 | 41% | 34 | -1,185 |
| v2_ml_d1_logit | USDJPY | 39 | -9,114 | 0.70 | 51% | 25 | -486 |
| trend_ema_adx | AUDUSD | 828 | -228,362 | 0.83 | 31% | 168 | -24,032 |
| trend_ema_adx | EURJPY | 805 | -141,323 | 0.90 | 30% | 113 | -29,242 |
| trend_ema_adx | EURUSD | 723 | -17,819 | 0.98 | 33% | 78 | -23,665 |
| trend_ema_adx | GBPUSD | 654 | -173,227 | 0.83 | 30% | 116 | -23,171 |
| trend_ema_adx | USDJPY | 694 | +41,146 | 1.04 | 32% | 93 | -21,878 |
| trend_donchian | AUDUSD | 540 | -507,687 | 0.58 | 23% | 133 | -30,290 |
| trend_donchian | EURJPY | 522 | -38,509 | 0.97 | 25% | 89 | -41,486 |
| trend_donchian | EURUSD | 442 | -219,664 | 0.75 | 23% | 62 | -31,381 |
| trend_donchian | GBPUSD | 443 | -253,056 | 0.74 | 23% | 95 | -39,590 |
| trend_donchian | USDJPY | 467 | +55,790 | 1.05 | 27% | 76 | -19,127 |
| trend_tsmom | AUDUSD | 186 | +12,481 | 1.03 | 39% | 95 | -15,817 |
| trend_tsmom | EURJPY | 189 | -108,330 | 0.77 | 34% | 56 | -9,502 |
| trend_tsmom | EURUSD | 208 | -35,985 | 0.94 | 36% | 52 | -24,961 |
| trend_tsmom | GBPUSD | 192 | +5,514 | 1.01 | 32% | 68 | -22,072 |
| trend_tsmom | USDJPY | 211 | -43,259 | 0.93 | 31% | 48 | -4,555 |
| mr_rsi_bb | AUDUSD | 451 | +947 | 1.00 | 51% | 138 | -3,940 |
| mr_rsi_bb | EURJPY | 503 | -81,420 | 0.86 | 48% | 89 | -7,431 |
| mr_rsi_bb | EURUSD | 562 | -35,463 | 0.94 | 49% | 67 | -7,957 |
| mr_rsi_bb | GBPUSD | 566 | -48,034 | 0.92 | 49% | 103 | -7,517 |
| mr_rsi_bb | USDJPY | 606 | -214,774 | 0.72 | 43% | 76 | -11,879 |
| mr_zscore | AUDUSD | 678 | -90,879 | 0.88 | 42% | 88 | -8,891 |
| mr_zscore | EURJPY | 667 | +27,883 | 1.04 | 46% | 53 | -11,192 |
| mr_zscore | EURUSD | 645 | +15,411 | 1.02 | 44% | 44 | -12,562 |
| mr_zscore | GBPUSD | 609 | -87,267 | 0.87 | 41% | 63 | -10,061 |
| mr_zscore | USDJPY | 694 | -95,230 | 0.88 | 41% | 46 | -15,370 |
| regime_switch | AUDUSD | 787 | -74,971 | 0.92 | 36% | 115 | -12,232 |
| regime_switch | EURJPY | 734 | -166,640 | 0.81 | 35% | 66 | -12,832 |
| regime_switch | EURUSD | 732 | -10,895 | 0.99 | 35% | 52 | -11,628 |
| regime_switch | GBPUSD | 717 | -63,058 | 0.92 | 36% | 77 | -12,306 |
| regime_switch | USDJPY | 834 | -202,365 | 0.79 | 32% | 60 | -13,403 |
| mtf_pullback | AUDUSD | 156 | -80,671 | 0.76 | 43% | 214 | -2,897 |
| mtf_pullback | EURJPY | 142 | -66,957 | 0.77 | 43% | 131 | -2,000 |
| mtf_pullback | EURUSD | 151 | -93,887 | 0.68 | 39% | 100 | -3,002 |
| mtf_pullback | GBPUSD | 168 | -142,877 | 0.62 | 38% | 155 | -3,052 |
| mtf_pullback | USDJPY | 157 | -10,679 | 0.96 | 46% | 95 | -308 |
| ml_logit | AUDUSD | 576 | +44,983 | 1.05 | 51% | 193 | -13,772 |
| ml_logit | EURJPY | 753 | +106,463 | 1.09 | 54% | 123 | -2,413 |
| ml_logit | EURUSD | 672 | -135,848 | 0.86 | 46% | 93 | -10,186 |
| ml_logit | GBPUSD | 366 | -140,379 | 0.75 | 45% | 134 | -4,134 |
| ml_logit | USDJPY | 860 | -71,734 | 0.95 | 50% | 111 | -7,587 |
| ml_lgbm | AUDUSD | 2861 | -389,340 | 0.88 | 48% | 157 | -28,224 |
| ml_lgbm | EURJPY | 2688 | -15,995 | 0.99 | 50% | 97 | -20,429 |
| ml_lgbm | EURUSD | 2880 | -189,836 | 0.93 | 49% | 66 | -37,722 |
| ml_lgbm | GBPUSD | 2502 | -229,945 | 0.91 | 49% | 109 | -21,867 |
| ml_lgbm | USDJPY | 3195 | +125,593 | 1.04 | 51% | 76 | -19,811 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v2_d1_donchian | regime4h | NEUTRAL | 43 | -47,458 | 35% | 0.48 |
| v2_d1_donchian | regime4h | RANGE | 28 | -24,701 | 29% | 0.68 |
| v2_d1_donchian | regime4h | TREND | 195 | -38,932 | 31% | 0.91 |
| v2_d1_donchian | month_dir | DOWN | 55 | +36,666 | 38% | 1.36 |
| v2_d1_donchian | month_dir | FLAT | 144 | -146,446 | 26% | 0.62 |
| v2_d1_donchian | month_dir | UP | 67 | -1,312 | 39% | 0.99 |
| v2_d1_donchian | month_vol | HIGH_VOL | 51 | -12,293 | 31% | 0.90 |
| v2_d1_donchian | month_vol | LOW_VOL | 215 | -98,798 | 32% | 0.80 |
| v2_d1_tsmom | regime4h | HIGH_VOL | 16 | -45,989 | 25% | 0.49 |
| v2_d1_tsmom | regime4h | NEUTRAL | 81 | -158,545 | 31% | 0.57 |
| v2_d1_tsmom | regime4h | RANGE | 87 | -82,870 | 33% | 0.78 |
| v2_d1_tsmom | regime4h | TREND | 191 | +191,678 | 35% | 1.20 |
| v2_d1_tsmom | month_dir | DOWN | 70 | -19,703 | 24% | 0.95 |
| v2_d1_tsmom | month_dir | FLAT | 221 | -150,718 | 34% | 0.86 |
| v2_d1_tsmom | month_dir | UP | 84 | +74,696 | 38% | 1.20 |
| v2_d1_tsmom | month_vol | HIGH_VOL | 106 | -217,293 | 29% | 0.54 |
| v2_d1_tsmom | month_vol | LOW_VOL | 269 | +121,567 | 35% | 1.09 |
| v2_h4_ema | regime4h | HIGH_VOL | 76 | +71,678 | 42% | 1.63 |
| v2_h4_ema | regime4h | NEUTRAL | 356 | -60,217 | 33% | 0.91 |
| v2_h4_ema | regime4h | TREND | 474 | +25,868 | 34% | 1.03 |
| v2_h4_ema | month_dir | DOWN | 161 | +322,486 | 42% | 2.27 |
| v2_h4_ema | month_dir | FLAT | 619 | -444,437 | 31% | 0.62 |
| v2_h4_ema | month_dir | UP | 126 | +159,280 | 41% | 1.71 |
| v2_h4_ema | month_vol | HIGH_VOL | 283 | +167,735 | 40% | 1.37 |
| v2_h4_ema | month_vol | LOW_VOL | 623 | -130,406 | 31% | 0.89 |
| v2_trend_carry | regime4h | HIGH_VOL | 10 | +17,524 | 50% | 2.83 |
| v2_trend_carry | regime4h | NEUTRAL | 36 | +19,842 | 36% | 1.48 |
| v2_trend_carry | regime4h | RANGE | 34 | +116,219 | 44% | 3.73 |
| v2_trend_carry | regime4h | TREND | 79 | +89,379 | 35% | 1.80 |
| v2_trend_carry | month_dir | DOWN | 32 | +29,619 | 47% | 1.69 |
| v2_trend_carry | month_dir | FLAT | 96 | +200,046 | 34% | 2.57 |
| v2_trend_carry | month_dir | UP | 31 | +13,299 | 42% | 1.37 |
| v2_trend_carry | month_vol | HIGH_VOL | 35 | +6,010 | 40% | 1.15 |
| v2_trend_carry | month_vol | LOW_VOL | 124 | +236,953 | 38% | 2.44 |
| v2_xpair_strength | regime4h | HIGH_VOL | 33 | -4,677 | 48% | 0.89 |
| v2_xpair_strength | regime4h | NEUTRAL | 90 | -29,392 | 40% | 0.67 |
| v2_xpair_strength | regime4h | RANGE | 134 | +9,996 | 47% | 1.09 |
| v2_xpair_strength | regime4h | TREND | 220 | -41,859 | 42% | 0.82 |
| v2_xpair_strength | month_dir | DOWN | 93 | +28,067 | 51% | 1.33 |
| v2_xpair_strength | month_dir | FLAT | 271 | -118,565 | 38% | 0.59 |
| v2_xpair_strength | month_dir | UP | 113 | +24,566 | 51% | 1.23 |
| v2_xpair_strength | month_vol | HIGH_VOL | 123 | -37,958 | 40% | 0.74 |
| v2_xpair_strength | month_vol | LOW_VOL | 354 | -27,974 | 45% | 0.92 |
| v2_session_breakout | regime4h | HIGH_VOL | 260 | +30,949 | 35% | 1.04 |
| v2_session_breakout | regime4h | NEUTRAL | 802 | -116,018 | 33% | 0.95 |
| v2_session_breakout | regime4h | RANGE | 1369 | -20,358 | 34% | 0.99 |
| v2_session_breakout | regime4h | TREND | 1492 | -329,130 | 33% | 0.92 |
| v2_session_breakout | month_dir | DOWN | 775 | +427,387 | 40% | 1.23 |
| v2_session_breakout | month_dir | FLAT | 2298 | -1,274,480 | 30% | 0.79 |
| v2_session_breakout | month_dir | UP | 850 | +412,538 | 37% | 1.20 |
| v2_session_breakout | month_vol | HIGH_VOL | 1475 | -15,253 | 34% | 1.00 |
| v2_session_breakout | month_vol | LOW_VOL | 2448 | -419,302 | 33% | 0.93 |
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
| trend_ema_adx | regime4h | NEUTRAL | 1002 | -123,911 | 33% | 0.92 |
| trend_ema_adx | regime4h | RANGE | 2222 | -101,455 | 31% | 0.97 |
| trend_ema_adx | regime4h | TREND | 794 | -233,465 | 29% | 0.82 |
| trend_ema_adx | month_dir | DOWN | 821 | +231,601 | 32% | 1.18 |
| trend_ema_adx | month_dir | FLAT | 2717 | -812,297 | 30% | 0.81 |
| trend_ema_adx | month_dir | UP | 754 | +33,727 | 34% | 1.03 |
| trend_ema_adx | month_vol | HIGH_VOL | 1453 | -429,876 | 31% | 0.82 |
| trend_ema_adx | month_vol | LOW_VOL | 2839 | -117,093 | 31% | 0.97 |
| trend_donchian | regime4h | HIGH_VOL | 214 | -69,802 | 22% | 0.87 |
| trend_donchian | regime4h | NEUTRAL | 724 | -734,843 | 20% | 0.60 |
| trend_donchian | regime4h | RANGE | 1141 | -72,438 | 26% | 0.97 |
| trend_donchian | regime4h | TREND | 827 | -30,951 | 26% | 0.98 |
| trend_donchian | month_dir | DOWN | 564 | +236,088 | 30% | 1.20 |
| trend_donchian | month_dir | FLAT | 1812 | -1,758,681 | 20% | 0.60 |
| trend_donchian | month_dir | UP | 530 | +614,559 | 31% | 1.57 |
| trend_donchian | month_vol | HIGH_VOL | 917 | -281,856 | 25% | 0.87 |
| trend_donchian | month_vol | LOW_VOL | 1989 | -626,177 | 24% | 0.86 |
| trend_tsmom | regime4h | HIGH_VOL | 86 | -11,139 | 36% | 0.94 |
| trend_tsmom | regime4h | NEUTRAL | 173 | -64,024 | 34% | 0.86 |
| trend_tsmom | regime4h | RANGE | 219 | +157,199 | 39% | 1.31 |
| trend_tsmom | regime4h | TREND | 586 | -124,677 | 33% | 0.92 |
| trend_tsmom | month_dir | DOWN | 248 | +320,629 | 47% | 1.62 |
| trend_tsmom | month_dir | FLAT | 582 | -902,930 | 24% | 0.49 |
| trend_tsmom | month_dir | UP | 234 | +539,659 | 50% | 2.16 |
| trend_tsmom | month_vol | HIGH_VOL | 383 | +86,012 | 36% | 1.09 |
| trend_tsmom | month_vol | LOW_VOL | 681 | -128,654 | 34% | 0.93 |
| mr_rsi_bb | regime4h | HIGH_VOL | 132 | -1,357 | 53% | 0.99 |
| mr_rsi_bb | regime4h | NEUTRAL | 541 | -34,252 | 48% | 0.94 |
| mr_rsi_bb | regime4h | RANGE | 1158 | -230,429 | 46% | 0.83 |
| mr_rsi_bb | regime4h | TREND | 857 | -112,705 | 48% | 0.89 |
| mr_rsi_bb | month_dir | DOWN | 558 | -124,833 | 47% | 0.82 |
| mr_rsi_bb | month_dir | FLAT | 1560 | -110,982 | 49% | 0.94 |
| mr_rsi_bb | month_dir | UP | 570 | -142,929 | 45% | 0.79 |
| mr_rsi_bb | month_vol | HIGH_VOL | 923 | -221,152 | 45% | 0.81 |
| mr_rsi_bb | month_vol | LOW_VOL | 1765 | -157,592 | 49% | 0.92 |
| mr_zscore | regime4h | HIGH_VOL | 335 | -55,352 | 42% | 0.85 |
| mr_zscore | regime4h | NEUTRAL | 628 | +29,591 | 47% | 1.05 |
| mr_zscore | regime4h | RANGE | 768 | -144,773 | 42% | 0.83 |
| mr_zscore | regime4h | TREND | 1562 | -59,547 | 42% | 0.97 |
| mr_zscore | month_dir | DOWN | 808 | -272,076 | 37% | 0.73 |
| mr_zscore | month_dir | FLAT | 1827 | +264,578 | 48% | 1.14 |
| mr_zscore | month_dir | UP | 658 | -222,583 | 37% | 0.71 |
| mr_zscore | month_vol | HIGH_VOL | 1202 | -138,232 | 41% | 0.90 |
| mr_zscore | month_vol | LOW_VOL | 2091 | -91,850 | 44% | 0.96 |
| regime_switch | regime4h | HIGH_VOL | 28 | -8,624 | 39% | 0.48 |
| regime_switch | regime4h | NEUTRAL | 126 | -51,343 | 33% | 0.65 |
| regime_switch | regime4h | RANGE | 2879 | -412,490 | 36% | 0.87 |
| regime_switch | regime4h | TREND | 1187 | -126,087 | 32% | 0.91 |
| regime_switch | month_dir | DOWN | 837 | +11,228 | 37% | 1.01 |
| regime_switch | month_dir | FLAT | 2538 | -509,471 | 34% | 0.82 |
| regime_switch | month_dir | UP | 845 | -100,302 | 34% | 0.89 |
| regime_switch | month_vol | HIGH_VOL | 1301 | +64,123 | 37% | 1.04 |
| regime_switch | month_vol | LOW_VOL | 2919 | -662,667 | 33% | 0.80 |
| mtf_pullback | regime4h | HIGH_VOL | 4 | +181 | 50% | 1.02 |
| mtf_pullback | regime4h | NEUTRAL | 145 | +22,905 | 50% | 1.09 |
| mtf_pullback | regime4h | RANGE | 215 | -163,782 | 38% | 0.64 |
| mtf_pullback | regime4h | TREND | 410 | -254,376 | 40% | 0.70 |
| mtf_pullback | month_dir | DOWN | 125 | -66,138 | 43% | 0.74 |
| mtf_pullback | month_dir | FLAT | 485 | -352,257 | 38% | 0.66 |
| mtf_pullback | month_dir | UP | 164 | +23,324 | 52% | 1.08 |
| mtf_pullback | month_vol | HIGH_VOL | 214 | -145,044 | 43% | 0.70 |
| mtf_pullback | month_vol | LOW_VOL | 560 | -250,028 | 41% | 0.77 |
| ml_logit | regime4h | HIGH_VOL | 1236 | +108,129 | 52% | 1.06 |
| ml_logit | regime4h | NEUTRAL | 949 | -76,963 | 49% | 0.95 |
| ml_logit | regime4h | RANGE | 1089 | +28,047 | 52% | 1.02 |
| ml_logit | regime4h | TREND | 2697 | -378,359 | 48% | 0.91 |
| ml_logit | month_dir | DOWN | 1569 | -260,914 | 48% | 0.90 |
| ml_logit | month_dir | FLAT | 3122 | -94,015 | 50% | 0.98 |
| ml_logit | month_dir | UP | 1280 | +35,782 | 51% | 1.02 |
| ml_logit | month_vol | HIGH_VOL | 2389 | +78,771 | 52% | 1.02 |
| ml_logit | month_vol | LOW_VOL | 3582 | -397,917 | 49% | 0.93 |
| ml_lgbm | regime4h | HIGH_VOL | 1960 | +52,005 | 52% | 1.03 |
| ml_lgbm | regime4h | NEUTRAL | 2925 | -418,918 | 47% | 0.87 |
| ml_lgbm | regime4h | RANGE | 4546 | -149,407 | 49% | 0.97 |
| ml_lgbm | regime4h | TREND | 6977 | -223,969 | 50% | 0.97 |
| ml_lgbm | month_dir | DOWN | 3814 | -196,755 | 49% | 0.95 |
| ml_lgbm | month_dir | FLAT | 9196 | -387,804 | 50% | 0.96 |
| ml_lgbm | month_dir | UP | 3398 | -155,729 | 50% | 0.96 |
| ml_lgbm | month_vol | HIGH_VOL | 6408 | +133,129 | 51% | 1.02 |
| ml_lgbm | month_vol | LOW_VOL | 10000 | -873,418 | 48% | 0.92 |

## 比較: session（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | session | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v2_session_breakout | all | 5312 | -1.6% | 1.00 | 0.06 | -0.15 | 0.29 | -42.6% |
| v2_session_breakout | london | 4200 | +21.5% | 1.02 | 0.16 | 0.02 | 0.43 | -40.9% |
| v2_session_breakout | london_ny | 3007 | -13.2% | 0.98 | -0.04 | -0.14 | -0.03 | -37.0% |
| v2_session_breakout | ny | 3759 | -3.6% | 1.00 | 0.04 | -0.08 | 0.02 | -37.2% |
| v2_session_breakout | tokyo | 3109 | -15.3% | 0.98 | -0.05 | -0.37 | 0.45 | -37.5% |
| v2_session_breakout | tokyo_london | 2277 | +23.5% | 1.04 | 0.18 | 0.15 | 0.43 | -26.9% |

## 比較: sizing（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | sizing | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v2_d1_donchian | fixed_notional | 253 | -41.9% | 0.81 | -0.16 | -0.21 | -0.28 | -55.5% |
| v2_d1_donchian | risk_stop | 261 | +0.1% | 1.03 | 0.00 | 0.03 | -0.35 | -16.7% |
| v2_d1_donchian | vol_target | 263 | -17.0% | 0.91 | -0.08 | -0.17 | -0.29 | -40.7% |
| v2_d1_tsmom | fixed_notional | 282 | -28.3% | 0.88 | -0.03 | -0.08 | -0.24 | -56.5% |
| v2_d1_tsmom | risk_stop | 277 | +6.3% | 1.18 | 0.13 | 0.14 | 0.02 | -13.0% |
| v2_d1_tsmom | vol_target | 284 | +11.8% | 1.07 | 0.11 | 0.08 | -0.09 | -42.2% |
| v2_trend_carry | risk_stop | 127 | +5.8% | 1.08 | 0.04 | 0.00 | 0.06 | -7.4% |
| v2_trend_carry | vol_target | 141 | +15.3% | 0.99 | 0.05 | 0.02 | 0.13 | -26.9% |
| v2_xpair_strength | fixed_notional | 437 | -26.8% | 0.88 | -0.08 | -0.13 | -0.23 | -52.5% |
| v2_xpair_strength | risk_stop | 373 | +0.8% | 1.02 | 0.03 | 0.03 | -0.36 | -8.5% |
| v2_xpair_strength | vol_target | 453 | -7.8% | 0.95 | -0.03 | -0.04 | -0.32 | -35.2% |

## 比較: regime（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | regime | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v2_d1_donchian | no_high_vol | 247 | -16.1% | 0.94 | -0.05 | -0.08 | -0.39 | -36.6% |
| v2_d1_donchian | none | 273 | -23.5% | 0.89 | -0.10 | -0.14 | -0.37 | -39.8% |
| v2_d1_donchian | trend_only | 257 | -19.3% | 0.92 | -0.08 | -0.12 | -0.16 | -36.4% |
| v2_h4_ema | no_high_vol | 970 | -6.5% | 0.94 | -0.11 | -0.12 | -0.28 | -17.4% |
| v2_h4_ema | none | 1097 | -1.1% | 0.97 | -0.04 | 0.02 | -0.31 | -16.9% |
| v2_h4_ema | trend_only | 903 | +0.1% | 0.97 | -0.02 | 0.04 | -0.36 | -16.0% |

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
USD     201     2026-10        -0.107             0.133            1.225
EUR     193     2026-01        -0.190             0.223            1.176
JPY     201     2026-09        -0.177             0.178            1.181
GBP     193     2026-01        -0.116             0.154            1.140
AUD     202     2026-10        -0.176             0.207            1.200
NZD     202     2026-10        -0.178             0.186            0.750
CAD     202     2026-10         0.050             0.084            0.422
CHF     202     2026-10         0.034             0.066            0.353
```

## データ品質: Dukascopy と米連銀 H.10 正午レートの突き合わせ（日次）

  pair  days  median_abs_diff_pct  p99_abs_diff_pct  max_abs_diff_pct  days_gt_0_5pct  days_gt_1pct  worst_day
USDJPY  4224               0.0219            0.2986             1.156               9             1 2013-06-06
EURUSD  4224               0.0254            0.3172             0.884               9             0 2011-10-07
GBPUSD  4224               0.0255            0.3171             1.817              11             1 2020-03-18
AUDUSD  4224               0.0303            0.3765             1.172              20             3 2020-03-12
NZDUSD  4224               0.0361            0.3991             1.450              23             2 2011-08-05
USDCAD  4224               0.0248            0.2944             0.895               9             0 2020-03-12
USDCHF  4224               0.0276            0.3098             1.041               8             1 2011-10-07
