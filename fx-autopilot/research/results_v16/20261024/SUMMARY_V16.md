# FX AUTOPILOT V16 研究結果（2026-10-24 01:56 UTC、データ〜2026-10-23 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v16.yaml`

> **検証汚染の申告**: 期間・コスト・ゲートは既出。株価の情報はこれまで一度も使っていない（新しい情報源）。 3 か月・1 か月ラグは登録時に固定、パラメータは閾値 2 通りのみ。ユーロ圏の集計系列が無い場合はドイツで代用（登録時に固定）。 DSR は V1 からの累積試行数で補正。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v16_equity_rebal_carry | REJECTED | 130 | -24.3% | -2.1% | 0.59 | -0.44 | -0.58 | -31.2% | -2,043 | 82 | — | 17 | 31% | 61% | -23.3% | -1.3% | 0.50 | 2 | 100% | 0.00 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |
| v16_equity_rebal | REJECTED | 240 | -33.2% | -3.1% | 0.66 | -0.46 | -0.62 | -34.6% | -1,248 | 62 | — | 13 | 15% | 79% | -22.1% | -14.3% | 0.60 | 1 | 100% | 0.00 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v16_equity_rebal | REJECTED | 240 | — | — | -493,893 | 0.44 | — | -9.8% |
| v16_equity_rebal_carry | REJECTED | 130 | — | — | -385,824 | 0.40 | — | +1.1% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v16_equity_rebal | v16_equity_rebal_carry |
|---|---|---|
| 2014.0 | -2.5% | -4.5% |
| 2015.0 | -7.6% | -4.3% |
| 2016.0 | +7.2% | +5.0% |
| 2017.0 | -3.7% | -7.8% |
| 2018.0 | -13.8% | -5.8% |
| 2019.0 | +1.9% | -2.4% |
| 2020.0 | -4.5% | -5.8% |
| 2021.0 | -0.3% | +0.1% |
| 2022.0 | -0.4% | -1.3% |
| 2023.0 | -4.6% | -1.0% |
| 2024.0 | -4.6% | +0.7% |
| 2025.0 | -3.9% | -2.0% |
| 2026.0 | -1.6% | +2.4% |

## 年別 Profit Factor（WF OOS）

