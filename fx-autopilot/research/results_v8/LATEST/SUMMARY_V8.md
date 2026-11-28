# FX AUTOPILOT V8 研究結果（2026-11-28 05:09 UTC、データ〜2026-11-27 21:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v8.yaml`

> **検証汚染の申告**: 期間・コスト・ゲートは既出。設計者は V2〜V7 の結果（2022 年の円安・ドル高で利益が集中）を知っている。 ドル・キャリーは 2022 年にドル買い（米金利 > 外国平均）になる規則なので、同じ相場への依存が出る可能性がある。 規則は論文どおりで調整パラメータはない（グリッド 1 通り × 2 候補）。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v8_dollar_carry | REJECTED | 44 | +1.6% | +0.1% | 2.01 | 0.06 | 0.08 | -17.3% | 2,802 | 28 | 0.01 | 11 | 46% | 26% | -11.2% | +14.3% | 1.27 | 4 | 60% | 0.14 | 1 | trades, sharpe, positive_years, subperiod_not_positive, few_positive_pairs, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |
| v8_dollar_carry_trend | REJECTED | 125 | -5.2% | -0.4% | 0.84 | -0.07 | -0.10 | -21.2% | -321 | 53 | — | 20 | 46% | 47% | -5.4% | +0.2% | 0.68 | 2 | 100% | 0.07 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v8_dollar_carry | REJECTED | 44 | 62% | 147% | -57,543 | 0.53 | 9% | +6.7% |
| v8_dollar_carry_trend | REJECTED | 125 | — | — | -127,126 | 0.50 | — | -5.2% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v8_dollar_carry | v8_dollar_carry_trend |
|---|---|---|
| 2014.0 | -7.5% | -3.0% |
| 2015.0 | -6.0% | +0.0% |
| 2016.0 | +7.5% | +4.7% |
| 2017.0 | -6.9% | -3.3% |
| 2018.0 | +5.4% | +1.0% |
| 2019.0 | -0.6% | -1.4% |
| 2020.0 | -5.9% | -3.7% |
| 2021.0 | +3.4% | +0.5% |
| 2022.0 | +7.8% | +7.9% |
| 2023.0 | -0.6% | -2.1% |
| 2024.0 | +10.0% | +1.7% |
| 2025.0 | -7.1% | -7.7% |
| 2026.0 | +4.4% | +1.0% |

## 年別 Profit Factor（WF OOS）

| year | v8_dollar_carry | v8_dollar_carry_trend |
|---|---|---|
| 2014.0 | 0.00 | 0.32 |
| 2015.0 | 1.47 | — |
| 2016.0 | 5.92 | 2.31 |
| 2017.0 | 0.00 | — |
| 2018.0 | 24.78 | 1.09 |
| 2019.0 | — | 1.05 |
| 2020.0 | 0.00 | 0.03 |
| 2021.0 | — | 12.30 |
| 2023.0 | 0.00 | 0.38 |
| 2024.0 | 0.00 | 0.13 |
| 2025.0 | 0.00 | 0.05 |
| 2026.0 | 4.25 | 1.59 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v8_dollar_carry | AUDUSD | 6 | +19,182 | 2.05 | 33% | 30 | -8,781 |
| v8_dollar_carry | EURUSD | 7 | +18,208 | 1.97 | 29% | 15 | +7,248 |
| v8_dollar_carry | GBPUSD | 4 | -5,997 | 0.57 | 25% | 23 | -8,393 |
| v8_dollar_carry | NZDUSD | 2 | +32,310 | — | 100% | 41 | -6,336 |
| v8_dollar_carry | USDCAD | 10 | -10,807 | 0.70 | 20% | 32 | -5,296 |
| v8_dollar_carry | USDCHF | 9 | -2,786 | 0.84 | 22% | 40 | +17,589 |
| v8_dollar_carry | USDJPY | 6 | +73,158 | 5.14 | 33% | 17 | +15,476 |
| v8_dollar_carry_trend | AUDUSD | 19 | -611 | 0.98 | 47% | 59 | -3,377 |
| v8_dollar_carry_trend | EURUSD | 17 | -6,832 | 0.80 | 35% | 23 | +4,093 |
| v8_dollar_carry_trend | GBPUSD | 15 | -5,075 | 0.86 | 40% | 33 | -3,578 |
| v8_dollar_carry_trend | NZDUSD | 18 | +192 | 1.01 | 44% | 85 | -4,273 |
| v8_dollar_carry_trend | USDCAD | 18 | -11,189 | 0.66 | 50% | 51 | -3,350 |
| v8_dollar_carry_trend | USDCHF | 20 | -31,335 | 0.34 | 20% | 85 | +10,465 |
| v8_dollar_carry_trend | USDJPY | 18 | +14,729 | 1.33 | 44% | 24 | +4,926 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v8_dollar_carry | regime4h | HIGH_VOL | 10 | +56,155 | 40% | 3.27 |
| v8_dollar_carry | regime4h | NEUTRAL | 9 | -14,868 | 11% | 0.50 |
| v8_dollar_carry | regime4h | RANGE | 10 | -2,942 | 30% | 0.90 |
| v8_dollar_carry | regime4h | TREND | 15 | +84,923 | 33% | 3.23 |
| v8_dollar_carry | month_dir | DOWN | 10 | +25,553 | 30% | 2.13 |
| v8_dollar_carry | month_dir | FLAT | 23 | +49,957 | 35% | 1.75 |
| v8_dollar_carry | month_dir | UP | 11 | +47,758 | 18% | 2.47 |
| v8_dollar_carry | month_vol | HIGH_VOL | 20 | -11,989 | 25% | 0.80 |
| v8_dollar_carry | month_vol | LOW_VOL | 24 | +135,257 | 33% | 3.18 |
| v8_dollar_carry_trend | regime4h | HIGH_VOL | 4 | -2,655 | 25% | 0.78 |
| v8_dollar_carry_trend | regime4h | NEUTRAL | 40 | -41,756 | 40% | 0.54 |
| v8_dollar_carry_trend | regime4h | RANGE | 36 | +50,086 | 47% | 1.84 |
| v8_dollar_carry_trend | regime4h | TREND | 45 | -45,797 | 36% | 0.51 |
| v8_dollar_carry_trend | month_dir | DOWN | 26 | +6,944 | 42% | 1.14 |
| v8_dollar_carry_trend | month_dir | FLAT | 78 | -55,961 | 36% | 0.66 |
| v8_dollar_carry_trend | month_dir | UP | 21 | +8,895 | 52% | 1.23 |
| v8_dollar_carry_trend | month_vol | HIGH_VOL | 24 | -18,411 | 42% | 0.63 |
| v8_dollar_carry_trend | month_vol | LOW_VOL | 101 | -21,711 | 40% | 0.89 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v8_dollar_carry | REJECTED | {"rule": "carry"} | vol_target | 2026-09-26T07:33 | 6118da3a2a7b |
| v8_dollar_carry_trend | REJECTED | {"rule": "carry_and_trend"} | vol_target | 2026-09-26T07:33 | 159d7b75c555 |

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
