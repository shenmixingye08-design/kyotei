# FX AUTOPILOT V2 研究結果（2026-11-14 03:13 UTC、データ〜2026-11-13 21:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v2.yaml`

> **検証汚染の申告**: 設計者は v1 の 2010〜2026 の結果（Stage1 WF 2014〜2021、TEST 2022〜2025-06、FORWARD 2025-07〜）を既に見ている。 V2 の候補選び（中期トレンド・キャリー・通貨強弱を優先したこと）はその知見の影響を受けている。 したがって V2 の Walk-Forward 成績は、どの年も「完全な未知データ」ではない（"汚染あり WF OOS" と表記する）。 V2 の最終判断は、LOCK 後に新しく到着する足での PAPER Forward のみで行う。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v2_trend_carry | CHALLENGER | 159 | +21.4% | +1.5% | 2.16 | 0.47 | 0.66 | -7.8% | 1,495 | 33 | 0.02 | 8 | 77% | 24% | +9.4% | +10.9% | 1.86 | 5 | 49% | 0.57 | 1 |  |
| v2_h4_ema | REJECTED | 906 | +3.2% | +0.2% | 1.02 | 0.08 | 0.12 | -13.4% | 34 | 82 | 0.46 | 16 | 46% | 44% | +7.7% | -4.1% | 0.91 | 3 | 78% | 0.12 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, single_regime_dependence, deflated_sharpe |
| v2_d1_tsmom | REJECTED | 203 | -13.8% | -1.1% | 0.91 | -0.08 | -0.11 | -27.8% | -432 | 119 | 0.38 | 18 | 46% | 43% | -3.1% | -11.0% | 0.85 | 1 | 100% | 0.03 | 4 | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_xpair_strength | REJECTED | 333 | -3.4% | -0.3% | 0.90 | -0.15 | -0.20 | -9.3% | -95 | 31 | — | 13 | 38% | 50% | +0.8% | -4.1% | 0.81 | 1 | 100% | 0.02 | 2 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_session_breakout | REJECTED | 2639 | -32.6% | -3.0% | 0.95 | -0.24 | -0.37 | -46.6% | -133 | 132 | 3.68 | 22 | 38% | 37% | -37.9% | +8.5% | 0.85 | 2 | 100% | 0.01 | 4 | profit_factor, sharpe, positive_years, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_d1_donchian | REJECTED | 166 | -9.7% | -0.8% | 0.75 | -0.25 | -0.35 | -16.9% | -609 | 42 | — | 12 | 31% | 41% | -2.5% | -7.4% | 0.65 | 0 | 100% | 0.01 | 3 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_ml_d1_logit | REJECTED | 155 | -6.0% | -0.5% | 0.60 | -0.64 | -0.78 | -6.5% | -384 | 30 | — | 6 | 23% | 45% | -4.6% | -1.4% | 0.54 | 0 | 100% | 0.00 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, ml_not_better_than_simple |
| trend_tsmom | REFERENCE_V1 | 984 | -18.5% | -1.6% | 0.93 | -0.19 | -0.27 | -28.0% | -186 | 63 | — | 20 | 54% | 34% | -16.1% | -2.9% | 0.87 | 2 | 100% | 0.01 | 3 | reference_v1 |
| ml_logit | REFERENCE_V1 | 3226 | -17.0% | -1.4% | 0.96 | -0.19 | -0.27 | -19.5% | -61 | 127 | 1.64 | 12 | 31% | 41% | -15.9% | -1.3% | 0.86 | 2 | 79% | 0.01 | 2 | reference_v1 |
| mr_zscore | REFERENCE_V1 | 3280 | -35.6% | -3.4% | 0.94 | -0.36 | -0.49 | -50.5% | -70 | 59 | 9.90 | 17 | 31% | 59% | -42.9% | +12.8% | 0.85 | 2 | 100% | 0.00 | 2 | reference_v1 |
| trend_ema_adx | REFERENCE_V1 | 3700 | -49.6% | -5.2% | 0.91 | -0.42 | -0.65 | -55.3% | -140 | 115 | 13.65 | 28 | 15% | 55% | -32.3% | -25.5% | 0.81 | 1 | 100% | 0.00 | 4 | reference_v1 |
| trend_donchian | REFERENCE_V1 | 2411 | -72.7% | -9.6% | 0.82 | -0.63 | -0.91 | -76.0% | -403 | 93 | — | 27 | 23% | 64% | -56.2% | -37.7% | 0.74 | 1 | 100% | 0.00 | 3 | reference_v1 |
| ml_lgbm | REFERENCE_V1 | 14080 | -67.3% | -8.3% | 0.95 | -0.68 | -0.91 | -69.4% | -49 | 100 | 1.66 | 13 | 15% | 95% | -50.5% | -33.9% | 0.85 | 1 | 100% | 0.00 | 2 | reference_v1 |
| mr_rsi_bb | REFERENCE_V1 | 2684 | -48.3% | -5.0% | 0.88 | -0.77 | -1.04 | -49.0% | -140 | 93 | — | 9 | 8% | 100% | -26.4% | -29.7% | 0.79 | 0 | 100% | 0.00 | 1 | reference_v1 |
| regime_switch | REFERENCE_V1 | 3796 | -69.0% | -8.7% | 0.88 | -0.89 | -1.27 | -71.9% | -137 | 74 | — | 15 | 23% | 63% | -55.4% | -30.5% | 0.80 | 0 | 100% | 0.00 | 2 | reference_v1 |
| mtf_pullback | REFERENCE_V1 | 769 | -40.1% | -3.9% | 0.74 | -1.06 | -1.36 | -42.4% | -522 | 140 | — | 15 | 23% | 50% | -38.0% | -3.3% | 0.67 | 0 | 99% | 0.00 | 2 | reference_v1 |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v2_d1_donchian | REJECTED | 166 | — | — | -233,656 | 0.42 | — | -6.4% |
| v2_d1_tsmom | REJECTED | 203 | — | — | -544,884 | 0.42 | — | -13.0% |
| v2_h4_ema | REJECTED | 906 | 117% | 485% | -117,977 | 0.93 | -192% | -3.2% |
| v2_trend_carry | CHALLENGER | 159 | 54% | 111% | -26,972 | 0.87 | 12% | +2.3% |
| v2_xpair_strength | REJECTED | 333 | — | — | -93,186 | 0.70 | — | -2.2% |
| v2_session_breakout | REJECTED | 2639 | — | — | -575,179 | 0.91 | — | +2.4% |
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
| 2026.0 | -0.6% | -6.5% | -1.5% | +1.6% | -2.9% | -2.7% | +0.0% | -4.9% | -6.5% | -5.2% | -5.9% | -9.6% | -6.8% | +3.5% | -1.3% | -9.8% |

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
| 2021.0 | 0.83 | 11.88 | 0.82 | 169.98 | 0.31 | 0.79 | 1.43 | 0.87 | 0.82 | 1.15 | 0.94 | 0.97 | 0.85 | 0.54 | 2.32 | 0.90 |
| 2022.0 | 1.66 | 0.00 | 1.47 | 3.28 | 0.29 | 1.10 | — | 1.03 | 1.00 | 1.13 | 0.80 | 0.88 | 1.02 | 1.15 | 1.29 | 1.00 |
| 2023.0 | 0.20 | 0.09 | 0.61 | 1.48 | 0.46 | 1.01 | 0.22 | 0.87 | 0.75 | 1.15 | 0.83 | 1.37 | 0.96 | 0.61 | 1.21 | 0.95 |
| 2024.0 | 0.27 | 0.13 | 1.19 | 0.22 | 0.97 | 0.96 | 0.00 | 0.74 | 1.15 | 1.08 | 0.99 | 1.08 | 0.90 | 1.19 | 0.80 | 0.96 |
| 2025.0 | 0.72 | 2.48 | 0.74 | 0.50 | 2.03 | 1.25 | 0.24 | 0.95 | 0.46 | 0.70 | 0.71 | 1.16 | 0.64 | 0.80 | 0.88 | 0.88 |
| 2026.0 | 0.53 | 0.49 | 0.85 | 1.69 | 0.29 | 0.87 | — | 0.85 | 0.78 | 0.76 | 0.79 | 0.77 | 0.85 | 1.62 | 0.89 | 0.92 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v2_d1_donchian | AUDUSD | 38 | -33,723 | 0.67 | 32% | 61 | -10,131 |
| v2_d1_donchian | EURJPY | 26 | -4,906 | 0.90 | 38% | 42 | -2,062 |
| v2_d1_donchian | EURUSD | 34 | -13,693 | 0.83 | 29% | 27 | -10,853 |
| v2_d1_donchian | GBPUSD | 35 | -27,108 | 0.66 | 29% | 43 | -9,411 |
| v2_d1_donchian | USDJPY | 33 | -21,719 | 0.75 | 33% | 34 | -110 |
| v2_d1_tsmom | AUDUSD | 55 | -15,182 | 0.90 | 35% | 156 | -29,978 |
| v2_d1_tsmom | EURJPY | 36 | -116,285 | 0.36 | 22% | 141 | -7,922 |
| v2_d1_tsmom | EURUSD | 34 | +149,929 | 1.74 | 32% | 62 | -42,116 |
| v2_d1_tsmom | GBPUSD | 36 | -5,703 | 0.98 | 42% | 183 | -42,167 |
| v2_d1_tsmom | USDJPY | 42 | -100,434 | 0.39 | 26% | 44 | -5,076 |
| v2_h4_ema | AUDUSD | 158 | -6,868 | 0.98 | 35% | 122 | -8,446 |
| v2_h4_ema | EURJPY | 189 | -27,834 | 0.92 | 36% | 74 | -13,262 |
| v2_h4_ema | EURUSD | 188 | +4,295 | 1.01 | 31% | 69 | -13,873 |
| v2_h4_ema | GBPUSD | 180 | +2,500 | 1.01 | 33% | 91 | -10,955 |
| v2_h4_ema | USDJPY | 191 | +58,514 | 1.17 | 36% | 63 | -12,137 |
| v2_trend_carry | AUDUSD | 44 | +9,426 | 1.25 | 36% | 50 | -3,411 |
| v2_trend_carry | EURJPY | 25 | +12,170 | 1.31 | 36% | 27 | +2,606 |
| v2_trend_carry | EURUSD | 34 | +65,859 | 2.28 | 35% | 22 | +974 |
| v2_trend_carry | GBPUSD | 33 | +4,801 | 1.11 | 45% | 36 | -6,337 |
| v2_trend_carry | USDJPY | 23 | +145,498 | 5.23 | 39% | 21 | +34,189 |
| v2_xpair_strength | AUDUSD | 95 | -19,914 | 0.73 | 42% | 39 | -4,668 |
| v2_xpair_strength | EURJPY | 54 | -8,105 | 0.85 | 43% | 34 | -1,189 |
| v2_xpair_strength | EURUSD | 72 | -7,702 | 0.89 | 43% | 20 | -7,068 |
| v2_xpair_strength | GBPUSD | 60 | -5,199 | 0.91 | 45% | 34 | -6,094 |
| v2_xpair_strength | USDJPY | 52 | +9,318 | 1.18 | 44% | 22 | +2,163 |
| v2_session_breakout | AUDUSD | 520 | -281,578 | 0.79 | 32% | 185 | -23,304 |
| v2_session_breakout | EURJPY | 569 | -234,462 | 0.85 | 33% | 136 | -12,045 |
| v2_session_breakout | EURUSD | 540 | +100,203 | 1.08 | 35% | 95 | -30,321 |
| v2_session_breakout | GBPUSD | 505 | -115,740 | 0.91 | 32% | 140 | -29,617 |
| v2_session_breakout | USDJPY | 505 | +181,733 | 1.15 | 37% | 106 | -528 |
| v2_ml_d1_logit | AUDUSD | 15 | -2,070 | 0.85 | 60% | 40 | -701 |
| v2_ml_d1_logit | EURJPY | 27 | -8,416 | 0.70 | 44% | 33 | -777 |
| v2_ml_d1_logit | EURUSD | 33 | -21,065 | 0.41 | 33% | 22 | -2,001 |
| v2_ml_d1_logit | GBPUSD | 41 | -18,845 | 0.52 | 41% | 34 | -1,185 |
| v2_ml_d1_logit | USDJPY | 39 | -9,114 | 0.70 | 51% | 25 | -486 |
| trend_ema_adx | AUDUSD | 828 | -228,362 | 0.83 | 31% | 168 | -24,032 |
| trend_ema_adx | EURJPY | 805 | -141,323 | 0.90 | 30% | 113 | -29,242 |
| trend_ema_adx | EURUSD | 723 | -20,748 | 0.98 | 33% | 78 | -23,755 |
| trend_ema_adx | GBPUSD | 654 | -173,227 | 0.83 | 30% | 116 | -23,171 |
| trend_ema_adx | USDJPY | 690 | +46,281 | 1.04 | 32% | 93 | -21,919 |
| trend_donchian | AUDUSD | 540 | -515,427 | 0.58 | 23% | 133 | -30,131 |
| trend_donchian | EURJPY | 521 | -43,215 | 0.96 | 25% | 89 | -40,816 |
| trend_donchian | EURUSD | 441 | -219,093 | 0.75 | 23% | 62 | -31,387 |
| trend_donchian | GBPUSD | 442 | -251,515 | 0.74 | 24% | 95 | -39,574 |
| trend_donchian | USDJPY | 467 | +58,536 | 1.06 | 27% | 76 | -19,294 |
| trend_tsmom | AUDUSD | 186 | +6,715 | 1.01 | 39% | 95 | -15,757 |
| trend_tsmom | EURJPY | 189 | -108,330 | 0.77 | 34% | 56 | -9,502 |
| trend_tsmom | EURUSD | 207 | -41,712 | 0.93 | 35% | 52 | -25,129 |
| trend_tsmom | GBPUSD | 192 | +5,514 | 1.01 | 32% | 68 | -22,072 |
| trend_tsmom | USDJPY | 210 | -44,998 | 0.92 | 30% | 49 | -4,815 |
| mr_rsi_bb | AUDUSD | 450 | -737 | 1.00 | 51% | 138 | -3,940 |
| mr_rsi_bb | EURJPY | 502 | -79,504 | 0.87 | 48% | 89 | -7,431 |
| mr_rsi_bb | EURUSD | 561 | -33,545 | 0.94 | 49% | 67 | -7,957 |
| mr_rsi_bb | GBPUSD | 565 | -46,808 | 0.93 | 49% | 103 | -7,485 |
| mr_rsi_bb | USDJPY | 606 | -214,774 | 0.72 | 43% | 76 | -11,879 |
| mr_zscore | AUDUSD | 672 | -87,472 | 0.88 | 42% | 88 | -8,853 |
| mr_zscore | EURJPY | 662 | +28,742 | 1.04 | 46% | 53 | -11,224 |
| mr_zscore | EURUSD | 644 | +13,596 | 1.02 | 44% | 44 | -12,537 |
| mr_zscore | GBPUSD | 609 | -87,267 | 0.87 | 41% | 63 | -10,061 |
| mr_zscore | USDJPY | 693 | -98,723 | 0.88 | 41% | 46 | -15,407 |
| regime_switch | AUDUSD | 786 | -76,729 | 0.91 | 36% | 115 | -12,209 |
| regime_switch | EURJPY | 731 | -165,205 | 0.81 | 35% | 66 | -12,748 |
| regime_switch | EURUSD | 732 | -11,184 | 0.98 | 35% | 52 | -11,643 |
| regime_switch | GBPUSD | 716 | -63,412 | 0.92 | 36% | 77 | -12,283 |
| regime_switch | USDJPY | 831 | -204,798 | 0.78 | 32% | 60 | -13,340 |
| mtf_pullback | AUDUSD | 156 | -80,671 | 0.76 | 43% | 214 | -2,897 |
| mtf_pullback | EURJPY | 141 | -63,280 | 0.78 | 43% | 131 | -2,000 |
| mtf_pullback | EURUSD | 150 | -96,698 | 0.67 | 39% | 100 | -3,002 |
| mtf_pullback | GBPUSD | 166 | -146,206 | 0.61 | 37% | 155 | -2,957 |
| mtf_pullback | USDJPY | 156 | -14,510 | 0.95 | 46% | 96 | -604 |
| ml_logit | AUDUSD | 576 | +44,983 | 1.05 | 51% | 193 | -13,772 |
| ml_logit | EURJPY | 752 | +105,145 | 1.09 | 54% | 123 | -2,435 |
| ml_logit | EURUSD | 672 | -135,848 | 0.86 | 46% | 93 | -10,186 |
| ml_logit | GBPUSD | 366 | -140,379 | 0.75 | 45% | 134 | -4,134 |
| ml_logit | USDJPY | 860 | -71,734 | 0.95 | 50% | 111 | -7,587 |
| ml_lgbm | AUDUSD | 2841 | -379,053 | 0.88 | 48% | 157 | -28,107 |
| ml_lgbm | EURJPY | 2682 | -14,629 | 0.99 | 50% | 97 | -20,443 |
| ml_lgbm | EURUSD | 2872 | -186,211 | 0.93 | 50% | 66 | -37,596 |
| ml_lgbm | GBPUSD | 2495 | -232,367 | 0.91 | 49% | 109 | -21,846 |
| ml_lgbm | USDJPY | 3190 | +124,520 | 1.04 | 51% | 76 | -19,885 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v2_d1_donchian | regime4h | NEUTRAL | 43 | -50,252 | 35% | 0.45 |
| v2_d1_donchian | regime4h | RANGE | 28 | -24,701 | 29% | 0.68 |
| v2_d1_donchian | regime4h | TREND | 185 | -40,041 | 33% | 0.91 |
| v2_d1_donchian | month_dir | DOWN | 51 | +37,542 | 41% | 1.39 |
| v2_d1_donchian | month_dir | FLAT | 139 | -148,185 | 27% | 0.61 |
| v2_d1_donchian | month_dir | UP | 66 | -4,350 | 39% | 0.97 |
| v2_d1_donchian | month_vol | HIGH_VOL | 50 | -11,458 | 32% | 0.90 |
| v2_d1_donchian | month_vol | LOW_VOL | 206 | -103,536 | 33% | 0.79 |
| v2_d1_tsmom | regime4h | HIGH_VOL | 16 | -45,989 | 25% | 0.49 |
| v2_d1_tsmom | regime4h | NEUTRAL | 81 | -184,672 | 31% | 0.50 |
| v2_d1_tsmom | regime4h | RANGE | 87 | -82,759 | 33% | 0.78 |
| v2_d1_tsmom | regime4h | TREND | 191 | +221,263 | 35% | 1.24 |
| v2_d1_tsmom | month_dir | DOWN | 70 | -26,310 | 24% | 0.93 |
| v2_d1_tsmom | month_dir | FLAT | 221 | -130,893 | 34% | 0.87 |
| v2_d1_tsmom | month_dir | UP | 84 | +65,047 | 38% | 1.18 |
| v2_d1_tsmom | month_vol | HIGH_VOL | 106 | -233,660 | 29% | 0.50 |
| v2_d1_tsmom | month_vol | LOW_VOL | 269 | +141,504 | 35% | 1.11 |
| v2_h4_ema | regime4h | HIGH_VOL | 76 | +71,678 | 42% | 1.63 |
| v2_h4_ema | regime4h | NEUTRAL | 356 | -61,508 | 33% | 0.91 |
| v2_h4_ema | regime4h | TREND | 474 | +20,437 | 34% | 1.02 |
| v2_h4_ema | month_dir | DOWN | 160 | +314,066 | 41% | 2.24 |
| v2_h4_ema | month_dir | FLAT | 620 | -442,739 | 31% | 0.62 |
| v2_h4_ema | month_dir | UP | 126 | +159,280 | 41% | 1.71 |
| v2_h4_ema | month_vol | HIGH_VOL | 283 | +167,735 | 40% | 1.37 |
| v2_h4_ema | month_vol | LOW_VOL | 623 | -137,128 | 31% | 0.89 |
| v2_trend_carry | regime4h | HIGH_VOL | 10 | +17,524 | 50% | 2.83 |
| v2_trend_carry | regime4h | NEUTRAL | 36 | +19,842 | 36% | 1.48 |
| v2_trend_carry | regime4h | RANGE | 34 | +116,263 | 44% | 3.73 |
| v2_trend_carry | regime4h | TREND | 79 | +84,126 | 35% | 1.75 |
| v2_trend_carry | month_dir | DOWN | 32 | +25,750 | 47% | 1.60 |
| v2_trend_carry | month_dir | FLAT | 96 | +198,707 | 34% | 2.56 |
| v2_trend_carry | month_dir | UP | 31 | +13,299 | 42% | 1.37 |
| v2_trend_carry | month_vol | HIGH_VOL | 35 | +6,010 | 40% | 1.15 |
| v2_trend_carry | month_vol | LOW_VOL | 124 | +231,745 | 38% | 2.41 |
| v2_xpair_strength | regime4h | HIGH_VOL | 33 | -4,677 | 48% | 0.89 |
| v2_xpair_strength | regime4h | NEUTRAL | 90 | -32,108 | 40% | 0.64 |
| v2_xpair_strength | regime4h | RANGE | 134 | +9,996 | 47% | 1.09 |
| v2_xpair_strength | regime4h | TREND | 220 | -43,794 | 42% | 0.81 |
| v2_xpair_strength | month_dir | DOWN | 93 | +26,132 | 51% | 1.31 |
| v2_xpair_strength | month_dir | FLAT | 271 | -121,280 | 38% | 0.58 |
| v2_xpair_strength | month_dir | UP | 113 | +24,566 | 51% | 1.23 |
| v2_xpair_strength | month_vol | HIGH_VOL | 123 | -37,958 | 40% | 0.74 |
| v2_xpair_strength | month_vol | LOW_VOL | 354 | -32,624 | 45% | 0.90 |
| v2_session_breakout | regime4h | HIGH_VOL | 260 | +30,949 | 35% | 1.04 |
| v2_session_breakout | regime4h | NEUTRAL | 801 | -117,432 | 33% | 0.94 |
| v2_session_breakout | regime4h | RANGE | 1364 | -33,080 | 34% | 0.99 |
| v2_session_breakout | regime4h | TREND | 1480 | -337,544 | 33% | 0.91 |
| v2_session_breakout | month_dir | DOWN | 773 | +403,175 | 39% | 1.22 |
| v2_session_breakout | month_dir | FLAT | 2284 | -1,267,158 | 30% | 0.79 |
| v2_session_breakout | month_dir | UP | 848 | +406,878 | 37% | 1.19 |
| v2_session_breakout | month_vol | HIGH_VOL | 1472 | -25,767 | 34% | 0.99 |
| v2_session_breakout | month_vol | LOW_VOL | 2433 | -431,339 | 33% | 0.93 |
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
| trend_ema_adx | regime4h | NEUTRAL | 998 | -126,437 | 33% | 0.92 |
| trend_ema_adx | regime4h | RANGE | 2216 | -97,709 | 31% | 0.97 |
| trend_ema_adx | regime4h | TREND | 792 | -232,236 | 29% | 0.82 |
| trend_ema_adx | month_dir | DOWN | 818 | +235,296 | 32% | 1.18 |
| trend_ema_adx | month_dir | FLAT | 2708 | -813,543 | 30% | 0.81 |
| trend_ema_adx | month_dir | UP | 754 | +33,727 | 34% | 1.03 |
| trend_ema_adx | month_vol | HIGH_VOL | 1453 | -429,876 | 31% | 0.82 |
| trend_ema_adx | month_vol | LOW_VOL | 2827 | -114,643 | 31% | 0.97 |
| trend_donchian | regime4h | HIGH_VOL | 214 | -69,802 | 22% | 0.87 |
| trend_donchian | regime4h | NEUTRAL | 722 | -734,824 | 20% | 0.60 |
| trend_donchian | regime4h | RANGE | 1140 | -76,343 | 26% | 0.97 |
| trend_donchian | regime4h | TREND | 821 | -34,463 | 26% | 0.98 |
| trend_donchian | month_dir | DOWN | 558 | +233,400 | 30% | 1.20 |
| trend_donchian | month_dir | FLAT | 1810 | -1,755,782 | 20% | 0.60 |
| trend_donchian | month_dir | UP | 529 | +606,950 | 31% | 1.56 |
| trend_donchian | month_vol | HIGH_VOL | 915 | -284,739 | 25% | 0.87 |
| trend_donchian | month_vol | LOW_VOL | 1982 | -630,692 | 24% | 0.86 |
| trend_tsmom | regime4h | HIGH_VOL | 86 | -11,139 | 36% | 0.94 |
| trend_tsmom | regime4h | NEUTRAL | 172 | -65,763 | 34% | 0.86 |
| trend_tsmom | regime4h | RANGE | 219 | +157,199 | 39% | 1.31 |
| trend_tsmom | regime4h | TREND | 585 | -136,170 | 33% | 0.91 |
| trend_tsmom | month_dir | DOWN | 246 | +322,721 | 48% | 1.63 |
| trend_tsmom | month_dir | FLAT | 582 | -918,255 | 23% | 0.49 |
| trend_tsmom | month_dir | UP | 234 | +539,659 | 50% | 2.16 |
| trend_tsmom | month_vol | HIGH_VOL | 383 | +86,012 | 36% | 1.09 |
| trend_tsmom | month_vol | LOW_VOL | 679 | -141,887 | 34% | 0.92 |
| mr_rsi_bb | regime4h | HIGH_VOL | 132 | -1,357 | 53% | 0.99 |
| mr_rsi_bb | regime4h | NEUTRAL | 541 | -33,821 | 48% | 0.95 |
| mr_rsi_bb | regime4h | RANGE | 1158 | -230,429 | 46% | 0.83 |
| mr_rsi_bb | regime4h | TREND | 853 | -109,761 | 48% | 0.89 |
| mr_rsi_bb | month_dir | DOWN | 556 | -125,291 | 47% | 0.81 |
| mr_rsi_bb | month_dir | FLAT | 1558 | -107,149 | 49% | 0.94 |
| mr_rsi_bb | month_dir | UP | 570 | -142,929 | 45% | 0.79 |
| mr_rsi_bb | month_vol | HIGH_VOL | 923 | -221,152 | 45% | 0.81 |
| mr_rsi_bb | month_vol | LOW_VOL | 1761 | -154,217 | 49% | 0.92 |
| mr_zscore | regime4h | HIGH_VOL | 335 | -55,352 | 42% | 0.85 |
| mr_zscore | regime4h | NEUTRAL | 628 | +29,591 | 47% | 1.05 |
| mr_zscore | regime4h | RANGE | 767 | -147,062 | 42% | 0.83 |
| mr_zscore | regime4h | TREND | 1550 | -58,302 | 42% | 0.97 |
| mr_zscore | month_dir | DOWN | 800 | -268,078 | 37% | 0.74 |
| mr_zscore | month_dir | FLAT | 1822 | +259,536 | 48% | 1.14 |
| mr_zscore | month_dir | UP | 658 | -222,583 | 37% | 0.71 |
| mr_zscore | month_vol | HIGH_VOL | 1202 | -138,232 | 41% | 0.90 |
| mr_zscore | month_vol | LOW_VOL | 2078 | -92,893 | 44% | 0.96 |
| regime_switch | regime4h | HIGH_VOL | 28 | -8,624 | 39% | 0.48 |
| regime_switch | regime4h | NEUTRAL | 126 | -51,343 | 33% | 0.65 |
| regime_switch | regime4h | RANGE | 2876 | -414,923 | 36% | 0.87 |
| regime_switch | regime4h | TREND | 1182 | -127,053 | 32% | 0.91 |
| regime_switch | month_dir | DOWN | 835 | +9,117 | 37% | 1.01 |
| regime_switch | month_dir | FLAT | 2532 | -510,758 | 34% | 0.82 |
| regime_switch | month_dir | UP | 845 | -100,302 | 34% | 0.89 |
| regime_switch | month_vol | HIGH_VOL | 1301 | +64,123 | 37% | 1.04 |
| regime_switch | month_vol | LOW_VOL | 2911 | -666,066 | 33% | 0.79 |
| mtf_pullback | regime4h | HIGH_VOL | 4 | +181 | 50% | 1.02 |
| mtf_pullback | regime4h | NEUTRAL | 145 | +22,905 | 50% | 1.09 |
| mtf_pullback | regime4h | RANGE | 214 | -167,613 | 38% | 0.63 |
| mtf_pullback | regime4h | TREND | 406 | -256,839 | 40% | 0.70 |
| mtf_pullback | month_dir | DOWN | 123 | -69,468 | 42% | 0.72 |
| mtf_pullback | month_dir | FLAT | 482 | -355,222 | 38% | 0.66 |
| mtf_pullback | month_dir | UP | 164 | +23,324 | 52% | 1.08 |
| mtf_pullback | month_vol | HIGH_VOL | 214 | -145,044 | 43% | 0.70 |
| mtf_pullback | month_vol | LOW_VOL | 555 | -256,322 | 41% | 0.76 |
| ml_logit | regime4h | HIGH_VOL | 1236 | +108,129 | 52% | 1.06 |
| ml_logit | regime4h | NEUTRAL | 949 | -76,963 | 49% | 0.95 |
| ml_logit | regime4h | RANGE | 1089 | +28,047 | 52% | 1.02 |
| ml_logit | regime4h | TREND | 2696 | -379,677 | 48% | 0.91 |
| ml_logit | month_dir | DOWN | 1569 | -260,914 | 48% | 0.90 |
| ml_logit | month_dir | FLAT | 3121 | -95,333 | 50% | 0.98 |
| ml_logit | month_dir | UP | 1280 | +35,782 | 51% | 1.02 |
| ml_logit | month_vol | HIGH_VOL | 2389 | +78,771 | 52% | 1.02 |
| ml_logit | month_vol | LOW_VOL | 3581 | -399,235 | 49% | 0.93 |
| ml_lgbm | regime4h | HIGH_VOL | 1960 | +52,005 | 52% | 1.03 |
| ml_lgbm | regime4h | NEUTRAL | 2923 | -418,492 | 48% | 0.87 |
| ml_lgbm | regime4h | RANGE | 4536 | -150,005 | 49% | 0.97 |
| ml_lgbm | regime4h | TREND | 6943 | -212,011 | 50% | 0.97 |
| ml_lgbm | month_dir | DOWN | 3780 | -185,580 | 49% | 0.96 |
| ml_lgbm | month_dir | FLAT | 9184 | -387,195 | 50% | 0.96 |
| ml_lgbm | month_dir | UP | 3398 | -155,729 | 50% | 0.96 |
| ml_lgbm | month_vol | HIGH_VOL | 6408 | +133,129 | 51% | 1.02 |
| ml_lgbm | month_vol | LOW_VOL | 9954 | -861,632 | 49% | 0.92 |

