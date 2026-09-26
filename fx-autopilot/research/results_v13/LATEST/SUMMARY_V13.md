# FX AUTOPILOT V13 研究結果（2026-09-26 09:49 UTC、データ〜2026-09-25 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v13.yaml`

> **検証汚染の申告**: 期間・コスト・ゲートは既出。設計者は V1〜V12 の結果（キャリー系が 2022〜24 の円安に依存）を知っている。 2022〜24 は米国の利上げ・日本の据え置きで、金利モメンタムもドル買い・円売りになるため同じ相場への依存が出る可能性がある。 パラメータは閾値 2 通りのみ（6 か月は登録時に固定）。DSR は V1 からの累積試行数で補正。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v13_carry_ratemom | REJECTED | 104 | -13.2% | -1.1% | 0.81 | -0.17 | -0.23 | -28.8% | -1,052 | 93 | — | 9 | 31% | 37% | -15.7% | +3.0% | 0.69 | 7 | 90% | 0.06 | 2 | profit_factor, sharpe, positive_years, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |
| v13_ratemom | REJECTED | 151 | -16.0% | -1.4% | 0.86 | -0.18 | -0.25 | -26.0% | -786 | 81 | — | 11 | 31% | 46% | -6.1% | -10.5% | 0.75 | 4 | 100% | 0.06 | 2 | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v13_ratemom | REJECTED | 151 | — | — | -290,558 | 0.66 | — | -12.0% |
| v13_carry_ratemom | REJECTED | 104 | — | — | -301,076 | 0.49 | — | +4.0% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v13_ratemom | v13_carry_ratemom |
|---|---|---|
| 2014.0 | -0.5% | -1.8% |
| 2015.0 | +6.0% | -3.5% |
| 2016.0 | -7.0% | -4.3% |
| 2017.0 | -11.0% | -12.5% |
| 2018.0 | +9.5% | +2.9% |
| 2019.0 | +2.7% | -1.1% |
| 2020.0 | -0.9% | +4.8% |
| 2021.0 | -3.5% | -0.4% |
| 2022.0 | -0.5% | -4.5% |
| 2023.0 | +2.2% | +3.7% |
| 2024.0 | -1.2% | +6.6% |
| 2025.0 | -9.0% | -1.9% |
| 2026.0 | -2.1% | -0.6% |

## 年別 Profit Factor（WF OOS）