| year | v16_equity_rebal | v16_equity_rebal_carry |
|---|---|---|
| 2014.0 | 0.89 | 0.50 |
| 2015.0 | 0.16 | 0.27 |
| 2016.0 | 2.17 | 2.19 |
| 2017.0 | 0.30 | 0.00 |
| 2018.0 | 0.16 | 0.68 |
| 2019.0 | 0.89 | 0.42 |
| 2020.0 | 0.67 | 0.40 |
| 2021.0 | 1.23 | 0.42 |
| 2022.0 | 1.10 | 0.63 |
| 2023.0 | 0.36 | 0.85 |
| 2024.0 | 0.63 | 0.76 |
| 2025.0 | 0.61 | 1.36 |
| 2026.0 | 0.51 | 1.28 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v16_equity_rebal | AUDJPY | 27 | -4,145 | 0.96 | 48% | 63 | -2,456 |
| v16_equity_rebal | AUDUSD | 22 | -10,293 | 0.84 | 50% | 86 | -3,607 |
| v16_equity_rebal | EURJPY | 23 | -40,476 | 0.48 | 39% | 48 | -9,378 |
| v16_equity_rebal | EURUSD | 28 | -80,549 | 0.28 | 25% | 31 | -8,134 |
| v16_equity_rebal | GBPJPY | 30 | -551 | 0.99 | 43% | 76 | -921 |
| v16_equity_rebal | GBPUSD | 17 | -10,370 | 0.81 | 35% | 65 | -8,680 |
| v16_equity_rebal | NZDUSD | 27 | -93,813 | 0.22 | 26% | 85 | -8,577 |
| v16_equity_rebal | USDCAD | 20 | -63,331 | 0.20 | 25% | 67 | -5,498 |
| v16_equity_rebal | USDCHF | 21 | -64,230 | 0.19 | 29% | 80 | -4,542 |
| v16_equity_rebal | USDJPY | 25 | +68,126 | 1.77 | 48% | 29 | -12,045 |
| v16_equity_rebal_carry | AUDJPY | 18 | -49,862 | 0.56 | 28% | 64 | +13,485 |
| v16_equity_rebal_carry | AUDUSD | 9 | +33,164 | 2.19 | 67% | 125 | +3,818 |
| v16_equity_rebal_carry | EURJPY | 11 | -16,169 | 0.70 | 45% | 61 | -2,187 |
| v16_equity_rebal_carry | EURUSD | 17 | -29,915 | 0.63 | 47% | 52 | +5,564 |
| v16_equity_rebal_carry | GBPJPY | 16 | +16,941 | 1.32 | 44% | 94 | +11,743 |
| v16_equity_rebal_carry | GBPUSD | 6 | -15,191 | 0.49 | 33% | 51 | -134 |
| v16_equity_rebal_carry | NZDUSD | 16 | -109,074 | 0.07 | 12% | 130 | -303 |
| v16_equity_rebal_carry | USDCAD | 7 | -12,907 | 0.31 | 43% | 73 | +388 |
| v16_equity_rebal_carry | USDCHF | 14 | -57,855 | 0.15 | 29% | 140 | +17,901 |
| v16_equity_rebal_carry | USDJPY | 16 | -24,676 | 0.69 | 38% | 32 | +9,187 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v16_equity_rebal | regime4h | HIGH_VOL | 18 | -59,376 | 22% | 0.30 |
| v16_equity_rebal | regime4h | NEUTRAL | 52 | -20,775 | 48% | 0.86 |
| v16_equity_rebal | regime4h | RANGE | 73 | -98,371 | 38% | 0.57 |
| v16_equity_rebal | regime4h | TREND | 97 | -121,109 | 33% | 0.71 |
| v16_equity_rebal | month_dir | DOWN | 56 | -198,070 | 25% | 0.29 |
| v16_equity_rebal | month_dir | FLAT | 129 | -85,553 | 40% | 0.78 |
| v16_equity_rebal | month_dir | UP | 55 | -16,008 | 44% | 0.92 |
| v16_equity_rebal | month_vol | HIGH_VOL | 67 | -63,134 | 33% | 0.73 |
| v16_equity_rebal | month_vol | LOW_VOL | 173 | -236,497 | 39% | 0.63 |
| v16_equity_rebal_carry | regime4h | HIGH_VOL | 12 | -45,477 | 17% | 0.29 |
| v16_equity_rebal_carry | regime4h | NEUTRAL | 23 | -35,435 | 39% | 0.68 |
| v16_equity_rebal_carry | regime4h | RANGE | 38 | -9,904 | 45% | 0.94 |
| v16_equity_rebal_carry | regime4h | TREND | 57 | -174,729 | 35% | 0.44 |
| v16_equity_rebal_carry | month_dir | DOWN | 26 | -128,914 | 15% | 0.26 |
| v16_equity_rebal_carry | month_dir | FLAT | 73 | -129,404 | 41% | 0.60 |
| v16_equity_rebal_carry | month_dir | UP | 31 | -7,226 | 45% | 0.95 |
| v16_equity_rebal_carry | month_vol | HIGH_VOL | 38 | -109,730 | 26% | 0.48 |
| v16_equity_rebal_carry | month_vol | LOW_VOL | 92 | -155,814 | 41% | 0.64 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v16_equity_rebal | REJECTED | {"threshold": 1.0} | vol_target | 2026-09-26T10:33 | 4b771139dc34 |
| v16_equity_rebal_carry | REJECTED | {"threshold": 1.0} | vol_target | 2026-09-26T10:33 | 626674dd76eb |

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
USDJPY  4200               0.0220            0.2987             1.156               9             1 2013-06-06
EURUSD  4200               0.0256            0.3174             0.884               9             0 2011-10-07
GBPUSD  4200               0.0257            0.3181             1.817              11             1 2020-03-18
AUDUSD  4200               0.0304            0.3768             1.172              20             3 2020-03-12
NZDUSD  4200               0.0365            0.4021             1.450              23             2 2011-08-05
USDCAD  4200               0.0250            0.2945             0.895               9             0 2020-03-12
USDCHF  4200               0.0278            0.3102             1.041               8             1 2011-10-07
