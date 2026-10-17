# FX AUTOPILOT V2 研究結果（2026-10-17 01:32 UTC、データ〜2026-10-16 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v2.yaml`

> **検証汚染の申告**: 設計者は v1 の 2010〜2026 の結果（Stage1 WF 2014〜2021、TEST 2022〜2025-06、FORWARD 2025-07〜）を既に見ている。 V2 の候補選び（中期トレンド・キャリー・通貨強弱を優先したこと）はその知見の影響を受けている。 したがって V2 の Walk-Forward 成績は、どの年も「完全な未知データ」ではない（"汚染あり WF OOS" と表記する）。 V2 の最終判断は、LOCK 後に新しく到着する足での PAPER Forward のみで行う。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v2_trend_carry | CHALLENGER | 157 | +20.1% | +1.4% | 2.10 | 0.45 | 0.63 | -7.8% | 1,434 | 32 | 0.03 | 8 | 77% | 26% | +9.4% | +9.8% | 1.80 | 5 | 50% | 0.55 | 1 |  |
| v2_h4_ema | REJECTED | 896 | +4.9% | +0.4% | 1.03 | 0.11 | 0.17 | -13.4% | 54 | 82 | 0.41 | 16 | 54% | 43% | +7.7% | -2.6% | 0.92 | 2 | 70% | 0.14 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_d1_tsmom | REJECTED | 201 | -14.3% | -1.2% | 0.90 | -0.09 | -0.12 | -27.8% | -479 | 119 | 0.44 | 18 | 46% | 43% | -3.1% | -11.6% | 0.84 | 2 | 100% | 0.03 | 4 | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_xpair_strength | REJECTED | 332 | -4.1% | -0.3% | 0.87 | -0.18 | -0.25 | -9.2% | -118 | 30 | — | 13 | 38% | 50% | +0.8% | -4.8% | 0.78 | 1 | 100% | 0.02 | 2 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_session_breakout | REJECTED | 2634 | -33.1% | -3.1% | 0.95 | -0.25 | -0.38 | -46.6% | -136 | 132 | 4.11 | 22 | 38% | 37% | -37.9% | +7.7% | 0.86 | 2 | 100% | 0.01 | 4 | profit_factor, sharpe, positive_years, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_d1_donchian | REJECTED | 164 | -10.0% | -0.8% | 0.74 | -0.26 | -0.37 | -16.8% | -640 | 42 | — | 12 | 31% | 41% | -2.5% | -7.7% | 0.65 | 0 | 100% | 0.01 | 3 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_ml_d1_logit | REJECTED | 155 | -6.0% | -0.5% | 0.60 | -0.64 | -0.79 | -6.5% | -384 | 30 | — | 6 | 23% | 45% | -4.6% | -1.4% | 0.54 | 0 | 100% | 0.00 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, ml_not_better_than_simple |
| trend_tsmom | REFERENCE_V1 | 978 | -17.8% | -1.5% | 0.93 | -0.18 | -0.26 | -28.0% | -179 | 63 | — | 20 | 54% | 34% | -16.1% | -2.0% | 0.88 | 2 | 100% | 0.02 | 3 | reference_v1 |
| ml_logit | REFERENCE_V1 | 3224 | -17.6% | -1.5% | 0.96 | -0.20 | -0.28 | -19.5% | -63 | 127 | 1.68 | 12 | 31% | 41% | -15.9% | -1.9% | 0.86 | 2 | 79% | 0.01 | 2 | reference_v1 |
| mr_zscore | REFERENCE_V1 | 3257 | -35.1% | -3.3% | 0.94 | -0.35 | -0.48 | -50.5% | -70 | 59 | 9.06 | 17 | 31% | 59% | -42.9% | +13.7% | 0.85 | 2 | 100% | 0.00 | 2 | reference_v1 |
| trend_ema_adx | REFERENCE_V1 | 3682 | -50.2% | -5.3% | 0.91 | -0.43 | -0.66 | -55.3% | -143 | 115 | 20.80 | 28 | 15% | 55% | -32.3% | -26.5% | 0.81 | 1 | 100% | 0.00 | 4 | reference_v1 |
| trend_donchian | REFERENCE_V1 | 2398 | -72.3% | -9.6% | 0.82 | -0.62 | -0.90 | -76.0% | -402 | 93 | — | 27 | 23% | 64% | -56.2% | -36.8% | 0.74 | 1 | 100% | 0.00 | 3 | reference_v1 |
| ml_lgbm | REFERENCE_V1 | 14025 | -65.4% | -8.0% | 0.95 | -0.64 | -0.87 | -68.4% | -48 | 100 | 1.63 | 13 | 15% | 95% | -50.5% | -30.2% | 0.85 | 1 | 100% | 0.00 | 2 | reference_v1 |
| mr_rsi_bb | REFERENCE_V1 | 2671 | -46.4% | -4.8% | 0.88 | -0.73 | -0.99 | -49.0% | -135 | 93 | — | 9 | 8% | 100% | -26.4% | -27.1% | 0.79 | 1 | 100% | 0.00 | 1 | reference_v1 |
| regime_switch | REFERENCE_V1 | 3774 | -67.8% | -8.5% | 0.88 | -0.86 | -1.24 | -71.6% | -136 | 75 | — | 15 | 23% | 63% | -55.4% | -27.9% | 0.80 | 0 | 100% | 0.00 | 2 | reference_v1 |
| mtf_pullback | REFERENCE_V1 | 767 | -40.2% | -3.9% | 0.74 | -1.07 | -1.37 | -42.4% | -525 | 140 | — | 15 | 23% | 49% | -38.0% | -3.4% | 0.67 | 0 | 99% | 0.00 | 2 | reference_v1 |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v2_d1_donchian | REJECTED | 164 | — | — | -237,498 | 0.41 | — | -6.7% |
| v2_d1_tsmom | REJECTED | 201 | — | — | -569,419 | 0.39 | — | -13.6% |
| v2_h4_ema | REJECTED | 896 | 74% | 307% | -100,214 | 0.94 | -120% | -1.7% |
| v2_trend_carry | CHALLENGER | 157 | 55% | 116% | -35,701 | 0.83 | 12% | +1.3% |
| v2_xpair_strength | REJECTED | 332 | — | — | -100,844 | 0.68 | — | -2.9% |
| v2_session_breakout | REJECTED | 2634 | — | — | -584,093 | 0.91 | — | +1.6% |
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
| 2026.0 | -1.0% | -7.1% | +0.1% | +0.6% | -3.6% | -3.4% | +0.0% | -6.2% | -5.2% | -4.4% | -2.5% | -8.8% | -3.3% | +3.4% | -2.0% | -4.7% |

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
| 2021.0 | 0.83 | 11.88 | 0.82 | 165.79 | 0.31 | 0.79 | 1.43 | 0.87 | 0.82 | 1.15 | 0.94 | 0.97 | 0.85 | 0.54 | 2.32 | 0.90 |
| 2022.0 | 1.66 | 0.00 | 1.47 | 3.28 | 0.29 | 1.10 | — | 1.03 | 1.00 | 1.13 | 0.80 | 0.88 | 1.02 | 1.15 | 1.29 | 1.00 |
| 2023.0 | 0.20 | 0.09 | 0.61 | 1.48 | 0.46 | 1.01 | 0.22 | 0.87 | 0.75 | 1.15 | 0.83 | 1.37 | 0.96 | 0.61 | 1.21 | 0.95 |
| 2024.0 | 0.27 | 0.13 | 1.19 | 0.22 | 0.97 | 0.96 | 0.00 | 0.74 | 1.15 | 1.08 | 0.99 | 1.08 | 0.90 | 1.19 | 0.80 | 0.96 |
| 2025.0 | 0.72 | 2.96 | 0.74 | 0.50 | 2.03 | 1.25 | 0.24 | 0.95 | 0.46 | 0.70 | 0.71 | 1.16 | 0.64 | 0.80 | 0.88 | 0.88 |
| 2026.0 | 0.00 | 0.07 | 1.01 | 0.91 | 0.13 | 0.82 | — | 0.80 | 0.80 | 0.79 | 0.90 | 0.76 | 0.92 | 1.63 | 0.83 | 0.96 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v2_d1_donchian | AUDUSD | 37 | -36,518 | 0.64 | 30% | 62 | -10,084 |
| v2_d1_donchian | EURJPY | 26 | -4,906 | 0.90 | 38% | 42 | -2,062 |
| v2_d1_donchian | EURUSD | 33 | -14,740 | 0.82 | 27% | 28 | -10,868 |
| v2_d1_donchian | GBPUSD | 35 | -27,108 | 0.66 | 29% | 43 | -9,411 |
| v2_d1_donchian | USDJPY | 33 | -21,719 | 0.75 | 33% | 34 | -110 |
| v2_d1_tsmom | AUDUSD | 55 | +9,856 | 1.07 | 35% | 156 | -29,253 |
| v2_d1_tsmom | EURJPY | 35 | -124,619 | 0.32 | 20% | 141 | -7,147 |
| v2_d1_tsmom | EURUSD | 34 | +125,180 | 1.61 | 29% | 62 | -42,668 |
| v2_d1_tsmom | GBPUSD | 36 | -777 | 1.00 | 42% | 181 | -42,119 |
| v2_d1_tsmom | USDJPY | 41 | -105,835 | 0.36 | 24% | 45 | -5,677 |
| v2_h4_ema | AUDUSD | 156 | -1,344 | 1.00 | 35% | 122 | -8,241 |
| v2_h4_ema | EURJPY | 185 | -22,260 | 0.94 | 36% | 74 | -13,233 |
| v2_h4_ema | EURUSD | 186 | +11,012 | 1.03 | 32% | 69 | -13,831 |
| v2_h4_ema | GBPUSD | 179 | -489 | 1.00 | 33% | 92 | -10,835 |
| v2_h4_ema | USDJPY | 190 | +61,451 | 1.18 | 36% | 63 | -12,049 |
| v2_trend_carry | AUDUSD | 42 | +4,319 | 1.12 | 36% | 48 | -3,299 |
| v2_trend_carry | EURJPY | 25 | +12,170 | 1.31 | 36% | 27 | +2,606 |
| v2_trend_carry | EURUSD | 34 | +62,238 | 2.21 | 35% | 22 | +895 |
| v2_trend_carry | GBPUSD | 33 | +4,801 | 1.11 | 45% | 36 | -6,337 |
| v2_trend_carry | USDJPY | 23 | +141,689 | 5.12 | 39% | 21 | +33,710 |
| v2_xpair_strength | AUDUSD | 94 | -22,911 | 0.69 | 41% | 40 | -4,630 |
| v2_xpair_strength | EURJPY | 54 | -9,231 | 0.83 | 41% | 32 | -874 |
| v2_xpair_strength | EURUSD | 72 | -11,238 | 0.84 | 42% | 20 | -7,147 |
| v2_xpair_strength | GBPUSD | 60 | -5,199 | 0.91 | 45% | 34 | -6,094 |
| v2_xpair_strength | USDJPY | 52 | +9,318 | 1.18 | 44% | 22 | +2,163 |
| v2_session_breakout | AUDUSD | 518 | -286,023 | 0.78 | 32% | 184 | -23,234 |
| v2_session_breakout | EURJPY | 569 | -234,471 | 0.85 | 33% | 136 | -12,045 |
| v2_session_breakout | EURUSD | 538 | +106,235 | 1.09 | 35% | 95 | -30,388 |
| v2_session_breakout | GBPUSD | 504 | -126,232 | 0.91 | 32% | 140 | -29,552 |
| v2_session_breakout | USDJPY | 505 | +181,733 | 1.15 | 37% | 106 | -528 |
| v2_ml_d1_logit | AUDUSD | 15 | -2,070 | 0.85 | 60% | 40 | -701 |
| v2_ml_d1_logit | EURJPY | 27 | -8,416 | 0.70 | 44% | 33 | -777 |
| v2_ml_d1_logit | EURUSD | 33 | -21,065 | 0.41 | 33% | 22 | -2,001 |
| v2_ml_d1_logit | GBPUSD | 41 | -18,845 | 0.52 | 41% | 34 | -1,185 |
| v2_ml_d1_logit | USDJPY | 39 | -9,114 | 0.70 | 51% | 25 | -486 |
| trend_ema_adx | AUDUSD | 826 | -231,688 | 0.83 | 31% | 167 | -23,853 |
| trend_ema_adx | EURJPY | 799 | -139,525 | 0.90 | 30% | 113 | -29,232 |
| trend_ema_adx | EURUSD | 718 | -33,575 | 0.96 | 33% | 78 | -23,575 |
| trend_ema_adx | GBPUSD | 652 | -170,625 | 0.83 | 31% | 116 | -23,153 |
| trend_ema_adx | USDJPY | 687 | +49,632 | 1.05 | 32% | 93 | -22,094 |
| trend_donchian | AUDUSD | 535 | -519,260 | 0.57 | 23% | 133 | -29,930 |
| trend_donchian | EURJPY | 519 | -38,846 | 0.97 | 25% | 89 | -40,500 |
| trend_donchian | EURUSD | 441 | -219,093 | 0.75 | 23% | 62 | -31,387 |
| trend_donchian | GBPUSD | 439 | -245,084 | 0.75 | 24% | 95 | -39,444 |
| trend_donchian | USDJPY | 464 | +58,591 | 1.06 | 27% | 76 | -19,462 |
| trend_tsmom | AUDUSD | 184 | +7,272 | 1.02 | 39% | 95 | -15,681 |
| trend_tsmom | EURJPY | 188 | -109,146 | 0.77 | 34% | 57 | -9,066 |
| trend_tsmom | EURUSD | 206 | -41,341 | 0.93 | 35% | 53 | -25,238 |
| trend_tsmom | GBPUSD | 190 | +13,372 | 1.03 | 33% | 67 | -21,995 |
| trend_tsmom | USDJPY | 210 | -44,998 | 0.92 | 30% | 49 | -4,815 |
| mr_rsi_bb | AUDUSD | 449 | +1,048 | 1.00 | 51% | 138 | -3,940 |
| mr_rsi_bb | EURJPY | 499 | -75,284 | 0.87 | 48% | 89 | -7,441 |
| mr_rsi_bb | EURUSD | 558 | -33,019 | 0.94 | 49% | 68 | -7,945 |
| mr_rsi_bb | GBPUSD | 563 | -43,876 | 0.93 | 49% | 103 | -7,450 |
| mr_rsi_bb | USDJPY | 602 | -209,880 | 0.73 | 43% | 76 | -11,861 |
| mr_zscore | AUDUSD | 668 | -87,363 | 0.88 | 42% | 88 | -8,789 |
| mr_zscore | EURJPY | 658 | +29,986 | 1.04 | 46% | 53 | -11,078 |
| mr_zscore | EURUSD | 639 | +9,905 | 1.02 | 44% | 44 | -12,440 |
| mr_zscore | GBPUSD | 603 | -78,733 | 0.88 | 41% | 63 | -9,810 |
| mr_zscore | USDJPY | 689 | -101,175 | 0.88 | 41% | 46 | -15,208 |
| regime_switch | AUDUSD | 784 | -76,972 | 0.91 | 36% | 115 | -12,191 |
| regime_switch | EURJPY | 727 | -162,291 | 0.81 | 35% | 66 | -12,758 |
| regime_switch | EURUSD | 726 | -8,129 | 0.99 | 35% | 52 | -11,621 |
| regime_switch | GBPUSD | 714 | -62,648 | 0.92 | 36% | 77 | -12,267 |
| regime_switch | USDJPY | 823 | -202,385 | 0.79 | 32% | 61 | -13,250 |
| mtf_pullback | AUDUSD | 156 | -80,671 | 0.76 | 43% | 214 | -2,897 |
| mtf_pullback | EURJPY | 141 | -63,280 | 0.78 | 43% | 131 | -2,000 |
| mtf_pullback | EURUSD | 149 | -94,138 | 0.67 | 39% | 100 | -3,002 |
| mtf_pullback | GBPUSD | 166 | -146,206 | 0.61 | 37% | 155 | -2,957 |
| mtf_pullback | USDJPY | 155 | -18,308 | 0.93 | 46% | 96 | -604 |
| ml_logit | AUDUSD | 576 | +44,983 | 1.05 | 51% | 193 | -13,772 |
| ml_logit | EURJPY | 751 | +101,647 | 1.09 | 54% | 123 | -2,435 |
| ml_logit | EURUSD | 671 | -139,041 | 0.85 | 46% | 93 | -10,186 |
| ml_logit | GBPUSD | 366 | -140,379 | 0.75 | 45% | 134 | -4,134 |
| ml_logit | USDJPY | 860 | -71,734 | 0.95 | 50% | 111 | -7,587 |
| ml_lgbm | AUDUSD | 2827 | -367,425 | 0.88 | 48% | 158 | -28,010 |
| ml_lgbm | EURJPY | 2669 | -10,519 | 1.00 | 50% | 97 | -20,501 |
| ml_lgbm | EURUSD | 2864 | -185,137 | 0.93 | 50% | 66 | -37,529 |
| ml_lgbm | GBPUSD | 2480 | -228,229 | 0.91 | 49% | 109 | -21,793 |
| ml_lgbm | USDJPY | 3185 | +122,235 | 1.04 | 51% | 76 | -19,922 |

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
| v2_d1_tsmom | regime4h | NEUTRAL | 79 | -241,699 | 27% | 0.36 |
| v2_d1_tsmom | regime4h | RANGE | 85 | -17,073 | 34% | 0.95 |
| v2_d1_tsmom | regime4h | TREND | 189 | +196,221 | 33% | 1.21 |
| v2_d1_tsmom | month_dir | DOWN | 69 | -30,780 | 23% | 0.92 |
| v2_d1_tsmom | month_dir | FLAT | 217 | -183,891 | 32% | 0.83 |
| v2_d1_tsmom | month_dir | UP | 83 | +106,131 | 37% | 1.30 |
| v2_d1_tsmom | month_vol | HIGH_VOL | 105 | -266,744 | 28% | 0.44 |
| v2_d1_tsmom | month_vol | LOW_VOL | 264 | +158,203 | 33% | 1.12 |
| v2_h4_ema | regime4h | HIGH_VOL | 76 | +71,678 | 42% | 1.63 |
| v2_h4_ema | regime4h | NEUTRAL | 351 | -53,333 | 33% | 0.92 |
| v2_h4_ema | regime4h | TREND | 469 | +30,024 | 34% | 1.03 |
| v2_h4_ema | month_dir | DOWN | 159 | +317,449 | 42% | 2.27 |
| v2_h4_ema | month_dir | FLAT | 611 | -428,360 | 31% | 0.63 |
| v2_h4_ema | month_dir | UP | 126 | +159,280 | 41% | 1.71 |
| v2_h4_ema | month_vol | HIGH_VOL | 283 | +167,735 | 40% | 1.37 |
| v2_h4_ema | month_vol | LOW_VOL | 613 | -119,366 | 32% | 0.90 |
| v2_trend_carry | regime4h | HIGH_VOL | 10 | +17,524 | 50% | 2.83 |
| v2_trend_carry | regime4h | NEUTRAL | 36 | +19,842 | 36% | 1.48 |
| v2_trend_carry | regime4h | RANGE | 33 | +113,339 | 45% | 3.72 |
| v2_trend_carry | regime4h | TREND | 78 | +74,511 | 35% | 1.66 |
| v2_trend_carry | month_dir | DOWN | 31 | +19,757 | 45% | 1.46 |
| v2_trend_carry | month_dir | FLAT | 95 | +192,161 | 35% | 2.52 |
| v2_trend_carry | month_dir | UP | 31 | +13,299 | 42% | 1.37 |
| v2_trend_carry | month_vol | HIGH_VOL | 35 | +6,010 | 40% | 1.15 |
| v2_trend_carry | month_vol | LOW_VOL | 122 | +219,206 | 38% | 2.34 |
| v2_xpair_strength | regime4h | HIGH_VOL | 33 | -4,677 | 48% | 0.89 |
| v2_xpair_strength | regime4h | NEUTRAL | 90 | -36,769 | 38% | 0.59 |
| v2_xpair_strength | regime4h | RANGE | 134 | +9,996 | 47% | 1.09 |
| v2_xpair_strength | regime4h | TREND | 219 | -46,791 | 42% | 0.80 |
| v2_xpair_strength | month_dir | DOWN | 92 | +23,136 | 50% | 1.28 |
| v2_xpair_strength | month_dir | FLAT | 271 | -125,942 | 37% | 0.56 |
| v2_xpair_strength | month_dir | UP | 113 | +24,566 | 51% | 1.23 |
| v2_xpair_strength | month_vol | HIGH_VOL | 123 | -37,958 | 40% | 0.74 |
| v2_xpair_strength | month_vol | LOW_VOL | 353 | -40,282 | 44% | 0.88 |
| v2_session_breakout | regime4h | HIGH_VOL | 260 | +30,949 | 35% | 1.04 |
| v2_session_breakout | regime4h | NEUTRAL | 797 | -128,732 | 33% | 0.94 |
| v2_session_breakout | regime4h | RANGE | 1358 | -48,622 | 34% | 0.99 |
| v2_session_breakout | regime4h | TREND | 1475 | -342,440 | 33% | 0.91 |
| v2_session_breakout | month_dir | DOWN | 769 | +393,639 | 39% | 1.21 |
| v2_session_breakout | month_dir | FLAT | 2275 | -1,300,200 | 30% | 0.79 |
| v2_session_breakout | month_dir | UP | 846 | +417,716 | 37% | 1.20 |
| v2_session_breakout | month_vol | HIGH_VOL | 1468 | -24,186 | 34% | 0.99 |
| v2_session_breakout | month_vol | LOW_VOL | 2422 | -464,658 | 33% | 0.92 |
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
| trend_ema_adx | regime4h | NEUTRAL | 986 | -141,206 | 33% | 0.91 |
| trend_ema_adx | regime4h | RANGE | 2186 | -102,705 | 31% | 0.97 |
| trend_ema_adx | regime4h | TREND | 780 | -233,975 | 30% | 0.82 |
| trend_ema_adx | month_dir | DOWN | 816 | +238,387 | 32% | 1.19 |
| trend_ema_adx | month_dir | FLAT | 2658 | -832,412 | 30% | 0.80 |
| trend_ema_adx | month_dir | UP | 752 | +28,001 | 34% | 1.02 |
| trend_ema_adx | month_vol | HIGH_VOL | 1453 | -429,876 | 31% | 0.82 |
| trend_ema_adx | month_vol | LOW_VOL | 2773 | -136,148 | 31% | 0.97 |
| trend_donchian | regime4h | HIGH_VOL | 205 | -53,631 | 23% | 0.90 |
| trend_donchian | regime4h | NEUTRAL | 714 | -733,352 | 20% | 0.60 |
| trend_donchian | regime4h | RANGE | 1127 | -120,019 | 25% | 0.95 |
| trend_donchian | regime4h | TREND | 812 | -54,115 | 26% | 0.97 |
| trend_donchian | month_dir | DOWN | 549 | +233,766 | 30% | 1.20 |
| trend_donchian | month_dir | FLAT | 1781 | -1,791,055 | 20% | 0.59 |
| trend_donchian | month_dir | UP | 528 | +596,173 | 31% | 1.55 |
| trend_donchian | month_vol | HIGH_VOL | 902 | -277,718 | 25% | 0.87 |
| trend_donchian | month_vol | LOW_VOL | 1956 | -683,399 | 24% | 0.85 |
| trend_tsmom | regime4h | HIGH_VOL | 86 | -11,139 | 36% | 0.94 |
| trend_tsmom | regime4h | NEUTRAL | 171 | -61,743 | 34% | 0.87 |
| trend_tsmom | regime4h | RANGE | 216 | +161,151 | 39% | 1.32 |
| trend_tsmom | regime4h | TREND | 583 | -136,172 | 33% | 0.91 |
| trend_tsmom | month_dir | DOWN | 244 | +321,378 | 48% | 1.64 |
| trend_tsmom | month_dir | FLAT | 578 | -908,940 | 23% | 0.49 |
| trend_tsmom | month_dir | UP | 234 | +539,659 | 50% | 2.16 |
| trend_tsmom | month_vol | HIGH_VOL | 383 | +86,012 | 36% | 1.09 |
| trend_tsmom | month_vol | LOW_VOL | 673 | -133,915 | 34% | 0.93 |
| mr_rsi_bb | regime4h | HIGH_VOL | 132 | -1,357 | 53% | 0.99 |
| mr_rsi_bb | regime4h | NEUTRAL | 537 | -28,289 | 49% | 0.95 |
| mr_rsi_bb | regime4h | RANGE | 1150 | -223,388 | 47% | 0.83 |
| mr_rsi_bb | regime4h | TREND | 852 | -107,976 | 48% | 0.89 |
| mr_rsi_bb | month_dir | DOWN | 555 | -123,506 | 47% | 0.82 |
| mr_rsi_bb | month_dir | FLAT | 1546 | -94,575 | 49% | 0.94 |
| mr_rsi_bb | month_dir | UP | 570 | -142,929 | 45% | 0.79 |
| mr_rsi_bb | month_vol | HIGH_VOL | 923 | -221,152 | 45% | 0.81 |
| mr_rsi_bb | month_vol | LOW_VOL | 1748 | -139,857 | 49% | 0.93 |
| mr_zscore | regime4h | HIGH_VOL | 335 | -55,352 | 42% | 0.85 |
| mr_zscore | regime4h | NEUTRAL | 622 | +24,779 | 46% | 1.04 |
| mr_zscore | regime4h | RANGE | 758 | -140,052 | 42% | 0.84 |
| mr_zscore | regime4h | TREND | 1542 | -56,756 | 42% | 0.97 |
| mr_zscore | month_dir | DOWN | 797 | -267,098 | 37% | 0.74 |
| mr_zscore | month_dir | FLAT | 1802 | +262,301 | 48% | 1.14 |
| mr_zscore | month_dir | UP | 658 | -222,583 | 37% | 0.71 |
| mr_zscore | month_vol | HIGH_VOL | 1202 | -138,232 | 41% | 0.90 |
| mr_zscore | month_vol | LOW_VOL | 2055 | -89,149 | 44% | 0.96 |
| regime_switch | regime4h | HIGH_VOL | 28 | -8,624 | 39% | 0.48 |
| regime_switch | regime4h | NEUTRAL | 126 | -51,343 | 33% | 0.65 |
| regime_switch | regime4h | RANGE | 2858 | -406,599 | 36% | 0.87 |
| regime_switch | regime4h | TREND | 1178 | -126,474 | 32% | 0.91 |
| regime_switch | month_dir | DOWN | 833 | +8,874 | 37% | 1.01 |
| regime_switch | month_dir | FLAT | 2512 | -501,612 | 34% | 0.82 |
| regime_switch | month_dir | UP | 845 | -100,302 | 34% | 0.89 |
| regime_switch | month_vol | HIGH_VOL | 1301 | +64,123 | 37% | 1.04 |
| regime_switch | month_vol | LOW_VOL | 2889 | -657,163 | 33% | 0.80 |
| mtf_pullback | regime4h | HIGH_VOL | 4 | +181 | 50% | 1.02 |
| mtf_pullback | regime4h | NEUTRAL | 144 | +25,465 | 51% | 1.10 |
| mtf_pullback | regime4h | RANGE | 213 | -171,411 | 38% | 0.63 |
| mtf_pullback | regime4h | TREND | 406 | -256,839 | 40% | 0.70 |
| mtf_pullback | month_dir | DOWN | 123 | -69,468 | 42% | 0.72 |
| mtf_pullback | month_dir | FLAT | 480 | -356,460 | 38% | 0.65 |
| mtf_pullback | month_dir | UP | 164 | +23,324 | 52% | 1.08 |
| mtf_pullback | month_vol | HIGH_VOL | 214 | -145,044 | 43% | 0.70 |
| mtf_pullback | month_vol | LOW_VOL | 553 | -257,560 | 41% | 0.76 |
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
| ml_lgbm | regime4h | NEUTRAL | 2910 | -412,524 | 48% | 0.87 |
| ml_lgbm | regime4h | RANGE | 4522 | -146,348 | 49% | 0.97 |
| ml_lgbm | regime4h | TREND | 6915 | -202,972 | 51% | 0.97 |
| ml_lgbm | month_dir | DOWN | 3773 | -182,491 | 49% | 0.96 |
| ml_lgbm | month_dir | FLAT | 9136 | -371,619 | 50% | 0.96 |
| ml_lgbm | month_dir | UP | 3398 | -155,729 | 50% | 0.96 |
| ml_lgbm | month_vol | HIGH_VOL | 6408 | +133,129 | 51% | 1.02 |
| ml_lgbm | month_vol | LOW_VOL | 9899 | -842,969 | 49% | 0.92 |