## 比較: session（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | session | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v2_session_breakout | all | 5304 | -2.9% | 1.00 | 0.05 | -0.15 | 0.27 | -42.6% |
| v2_session_breakout | london | 4190 | +22.1% | 1.02 | 0.16 | 0.02 | 0.44 | -40.9% |
| v2_session_breakout | london_ny | 3003 | -14.5% | 0.98 | -0.04 | -0.14 | -0.06 | -37.0% |
| v2_session_breakout | ny | 3753 | -4.4% | 1.00 | 0.03 | -0.08 | 0.00 | -37.2% |
| v2_session_breakout | tokyo | 3103 | -16.8% | 0.97 | -0.06 | -0.37 | 0.41 | -37.5% |
| v2_session_breakout | tokyo_london | 2271 | +22.8% | 1.04 | 0.18 | 0.15 | 0.42 | -26.9% |

## 比較: sizing（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | sizing | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v2_d1_donchian | fixed_notional | 251 | -42.9% | 0.80 | -0.17 | -0.21 | -0.31 | -55.5% |
| v2_d1_donchian | risk_stop | 259 | -0.4% | 1.02 | -0.01 | 0.03 | -0.39 | -16.7% |
| v2_d1_donchian | vol_target | 262 | -18.3% | 0.90 | -0.09 | -0.17 | -0.33 | -40.7% |
| v2_d1_tsmom | fixed_notional | 281 | -29.8% | 0.87 | -0.04 | -0.08 | -0.27 | -56.5% |
| v2_d1_tsmom | risk_stop | 276 | +6.0% | 1.17 | 0.12 | 0.14 | 0.00 | -13.0% |
| v2_d1_tsmom | vol_target | 283 | +10.4% | 1.07 | 0.10 | 0.08 | -0.12 | -42.2% |
| v2_trend_carry | risk_stop | 127 | +5.5% | 1.06 | 0.03 | 0.00 | 0.04 | -7.4% |
| v2_trend_carry | vol_target | 140 | +14.0% | 0.97 | 0.04 | 0.02 | 0.12 | -26.9% |
| v2_xpair_strength | fixed_notional | 436 | -28.6% | 0.88 | -0.09 | -0.13 | -0.27 | -52.5% |
| v2_xpair_strength | risk_stop | 372 | +0.4% | 1.01 | 0.02 | 0.03 | -0.42 | -8.5% |
| v2_xpair_strength | vol_target | 452 | -9.6% | 0.94 | -0.04 | -0.04 | -0.37 | -35.2% |

