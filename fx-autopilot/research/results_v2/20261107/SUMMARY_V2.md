# FX AUTOPILOT V2 研究結果（2026-11-07 03:03 UTC、データ〜2026-11-06 21:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v2.yaml`

> **検証汚染の申告**: 設計者は v1 の 2010〜2026 の結果（Stage1 WF 2014〜2021、TEST 2022〜2025-06、FORWARD 2025-07〜）を既に見ている。 V2 の候補選び（中期トレンド・キャリー・通貨強弱を優先したこと）はその知見の影響を受けている。 したがって V2 の Walk-Forward 成績は、どの年も「完全な未知データ」ではない（"汚染あり WF OOS" と表記する）。 V2 の最終判断は、LOCK 後に新しく到着する足での PAPER Forward のみで行う。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v2_trend_carry | CHALLENGER | 159 | +20.6% | +1.5% | 2.12 | 0.46 | 0.64 | -7.8% | 1,447 | 33 | 0.03 | 8 | 77% | 25% | +9.4% | +10.3% | 1.82 | 5 | 49% | 0.55 | 1 |  |
| v2_h4_ema | REJECTED | 902 | +3.7% | +0.3% | 1.02 | 0.09 | 0.13 | -13.4% | 40 | 83 | 0.44 | 16 | 46% | 44% | +7.7% | -3.7% | 0.91 | 2 | 76% | 0.12 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_d1_tsmom | REJECTED | 203 | -14.4% | -1.2% | 0.90 | -0.09 | -0.12 | -27.8% | -481 | 119 | 0.45 | 18 | 46% | 43% | -3.1% | -11.7% | 0.84 | 1 | 100% | 0.03 | 4 | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_xpair_strength | REJECTED | 333 | -3.7% | -0.3% | 0.88 | -0.16 | -0.23 | -9.3% | -107 | 31 | — | 13 | 38% | 50% | +0.8% | -4.5% | 0.79 | 1 | 100% | 0.02 | 2 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_session_breakout | REJECTED | 2638 | -32.6% | -3.0% | 0.95 | -0.24 | -0.37 | -46.6% | -133 | 132 | 3.72 | 22 | 38% | 37% | -37.9% | +8.4% | 0.85 | 2 | 100% | 0.01 | 4 | profit_factor, sharpe, positive_years, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_d1_donchian | REJECTED | 165 | -10.1% | -0.8% | 0.74 | -0.26 | -0.37 | -16.8% | -638 | 42 | — | 12 | 31% | 41% | -2.5% | -7.8% | 0.64 | 0 | 100% | 0.01 | 3 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_ml_d1_logit | REJECTED | 155 | -6.0% | -0.5% | 0.60 | -0.64 | -0.79 | -6.5% | -384 | 30 | — | 6 | 23% | 45% | -4.6% | -1.4% | 0.54 | 0 | 100% | 0.00 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, ml_not_better_than_simple |
| trend_tsmom | REFERENCE_V1 | 982 | -18.7% | -1.6% | 0.93 | -0.19 | -0.27 | -28.0% | -188 | 63 | — | 20 | 54% | 34% | -16.1% | -3.1% | 0.87 | 2 | 100% | 0.01 | 3 | reference_v1 |
| ml_logit | REFERENCE_V1 | 3224 | -17.6% | -1.5% | 0.96 | -0.20 | -0.28 | -19.5% | -63 | 127 | 1.68 | 12 | 31% | 41% | -15.9% | -1.9% | 0.86 | 2 | 79% | 0.01 | 2 | reference_v1 |
| mr_zscore | REFERENCE_V1 | 3275 | -35.3% | -3.3% | 0.94 | -0.35 | -0.49 | -50.5% | -70 | 59 | 9.13 | 17 | 31% | 59% | -42.9% | +13.3% | 0.85 | 2 | 100% | 0.00 | 2 | reference_v1 |
| trend_ema_adx | REFERENCE_V1 | 3694 | -50.3% | -5.3% | 0.91 | -0.43 | -0.66 | -55.3% | -142 | 115 | 19.24 | 28 | 15% | 55% | -32.3% | -26.5% | 0.81 | 1 | 100% | 0.00 | 4 | reference_v1 |
| trend_donchian | REFERENCE_V1 | 2410 | -73.2% | -9.7% | 0.82 | -0.64 | -0.92 | -76.0% | -406 | 93 | — | 27 | 23% | 64% | -56.2% | -38.8% | 0.74 | 1 | 100% | 0.00 | 3 | reference_v1 |
| ml_lgbm | REFERENCE_V1 | 14060 | -66.9% | -8.2% | 0.95 | -0.67 | -0.90 | -69.1% | -49 | 100 | 1.65 | 13 | 15% | 95% | -50.5% | -33.1% | 0.85 | 1 | 100% | 0.00 | 2 | reference_v1 |
| mr_rsi_bb | REFERENCE_V1 | 2681 | -47.8% | -4.9% | 0.88 | -0.76 | -1.03 | -49.0% | -139 | 93 | — | 9 | 8% | 100% | -26.4% | -29.1% | 0.79 | 1 | 100% | 0.00 | 1 | reference_v1 |
| regime_switch | REFERENCE_V1 | 3789 | -68.8% | -8.7% | 0.88 | -0.88 | -1.27 | -71.7% | -137 | 74 | — | 15 | 23% | 63% | -55.4% | -30.1% | 0.80 | 0 | 100% | 0.00 | 2 | reference_v1 |
| mtf_pullback | REFERENCE_V1 | 768 | -39.9% | -3.9% | 0.75 | -1.05 | -1.35 | -42.4% | -519 | 140 | — | 15 | 23% | 52% | -38.0% | -3.0% | 0.67 | 0 | 99% | 0.00 | 2 | reference_v1 |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v2_d1_donchian | REJECTED | 165 | — | — | -237,716 | 0.41 | — | -6.7% |
| v2_d1_tsmom | REJECTED | 203 | — | — | -559,086 | 0.40 | — | -13.6% |
| v2_h4_ema | REJECTED | 902 | 101% | 417% | -112,918 | 0.93 | -164% | -2.8% |
| v2_trend_carry | CHALLENGER | 159 | 54% | 114% | -32,051 | 0.84 | 12% | +1.7% |
| v2_xpair_strength | REJECTED | 333 | — | — | -97,204 | 0.69 | — | -2.6% |
| v2_session_breakout | REJECTED | 2638 | — | — | -575,981 | 0.91 | — | +2.3% |
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
| 2026.0 | -1.0% | -7.2% | -1.1% | +1.0% | -3.3% | -2.7% | +0.0% | -6.2% | -8.1% | -5.4% | -5.1% | -9.2% | -6.3% | +3.9% | -2.0% | -8.7% |

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
| 2021.0 | 0.83 | 11.88 | 0.82 | 167.09 | 0.31 | 0.79 | 1.43 | 0.87 | 0.82 | 1.15 | 0.94 | 0.97 | 0.85 | 0.54 | 2.32 | 0.90 |
| 2022.0 | 1.66 | 0.00 | 1.47 | 3.28 | 0.29 | 1.10 | — | 1.03 | 1.00 | 1.13 | 0.80 | 0.88 | 1.02 | 1.15 | 1.29 | 1.00 |
| 2023.0 | 0.20 | 0.09 | 0.61 | 1.48 | 0.46 | 1.01 | 0.22 | 0.87 | 0.75 | 1.15 | 0.83 | 1.37 | 0.96 | 0.61 | 1.21 | 0.95 |
| 2024.0 | 0.27 | 0.13 | 1.19 | 0.22 | 0.97 | 0.96 | 0.00 | 0.74 | 1.15 | 1.08 | 0.99 | 1.08 | 0.90 | 1.19 | 0.80 | 0.96 |
| 2025.0 | 0.72 | 2.74 | 0.74 | 0.50 | 2.03 | 1.25 | 0.24 | 0.95 | 0.46 | 0.70 | 0.71 | 1.16 | 0.64 | 0.80 | 0.88 | 0.88 |
| 2026.0 | 0.00 | 0.21 | 0.88 | 1.24 | 0.20 | 0.86 | — | 0.80 | 0.72 | 0.75 | 0.81 | 0.78 | 0.86 | 1.72 | 0.83 | 0.92 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v2_d1_donchian | AUDUSD | 38 | -36,736 | 0.64 | 29% | 61 | -10,090 |
| v2_d1_donchian | EURJPY | 26 | -4,906 | 0.90 | 38% | 42 | -2,062 |
| v2_d1_donchian | EURUSD | 33 | -14,740 | 0.82 | 27% | 28 | -10,868 |
| v2_d1_donchian | GBPUSD | 35 | -27,108 | 0.66 | 29% | 43 | -9,411 |
| v2_d1_donchian | USDJPY | 33 | -21,719 | 0.75 | 33% | 34 | -110 |
| v2_d1_tsmom | AUDUSD | 55 | -2,158 | 0.99 | 35% | 156 | -29,785 |
| v2_d1_tsmom | EURJPY | 36 | -118,885 | 0.35 | 22% | 141 | -7,498 |
| v2_d1_tsmom | EURUSD | 34 | +136,086 | 1.67 | 32% | 62 | -42,265 |
| v2_d1_tsmom | GBPUSD | 36 | -5,703 | 0.98 | 42% | 183 | -42,167 |
| v2_d1_tsmom | USDJPY | 42 | -106,998 | 0.36 | 24% | 44 | -5,401 |
| v2_h4_ema | AUDUSD | 158 | -6,868 | 0.98 | 35% | 122 | -8,446 |
| v2_h4_ema | EURJPY | 186 | -23,058 | 0.93 | 36% | 74 | -13,204 |
| v2_h4_ema | EURUSD | 188 | +7,567 | 1.02 | 31% | 69 | -13,873 |
| v2_h4_ema | GBPUSD | 179 | -489 | 1.00 | 33% | 92 | -10,835 |
| v2_h4_ema | USDJPY | 191 | +58,514 | 1.17 | 36% | 63 | -12,137 |
| v2_trend_carry | AUDUSD | 44 | +6,387 | 1.17 | 36% | 50 | -3,370 |
| v2_trend_carry | EURJPY | 25 | +12,170 | 1.31 | 36% | 27 | +2,606 |
| v2_trend_carry | EURUSD | 34 | +63,819 | 2.24 | 35% | 22 | +953 |
| v2_trend_carry | GBPUSD | 33 | +4,801 | 1.11 | 45% | 36 | -6,337 |
| v2_trend_carry | USDJPY | 23 | +142,872 | 5.15 | 39% | 21 | +34,059 |
| v2_xpair_strength | AUDUSD | 95 | -21,434 | 0.71 | 42% | 39 | -4,647 |
| v2_xpair_strength | EURJPY | 54 | -8,625 | 0.84 | 43% | 34 | -1,104 |
| v2_xpair_strength | EURUSD | 72 | -9,680 | 0.86 | 43% | 20 | -7,090 |
| v2_xpair_strength | GBPUSD | 60 | -5,199 | 0.91 | 45% | 34 | -6,094 |
| v2_xpair_strength | USDJPY | 52 | +9,318 | 1.18 | 44% | 22 | +2,163 |
| v2_session_breakout | AUDUSD | 519 | -292,209 | 0.78 | 32% | 185 | -23,234 |
| v2_session_breakout | EURJPY | 569 | -234,462 | 0.85 | 33% | 136 | -12,045 |
| v2_session_breakout | EURUSD | 540 | +110,032 | 1.09 | 35% | 95 | -30,321 |
| v2_session_breakout | GBPUSD | 505 | -115,740 | 0.91 | 32% | 140 | -29,617 |
| v2_session_breakout | USDJPY | 505 | +181,733 | 1.15 | 37% | 106 | -528 |
| v2_ml_d1_logit | AUDUSD | 15 | -2,070 | 0.85 | 60% | 40 | -701 |
| v2_ml_d1_logit | EURJPY | 27 | -8,416 | 0.70 | 44% | 33 | -777 |
| v2_ml_d1_logit | EURUSD | 33 | -21,065 | 0.41 | 33% | 22 | -2,001 |
| v2_ml_d1_logit | GBPUSD | 41 | -18,845 | 0.52 | 41% | 34 | -1,185 |
| v2_ml_d1_logit | USDJPY | 39 | -9,114 | 0.70 | 51% | 25 | -486 |
| trend_ema_adx | AUDUSD | 828 | -228,362 | 0.83 | 31% | 168 | -24,032 |
| trend_ema_adx | EURJPY | 802 | -140,122 | 0.90 | 30% | 113 | -29,256 |
| trend_ema_adx | EURUSD | 721 | -31,233 | 0.97 | 33% | 78 | -23,864 |
| trend_ema_adx | GBPUSD | 653 | -172,775 | 0.83 | 30% | 116 | -23,153 |
| trend_ema_adx | USDJPY | 690 | +46,281 | 1.04 | 32% | 93 | -21,919 |
| trend_donchian | AUDUSD | 540 | -521,496 | 0.57 | 23% | 133 | -30,049 |
| trend_donchian | EURJPY | 521 | -43,215 | 0.96 | 25% | 89 | -40,816 |
| trend_donchian | EURUSD | 441 | -219,093 | 0.75 | 23% | 62 | -31,387 |
| trend_donchian | GBPUSD | 442 | -251,515 | 0.74 | 24% | 95 | -39,574 |
| trend_donchian | USDJPY | 466 | +55,922 | 1.05 | 27% | 76 | -19,434 |
| trend_tsmom | AUDUSD | 185 | +975 | 1.00 | 38% | 95 | -15,696 |
| trend_tsmom | EURJPY | 189 | -108,330 | 0.77 | 34% | 56 | -9,502 |
| trend_tsmom | EURUSD | 207 | -41,712 | 0.93 | 35% | 52 | -25,129 |
| trend_tsmom | GBPUSD | 191 | +9,351 | 1.02 | 32% | 68 | -22,061 |
| trend_tsmom | USDJPY | 210 | -44,998 | 0.92 | 30% | 49 | -4,815 |
| mr_rsi_bb | AUDUSD | 449 | +1,048 | 1.00 | 51% | 138 | -3,940 |
| mr_rsi_bb | EURJPY | 501 | -78,254 | 0.87 | 48% | 89 | -7,441 |
| mr_rsi_bb | EURUSD | 561 | -33,545 | 0.94 | 49% | 67 | -7,957 |
| mr_rsi_bb | GBPUSD | 565 | -46,808 | 0.93 | 49% | 103 | -7,485 |
| mr_rsi_bb | USDJPY | 605 | -214,411 | 0.72 | 43% | 76 | -11,861 |
| mr_zscore | AUDUSD | 671 | -86,419 | 0.88 | 42% | 88 | -8,828 |
| mr_zscore | EURJPY | 662 | +28,742 | 1.04 | 46% | 53 | -11,224 |
| mr_zscore | EURUSD | 643 | +11,076 | 1.02 | 44% | 44 | -12,524 |
| mr_zscore | GBPUSD | 608 | -85,323 | 0.87 | 41% | 63 | -10,050 |
| mr_zscore | USDJPY | 691 | -97,176 | 0.88 | 41% | 46 | -15,262 |
| regime_switch | AUDUSD | 785 | -77,894 | 0.91 | 36% | 115 | -12,191 |
| regime_switch | EURJPY | 730 | -165,196 | 0.81 | 35% | 66 | -12,753 |
| regime_switch | EURUSD | 730 | -10,912 | 0.99 | 35% | 52 | -11,646 |
| regime_switch | GBPUSD | 716 | -63,412 | 0.92 | 36% | 77 | -12,283 |
| regime_switch | USDJPY | 828 | -202,609 | 0.79 | 32% | 61 | -13,304 |
| mtf_pullback | AUDUSD | 156 | -80,671 | 0.76 | 43% | 214 | -2,897 |
| mtf_pullback | EURJPY | 141 | -63,280 | 0.78 | 43% | 131 | -2,000 |
| mtf_pullback | EURUSD | 149 | -94,138 | 0.67 | 39% | 100 | -3,002 |
| mtf_pullback | GBPUSD | 166 | -146,206 | 0.61 | 37% | 155 | -2,957 |
| mtf_pullback | USDJPY | 156 | -14,510 | 0.95 | 46% | 96 | -604 |
| ml_logit | AUDUSD | 576 | +44,983 | 1.05 | 51% | 193 | -13,772 |
| ml_logit | EURJPY | 751 | +101,647 | 1.09 | 54% | 123 | -2,435 |
| ml_logit | EURUSD | 671 | -139,041 | 0.85 | 46% | 93 | -10,186 |
| ml_logit | GBPUSD | 366 | -140,379 | 0.75 | 45% | 134 | -4,134 |
| ml_logit | USDJPY | 860 | -71,734 | 0.95 | 50% | 111 | -7,587 |
| ml_lgbm | AUDUSD | 2834 | -375,965 | 0.88 | 48% | 158 | -28,046 |
| ml_lgbm | EURJPY | 2680 | -15,064 | 0.99 | 50% | 97 | -20,443 |
| ml_lgbm | EURUSD | 2869 | -187,065 | 0.93 | 49% | 66 | -37,567 |
| ml_lgbm | GBPUSD | 2489 | -230,368 | 0.91 | 49% | 109 | -21,817 |
| ml_lgbm | USDJPY | 3188 | +124,813 | 1.04 | 51% | 76 | -19,922 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v2_d1_donchian | regime4h | NEUTRAL | 39 | -42,862 | 33% | 0.48 |
| v2_d1_donchian | regime4h | RANGE | 28 | -24,701 | 29% | 0.68 |
| v2_d1_donchian | regime4h | TREND | 184 | -50,127 | 31% | 0.89 |
| v2_d1_donchian | month_dir | DOWN | 51 | +34,529 | 39% | 1.36 |
| v2_d1_donchian | month_dir | FLAT | 134 | -144,856 | 25% | 0.61 |
| v2_d1_donchian | month_dir | UP | 66 | -7,363 | 38% | 0.95 |
| v2_d1_donchian | month_vol | HIGH_VOL | 50 | -11,458 | 32% | 0.90 |
| v2_d1_donchian | month_vol | LOW_VOL | 201 | -106,233 | 31% | 0.78 |
| v2_d1_tsmom | regime4h | HIGH_VOL | 16 | -45,989 | 25% | 0.49 |
| v2_d1_tsmom | regime4h | NEUTRAL | 81 | -214,960 | 31% | 0.42 |
| v2_d1_tsmom | regime4h | RANGE | 87 | -89,324 | 32% | 0.77 |
| v2_d1_tsmom | regime4h | TREND | 191 | +238,146 | 34% | 1.25 |
| v2_d1_tsmom | month_dir | DOWN | 70 | -28,911 | 24% | 0.92 |
| v2_d1_tsmom | month_dir | FLAT | 221 | -127,854 | 33% | 0.88 |
| v2_d1_tsmom | month_dir | UP | 84 | +44,638 | 37% | 1.12 |
| v2_d1_tsmom | month_vol | HIGH_VOL | 106 | -250,104 | 29% | 0.47 |
| v2_d1_tsmom | month_vol | LOW_VOL | 269 | +137,978 | 34% | 1.11 |
| v2_h4_ema | regime4h | HIGH_VOL | 76 | +71,678 | 42% | 1.63 |
| v2_h4_ema | regime4h | NEUTRAL | 355 | -59,256 | 33% | 0.91 |
| v2_h4_ema | regime4h | TREND | 471 | +23,244 | 34% | 1.03 |
| v2_h4_ema | month_dir | DOWN | 160 | +314,066 | 41% | 2.24 |
| v2_h4_ema | month_dir | FLAT | 616 | -437,681 | 31% | 0.63 |
| v2_h4_ema | month_dir | UP | 126 | +159,280 | 41% | 1.71 |
| v2_h4_ema | month_vol | HIGH_VOL | 283 | +167,735 | 40% | 1.37 |
| v2_h4_ema | month_vol | LOW_VOL | 619 | -132,070 | 31% | 0.89 |
| v2_trend_carry | regime4h | HIGH_VOL | 10 | +17,524 | 50% | 2.83 |
| v2_trend_carry | regime4h | NEUTRAL | 36 | +19,842 | 36% | 1.48 |
| v2_trend_carry | regime4h | RANGE | 34 | +113,637 | 44% | 3.67 |
| v2_trend_carry | regime4h | TREND | 79 | +79,046 | 35% | 1.70 |
| v2_trend_carry | month_dir | DOWN | 32 | +22,710 | 47% | 1.53 |
| v2_trend_carry | month_dir | FLAT | 96 | +194,040 | 34% | 2.52 |
| v2_trend_carry | month_dir | UP | 31 | +13,299 | 42% | 1.37 |
| v2_trend_carry | month_vol | HIGH_VOL | 35 | +6,010 | 40% | 1.15 |
| v2_trend_carry | month_vol | LOW_VOL | 124 | +224,039 | 38% | 2.36 |
| v2_xpair_strength | regime4h | HIGH_VOL | 33 | -4,677 | 48% | 0.89 |
| v2_xpair_strength | regime4h | NEUTRAL | 90 | -34,605 | 40% | 0.61 |
| v2_xpair_strength | regime4h | RANGE | 134 | +9,996 | 47% | 1.09 |
| v2_xpair_strength | regime4h | TREND | 220 | -45,314 | 42% | 0.81 |
| v2_xpair_strength | month_dir | DOWN | 93 | +24,612 | 51% | 1.29 |
| v2_xpair_strength | month_dir | FLAT | 271 | -123,778 | 38% | 0.57 |
| v2_xpair_strength | month_dir | UP | 113 | +24,566 | 51% | 1.23 |
| v2_xpair_strength | month_vol | HIGH_VOL | 123 | -37,958 | 40% | 0.74 |
| v2_xpair_strength | month_vol | LOW_VOL | 354 | -36,642 | 45% | 0.89 |
| v2_session_breakout | regime4h | HIGH_VOL | 260 | +30,949 | 35% | 1.04 |
| v2_session_breakout | regime4h | NEUTRAL | 801 | -107,603 | 33% | 0.95 |
| v2_session_breakout | regime4h | RANGE | 1363 | -43,711 | 34% | 0.99 |
| v2_session_breakout | regime4h | TREND | 1478 | -332,960 | 33% | 0.91 |
| v2_session_breakout | month_dir | DOWN | 771 | +397,929 | 39% | 1.22 |
| v2_session_breakout | month_dir | FLAT | 2283 | -1,267,960 | 30% | 0.79 |
| v2_session_breakout | month_dir | UP | 848 | +416,707 | 37% | 1.20 |
| v2_session_breakout | month_vol | HIGH_VOL | 1471 | -26,568 | 34% | 0.99 |
| v2_session_breakout | month_vol | LOW_VOL | 2431 | -426,756 | 33% | 0.93 |
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
| trend_ema_adx | regime4h | NEUTRAL | 993 | -129,409 | 33% | 0.91 |
| trend_ema_adx | regime4h | RANGE | 2213 | -105,631 | 31% | 0.97 |
| trend_ema_adx | regime4h | TREND | 782 | -237,814 | 30% | 0.81 |
| trend_ema_adx | month_dir | DOWN | 818 | +235,296 | 32% | 1.18 |
| trend_ema_adx | month_dir | FLAT | 2690 | -830,015 | 30% | 0.80 |
| trend_ema_adx | month_dir | UP | 754 | +33,727 | 34% | 1.03 |
| trend_ema_adx | month_vol | HIGH_VOL | 1453 | -429,876 | 31% | 0.82 |
| trend_ema_adx | month_vol | LOW_VOL | 2809 | -131,116 | 32% | 0.97 |
| trend_donchian | regime4h | HIGH_VOL | 214 | -69,802 | 22% | 0.87 |
| trend_donchian | regime4h | NEUTRAL | 721 | -737,438 | 20% | 0.60 |
| trend_donchian | regime4h | RANGE | 1138 | -81,392 | 26% | 0.97 |
| trend_donchian | regime4h | TREND | 821 | -40,532 | 26% | 0.98 |
| trend_donchian | month_dir | DOWN | 558 | +227,332 | 30% | 1.19 |
| trend_donchian | month_dir | FLAT | 1807 | -1,757,377 | 20% | 0.60 |
| trend_donchian | month_dir | UP | 529 | +600,882 | 31% | 1.56 |
| trend_donchian | month_vol | HIGH_VOL | 914 | -293,422 | 25% | 0.86 |
| trend_donchian | month_vol | LOW_VOL | 1980 | -635,741 | 24% | 0.86 |
| trend_tsmom | regime4h | HIGH_VOL | 86 | -11,139 | 36% | 0.94 |
| trend_tsmom | regime4h | NEUTRAL | 172 | -65,763 | 34% | 0.86 |
| trend_tsmom | regime4h | RANGE | 219 | +157,199 | 39% | 1.31 |
| trend_tsmom | regime4h | TREND | 583 | -138,072 | 33% | 0.91 |
| trend_tsmom | month_dir | DOWN | 245 | +316,982 | 47% | 1.62 |
| trend_tsmom | month_dir | FLAT | 581 | -914,417 | 23% | 0.49 |
| trend_tsmom | month_dir | UP | 234 | +539,659 | 50% | 2.16 |
| trend_tsmom | month_vol | HIGH_VOL | 383 | +86,012 | 36% | 1.09 |
| trend_tsmom | month_vol | LOW_VOL | 677 | -143,789 | 34% | 0.92 |
| mr_rsi_bb | regime4h | HIGH_VOL | 132 | -1,357 | 53% | 0.99 |
| mr_rsi_bb | regime4h | NEUTRAL | 540 | -32,571 | 48% | 0.95 |
| mr_rsi_bb | regime4h | RANGE | 1157 | -230,066 | 46% | 0.83 |
| mr_rsi_bb | regime4h | TREND | 852 | -107,976 | 48% | 0.89 |
| mr_rsi_bb | month_dir | DOWN | 555 | -123,506 | 47% | 0.82 |
| mr_rsi_bb | month_dir | FLAT | 1556 | -105,535 | 49% | 0.94 |
| mr_rsi_bb | month_dir | UP | 570 | -142,929 | 45% | 0.79 |
| mr_rsi_bb | month_vol | HIGH_VOL | 923 | -221,152 | 45% | 0.81 |
| mr_rsi_bb | month_vol | LOW_VOL | 1758 | -150,818 | 49% | 0.92 |
| mr_zscore | regime4h | HIGH_VOL | 335 | -55,352 | 42% | 0.85 |
| mr_zscore | regime4h | NEUTRAL | 628 | +26,523 | 47% | 1.04 |
| mr_zscore | regime4h | RANGE | 766 | -145,528 | 42% | 0.83 |
| mr_zscore | regime4h | TREND | 1546 | -54,744 | 42% | 0.97 |
| mr_zscore | month_dir | DOWN | 799 | -267,025 | 37% | 0.74 |
| mr_zscore | month_dir | FLAT | 1818 | +260,508 | 48% | 1.14 |
| mr_zscore | month_dir | UP | 658 | -222,583 | 37% | 0.71 |
| mr_zscore | month_vol | HIGH_VOL | 1202 | -138,232 | 41% | 0.90 |
| mr_zscore | month_vol | LOW_VOL | 2073 | -90,869 | 44% | 0.96 |
| regime_switch | regime4h | HIGH_VOL | 28 | -8,624 | 39% | 0.48 |
| regime_switch | regime4h | NEUTRAL | 126 | -51,343 | 33% | 0.65 |
| regime_switch | regime4h | RANGE | 2871 | -412,382 | 36% | 0.87 |
| regime_switch | regime4h | TREND | 1180 | -128,289 | 32% | 0.91 |
| regime_switch | month_dir | DOWN | 834 | +7,952 | 37% | 1.01 |
| regime_switch | month_dir | FLAT | 2526 | -508,288 | 34% | 0.82 |
| regime_switch | month_dir | UP | 845 | -100,302 | 34% | 0.89 |
| regime_switch | month_vol | HIGH_VOL | 1301 | +64,123 | 37% | 1.04 |
| regime_switch | month_vol | LOW_VOL | 2904 | -664,761 | 33% | 0.80 |
| mtf_pullback | regime4h | HIGH_VOL | 4 | +181 | 50% | 1.02 |
| mtf_pullback | regime4h | NEUTRAL | 144 | +25,465 | 51% | 1.10 |
| mtf_pullback | regime4h | RANGE | 214 | -167,613 | 38% | 0.63 |
| mtf_pullback | regime4h | TREND | 406 | -256,839 | 40% | 0.70 |
| mtf_pullback | month_dir | DOWN | 123 | -69,468 | 42% | 0.72 |
| mtf_pullback | month_dir | FLAT | 481 | -352,661 | 38% | 0.66 |
| mtf_pullback | month_dir | UP | 164 | +23,324 | 52% | 1.08 |
| mtf_pullback | month_vol | HIGH_VOL | 214 | -145,044 | 43% | 0.70 |
| mtf_pullback | month_vol | LOW_VOL | 554 | -253,762 | 41% | 0.77 |
| ml_logit | regime4h | HIGH_VOL | 1236 | +108,129 | 52% | 1.06 |
| ml_logit | regime4h | NEUTRAL | 948 | -80,156 | 49% | 0.94 |
| ml_logit | regime4h | RANGE | 1089 | +28,047 | 52% | 1.02 |
| ml_logit | regime4h | TREND | 2695 | -383,175 | 48% | 0.91 |
| ml_logit | month_dir | DOWN | 1569 | -260,914 | 48% | 0.90 |
| ml_logit | month_dir | FLAT | 3119 | -102,024 | 50% | 0.98 |
| ml_logit | month_dir | UP | 1280 | +35,782 | 51% | 1.02 |
| ml_logit | month_vol | HIGH_VOL | 2389 | +78,771 | 52% | 1.02 |
| ml_logit | month_vol | LOW_VOL | 3579 | -405,926 | 49% | 0.93 |
| ml_lgbm | regime4h | HIGH_VOL | 1960 | +52,005 | 52% | 1.03 |
| ml_lgbm | regime4h | NEUTRAL | 2919 | -418,393 | 47% | 0.87 |
| ml_lgbm | regime4h | RANGE | 4535 | -151,356 | 49% | 0.97 |
| ml_lgbm | regime4h | TREND | 6928 | -206,669 | 50% | 0.97 |
| ml_lgbm | month_dir | DOWN | 3773 | -182,491 | 49% | 0.96 |
| ml_lgbm | month_dir | FLAT | 9171 | -386,192 | 50% | 0.96 |
| ml_lgbm | month_dir | UP | 3398 | -155,729 | 50% | 0.96 |
| ml_lgbm | month_vol | HIGH_VOL | 6408 | +133,129 | 51% | 1.02 |
| ml_lgbm | month_vol | LOW_VOL | 9934 | -857,542 | 49% | 0.92 |