| year | v13_ratemom | v13_carry_ratemom |
|---|---|---|
| 2014.0 | 2.88 | 0.32 |
| 2015.0 | 0.79 | 0.32 |
| 2016.0 | 0.26 | 0.14 |
| 2017.0 | 0.46 | 0.09 |
| 2018.0 | 4.49 | 4.13 |
| 2019.0 | 0.60 | 0.00 |
| 2020.0 | 1.93 | 4.33 |
| 2021.0 | 0.63 | 0.73 |
| 2022.0 | 2.98 | 1.84 |
| 2023.0 | 0.35 | 0.56 |
| 2024.0 | 0.45 | 1.72 |
| 2025.0 | 0.15 | 0.19 |
| 2026.0 | 0.85 | 1.19 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v13_ratemom | AUDJPY | 7 | -40,960 | 0.28 | 14% | 60 | -5,723 |
| v13_ratemom | AUDUSD | 17 | +48,395 | 1.61 | 47% | 112 | -15,181 |
| v13_ratemom | EURJPY | 9 | +1,514 | 1.03 | 33% | 79 | -5,759 |
| v13_ratemom | EURUSD | 20 | +36,533 | 1.35 | 40% | 45 | -11,173 |
| v13_ratemom | GBPJPY | 9 | -16,156 | 0.74 | 22% | 86 | -3,259 |
| v13_ratemom | GBPUSD | 22 | -45,417 | 0.64 | 36% | 55 | -7,857 |
| v13_ratemom | NZDUSD | 15 | -51,922 | 0.38 | 33% | 122 | -4,514 |
| v13_ratemom | USDCAD | 21 | -36,456 | 0.63 | 43% | 106 | -9,226 |
| v13_ratemom | USDCHF | 17 | +27,840 | 1.38 | 47% | 108 | -6,135 |
| v13_ratemom | USDJPY | 14 | -42,122 | 0.59 | 29% | 28 | -14,894 |
| v13_carry_ratemom | AUDJPY | 17 | -83,562 | 0.34 | 12% | 80 | +10,950 |
| v13_carry_ratemom | AUDUSD | 14 | +17,831 | 1.36 | 43% | 119 | -4,601 |
| v13_carry_ratemom | EURJPY | 3 | +4,943 | 1.22 | 33% | 97 | +3,955 |
| v13_carry_ratemom | EURUSD | 12 | +1,266 | 1.02 | 42% | 38 | +7,884 |
| v13_carry_ratemom | GBPJPY | 5 | +10,206 | 1.40 | 20% | 61 | +8,476 |
| v13_carry_ratemom | GBPUSD | 7 | +6,132 | 1.12 | 29% | 51 | -112 |
| v13_carry_ratemom | NZDUSD | 8 | -48,832 | 0.32 | 25% | 106 | +487 |
| v13_carry_ratemom | USDCAD | 17 | -36,337 | 0.53 | 47% | 121 | -5,292 |
| v13_carry_ratemom | USDCHF | 15 | +9,564 | 1.14 | 47% | 145 | +29,895 |
| v13_carry_ratemom | USDJPY | 6 | +9,392 | 1.28 | 50% | 33 | +8,939 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v13_ratemom | regime4h | HIGH_VOL | 14 | +95,051 | 50% | 2.46 |
| v13_ratemom | regime4h | NEUTRAL | 27 | -134,144 | 26% | 0.32 |
| v13_ratemom | regime4h | RANGE | 51 | -37,278 | 31% | 0.87 |
| v13_ratemom | regime4h | TREND | 61 | -44,331 | 44% | 0.85 |
| v13_ratemom | month_dir | DOWN | 34 | +17,178 | 38% | 1.08 |
| v13_ratemom | month_dir | FLAT | 85 | -188,529 | 33% | 0.61 |
| v13_ratemom | month_dir | UP | 34 | +50,649 | 47% | 1.33 |
| v13_ratemom | month_vol | HIGH_VOL | 58 | -34,888 | 40% | 0.89 |
| v13_ratemom | month_vol | LOW_VOL | 95 | -85,815 | 36% | 0.84 |
| v13_carry_ratemom | regime4h | HIGH_VOL | 21 | +185,171 | 52% | 2.81 |
| v13_carry_ratemom | regime4h | NEUTRAL | 43 | -7,384 | 42% | 0.96 |
| v13_carry_ratemom | regime4h | RANGE | 49 | +20,051 | 37% | 1.08 |
| v13_carry_ratemom | regime4h | TREND | 67 | -318,241 | 24% | 0.31 |
| v13_carry_ratemom | month_dir | DOWN | 40 | +6,416 | 35% | 1.03 |
| v13_carry_ratemom | month_dir | FLAT | 90 | -203,776 | 30% | 0.62 |
| v13_carry_ratemom | month_dir | UP | 50 | +76,957 | 44% | 1.32 |
| v13_carry_ratemom | month_vol | HIGH_VOL | 69 | -70,953 | 33% | 0.82 |
| v13_carry_ratemom | month_vol | LOW_VOL | 111 | -49,450 | 36% | 0.92 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v13_ratemom | REJECTED | {"threshold": 0.5} | vol_target | 2026-09-26T09:49 | 46b7a171be92 |
| v13_carry_ratemom | REJECTED | {"threshold": 1.0} | vol_target | 2026-09-26T09:49 | 820965d2eb31 |

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
