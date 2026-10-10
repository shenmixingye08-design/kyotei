# FX AUTOPILOT V2 研究結果（2026-10-10 02:44 UTC、データ〜2026-10-09 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v2.yaml`

> **検証汚染の申告**: 設計者は v1 の 2010〜2026 の結果（Stage1 WF 2014〜2021、TEST 2022〜2025-06、FORWARD 2025-07〜）を既に見ている。 V2 の候補選び（中期トレンド・キャリー・通貨強弱を優先したこと）はその知見の影響を受けている。 したがって V2 の Walk-Forward 成績は、どの年も「完全な未知データ」ではない（"汚染あり WF OOS" と表記する）。 V2 の最終判断は、LOCK 後に新しく到着する足での PAPER Forward のみで行う。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v2_trend_carry | CHALLENGER | 157 | +20.2% | +1.5% | 2.10 | 0.45 | 0.63 | -7.8% | 1,441 | 32 | 0.03 | 8 | 77% | 25% | +9.4% | +9.9% | 1.81 | 5 | 50% | 0.55 | 1 |  |
| v2_h4_ema | REJECTED | 896 | +4.9% | +0.4% | 1.03 | 0.11 | 0.17 | -13.4% | 54 | 82 | 0.41 | 16 | 54% | 43% | +7.7% | -2.6% | 0.92 | 2 | 70% | 0.14 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_d1_tsmom | REJECTED | 200 | -13.2% | -1.1% | 0.91 | -0.08 | -0.11 | -27.8% | -395 | 119 | 0.33 | 18 | 46% | 43% | -3.1% | -10.4% | 0.85 | 3 | 100% | 0.04 | 4 | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, single_regime_dependence, deflated_sharpe |
| v2_xpair_strength | REJECTED | 330 | -4.0% | -0.3% | 0.88 | -0.18 | -0.25 | -9.1% | -116 | 30 | — | 13 | 38% | 50% | +0.8% | -4.7% | 0.79 | 1 | 100% | 0.02 | 2 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_session_breakout | REJECTED | 2631 | -32.1% | -3.0% | 0.95 | -0.24 | -0.36 | -46.6% | -130 | 132 | 3.43 | 22 | 38% | 37% | -37.9% | +9.2% | 0.86 | 2 | 100% | 0.01 | 4 | profit_factor, sharpe, positive_years, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_d1_donchian | REJECTED | 164 | -10.0% | -0.8% | 0.74 | -0.26 | -0.37 | -16.8% | -640 | 42 | — | 12 | 31% | 41% | -2.5% | -7.7% | 0.65 | 0 | 100% | 0.01 | 3 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe |
| v2_ml_d1_logit | REJECTED | 155 | -6.0% | -0.5% | 0.60 | -0.65 | -0.79 | -6.5% | -384 | 30 | — | 6 | 23% | 45% | -4.6% | -1.4% | 0.54 | 0 | 100% | 0.00 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, ml_not_better_than_simple |
| trend_tsmom | REFERENCE_V1 | 976 | -17.4% | -1.5% | 0.93 | -0.17 | -0.25 | -28.0% | -175 | 63 | — | 20 | 54% | 34% | -16.1% | -1.6% | 0.88 | 2 | 100% | 0.02 | 3 | reference_v1 |
| ml_logit | REFERENCE_V1 | 3223 | -17.6% | -1.5% | 0.96 | -0.20 | -0.28 | -19.5% | -63 | 127 | 1.68 | 12 | 31% | 41% | -15.9% | -2.0% | 0.86 | 2 | 79% | 0.01 | 2 | reference_v1 |
| mr_zscore | REFERENCE_V1 | 3252 | -36.1% | -3.4% | 0.94 | -0.37 | -0.50 | -50.5% | -72 | 59 | 13.90 | 17 | 31% | 59% | -42.9% | +12.0% | 0.85 | 2 | 100% | 0.00 | 2 | reference_v1 |
| trend_ema_adx | REFERENCE_V1 | 3676 | -50.2% | -5.3% | 0.91 | -0.43 | -0.66 | -55.3% | -143 | 115 | 20.91 | 28 | 15% | 55% | -32.3% | -26.4% | 0.81 | 1 | 100% | 0.00 | 4 | reference_v1 |
| trend_donchian | REFERENCE_V1 | 2395 | -72.0% | -9.5% | 0.82 | -0.62 | -0.89 | -76.0% | -400 | 93 | — | 27 | 23% | 64% | -56.2% | -36.1% | 0.74 | 1 | 100% | 0.00 | 3 | reference_v1 |
| ml_lgbm | REFERENCE_V1 | 14001 | -65.6% | -8.0% | 0.95 | -0.65 | -0.87 | -68.4% | -48 | 100 | 1.63 | 13 | 15% | 95% | -50.5% | -30.4% | 0.85 | 1 | 100% | 0.00 | 2 | reference_v1 |
| mr_rsi_bb | REFERENCE_V1 | 2669 | -46.7% | -4.8% | 0.88 | -0.74 | -1.00 | -49.0% | -136 | 93 | — | 9 | 8% | 100% | -26.4% | -27.6% | 0.79 | 1 | 100% | 0.00 | 1 | reference_v1 |
| regime_switch | REFERENCE_V1 | 3765 | -68.6% | -8.7% | 0.88 | -0.88 | -1.27 | -71.6% | -138 | 75 | — | 15 | 23% | 63% | -55.4% | -29.6% | 0.80 | 0 | 100% | 0.00 | 2 | reference_v1 |
| mtf_pullback | REFERENCE_V1 | 766 | -40.0% | -3.9% | 0.74 | -1.06 | -1.36 | -42.4% | -523 | 140 | — | 15 | 23% | 51% | -38.0% | -3.2% | 0.67 | 0 | 99% | 0.00 | 2 | reference_v1 |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v2_d1_donchian | REJECTED | 164 | — | — | -237,498 | 0.41 | — | -6.7% |
| v2_d1_tsmom | REJECTED | 200 | — | — | -557,669 | 0.40 | — | -12.4% |
| v2_h4_ema | REJECTED | 896 | 74% | 307% | -100,214 | 0.94 | -120% | -1.7% |
| v2_trend_carry | CHALLENGER | 157 | 55% | 116% | -35,107 | 0.83 | 12% | +1.3% |
| v2_xpair_strength | REJECTED | 330 | — | — | -99,833 | 0.68 | — | -2.8% |
| v2_session_breakout | REJECTED | 2631 | — | — | -567,141 | 0.91 | — | +3.0% |
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
| 2026.0 | -1.0% | -5.8% | +0.1% | +0.7% | -3.5% | -2.0% | +0.0% | -6.1% | -4.1% | -3.9% | -3.1% | -10.2% | -5.6% | +3.7% | -2.0% | -5.1% |

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
| 2021.0 | 0.83 | 11.88 | 0.82 | 166.23 | 0.31 | 0.79 | 1.43 | 0.87 | 0.82 | 1.15 | 0.94 | 0.97 | 0.85 | 0.54 | 2.32 | 0.90 |
| 2022.0 | 1.66 | 0.00 | 1.47 | 3.28 | 0.29 | 1.10 | — | 1.03 | 1.00 | 1.13 | 0.80 | 0.88 | 1.02 | 1.15 | 1.29 | 1.00 |
| 2023.0 | 0.20 | 0.09 | 0.61 | 1.48 | 0.46 | 1.01 | 0.22 | 0.87 | 0.75 | 1.15 | 0.83 | 1.37 | 0.96 | 0.61 | 1.21 | 0.95 |
| 2024.0 | 0.27 | 0.13 | 1.19 | 0.22 | 0.97 | 0.96 | 0.00 | 0.74 | 1.15 | 1.08 | 0.99 | 1.08 | 0.90 | 1.19 | 0.80 | 0.96 |
| 2025.0 | 0.72 | 3.04 | 0.74 | 0.50 | 2.03 | 1.25 | 0.24 | 0.95 | 0.46 | 0.70 | 0.71 | 1.16 | 0.64 | 0.80 | 0.88 | 0.88 |
| 2026.0 | 0.00 | 0.08 | 1.01 | 0.97 | 0.14 | 0.89 | — | 0.79 | 0.84 | 0.81 | 0.87 | 0.72 | 0.86 | 1.72 | 0.83 | 0.95 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v2_d1_donchian | AUDUSD | 37 | -36,518 | 0.64 | 30% | 62 | -10,084 |
| v2_d1_donchian | EURJPY | 26 | -4,906 | 0.90 | 38% | 42 | -2,062 |
| v2_d1_donchian | EURUSD | 33 | -14,740 | 0.82 | 27% | 28 | -10,868 |
| v2_d1_donchian | GBPUSD | 35 | -27,108 | 0.66 | 29% | 43 | -9,411 |
| v2_d1_donchian | USDJPY | 33 | -21,719 | 0.75 | 33% | 34 | -110 |
| v2_d1_tsmom | AUDUSD | 55 | +15,267 | 1.10 | 35% | 156 | -29,086 |
| v2_d1_tsmom | EURJPY | 35 | -126,237 | 0.31 | 20% | 141 | -7,235 |
| v2_d1_tsmom | EURUSD | 33 | +129,752 | 1.64 | 30% | 61 | -42,774 |
| v2_d1_tsmom | GBPUSD | 36 | +8,018 | 1.04 | 42% | 181 | -41,835 |
| v2_d1_tsmom | USDJPY | 41 | -105,835 | 0.36 | 24% | 45 | -5,677 |
| v2_h4_ema | AUDUSD | 156 | -1,344 | 1.00 | 35% | 122 | -8,241 |
| v2_h4_ema | EURJPY | 185 | -22,260 | 0.94 | 36% | 74 | -13,233 |
| v2_h4_ema | EURUSD | 186 | +11,012 | 1.03 | 32% | 69 | -13,831 |
| v2_h4_ema | GBPUSD | 179 | -489 | 1.00 | 33% | 92 | -10,835 |
| v2_h4_ema | USDJPY | 190 | +61,451 | 1.18 | 36% | 63 | -12,049 |
| v2_trend_carry | AUDUSD | 42 | +4,319 | 1.12 | 36% | 48 | -3,299 |
| v2_trend_carry | EURJPY | 25 | +12,170 | 1.31 | 36% | 27 | +2,606 |
| v2_trend_carry | EURUSD | 34 | +62,832 | 2.22 | 35% | 22 | +877 |
| v2_trend_carry | GBPUSD | 33 | +4,801 | 1.11 | 45% | 36 | -6,337 |
| v2_trend_carry | USDJPY | 23 | +142,086 | 5.13 | 39% | 21 | +33,599 |
| v2_xpair_strength | AUDUSD | 94 | -22,911 | 0.69 | 41% | 40 | -4,630 |
| v2_xpair_strength | EURJPY | 53 | -8,873 | 0.84 | 42% | 32 | -813 |
| v2_xpair_strength | EURUSD | 71 | -10,584 | 0.85 | 42% | 20 | -7,162 |
| v2_xpair_strength | GBPUSD | 60 | -5,199 | 0.91 | 45% | 34 | -6,094 |
| v2_xpair_strength | USDJPY | 52 | +9,318 | 1.18 | 44% | 22 | +2,163 |
| v2_session_breakout | AUDUSD | 517 | -281,109 | 0.78 | 32% | 184 | -23,193 |
| v2_session_breakout | EURJPY | 568 | -228,534 | 0.85 | 33% | 136 | -12,045 |
| v2_session_breakout | EURUSD | 538 | +106,235 | 1.09 | 35% | 95 | -30,388 |
| v2_session_breakout | GBPUSD | 504 | -126,232 | 0.91 | 32% | 140 | -29,552 |
| v2_session_breakout | USDJPY | 504 | +187,833 | 1.15 | 37% | 106 | -648 |
| v2_ml_d1_logit | AUDUSD | 15 | -2,070 | 0.85 | 60% | 40 | -701 |
| v2_ml_d1_logit | EURJPY | 27 | -8,416 | 0.70 | 44% | 33 | -777 |
| v2_ml_d1_logit | EURUSD | 33 | -21,065 | 0.41 | 33% | 22 | -2,001 |
| v2_ml_d1_logit | GBPUSD | 41 | -18,845 | 0.52 | 41% | 34 | -1,185 |
| v2_ml_d1_logit | USDJPY | 39 | -9,114 | 0.70 | 51% | 25 | -486 |
| trend_ema_adx | AUDUSD | 824 | -232,485 | 0.83 | 31% | 168 | -23,832 |
| trend_ema_adx | EURJPY | 799 | -139,525 | 0.90 | 30% | 113 | -29,232 |
| trend_ema_adx | EURUSD | 717 | -32,491 | 0.97 | 33% | 78 | -23,575 |
| trend_ema_adx | GBPUSD | 649 | -170,451 | 0.83 | 31% | 116 | -23,138 |
| trend_ema_adx | USDJPY | 687 | +49,632 | 1.05 | 32% | 93 | -22,094 |
| trend_donchian | AUDUSD | 534 | -516,891 | 0.57 | 23% | 133 | -29,930 |
| trend_donchian | EURJPY | 519 | -38,846 | 0.97 | 25% | 89 | -40,500 |
| trend_donchian | EURUSD | 441 | -218,273 | 0.76 | 23% | 62 | -31,405 |
| trend_donchian | GBPUSD | 438 | -244,480 | 0.75 | 24% | 96 | -39,380 |
| trend_donchian | USDJPY | 463 | +60,701 | 1.06 | 27% | 77 | -19,462 |
| trend_tsmom | AUDUSD | 184 | +4,875 | 1.01 | 39% | 95 | -15,610 |
| trend_tsmom | EURJPY | 188 | -109,072 | 0.77 | 34% | 57 | -9,066 |
| trend_tsmom | EURUSD | 205 | -38,448 | 0.93 | 36% | 53 | -25,292 |
| trend_tsmom | GBPUSD | 190 | +13,372 | 1.03 | 33% | 67 | -21,995 |
| trend_tsmom | USDJPY | 209 | -41,072 | 0.93 | 31% | 49 | -5,045 |
| mr_rsi_bb | AUDUSD | 449 | +1,048 | 1.00 | 51% | 138 | -3,940 |
| mr_rsi_bb | EURJPY | 499 | -75,284 | 0.87 | 48% | 89 | -7,441 |
| mr_rsi_bb | EURUSD | 558 | -33,019 | 0.94 | 49% | 68 | -7,945 |
| mr_rsi_bb | GBPUSD | 562 | -42,560 | 0.93 | 49% | 103 | -7,450 |
| mr_rsi_bb | USDJPY | 601 | -213,560 | 0.72 | 43% | 76 | -11,861 |
| mr_zscore | AUDUSD | 667 | -89,709 | 0.88 | 42% | 88 | -8,773 |
| mr_zscore | EURJPY | 658 | +29,986 | 1.04 | 46% | 53 | -11,078 |
| mr_zscore | EURUSD | 636 | +3,257 | 1.00 | 44% | 44 | -12,233 |
| mr_zscore | GBPUSD | 602 | -76,549 | 0.88 | 42% | 63 | -9,810 |
| mr_zscore | USDJPY | 689 | -101,175 | 0.88 | 41% | 46 | -15,208 |
| regime_switch | AUDUSD | 784 | -76,972 | 0.91 | 36% | 115 | -12,191 |
| regime_switch | EURJPY | 726 | -162,857 | 0.81 | 35% | 66 | -12,758 |
| regime_switch | EURUSD | 725 | -10,708 | 0.99 | 35% | 52 | -11,545 |
| regime_switch | GBPUSD | 708 | -66,140 | 0.91 | 36% | 78 | -12,245 |
| regime_switch | USDJPY | 822 | -201,553 | 0.79 | 32% | 61 | -13,269 |
| mtf_pullback | AUDUSD | 156 | -80,671 | 0.76 | 43% | 214 | -2,897 |
| mtf_pullback | EURJPY | 141 | -63,280 | 0.78 | 43% | 131 | -2,000 |
| mtf_pullback | EURUSD | 149 | -94,138 | 0.67 | 39% | 100 | -3,002 |
| mtf_pullback | GBPUSD | 166 | -146,206 | 0.61 | 37% | 155 | -2,957 |
| mtf_pullback | USDJPY | 154 | -16,176 | 0.94 | 46% | 96 | -604 |
| ml_logit | AUDUSD | 576 | +44,983 | 1.05 | 51% | 193 | -13,772 |
| ml_logit | EURJPY | 751 | +101,647 | 1.09 | 54% | 123 | -2,435 |
| ml_logit | EURUSD | 671 | -139,041 | 0.85 | 46% | 93 | -10,186 |
| ml_logit | GBPUSD | 365 | -140,493 | 0.75 | 45% | 133 | -4,134 |
| ml_logit | USDJPY | 860 | -71,734 | 0.95 | 50% | 111 | -7,587 |
| ml_lgbm | AUDUSD | 2819 | -367,152 | 0.88 | 48% | 158 | -27,991 |
| ml_lgbm | EURJPY | 2661 | -9,754 | 1.00 | 50% | 97 | -20,530 |
| ml_lgbm | EURUSD | 2860 | -189,115 | 0.93 | 49% | 66 | -37,500 |
| ml_lgbm | GBPUSD | 2477 | -227,382 | 0.91 | 49% | 109 | -21,785 |
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
| v2_d1_tsmom | regime4h | RANGE | 85 | -13,279 | 34% | 0.96 |
| v2_d1_tsmom | regime4h | TREND | 189 | +217,604 | 33% | 1.24 |
| v2_d1_tsmom | month_dir | DOWN | 69 | -23,603 | 23% | 0.93 |
| v2_d1_tsmom | month_dir | FLAT | 215 | -163,710 | 33% | 0.84 |
| v2_d1_tsmom | month_dir | UP | 82 | +116,114 | 38% | 1.33 |
| v2_d1_tsmom | month_vol | HIGH_VOL | 104 | -263,789 | 28% | 0.44 |
| v2_d1_tsmom | month_vol | LOW_VOL | 262 | +192,590 | 34% | 1.15 |
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
| v2_trend_carry | regime4h | RANGE | 33 | +113,736 | 45% | 3.73 |
| v2_trend_carry | regime4h | TREND | 78 | +75,105 | 35% | 1.67 |
| v2_trend_carry | month_dir | DOWN | 31 | +19,757 | 45% | 1.46 |
| v2_trend_carry | month_dir | FLAT | 95 | +193,152 | 35% | 2.53 |
| v2_trend_carry | month_dir | UP | 31 | +13,299 | 42% | 1.37 |
| v2_trend_carry | month_vol | HIGH_VOL | 35 | +6,010 | 40% | 1.15 |
| v2_trend_carry | month_vol | LOW_VOL | 122 | +220,198 | 38% | 2.35 |
| v2_xpair_strength | regime4h | HIGH_VOL | 33 | -4,677 | 48% | 0.89 |
| v2_xpair_strength | regime4h | NEUTRAL | 88 | -35,758 | 39% | 0.60 |
| v2_xpair_strength | regime4h | RANGE | 134 | +9,996 | 47% | 1.09 |
| v2_xpair_strength | regime4h | TREND | 219 | -46,791 | 42% | 0.80 |
| v2_xpair_strength | month_dir | DOWN | 92 | +23,136 | 50% | 1.28 |
| v2_xpair_strength | month_dir | FLAT | 269 | -124,931 | 37% | 0.57 |
| v2_xpair_strength | month_dir | UP | 113 | +24,566 | 51% | 1.23 |
| v2_xpair_strength | month_vol | HIGH_VOL | 123 | -37,958 | 40% | 0.74 |
| v2_xpair_strength | month_vol | LOW_VOL | 351 | -39,272 | 44% | 0.88 |
| v2_session_breakout | regime4h | HIGH_VOL | 260 | +30,949 | 35% | 1.04 |
| v2_session_breakout | regime4h | NEUTRAL | 793 | -111,621 | 33% | 0.95 |
| v2_session_breakout | regime4h | RANGE | 1356 | -37,770 | 34% | 0.99 |
| v2_session_breakout | regime4h | TREND | 1472 | -329,269 | 33% | 0.91 |
| v2_session_breakout | month_dir | DOWN | 769 | +393,639 | 39% | 1.21 |
| v2_session_breakout | month_dir | FLAT | 2266 | -1,259,067 | 30% | 0.79 |
| v2_session_breakout | month_dir | UP | 846 | +417,716 | 37% | 1.20 |
| v2_session_breakout | month_vol | HIGH_VOL | 1470 | -2,516 | 34% | 1.00 |
| v2_session_breakout | month_vol | LOW_VOL | 2411 | -445,195 | 33% | 0.93 |
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
| trend_ema_adx | regime4h | RANGE | 2172 | -88,085 | 31% | 0.97 |
| trend_ema_adx | regime4h | TREND | 776 | -231,132 | 30% | 0.82 |
| trend_ema_adx | month_dir | DOWN | 816 | +238,387 | 32% | 1.19 |
| trend_ema_adx | month_dir | FLAT | 2641 | -816,683 | 30% | 0.81 |
| trend_ema_adx | month_dir | UP | 751 | +29,735 | 34% | 1.03 |
| trend_ema_adx | month_vol | HIGH_VOL | 1453 | -429,876 | 31% | 0.82 |
| trend_ema_adx | month_vol | LOW_VOL | 2755 | -118,684 | 31% | 0.97 |
| trend_donchian | regime4h | HIGH_VOL | 202 | -47,727 | 23% | 0.91 |
| trend_donchian | regime4h | NEUTRAL | 714 | -733,352 | 20% | 0.60 |
| trend_donchian | regime4h | RANGE | 1123 | -146,949 | 25% | 0.94 |
| trend_donchian | regime4h | TREND | 810 | -30,752 | 26% | 0.98 |
| trend_donchian | month_dir | DOWN | 547 | +246,749 | 30% | 1.21 |
| trend_donchian | month_dir | FLAT | 1774 | -1,801,701 | 20% | 0.58 |
| trend_donchian | month_dir | UP | 528 | +596,173 | 31% | 1.55 |
| trend_donchian | month_vol | HIGH_VOL | 900 | -282,103 | 25% | 0.87 |
| trend_donchian | month_vol | LOW_VOL | 1949 | -676,676 | 24% | 0.85 |
| trend_tsmom | regime4h | HIGH_VOL | 86 | -11,139 | 36% | 0.94 |
| trend_tsmom | regime4h | NEUTRAL | 171 | -61,743 | 34% | 0.87 |
| trend_tsmom | regime4h | RANGE | 216 | +161,225 | 39% | 1.32 |
| trend_tsmom | regime4h | TREND | 581 | -131,750 | 33% | 0.92 |
| trend_tsmom | month_dir | DOWN | 244 | +321,452 | 48% | 1.64 |
| trend_tsmom | month_dir | FLAT | 576 | -904,518 | 23% | 0.49 |
| trend_tsmom | month_dir | UP | 234 | +539,659 | 50% | 2.16 |
| trend_tsmom | month_vol | HIGH_VOL | 383 | +86,012 | 36% | 1.09 |
| trend_tsmom | month_vol | LOW_VOL | 671 | -129,419 | 34% | 0.93 |
| mr_rsi_bb | regime4h | HIGH_VOL | 132 | -1,357 | 53% | 0.99 |
| mr_rsi_bb | regime4h | NEUTRAL | 537 | -28,289 | 49% | 0.95 |
| mr_rsi_bb | regime4h | RANGE | 1149 | -222,072 | 47% | 0.83 |
| mr_rsi_bb | regime4h | TREND | 851 | -111,656 | 48% | 0.89 |
| mr_rsi_bb | month_dir | DOWN | 555 | -123,506 | 47% | 0.82 |
| mr_rsi_bb | month_dir | FLAT | 1544 | -96,939 | 49% | 0.94 |
| mr_rsi_bb | month_dir | UP | 570 | -142,929 | 45% | 0.79 |
| mr_rsi_bb | month_vol | HIGH_VOL | 926 | -222,457 | 45% | 0.81 |
| mr_rsi_bb | month_vol | LOW_VOL | 1743 | -140,917 | 49% | 0.92 |
| mr_zscore | regime4h | HIGH_VOL | 335 | -55,352 | 42% | 0.85 |
| mr_zscore | regime4h | NEUTRAL | 620 | +22,690 | 46% | 1.04 |
| mr_zscore | regime4h | RANGE | 756 | -141,807 | 42% | 0.83 |
| mr_zscore | regime4h | TREND | 1541 | -59,722 | 42% | 0.97 |
| mr_zscore | month_dir | DOWN | 797 | -267,098 | 37% | 0.74 |
| mr_zscore | month_dir | FLAT | 1797 | +255,491 | 47% | 1.14 |
| mr_zscore | month_dir | UP | 658 | -222,583 | 37% | 0.71 |
| mr_zscore | month_vol | HIGH_VOL | 1205 | -140,435 | 41% | 0.90 |
| mr_zscore | month_vol | LOW_VOL | 2047 | -93,756 | 44% | 0.96 |
| regime_switch | regime4h | HIGH_VOL | 28 | -8,624 | 39% | 0.48 |
| regime_switch | regime4h | NEUTRAL | 126 | -51,343 | 33% | 0.65 |
| regime_switch | regime4h | RANGE | 2850 | -413,236 | 36% | 0.87 |
| regime_switch | regime4h | TREND | 1177 | -125,642 | 32% | 0.91 |
| regime_switch | month_dir | DOWN | 833 | +8,874 | 37% | 1.01 |
| regime_switch | month_dir | FLAT | 2503 | -507,417 | 34% | 0.82 |
| regime_switch | month_dir | UP | 845 | -100,302 | 34% | 0.89 |
| regime_switch | month_vol | HIGH_VOL | 1303 | +64,442 | 37% | 1.04 |
| regime_switch | month_vol | LOW_VOL | 2878 | -663,287 | 33% | 0.79 |
| mtf_pullback | regime4h | HIGH_VOL | 4 | +181 | 50% | 1.02 |
| mtf_pullback | regime4h | NEUTRAL | 144 | +25,465 | 51% | 1.10 |
| mtf_pullback | regime4h | RANGE | 213 | -171,411 | 38% | 0.63 |
| mtf_pullback | regime4h | TREND | 405 | -254,707 | 40% | 0.70 |
| mtf_pullback | month_dir | DOWN | 123 | -69,468 | 42% | 0.72 |
| mtf_pullback | month_dir | FLAT | 479 | -354,328 | 38% | 0.66 |
| mtf_pullback | month_dir | UP | 164 | +23,324 | 52% | 1.08 |
| mtf_pullback | month_vol | HIGH_VOL | 214 | -145,044 | 43% | 0.70 |
| mtf_pullback | month_vol | LOW_VOL | 552 | -255,428 | 41% | 0.76 |
| ml_logit | regime4h | HIGH_VOL | 1236 | +108,129 | 52% | 1.06 |
| ml_logit | regime4h | NEUTRAL | 948 | -80,156 | 49% | 0.94 |
| ml_logit | regime4h | RANGE | 1088 | +27,933 | 52% | 1.02 |
| ml_logit | regime4h | TREND | 2695 | -383,175 | 48% | 0.91 |
| ml_logit | month_dir | DOWN | 1569 | -260,914 | 48% | 0.90 |
| ml_logit | month_dir | FLAT | 3118 | -102,138 | 50% | 0.98 |
| ml_logit | month_dir | UP | 1280 | +35,782 | 51% | 1.02 |
| ml_logit | month_vol | HIGH_VOL | 2389 | +78,771 | 52% | 1.02 |
| ml_logit | month_vol | LOW_VOL | 3578 | -406,040 | 49% | 0.93 |
| ml_lgbm | regime4h | HIGH_VOL | 1960 | +52,005 | 52% | 1.03 |
| ml_lgbm | regime4h | NEUTRAL | 2906 | -413,731 | 48% | 0.87 |
| ml_lgbm | regime4h | RANGE | 4507 | -149,285 | 49% | 0.97 |
| ml_lgbm | regime4h | TREND | 6910 | -200,077 | 51% | 0.97 |
| ml_lgbm | month_dir | DOWN | 3773 | -182,491 | 49% | 0.96 |
| ml_lgbm | month_dir | FLAT | 9112 | -372,868 | 50% | 0.96 |
| ml_lgbm | month_dir | UP | 3398 | -155,729 | 50% | 0.96 |
| ml_lgbm | month_vol | HIGH_VOL | 6409 | +133,229 | 52% | 1.02 |
| ml_lgbm | month_vol | LOW_VOL | 9874 | -844,318 | 49% | 0.92 |