## 比較: regime（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | regime | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v2_d1_donchian | no_high_vol | 246 | -17.0% | 0.94 | -0.06 | -0.08 | -0.43 | -36.6% |
| v2_d1_donchian | none | 271 | -24.3% | 0.89 | -0.11 | -0.14 | -0.41 | -39.8% |
| v2_d1_donchian | trend_only | 256 | -20.2% | 0.91 | -0.09 | -0.12 | -0.19 | -36.4% |
| v2_h4_ema | no_high_vol | 970 | -7.1% | 0.94 | -0.12 | -0.12 | -0.32 | -17.4% |
| v2_h4_ema | none | 1097 | -1.7% | 0.97 | -0.05 | 0.02 | -0.35 | -16.9% |
| v2_h4_ema | trend_only | 903 | -0.5% | 0.97 | -0.03 | 0.04 | -0.40 | -16.0% |

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
USD     200     2026-09        -0.105             0.131            1.225
EUR     193     2026-01        -0.190             0.223            1.176
JPY     200     2026-08        -0.172             0.173            1.060
GBP     193     2026-01        -0.116             0.154            1.140
AUD     200     2026-08        -0.167             0.197            0.910
NZD     201     2026-09        -0.175             0.183            0.680
CAD     201     2026-09         0.051             0.084            0.422
CHF     201     2026-09         0.034             0.066            0.353
```

## データ品質: Dukascopy と米連銀 H.10 正午レートの突き合わせ（日次）

  pair  days  median_abs_diff_pct  p99_abs_diff_pct  max_abs_diff_pct  days_gt_0_5pct  days_gt_1pct  worst_day
USDJPY  4215               0.0220            0.2986             1.156               9             1 2013-06-06
EURUSD  4215               0.0256            0.3172             0.884               9             0 2011-10-07
GBPUSD  4215               0.0257            0.3175             1.817              11             1 2020-03-18
AUDUSD  4215               0.0304            0.3766             1.172              20             3 2020-03-12
NZDUSD  4215               0.0365            0.4003             1.450              23             2 2011-08-05
USDCAD  4215               0.0250            0.2944             0.895               9             0 2020-03-12
USDCHF  4215               0.0278            0.3100             1.041               8             1 2011-10-07
