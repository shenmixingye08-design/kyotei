# FX AUTOPILOT V8 研究結果（2026-11-21 04:24 UTC、データ〜2026-11-20 21:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v8.yaml`

> **検証汚染の申告**: 期間・コスト・ゲートは既出。設計者は V2〜V7 の結果（2022 年の円安・ドル高で利益が集中）を知っている。 ドル・キャリーは 2022 年にドル買い（米金利 > 外国平均）になる規則なので、同じ相場への依存が出る可能性がある。 規則は論文どおりで調整パラメータはない（グリッド 1 通り × 2 候補）。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v8_dollar_carry | REJECTED | 44 | +1.6% | +0.1% | 2.01 | 0.06 | 0.08 | -17.3% | 2,802 | 28 | 0.01 | 11 | 46% | 26% | -11.2% | +14.3% | 1.27 | 4 | 60% | 0.15 | 1 | trades, sharpe, positive_years, subperiod_not_positive, few_positive_pairs, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |
| v8_dollar_carry_trend | REJECTED | 125 | -5.1% | -0.4% | 0.85 | -0.07 | -0.10 | -21.2% | -315 | 53 | — | 20 | 46% | 47% | -5.4% | +0.2% | 0.68 | 3 | 100% | 0.07 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v8_dollar_carry | REJECTED | 44 | 61% | 146% | -56,978 | 0.53 | 9% | +6.7% |
| v8_dollar_carry_trend | REJECTED | 125 | — | — | -126,846 | 0.50 | — | -5.1% |

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
| 2026.0 | +4.4% | +1.1% |

## 年別 Profit Factor（WF OOS）

| year | v8_dollar_carry | v8_dollar_carry_trend |
|---|---|---|
| 2014.0 | 0.00 | 0.32 |
| 2015.0 | 1.47 | — |
| 2016.0 | 5.84 | 2.31 |
| 2017.0 | 0.00 | — |
| 2018.0 | 24.80 | 1.09 |
| 2019.0 | — | 1.05 |
| 2020.0 | 0.00 | 0.03 |
| 2021.0 | — | 12.30 |
| 2023.0 | 0.00 | 0.38 |
| 2024.0 | 0.00 | 0.13 |
| 2025.0 | 0.00 | 0.05 |
| 2026.0 | 4.41 | 1.62 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v8_dollar_carry | AUDUSD | 6 | +19,880 | 2.09 | 33% | 29 | -8,713 |
| v8_dollar_carry | EURUSD | 7 | +17,519 | 1.94 | 29% | 16 | +7,212 |
| v8_dollar_carry | GBPUSD | 4 | -5,955 | 0.58 | 25% | 23 | -8,370 |
| v8_dollar_carry | NZDUSD | 2 | +32,061 | — | 100% | 41 | -6,334 |
| v8_dollar_carry | USDCAD | 10 | -10,063 | 0.72 | 20% | 32 | -5,316 |
| v8_dollar_carry | USDCHF | 9 | -2,264 | 0.87 | 22% | 40 | +17,493 |
| v8_dollar_carry | USDJPY | 6 | +72,104 | 5.08 | 33% | 17 | +15,432 |
| v8_dollar_carry_trend | AUDUSD | 19 | +287 | 1.01 | 47% | 58 | -3,309 |
| v8_dollar_carry_trend | EURUSD | 17 | -7,419 | 0.79 | 35% | 23 | +4,056 |
| v8_dollar_carry_trend | GBPUSD | 15 | -4,957 | 0.86 | 40% | 33 | -3,554 |
| v8_dollar_carry_trend | NZDUSD | 18 | +94 | 1.00 | 44% | 85 | -4,271 |
| v8_dollar_carry_trend | USDCAD | 18 | -10,247 | 0.69 | 50% | 51 | -3,371 |
| v8_dollar_carry_trend | USDCHF | 20 | -30,745 | 0.35 | 20% | 85 | +10,369 |
| v8_dollar_carry_trend | USDJPY | 18 | +13,674 | 1.30 | 44% | 24 | +4,882 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v8_dollar_carry | regime4h | HIGH_VOL | 10 | +56,207 | 40% | 3.27 |
| v8_dollar_carry | regime4h | NEUTRAL | 9 | -14,868 | 11% | 0.50 |
| v8_dollar_carry | regime4h | RANGE | 10 | -2,199 | 30% | 0.93 |
| v8_dollar_carry | regime4h | TREND | 15 | +84,141 | 33% | 3.21 |
| v8_dollar_carry | month_dir | DOWN | 10 | +26,294 | 30% | 2.17 |
| v8_dollar_carry | month_dir | FLAT | 23 | +50,284 | 35% | 1.75 |
| v8_dollar_carry | month_dir | UP | 11 | +46,703 | 18% | 2.44 |
| v8_dollar_carry | month_vol | HIGH_VOL | 20 | -11,203 | 25% | 0.81 |
| v8_dollar_carry | month_vol | LOW_VOL | 24 | +134,484 | 33% | 3.16 |
| v8_dollar_carry_trend | regime4h | HIGH_VOL | 4 | -2,655 | 25% | 0.78 |
| v8_dollar_carry_trend | regime4h | NEUTRAL | 40 | -41,282 | 40% | 0.54 |
| v8_dollar_carry_trend | regime4h | RANGE | 36 | +49,928 | 47% | 1.84 |
| v8_dollar_carry_trend | regime4h | TREND | 45 | -45,304 | 36% | 0.51 |
| v8_dollar_carry_trend | month_dir | DOWN | 26 | +7,961 | 42% | 1.16 |
| v8_dollar_carry_trend | month_dir | FLAT | 78 | -57,701 | 36% | 0.65 |
| v8_dollar_carry_trend | month_dir | UP | 21 | +10,427 | 52% | 1.27 |
| v8_dollar_carry_trend | month_vol | HIGH_VOL | 24 | -18,411 | 42% | 0.63 |
| v8_dollar_carry_trend | month_vol | LOW_VOL | 101 | -20,903 | 40% | 0.90 |

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
USDJPY  4219               0.0219            0.2986             1.156               9             1 2013-06-06
EURUSD  4219               0.0255            0.3172             0.884               9             0 2011-10-07
GBPUSD  4219               0.0256            0.3173             1.817              11             1 2020-03-18
AUDUSD  4219               0.0303            0.3765             1.172              20             3 2020-03-12
NZDUSD  4219               0.0362            0.3998             1.450              23             2 2011-08-05
USDCAD  4219               0.0249            0.2944             0.895               9             0 2020-03-12
USDCHF  4219               0.0278            0.3099             1.041               8             1 2011-10-07
