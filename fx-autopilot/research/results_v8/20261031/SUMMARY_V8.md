# FX AUTOPILOT V8 研究結果（2026-10-31 02:50 UTC、データ〜2026-10-30 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v8.yaml`

> **検証汚染の申告**: 期間・コスト・ゲートは既出。設計者は V2〜V7 の結果（2022 年の円安・ドル高で利益が集中）を知っている。 ドル・キャリーは 2022 年にドル買い（米金利 > 外国平均）になる規則なので、同じ相場への依存が出る可能性がある。 規則は論文どおりで調整パラメータはない（グリッド 1 通り × 2 候補）。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v8_dollar_carry | REJECTED | 44 | -1.5% | -0.1% | 1.75 | 0.02 | 0.03 | -17.3% | 2,082 | 28 | 0.02 | 11 | 46% | 28% | -11.2% | +10.9% | 1.05 | 4 | 69% | 0.09 | 1 | trades, sharpe, positive_years, subperiod_not_positive, few_positive_pairs, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |
| v8_dollar_carry_trend | REJECTED | 122 | -8.2% | -0.7% | 0.73 | -0.13 | -0.18 | -21.2% | -570 | 53 | — | 20 | 38% | 50% | -5.4% | -3.0% | 0.58 | 1 | 100% | 0.03 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v8_dollar_carry | REJECTED | 44 | 81% | 171% | -64,975 | 0.47 | 12% | +3.5% |
| v8_dollar_carry_trend | REJECTED | 122 | — | — | -154,009 | 0.39 | — | -8.2% |

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
| 2026.0 | +1.3% | -2.1% |

## 年別 Profit Factor（WF OOS）

| year | v8_dollar_carry | v8_dollar_carry_trend |
|---|---|---|
| 2014.0 | 0.00 | 0.32 |
| 2015.0 | 1.47 | — |
| 2016.0 | 5.63 | 2.31 |
| 2017.0 | 0.00 | — |
| 2018.0 | 17.73 | 1.09 |
| 2019.0 | — | 1.05 |
| 2020.0 | 0.00 | 0.03 |
| 2021.0 | — | 12.30 |
| 2023.0 | 0.00 | 0.38 |
| 2024.0 | 0.00 | 0.13 |
| 2025.0 | 0.00 | 0.05 |
| 2026.0 | 3.51 | 0.51 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v8_dollar_carry | AUDUSD | 6 | +6,857 | 1.38 | 33% | 29 | -8,479 |
| v8_dollar_carry | EURUSD | 7 | +14,233 | 1.76 | 29% | 15 | +7,101 |
| v8_dollar_carry | GBPUSD | 4 | -10,753 | 0.23 | 25% | 23 | -8,298 |
| v8_dollar_carry | NZDUSD | 2 | +29,357 | — | 100% | 41 | -6,328 |
| v8_dollar_carry | USDCAD | 10 | -13,874 | 0.61 | 20% | 32 | -5,378 |
| v8_dollar_carry | USDCHF | 9 | -5,215 | 0.70 | 22% | 40 | +17,203 |
| v8_dollar_carry | USDJPY | 6 | +71,012 | 5.02 | 33% | 17 | +15,313 |
| v8_dollar_carry_trend | AUDUSD | 18 | -11,354 | 0.64 | 44% | 60 | -3,099 |
| v8_dollar_carry_trend | EURUSD | 17 | -10,611 | 0.69 | 35% | 23 | +3,946 |
| v8_dollar_carry_trend | GBPUSD | 14 | -9,942 | 0.72 | 36% | 33 | -3,483 |
| v8_dollar_carry_trend | NZDUSD | 18 | -2,471 | 0.91 | 44% | 85 | -4,265 |
| v8_dollar_carry_trend | USDCAD | 18 | -14,358 | 0.57 | 50% | 51 | -3,432 |
| v8_dollar_carry_trend | USDCHF | 20 | -33,776 | 0.29 | 20% | 85 | +10,079 |
| v8_dollar_carry_trend | USDJPY | 17 | +12,939 | 1.29 | 41% | 25 | +4,750 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v8_dollar_carry | regime4h | HIGH_VOL | 10 | +35,100 | 40% | 2.42 |
| v8_dollar_carry | regime4h | NEUTRAL | 9 | -14,868 | 11% | 0.50 |
| v8_dollar_carry | regime4h | RANGE | 10 | -6,009 | 30% | 0.80 |
| v8_dollar_carry | regime4h | TREND | 15 | +77,394 | 33% | 3.04 |
| v8_dollar_carry | month_dir | DOWN | 10 | +8,473 | 30% | 1.38 |
| v8_dollar_carry | month_dir | FLAT | 23 | +37,533 | 35% | 1.56 |
| v8_dollar_carry | month_dir | UP | 11 | +45,612 | 18% | 2.41 |
| v8_dollar_carry | month_vol | HIGH_VOL | 20 | -19,812 | 25% | 0.67 |
| v8_dollar_carry | month_vol | LOW_VOL | 24 | +111,429 | 33% | 2.79 |
| v8_dollar_carry_trend | regime4h | HIGH_VOL | 4 | -2,655 | 25% | 0.78 |
| v8_dollar_carry_trend | regime4h | NEUTRAL | 39 | -53,571 | 38% | 0.40 |
| v8_dollar_carry_trend | regime4h | RANGE | 34 | +37,553 | 44% | 1.63 |
| v8_dollar_carry_trend | regime4h | TREND | 45 | -50,900 | 36% | 0.45 |
| v8_dollar_carry_trend | month_dir | DOWN | 24 | -8,666 | 38% | 0.83 |
| v8_dollar_carry_trend | month_dir | FLAT | 77 | -64,193 | 35% | 0.61 |
| v8_dollar_carry_trend | month_dir | UP | 21 | +3,285 | 52% | 1.09 |
| v8_dollar_carry_trend | month_vol | HIGH_VOL | 24 | -18,411 | 42% | 0.63 |
| v8_dollar_carry_trend | month_vol | LOW_VOL | 98 | -51,163 | 38% | 0.75 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v8_dollar_carry | REJECTED | {"rule": "carry"} | vol_target | 2026-09-26T07:33 | 6118da3a2a7b |
| v8_dollar_carry_trend | REJECTED | {"rule": "carry_and_trend"} | vol_target | 2026-09-26T07:33 | 159d7b75c555 |

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