## 比較: session（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | session | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v2_session_breakout | all | 5296 | -4.2% | 1.00 | 0.05 | -0.15 | 0.25 | -42.6% |
| v2_session_breakout | london | 4184 | +20.2% | 1.02 | 0.15 | 0.02 | 0.42 | -40.9% |
| v2_session_breakout | london_ny | 2999 | -14.7% | 0.98 | -0.05 | -0.14 | -0.07 | -37.0% |
| v2_session_breakout | ny | 3745 | -3.7% | 1.00 | 0.03 | -0.08 | 0.01 | -37.2% |
| v2_session_breakout | tokyo | 3100 | -16.0% | 0.98 | -0.05 | -0.37 | 0.43 | -37.5% |
| v2_session_breakout | tokyo_london | 2270 | +22.7% | 1.04 | 0.18 | 0.15 | 0.42 | -26.9% |

## 比較: sizing（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | sizing | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v2_d1_donchian | fixed_notional | 250 | -43.7% | 0.80 | -0.17 | -0.21 | -0.33 | -55.4% |
| v2_d1_donchian | risk_stop | 258 | -0.7% | 1.02 | -0.01 | 0.03 | -0.41 | -16.6% |
| v2_d1_donchian | vol_target | 260 | -19.3% | 0.90 | -0.10 | -0.17 | -0.36 | -40.5% |
| v2_d1_tsmom | fixed_notional | 280 | -31.1% | 0.86 | -0.05 | -0.08 | -0.29 | -56.5% |
| v2_d1_tsmom | risk_stop | 275 | +5.7% | 1.16 | 0.12 | 0.14 | -0.02 | -13.0% |
| v2_d1_tsmom | vol_target | 282 | +8.9% | 1.06 | 0.09 | 0.08 | -0.14 | -42.2% |
| v2_trend_carry | risk_stop | 127 | +5.1% | 1.04 | 0.02 | 0.00 | 0.01 | -7.4% |
| v2_trend_carry | vol_target | 140 | +12.1% | 0.95 | 0.03 | 0.02 | 0.09 | -26.9% |
| v2_xpair_strength | fixed_notional | 436 | -29.8% | 0.87 | -0.10 | -0.13 | -0.30 | -52.5% |
| v2_xpair_strength | risk_stop | 372 | +0.1% | 1.00 | 0.01 | 0.03 | -0.46 | -8.5% |
| v2_xpair_strength | vol_target | 452 | -11.0% | 0.94 | -0.05 | -0.04 | -0.42 | -35.2% |