## 比較: session（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | session | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v2_session_breakout | all | 5279 | -4.3% | 1.00 | 0.04 | -0.15 | 0.25 | -42.6% |
| v2_session_breakout | london | 4169 | +20.0% | 1.02 | 0.15 | 0.02 | 0.42 | -40.9% |
| v2_session_breakout | london_ny | 2989 | -15.1% | 0.98 | -0.05 | -0.14 | -0.08 | -37.0% |
| v2_session_breakout | ny | 3735 | -4.0% | 1.00 | 0.03 | -0.08 | 0.01 | -37.2% |
| v2_session_breakout | tokyo | 3092 | -16.6% | 0.97 | -0.06 | -0.37 | 0.42 | -37.5% |
| v2_session_breakout | tokyo_london | 2266 | +21.9% | 1.04 | 0.18 | 0.15 | 0.41 | -26.9% |

## 比較: sizing（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | sizing | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v2_d1_donchian | fixed_notional | 249 | -43.3% | 0.80 | -0.17 | -0.21 | -0.32 | -55.2% |
| v2_d1_donchian | risk_stop | 256 | -0.4% | 1.02 | -0.01 | 0.03 | -0.39 | -16.5% |
| v2_d1_donchian | vol_target | 259 | -18.7% | 0.90 | -0.09 | -0.17 | -0.34 | -40.3% |
| v2_d1_tsmom | fixed_notional | 278 | -32.2% | 0.86 | -0.05 | -0.08 | -0.31 | -56.2% |
| v2_d1_tsmom | risk_stop | 274 | +5.5% | 1.16 | 0.11 | 0.14 | -0.03 | -12.9% |
| v2_d1_tsmom | vol_target | 280 | +7.9% | 1.06 | 0.09 | 0.08 | -0.16 | -42.0% |
| v2_trend_carry | risk_stop | 126 | +4.8% | 1.03 | 0.01 | 0.00 | -0.00 | -7.4% |
| v2_trend_carry | vol_target | 139 | +10.9% | 0.94 | 0.03 | 0.02 | 0.07 | -26.8% |
| v2_xpair_strength | fixed_notional | 435 | -30.4% | 0.87 | -0.10 | -0.13 | -0.31 | -52.4% |
| v2_xpair_strength | risk_stop | 371 | -0.1% | 1.00 | 0.01 | 0.03 | -0.48 | -8.5% |
| v2_xpair_strength | vol_target | 451 | -11.7% | 0.93 | -0.05 | -0.04 | -0.44 | -35.0% |

