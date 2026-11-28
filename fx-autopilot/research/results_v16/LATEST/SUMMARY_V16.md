# FX AUTOPILOT V16 研究結果（2026-11-28 05:12 UTC、データ〜2026-11-27 21:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v16.yaml`

> **検証汚染の申告**: 期間・コスト・ゲートは既出。株価の情報はこれまで一度も使っていない（新しい情報源）。 3 か月・1 か月ラグは登録時に固定、パラメータは閾値 2 通りのみ。ユーロ圏の集計系列が無い場合はドイツで代用（登録時に固定）。 DSR は V1 からの累積試行数で補正。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v16_equity_rebal_carry | REJECTED | 133 | -24.2% | -2.1% | 0.59 | -0.43 | -0.57 | -31.2% | -1,989 | 85 | — | 17 | 31% | 60% | -23.3% | -1.2% | 0.50 | 2 | 100% | 0.00 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |
| v16_equity_rebal | REJECTED | 244 | -35.6% | -3.4% | 0.64 | -0.50 | -0.68 | -36.3% | -1,320 | 63 | — | 13 | 15% | 79% | -22.1% | -17.3% | 0.60 | 1 | 100% | 0.00 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v16_equity_rebal | REJECTED | 244 | — | — | -516,300 | 0.43 | — | -13.0% |
| v16_equity_rebal_carry | REJECTED | 133 | — | — | -381,586 | 0.41 | — | +1.2% |

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
| 2026.0 | -5.1% | +2.6% |

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
| 2025.0 | 0.61 | 1.18 |
| 2026.0 | 0.33 | 1.81 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v16_equity_rebal | AUDJPY | 28 | -10,737 | 0.90 | 46% | 61 | -2,265 |
| v16_equity_rebal | AUDUSD | 22 | -20,710 | 0.71 | 45% | 87 | -3,635 |
| v16_equity_rebal | EURJPY | 23 | -40,437 | 0.48 | 39% | 52 | -9,378 |
| v16_equity_rebal | EURUSD | 28 | -80,549 | 0.28 | 25% | 31 | -8,134 |
| v16_equity_rebal | GBPJPY | 31 | -3,270 | 0.97 | 42% | 74 | -755 |
| v16_equity_rebal | GBPUSD | 17 | -10,370 | 0.81 | 35% | 65 | -8,680 |
| v16_equity_rebal | NZDUSD | 28 | -102,369 | 0.21 | 25% | 85 | -8,862 |
| v16_equity_rebal | USDCAD | 21 | -57,491 | 0.28 | 29% | 65 | -5,334 |
| v16_equity_rebal | USDCHF | 21 | -64,230 | 0.19 | 29% | 80 | -4,542 |
| v16_equity_rebal | USDJPY | 25 | +68,126 | 1.77 | 48% | 29 | -12,045 |
| v16_equity_rebal_carry | AUDJPY | 18 | -58,000 | 0.49 | 28% | 64 | +13,913 |
| v16_equity_rebal_carry | AUDUSD | 9 | +33,164 | 2.19 | 67% | 125 | +3,818 |
| v16_equity_rebal_carry | EURJPY | 11 | -16,169 | 0.70 | 45% | 61 | -2,187 |
| v16_equity_rebal_carry | EURUSD | 17 | -29,915 | 0.63 | 47% | 52 | +5,564 |
| v16_equity_rebal_carry | GBPJPY | 17 | +14,024 | 1.25 | 41% | 99 | +11,909 |
| v16_equity_rebal_carry | GBPUSD | 6 | -15,191 | 0.49 | 33% | 51 | -134 |
| v16_equity_rebal_carry | NZDUSD | 16 | -109,074 | 0.07 | 12% | 130 | -303 |
| v16_equity_rebal_carry | USDCAD | 8 | -4,146 | 0.78 | 50% | 70 | +634 |
| v16_equity_rebal_carry | USDCHF | 14 | -58,107 | 0.15 | 29% | 160 | +17,902 |
| v16_equity_rebal_carry | USDJPY | 17 | -21,097 | 0.74 | 41% | 31 | +9,539 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v16_equity_rebal | regime4h | HIGH_VOL | 18 | -59,376 | 22% | 0.30 |
| v16_equity_rebal | regime4h | NEUTRAL | 53 | -39,748 | 45% | 0.77 |
| v16_equity_rebal | regime4h | RANGE | 74 | -101,052 | 38% | 0.56 |
| v16_equity_rebal | regime4h | TREND | 99 | -121,861 | 33% | 0.71 |
| v16_equity_rebal | month_dir | DOWN | 58 | -213,218 | 24% | 0.28 |
| v16_equity_rebal | month_dir | FLAT | 131 | -92,811 | 39% | 0.77 |
| v16_equity_rebal | month_dir | UP | 55 | -16,008 | 44% | 0.92 |
| v16_equity_rebal | month_vol | HIGH_VOL | 67 | -63,134 | 33% | 0.73 |
| v16_equity_rebal | month_vol | LOW_VOL | 177 | -258,904 | 38% | 0.61 |
| v16_equity_rebal_carry | regime4h | HIGH_VOL | 12 | -45,477 | 17% | 0.29 |
| v16_equity_rebal_carry | regime4h | NEUTRAL | 23 | -43,573 | 39% | 0.60 |
| v16_equity_rebal_carry | regime4h | RANGE | 40 | -9,242 | 45% | 0.94 |
| v16_equity_rebal_carry | regime4h | TREND | 58 | -166,220 | 36% | 0.47 |
| v16_equity_rebal_carry | month_dir | DOWN | 26 | -128,914 | 15% | 0.26 |
| v16_equity_rebal_carry | month_dir | FLAT | 76 | -128,119 | 42% | 0.61 |
| v16_equity_rebal_carry | month_dir | UP | 31 | -7,478 | 45% | 0.95 |
| v16_equity_rebal_carry | month_vol | HIGH_VOL | 38 | -109,730 | 26% | 0.48 |
| v16_equity_rebal_carry | month_vol | LOW_VOL | 95 | -154,781 | 42% | 0.64 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v16_equity_rebal | REJECTED | {"threshold": 1.0} | vol_target | 2026-09-26T10:33 | 4b771139dc34 |
| v16_equity_rebal_carry | REJECTED | {"threshold": 1.0} | vol_target | 2026-09-26T10:33 | 626674dd76eb |

