# FX AUTOPILOT V14 研究結果（2026-09-26 10:16 UTC、データ〜2026-09-25 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v14.yaml`

> **検証汚染の申告**: 期間・コスト・ゲートは既出。設計者は V1〜V13 の結果を知っている。符号（傾きが負に予測）は論文から登録時に固定、 パラメータは閾値 2 通りのみ。DSR は V1 からの累積試行数で補正。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v14_term_ratemom | REJECTED | 118 | -19.4% | -1.7% | 0.81 | -0.27 | -0.37 | -30.3% | -914 | 65 | — | 15 | 46% | 48% | -23.8% | +5.7% | 0.68 | 4 | 100% | 0.03 | 2 | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |
| v14_term | REJECTED | 102 | -28.0% | -2.5% | 0.67 | -0.27 | -0.39 | -40.6% | -1,570 | 60 | — | 14 | 23% | 57% | -32.5% | +6.6% | 0.42 | 2 | 100% | 0.03 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v14_term | REJECTED | 102 | — | — | -320,409 | 0.33 | — | +14.3% |
| v14_term_ratemom | REJECTED | 118 | — | — | -281,463 | 0.52 | — | +5.5% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v14_term | v14_term_ratemom |
|---|---|---|
| 2014.0 | -11.6% | -12.5% |
| 2015.0 | -8.7% | -1.7% |
| 2016.0 | -4.3% | +0.5% |
| 2017.0 | -1.2% | -13.9% |
| 2018.0 | +9.4% | +13.5% |
| 2019.0 | -3.7% | +0.7% |
| 2020.0 | -4.6% | +1.1% |
| 2021.0 | -12.0% | -11.3% |
| 2022.0 | -6.1% | -4.5% |
| 2023.0 | -0.7% | +4.9% |
| 2024.0 | +14.0% | +7.4% |
| 2025.0 | -0.9% | -0.9% |
| 2026.0 | +1.1% | -0.9% |

## 年別 Profit Factor（WF OOS）

| year | v14_term | v14_term_ratemom |
|---|---|---|
| 2014.0 | 0.00 | 0.10 |
| 2015.0 | 0.25 | 2.04 |
| 2016.0 | 0.69 | 0.06 |
| 2017.0 | 0.24 | 0.18 |
| 2018.0 | 10.13 | 12.08 |
| 2019.0 | 0.04 | 2.05 |
| 2020.0 | 0.18 | 0.51 |
| 2021.0 | 0.00 | 0.00 |
| 2022.0 | 1.91 | 0.99 |
| 2023.0 | 4.42 | 4.03 |
| 2024.0 | 2.00 | 13.22 |
| 2025.0 | 1.29 | 0.79 |
| 2026.0 | 0.30 | 0.31 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v14_term | AUDJPY | 11 | -66,198 | 0.09 | 9% | 39 | -20,088 |
| v14_term | AUDUSD | 12 | +3,509 | 1.06 | 42% | 73 | -1,023 |
| v14_term | EURJPY | 6 | -26,805 | 0.16 | 17% | 18 | -6,422 |
| v14_term | EURUSD | 13 | -9,903 | 0.85 | 31% | 22 | +6,585 |
| v14_term | GBPJPY | 7 | +49,798 | 3.71 | 43% | 112 | +10,661 |
| v14_term | GBPUSD | 15 | -19,701 | 0.61 | 33% | 57 | -7,304 |
| v14_term | NZDUSD | 10 | -18,503 | 0.54 | 40% | 75 | -932 |
| v14_term | USDCAD | 10 | -8,547 | 0.75 | 50% | 102 | -543 |
| v14_term | USDCHF | 8 | -18,089 | 0.45 | 25% | 79 | +1,667 |
| v14_term | USDJPY | 10 | -45,706 | 0.43 | 20% | 34 | -8,865 |
| v14_term_ratemom | AUDJPY | 10 | -14,461 | 0.75 | 30% | 65 | -7,786 |
| v14_term_ratemom | AUDUSD | 15 | -28,969 | 0.58 | 33% | 75 | +2,901 |
| v14_term_ratemom | EURJPY | 7 | -17,297 | 0.66 | 14% | 54 | -5,129 |
| v14_term_ratemom | EURUSD | 12 | +19,904 | 1.53 | 42% | 28 | +6,219 |
| v14_term_ratemom | GBPJPY | 9 | +17,001 | 1.32 | 22% | 65 | -936 |
| v14_term_ratemom | GBPUSD | 9 | +7,941 | 1.23 | 44% | 49 | -3,026 |
| v14_term_ratemom | NZDUSD | 12 | -8,092 | 0.87 | 33% | 103 | -1,246 |
| v14_term_ratemom | USDCAD | 13 | -23,042 | 0.58 | 38% | 76 | -1,399 |
| v14_term_ratemom | USDCHF | 16 | +1,352 | 1.02 | 38% | 85 | +4,475 |
| v14_term_ratemom | USDJPY | 15 | -62,175 | 0.38 | 33% | 35 | -5,347 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v14_term | regime4h | HIGH_VOL | 13 | -52,989 | 23% | 0.38 |
| v14_term | regime4h | NEUTRAL | 20 | -42,112 | 30% | 0.51 |
| v14_term | regime4h | RANGE | 37 | -61,812 | 32% | 0.61 |
| v14_term | regime4h | TREND | 32 | -3,232 | 34% | 0.98 |
| v14_term | month_dir | DOWN | 21 | +39,518 | 43% | 1.54 |
| v14_term | month_dir | FLAT | 52 | -187,434 | 25% | 0.29 |
| v14_term | month_dir | UP | 29 | -12,230 | 34% | 0.91 |
| v14_term | month_vol | HIGH_VOL | 35 | -25,334 | 34% | 0.83 |
| v14_term | month_vol | LOW_VOL | 67 | -134,812 | 30% | 0.59 |
| v14_term_ratemom | regime4h | HIGH_VOL | 18 | -23,281 | 28% | 0.79 |
| v14_term_ratemom | regime4h | NEUTRAL | 29 | -3,500 | 38% | 0.97 |
| v14_term_ratemom | regime4h | RANGE | 49 | -93,879 | 29% | 0.64 |
| v14_term_ratemom | regime4h | TREND | 76 | -19,740 | 37% | 0.94 |
| v14_term_ratemom | month_dir | DOWN | 25 | +29,603 | 40% | 1.30 |
| v14_term_ratemom | month_dir | FLAT | 93 | -125,290 | 34% | 0.72 |
| v14_term_ratemom | month_dir | UP | 54 | -44,713 | 30% | 0.84 |
| v14_term_ratemom | month_vol | HIGH_VOL | 58 | -175,411 | 26% | 0.40 |
| v14_term_ratemom | month_vol | LOW_VOL | 114 | +35,011 | 38% | 1.07 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v14_term | REJECTED | {"threshold": 0.5} | vol_target | 2026-09-26T10:16 | 3edf4710facf |
| v14_term_ratemom | REJECTED | {"threshold": 1.0} | vol_target | 2026-09-26T10:16 | daf5b3d93c01 |

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
