# FX AUTOPILOT V12 研究結果（2026-09-26 10:05 UTC、データ〜2026-09-25 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v12.yaml`

> **検証汚染の申告**: 期間・コスト・ゲートは既出。V7 のキャリーのみ（フィルターなし）は -2.3% で不合格、前半（2014〜2021）がマイナスだった。 フィルターは論文由来、期間は 3 か月 / 6 か月の 2 通りのみ。V7 の結果を見た後の登録であることを申告する。 DSR は V1 からの累積試行数で補正。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v12_carry_timed | REJECTED | 96 | +6.2% | +0.5% | 1.16 | 0.12 | 0.16 | -14.3% | 682 | 94 | 2.91 | 13 | 62% | 25% | -1.8% | +8.2% | 0.90 | 4 | 61% | 0.58 | 2 | trades, sharpe, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v12_carry_timed | REJECTED | 96 | 89% | 286% | -121,921 | 0.70 | 109% | +7.0% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v12_carry_timed |
|---|---|
| 2014.0 | -3.5% |
| 2015.0 | -2.7% |
| 2016.0 | +3.1% |
| 2017.0 | -3.5% |
| 2018.0 | +0.5% |
| 2019.0 | -0.4% |
| 2020.0 | +1.5% |
| 2021.0 | +3.4% |
| 2022.0 | +5.1% |
| 2023.0 | -3.8% |
| 2024.0 | +1.3% |
| 2025.0 | +1.0% |
| 2026.0 | +4.5% |

## 年別 Profit Factor（WF OOS）

| year | v12_carry_timed |
|---|---|
| 2014.0 | 0.00 |
| 2015.0 | 0.14 |
| 2016.0 | 0.93 |
| 2017.0 | 0.07 |
| 2018.0 | 1.32 |
| 2019.0 | 1.22 |
| 2021.0 | 2.56 |
| 2022.0 | 1.96 |
| 2023.0 | 0.07 |
| 2024.0 | 3.28 |
| 2025.0 | 1.31 |
| 2026.0 | 4.98 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v12_carry_timed | AUDJPY | 12 | -15,270 | 0.79 | 25% | 82 | +13,553 |
| v12_carry_timed | AUDUSD | 11 | -40,793 | 0.36 | 18% | 109 | +2,895 |
| v12_carry_timed | EURJPY | 8 | -31,097 | 0.39 | 38% | 142 | +3,046 |
| v12_carry_timed | EURUSD | 15 | +89,228 | 3.40 | 67% | 57 | +9,345 |
| v12_carry_timed | GBPJPY | 8 | -5,930 | 0.78 | 38% | 82 | +13,239 |
| v12_carry_timed | GBPUSD | 5 | -14,521 | 0.38 | 60% | 61 | +132 |
| v12_carry_timed | NZDUSD | 10 | -53,894 | 0.31 | 20% | 110 | +5,063 |
| v12_carry_timed | USDCAD | 7 | +15,015 | 1.72 | 43% | 77 | -239 |
| v12_carry_timed | USDCHF | 11 | +75,471 | 8.57 | 73% | 147 | +8,732 |
| v12_carry_timed | USDJPY | 9 | +47,244 | 3.14 | 78% | 65 | +15,595 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v12_carry_timed | regime4h | HIGH_VOL | 8 | +37,337 | 25% | 1.57 |
| v12_carry_timed | regime4h | NEUTRAL | 26 | +59,632 | 58% | 1.96 |
| v12_carry_timed | regime4h | RANGE | 41 | -100,398 | 37% | 0.51 |
| v12_carry_timed | regime4h | TREND | 47 | -25,850 | 38% | 0.88 |
| v12_carry_timed | month_dir | DOWN | 30 | -186,160 | 13% | 0.16 |
| v12_carry_timed | month_dir | FLAT | 63 | +144,978 | 49% | 1.70 |
| v12_carry_timed | month_dir | UP | 29 | +11,903 | 52% | 1.10 |
| v12_carry_timed | month_vol | HIGH_VOL | 46 | -132,453 | 24% | 0.50 |
| v12_carry_timed | month_vol | LOW_VOL | 76 | +103,174 | 51% | 1.36 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v12_carry_timed | REJECTED | {"lookback": 126} | vol_target | 2026-09-26T09:28 | f16f02e79d3e |

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
