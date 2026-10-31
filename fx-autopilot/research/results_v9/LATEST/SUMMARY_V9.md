# FX AUTOPILOT V9 研究結果（2026-10-31 02:50 UTC、データ〜2026-10-30 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v9.yaml`

> **検証汚染の申告**: 期間・コスト・ゲートは既出。V2 で単一期間の週次 TSMOM（5 ペア）は不合格。V5 で 10 ペアの追加 3 ペアは弱かったが、 ペアを結果で選ばないため 10 ペアすべてを使う。規則は論文どおり（1/3/12 か月・等ウェイト）で、調整は「全期間一致のみ / 多数決」の 2 通り。 DSR は V1 からの累積試行数で補正。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v9_tsmom_multi | REJECTED | 1241 | -22.6% | -2.0% | 0.90 | -0.18 | -0.25 | -35.1% | -150 | 106 | 3.12 | 22 | 31% | 48% | -13.6% | -10.5% | 0.78 | 4 | 100% | 0.06 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v9_tsmom_multi | REJECTED | 1241 | — | — | -370,294 | 0.80 | — | -10.0% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v9_tsmom_multi |
|---|---|
| 2014.0 | +3.1% |
| 2015.0 | +9.4% |
| 2016.0 | -8.2% |
| 2017.0 | -10.9% |
| 2018.0 | -4.3% |
| 2019.0 | -1.6% |
| 2020.0 | +6.3% |
| 2021.0 | -6.4% |
| 2022.0 | +0.5% |
| 2023.0 | -1.1% |
| 2024.0 | -1.7% |
| 2025.0 | -4.3% |
| 2026.0 | -4.2% |

## 年別 Profit Factor（WF OOS）

| year | v9_tsmom_multi |
|---|---|
| 2014.0 | 1.80 |
| 2015.0 | 1.63 |
| 2016.0 | 0.40 |
| 2017.0 | 0.47 |
| 2018.0 | 0.60 |
| 2019.0 | 0.82 |
| 2020.0 | 1.46 |
| 2021.0 | 0.57 |
| 2022.0 | 1.03 |
| 2023.0 | 0.76 |
| 2024.0 | 0.95 |
| 2025.0 | 0.89 |
| 2026.0 | 0.46 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v9_tsmom_multi | AUDJPY | 104 | -22,832 | 0.86 | 32% | 111 | -6,229 |
| v9_tsmom_multi | AUDUSD | 146 | -76,486 | 0.67 | 27% | 122 | -11,742 |
| v9_tsmom_multi | EURJPY | 114 | -52,984 | 0.71 | 35% | 93 | -5,604 |
| v9_tsmom_multi | EURUSD | 132 | +4,326 | 1.02 | 35% | 47 | -13,835 |
| v9_tsmom_multi | GBPJPY | 85 | +1,158 | 1.01 | 29% | 109 | +328 |
| v9_tsmom_multi | GBPUSD | 126 | -37,071 | 0.78 | 37% | 71 | -14,385 |
| v9_tsmom_multi | NZDUSD | 121 | -24,050 | 0.86 | 35% | 179 | -10,218 |
| v9_tsmom_multi | USDCAD | 165 | +15,327 | 1.07 | 35% | 110 | -17,991 |
| v9_tsmom_multi | USDCHF | 134 | -73,751 | 0.65 | 36% | 157 | -12,434 |
| v9_tsmom_multi | USDJPY | 114 | +80,031 | 1.54 | 34% | 56 | -4,578 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v9_tsmom_multi | regime4h | HIGH_VOL | 77 | -38,346 | 23% | 0.76 |
| v9_tsmom_multi | regime4h | NEUTRAL | 260 | -49,828 | 35% | 0.87 |
| v9_tsmom_multi | regime4h | RANGE | 371 | +148,363 | 41% | 1.34 |
| v9_tsmom_multi | regime4h | TREND | 533 | -246,522 | 29% | 0.71 |
| v9_tsmom_multi | month_dir | DOWN | 253 | +234,513 | 40% | 1.62 |
| v9_tsmom_multi | month_dir | FLAT | 749 | -667,958 | 29% | 0.42 |
| v9_tsmom_multi | month_dir | UP | 239 | +247,113 | 41% | 1.82 |
| v9_tsmom_multi | month_vol | HIGH_VOL | 336 | -43,071 | 32% | 0.92 |
| v9_tsmom_multi | month_vol | LOW_VOL | 905 | -143,261 | 34% | 0.89 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v9_tsmom_multi | REJECTED | {"agree": "all"} | vol_target | 2026-09-26T07:46 | aac8fa596c13 |

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
USDJPY  4205               0.0220            0.2986             1.156               9             1 2013-06-06
EURUSD  4205               0.0256            0.3173             0.884               9             0 2011-10-07
GBPUSD  4205               0.0258            0.3179             1.817              11             1 2020-03-18
AUDUSD  4205               0.0304            0.3767             1.172              20             3 2020-03-12
NZDUSD  4205               0.0365            0.4016             1.450              23             2 2011-08-05
USDCAD  4205               0.0250            0.2945             0.895               9             0 2020-03-12
USDCHF  4205               0.0279            0.3101             1.041               8             1 2011-10-07
