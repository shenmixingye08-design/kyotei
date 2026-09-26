# FX AUTOPILOT V16 研究結果（2026-09-26 10:33 UTC、データ〜2026-09-25 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v16.yaml`

> **検証汚染の申告**: 期間・コスト・ゲートは既出。株価の情報はこれまで一度も使っていない（新しい情報源）。 3 か月・1 か月ラグは登録時に固定、パラメータは閾値 2 通りのみ。ユーロ圏の集計系列が無い場合はドイツで代用（登録時に固定）。 DSR は V1 からの累積試行数で補正。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v16_equity_rebal | REJECTED | 236 | -25.9% | -2.3% | 0.75 | -0.30 | -0.41 | -32.6% | -953 | 69 | — | 13 | 46% | 50% | -12.3% | -15.5% | 0.64 | 4 | 100% | 0.02 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |
| v16_equity_rebal_carry | REJECTED | 163 | -34.5% | -3.3% | 0.56 | -0.57 | -0.74 | -39.5% | -2,187 | 79 | — | 17 | 23% | 64% | -28.3% | -8.6% | 0.48 | 1 | 100% | 0.00 | 2 | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v16_equity_rebal | REJECTED | 236 | — | — | -436,177 | 0.52 | — | -10.2% |
| v16_equity_rebal_carry | REJECTED | 163 | — | — | -505,056 | 0.37 | — | +1.3% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v16_equity_rebal | v16_equity_rebal_carry |
|---|---|---|
| 2014.0 | +1.6% | -7.5% |
| 2015.0 | -7.7% | -9.9% |
| 2016.0 | +8.5% | +5.1% |
| 2017.0 | -4.1% | -7.8% |
| 2018.0 | -12.7% | -4.5% |
| 2019.0 | +4.1% | -2.0% |
| 2020.0 | -1.7% | -4.9% |
| 2021.0 | +0.6% | -0.3% |
| 2022.0 | +1.1% | -4.0% |
| 2023.0 | -7.0% | -6.0% |
| 2024.0 | -6.7% | +1.4% |
| 2025.0 | -4.7% | -1.6% |
| 2026.0 | +1.0% | +1.5% |

## 年別 Profit Factor（WF OOS）