CHALLENGER でも自動で Champion にはならない。Champion 昇格は LOCK 後 PAPER Forward（3 か月・20 取引・プラス・乖離）合格が必須。

## データ品質: 政策金利近似表（旧）と FRED 市場金利（3 か月物）の差（2010〜、%ポイント）

```
ccy  months market_last  mean_diff_pp  mean_abs_diff_pp  max_abs_diff_pp
USD     201     2026-10        -0.107             0.133            1.225
EUR     193     2026-01        -0.190             0.223            1.176
JPY     201     2026-09        -0.177             0.178            1.181
GBP     193     2026-01        -0.116             0.154            1.140
AUD     202     2026-10        -0.176             0.207            1.200
NZD     202     2026-10        -0.178             0.186            0.750
CAD     202     2026-10         0.050             0.084            0.422
CHF     202     2026-10         0.034             0.066            0.353
```

## データ品質: Dukascopy と米連銀 H.10 正午レートの突き合わせ（日次）

  pair  days  median_abs_diff_pct  p99_abs_diff_pct  max_abs_diff_pct  days_gt_0_5pct  days_gt_1pct  worst_day
USDJPY  4224               0.0219            0.2986             1.156               9             1 2013-06-06
EURUSD  4224               0.0254            0.3172             0.884               9             0 2011-10-07
GBPUSD  4224               0.0255            0.3171             1.817              11             1 2020-03-18
AUDUSD  4224               0.0303            0.3765             1.172              20             3 2020-03-12
NZDUSD  4224               0.0361            0.3991             1.450              23             2 2011-08-05
USDCAD  4224               0.0248            0.2944             0.895               9             0 2020-03-12
USDCHF  4224               0.0276            0.3098             1.041               8             1 2011-10-07
