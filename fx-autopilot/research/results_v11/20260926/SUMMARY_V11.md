# FX AUTOPILOT V11 研究結果（2026-09-26 10:05 UTC、データ〜2026-09-25 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v11.yaml`

> **検証汚染の申告**: 期間・コスト・ゲートは既出。時間帯の区切りは論文の考え方に沿って登録時に固定（グリッド 1 通り）。 コスト（個人口座の原則固定スプレッドと実測の大きい方 + スリッページ）が効果を上回る可能性が高いことは登録時点で予想している。 DSR は V1 からの累積試行数で補正。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v11_intraday_region | REJECTED | 26241 | -53.0% | -5.8% | 0.90 | -1.17 | -1.57 | -54.0% | -11 | 16 | 3.07 | 32 | 8% | 100% | -49.7% | -6.5% | 0.71 | 2 | 100% | 0.00 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v11_intraday_region | REJECTED | 26241 | — | — | -294,944 | 0.90 | — | -6.1% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v11_intraday_region |
|---|---|
| 2014.0 | -6.7% |
| 2015.0 | -1.7% |
| 2016.0 | -3.2% |
| 2017.0 | -5.1% |
| 2018.0 | -11.0% |
| 2019.0 | -17.4% |
| 2020.0 | -13.6% |
| 2021.0 | -6.1% |
| 2022.0 | -0.6% |
| 2023.0 | +0.2% |
| 2024.0 | -0.9% |
| 2025.0 | -1.7% |
| 2026.0 | -3.7% |

## 年別 Profit Factor（WF OOS）

| year | v11_intraday_region |
|---|---|
| 2014.0 | 0.93 |
| 2015.0 | 0.97 |
| 2016.0 | 0.96 |
| 2017.0 | 0.94 |
| 2018.0 | 0.88 |
| 2019.0 | 0.78 |
| 2020.0 | 0.80 |
| 2021.0 | 0.91 |
| 2022.0 | 0.96 |
| 2023.0 | 1.20 |
| 2024.0 | 0.93 |
| 2025.0 | 0.90 |
| 2026.0 | 0.61 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v11_intraday_region | AUDUSD | 4407 | -104,079 | 0.78 | 45% | 19 | +0 |
| v11_intraday_region | EURJPY | 3497 | -5,286 | 0.99 | 49% | 11 | +0 |
| v11_intraday_region | EURUSD | 3589 | +44,809 | 1.13 | 50% | 9 | +0 |
| v11_intraday_region | GBPJPY | 802 | -7,981 | 0.94 | 49% | 19 | +0 |
| v11_intraday_region | GBPUSD | 1818 | +7,993 | 1.03 | 48% | 17 | +0 |
| v11_intraday_region | NZDUSD | 4633 | -122,901 | 0.75 | 44% | 24 | +0 |
| v11_intraday_region | USDCHF | 3541 | -26,811 | 0.93 | 47% | 20 | +0 |
| v11_intraday_region | USDJPY | 3954 | -65,456 | 0.83 | 46% | 9 | +0 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v11_intraday_region | regime4h | HIGH_VOL | 1298 | -10,875 | 47% | 0.95 |
| v11_intraday_region | regime4h | NEUTRAL | 5693 | -61,443 | 47% | 0.90 |
| v11_intraday_region | regime4h | RANGE | 7761 | -84,933 | 46% | 0.89 |
| v11_intraday_region | regime4h | TREND | 11489 | -122,460 | 47% | 0.90 |
| v11_intraday_region | month_dir | DOWN | 5605 | -17,980 | 47% | 0.97 |
| v11_intraday_region | month_dir | FLAT | 15817 | -152,404 | 47% | 0.91 |
| v11_intraday_region | month_dir | UP | 4819 | -109,327 | 47% | 0.81 |
| v11_intraday_region | month_vol | HIGH_VOL | 4679 | -65,251 | 46% | 0.90 |
| v11_intraday_region | month_vol | LOW_VOL | 21562 | -214,460 | 47% | 0.90 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v11_intraday_region | REJECTED | {"windows": "asia0_6_eu7_12_us16_20"} | vol_target | 2026-09-26T08:51 | 7b2cf2c1c2e0 |

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
