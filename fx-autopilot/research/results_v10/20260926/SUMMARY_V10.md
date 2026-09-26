# FX AUTOPILOT V10 研究結果（2026-09-26 11:57 UTC、データ〜2026-09-25 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v10.yaml`

> **検証汚染の申告**: 期間・コスト・ゲートは既出。V3 のキャリーのみ（フィルターなし、7 ペア）は 28 トレード・前半マイナスで不合格。 フィルターの考え方は論文由来で、閾値は中央値 / 80 パーセンタイルの 2 通りだけ。ペアは結果で選ばず 10 ペアすべて。 DSR は V1 からの累積試行数で補正。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v10_carry_vix | REJECTED | 490 | -12.9% | -1.1% | 0.90 | -0.17 | -0.23 | -30.0% | -197 | 102 | — | 13 | 54% | 28% | -22.1% | +11.8% | 0.75 | 3 | 100% | 0.14 | 2 | profit_factor, sharpe, positive_years, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v10_carry_vix | REJECTED | 490 | — | — | -182,429 | 0.81 | — | +15.2% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v10_carry_vix |
|---|---|
| 2014.0 | -8.0% |
| 2015.0 | -6.5% |
| 2016.0 | +1.2% |
| 2017.0 | -6.4% |
| 2018.0 | -4.4% |
| 2019.0 | -4.8% |
| 2020.0 | +0.6% |
| 2021.0 | +4.3% |
| 2022.0 | -5.2% |
| 2023.0 | +2.4% |
| 2024.0 | +6.3% |
| 2025.0 | +5.5% |
| 2026.0 | +2.7% |

## 年別 Profit Factor（WF OOS）

| year | v10_carry_vix |
|---|---|
| 2014.0 | 0.53 |
| 2015.0 | 0.35 |
| 2016.0 | 1.09 |
| 2017.0 | 0.71 |
| 2018.0 | 0.52 |
| 2019.0 | 0.73 |
| 2020.0 | 0.64 |
| 2021.0 | 3.57 |
| 2022.0 | 0.32 |
| 2023.0 | 2.00 |
| 2024.0 | 1.13 |
| 2025.0 | 2.75 |
| 2026.0 | 1.23 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v10_carry_vix | AUDJPY | 57 | -33,434 | 0.74 | 46% | 82 | +14,177 |
| v10_carry_vix | AUDUSD | 58 | -18,136 | 0.85 | 48% | 110 | +4,250 |
| v10_carry_vix | EURJPY | 25 | +24,703 | 1.84 | 48% | 130 | +5,991 |
| v10_carry_vix | EURUSD | 68 | +5,183 | 1.04 | 56% | 48 | +7,437 |
| v10_carry_vix | GBPJPY | 40 | +5,624 | 1.10 | 48% | 144 | +8,973 |
| v10_carry_vix | GBPUSD | 23 | -8,970 | 0.79 | 43% | 79 | +107 |
| v10_carry_vix | NZDUSD | 60 | -45,916 | 0.68 | 40% | 135 | +7,471 |
| v10_carry_vix | USDCAD | 53 | -7,343 | 0.93 | 49% | 132 | -213 |
| v10_carry_vix | USDCHF | 60 | -17,615 | 0.86 | 57% | 127 | +9,453 |
| v10_carry_vix | USDJPY | 46 | -560 | 0.99 | 52% | 44 | +10,537 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v10_carry_vix | regime4h | HIGH_VOL | 37 | -22,009 | 43% | 0.76 |
| v10_carry_vix | regime4h | NEUTRAL | 100 | -41,211 | 46% | 0.79 |
| v10_carry_vix | regime4h | RANGE | 157 | +17,901 | 55% | 1.06 |
| v10_carry_vix | regime4h | TREND | 230 | -109,186 | 46% | 0.77 |
| v10_carry_vix | month_dir | DOWN | 109 | -149,939 | 39% | 0.49 |
| v10_carry_vix | month_dir | FLAT | 292 | +26,890 | 51% | 1.05 |
| v10_carry_vix | month_dir | UP | 123 | -31,457 | 50% | 0.88 |
| v10_carry_vix | month_vol | HIGH_VOL | 153 | -55,812 | 48% | 0.83 |
| v10_carry_vix | month_vol | LOW_VOL | 371 | -98,693 | 48% | 0.87 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v10_carry_vix | REJECTED | {"calm": "below_median"} | vol_target | 2026-09-26T08:26 | 41e3a2922b91 |

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