## 比較: session（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | session | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v2_session_breakout | all | 5272 | -2.6% | 1.00 | 0.05 | -0.15 | 0.28 | -42.6% |
| v2_session_breakout | london | 4163 | +21.7% | 1.02 | 0.16 | 0.02 | 0.44 | -40.9% |
| v2_session_breakout | london_ny | 2984 | -13.9% | 0.98 | -0.04 | -0.14 | -0.05 | -37.0% |
| v2_session_breakout | ny | 3729 | -1.8% | 1.00 | 0.05 | -0.08 | 0.05 | -37.2% |
| v2_session_breakout | tokyo | 3089 | -15.6% | 0.98 | -0.05 | -0.37 | 0.45 | -37.5% |
| v2_session_breakout | tokyo_london | 2263 | +23.6% | 1.04 | 0.19 | 0.15 | 0.44 | -26.9% |

## 比較: sizing（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | sizing | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v2_d1_donchian | fixed_notional | 249 | -43.4% | 0.80 | -0.17 | -0.21 | -0.32 | -55.2% |
| v2_d1_donchian | risk_stop | 256 | -0.5% | 1.02 | -0.01 | 0.03 | -0.39 | -16.5% |
| v2_d1_donchian | vol_target | 259 | -18.8% | 0.90 | -0.09 | -0.17 | -0.34 | -40.3% |
| v2_d1_tsmom | fixed_notional | 277 | -31.6% | 0.86 | -0.05 | -0.08 | -0.30 | -56.2% |
| v2_d1_tsmom | risk_stop | 272 | +5.8% | 1.17 | 0.12 | 0.14 | -0.01 | -12.8% |
| v2_d1_tsmom | vol_target | 279 | +9.0% | 1.06 | 0.09 | 0.08 | -0.15 | -41.9% |
| v2_trend_carry | risk_stop | 125 | +4.9% | 1.03 | 0.02 | 0.00 | 0.00 | -7.4% |
| v2_trend_carry | vol_target | 139 | +11.2% | 0.95 | 0.03 | 0.02 | 0.08 | -26.8% |
| v2_xpair_strength | fixed_notional | 433 | -30.2% | 0.87 | -0.10 | -0.13 | -0.31 | -52.4% |
| v2_xpair_strength | risk_stop | 369 | +0.0% | 1.00 | 0.01 | 0.03 | -0.47 | -8.4% |
| v2_xpair_strength | vol_target | 449 | -11.3% | 0.93 | -0.05 | -0.04 | -0.43 | -34.8% |

## 比較: regime（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | regime | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v2_d1_donchian | no_high_vol | 243 | -17.3% | 0.93 | -0.06 | -0.08 | -0.43 | -36.2% |
| v2_d1_donchian | none | 268 | -24.6% | 0.88 | -0.11 | -0.14 | -0.41 | -39.5% |
| v2_d1_donchian | trend_only | 253 | -20.7% | 0.90 | -0.09 | -0.12 | -0.21 | -36.3% |
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
USDJPY  4191               0.0219            0.2991             1.156               9             1 2013-06-06
EURUSD  4191               0.0254            0.3177             0.884               9             0 2011-10-07
GBPUSD  4191               0.0257            0.3183             1.817              11             1 2020-03-18
AUDUSD  4191               0.0303            0.3768             1.172              20             3 2020-03-12
NZDUSD  4191               0.0362            0.4022             1.450              23             2 2011-08-05
USDCAD  4191               0.0250            0.2946             0.895               9             0 2020-03-12
USDCHF  4191               0.0277            0.3102             1.041               8             1 2011-10-07