## 比較: regime（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | regime | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v2_d1_donchian | no_high_vol | 244 | -17.8% | 0.93 | -0.07 | -0.08 | -0.45 | -36.5% |
| v2_d1_donchian | none | 270 | -25.0% | 0.88 | -0.12 | -0.14 | -0.43 | -39.7% |
| v2_d1_donchian | trend_only | 254 | -21.0% | 0.90 | -0.09 | -0.12 | -0.22 | -36.4% |
| v2_h4_ema | no_high_vol | 968 | -6.9% | 0.94 | -0.12 | -0.12 | -0.31 | -17.4% |
| v2_h4_ema | none | 1094 | -1.5% | 0.97 | -0.04 | 0.02 | -0.34 | -16.9% |
| v2_h4_ema | trend_only | 900 | -0.2% | 0.97 | -0.03 | 0.04 | -0.39 | -16.0% |

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
USDJPY  4210               0.0220            0.2986             1.156               9             1 2013-06-06
EURUSD  4210               0.0257            0.3173             0.884               9             0 2011-10-07
GBPUSD  4210               0.0258            0.3177             1.817              11             1 2020-03-18
AUDUSD  4210               0.0304            0.3767             1.172              20             3 2020-03-12
NZDUSD  4210               0.0365            0.4009             1.450              23             2 2011-08-05
USDCAD  4210               0.0251            0.2945             0.895               9             0 2020-03-12
USDCHF  4210               0.0279            0.3100             1.041               8             1 2011-10-07