## 比較: regime（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | regime | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v2_d1_donchian | no_high_vol | 243 | -17.3% | 0.93 | -0.06 | -0.08 | -0.43 | -36.2% |
| v2_d1_donchian | none | 268 | -24.5% | 0.88 | -0.11 | -0.14 | -0.41 | -39.5% |
| v2_d1_donchian | trend_only | 253 | -20.7% | 0.90 | -0.09 | -0.12 | -0.20 | -36.3% |
| v2_h4_ema | no_high_vol | 961 | -5.8% | 0.94 | -0.10 | -0.12 | -0.24 | -17.4% |
| v2_h4_ema | none | 1088 | -0.2% | 0.97 | -0.03 | 0.02 | -0.28 | -16.9% |
| v2_h4_ema | trend_only | 896 | +0.8% | 0.98 | -0.01 | 0.04 | -0.33 | -16.0% |

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
USDJPY  4196               0.0219            0.2988             1.156               9             1 2013-06-06
EURUSD  4196               0.0255            0.3175             0.884               9             0 2011-10-07
GBPUSD  4196               0.0257            0.3182             1.817              11             1 2020-03-18
AUDUSD  4196               0.0303            0.3768             1.172              20             3 2020-03-12
NZDUSD  4196               0.0364            0.4022             1.450              23             2 2011-08-05
USDCAD  4196               0.0250            0.2946             0.895               9             0 2020-03-12
USDCHF  4196               0.0278            0.3102             1.041               8             1 2011-10-07