| year | v16_equity_rebal | v16_equity_rebal_carry |
|---|---|---|
| 2014.0 | 1.14 | 0.33 |
| 2015.0 | 0.16 | 0.21 |
| 2016.0 | 2.09 | 2.19 |
| 2017.0 | 0.30 | 0.00 |
| 2018.0 | 0.24 | 0.96 |
| 2019.0 | 1.17 | 0.45 |
| 2020.0 | 0.94 | 0.56 |
| 2021.0 | 2.05 | 0.35 |
| 2022.0 | 1.13 | 0.37 |
| 2023.0 | 0.28 | 0.76 |
| 2024.0 | 0.45 | 0.82 |
| 2025.0 | 1.13 | 1.56 |
| 2026.0 | 0.25 | 0.83 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v16_equity_rebal | AUDJPY | 27 | +4,795 | 1.05 | 48% | 71 | -813 |
| v16_equity_rebal | AUDUSD | 18 | +6,120 | 1.13 | 50% | 88 | -2,122 |
| v16_equity_rebal | EURJPY | 26 | -4,158 | 0.95 | 50% | 47 | -9,677 |
| v16_equity_rebal | EURUSD | 21 | -54,014 | 0.41 | 29% | 37 | -7,374 |
| v16_equity_rebal | GBPJPY | 31 | +4,897 | 1.05 | 48% | 80 | -21 |
| v16_equity_rebal | GBPUSD | 18 | -21,853 | 0.68 | 33% | 52 | -9,196 |
| v16_equity_rebal | NZDUSD | 27 | -98,735 | 0.24 | 26% | 94 | -9,145 |
| v16_equity_rebal | USDCAD | 23 | -56,975 | 0.35 | 30% | 72 | -7,083 |
| v16_equity_rebal | USDCHF | 21 | -86,570 | 0.13 | 24% | 103 | -5,247 |
| v16_equity_rebal | USDJPY | 24 | +81,602 | 1.86 | 50% | 40 | -20,476 |
| v16_equity_rebal_carry | AUDJPY | 19 | -56,555 | 0.52 | 26% | 72 | +14,419 |
| v16_equity_rebal_carry | AUDUSD | 16 | -20,351 | 0.72 | 31% | 107 | +3,879 |
| v16_equity_rebal_carry | EURJPY | 13 | -974 | 0.97 | 54% | 62 | -2,590 |
| v16_equity_rebal_carry | EURUSD | 17 | -38,343 | 0.60 | 35% | 56 | +7,618 |
| v16_equity_rebal_carry | GBPJPY | 17 | +31,055 | 1.47 | 41% | 98 | +15,513 |
| v16_equity_rebal_carry | GBPUSD | 11 | -10,238 | 0.79 | 36% | 49 | -1,338 |
| v16_equity_rebal_carry | NZDUSD | 19 | -128,798 | 0.08 | 16% | 114 | +730 |
| v16_equity_rebal_carry | USDCAD | 12 | -24,167 | 0.36 | 42% | 68 | -168 |
| v16_equity_rebal_carry | USDCHF | 19 | -63,924 | 0.30 | 32% | 118 | +18,389 |
| v16_equity_rebal_carry | USDJPY | 20 | -44,111 | 0.57 | 35% | 30 | +8,672 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v16_equity_rebal | regime4h | HIGH_VOL | 21 | -45,492 | 33% | 0.50 |
| v16_equity_rebal | regime4h | NEUTRAL | 47 | -9,190 | 49% | 0.94 |
| v16_equity_rebal | regime4h | RANGE | 70 | -87,475 | 39% | 0.62 |
| v16_equity_rebal | regime4h | TREND | 98 | -82,734 | 37% | 0.81 |
| v16_equity_rebal | month_dir | DOWN | 53 | -186,249 | 28% | 0.35 |
| v16_equity_rebal | month_dir | FLAT | 127 | +14,653 | 43% | 1.04 |
| v16_equity_rebal | month_dir | UP | 56 | -53,295 | 43% | 0.78 |
| v16_equity_rebal | month_vol | HIGH_VOL | 70 | -75,234 | 34% | 0.73 |
| v16_equity_rebal | month_vol | LOW_VOL | 166 | -149,657 | 42% | 0.76 |
| v16_equity_rebal_carry | regime4h | HIGH_VOL | 16 | -95,102 | 6% | 0.07 |
| v16_equity_rebal_carry | regime4h | NEUTRAL | 40 | -62,236 | 38% | 0.64 |
| v16_equity_rebal_carry | regime4h | RANGE | 58 | -126,785 | 33% | 0.56 |
| v16_equity_rebal_carry | regime4h | TREND | 85 | -204,546 | 35% | 0.53 |
| v16_equity_rebal_carry | month_dir | DOWN | 44 | -191,186 | 25% | 0.28 |
| v16_equity_rebal_carry | month_dir | FLAT | 108 | -260,734 | 34% | 0.49 |
| v16_equity_rebal_carry | month_dir | UP | 47 | -36,750 | 36% | 0.84 |
| v16_equity_rebal_carry | month_vol | HIGH_VOL | 72 | -333,940 | 17% | 0.23 |
| v16_equity_rebal_carry | month_vol | LOW_VOL | 127 | -154,731 | 42% | 0.73 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v16_equity_rebal | REJECTED | {"threshold": 1.0} | vol_target | 2026-09-26T10:33 | 4b771139dc34 |
| v16_equity_rebal_carry | REJECTED | {"threshold": 1.0} | vol_target | 2026-09-26T10:33 | 626674dd76eb |

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
