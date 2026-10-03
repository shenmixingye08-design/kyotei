# FX AUTOPILOT V7 研究結果（2026-10-03 02:05 UTC、データ〜2026-10-02 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v7.yaml`

> **検証汚染の申告**: 期間（2010〜2026）・コスト・ゲートは既出。設計者は V2〜V6 の結果（トレンド×キャリーは少数トレード依存・2022 年の円安が大きい）を 知った上でこの枠組みを選んでいる。ファクターの定義は文献の標準形をそのまま使い、閾値以外のパラメータは持たない（グリッドは閾値 2 通りのみ）。 文献の数値の多くはコスト抜き・1970〜2000 年代・新興国通貨を含むため、ここで同じ効果が出る保証はない。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v7_cm_monthly | REJECTED | 123 | +19.7% | +1.4% | 1.43 | 0.22 | 0.31 | -21.5% | 2,411 | 135 | 0.09 | 11 | 62% | 30% | -2.4% | +22.7% | 1.17 | 3 | 39% | 0.64 | 1 | sharpe, subperiod_not_positive, few_positive_pairs, top5_trade_dependence, top1_trade_dependence |
| v7_carry_monthly | REJECTED | 58 | -1.7% | -0.1% | 1.53 | 0.02 | 0.02 | -18.8% | 2,777 | 70 | 0.23 | 7 | 46% | 24% | -11.0% | +10.4% | 1.09 | 8 | 73% | 0.36 | 2 | trades, sharpe, positive_years, subperiod_not_positive, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |
| v7_ccv_monthly | REJECTED | 130 | -16.1% | -1.4% | 0.93 | -0.18 | -0.23 | -27.0% | -355 | 93 | — | 10 | 38% | 33% | -21.8% | +7.3% | 0.76 | 3 | 53% | 0.14 | 2 | profit_factor, sharpe, positive_years, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v7_ccv_monthly | REJECTED | 130 | — | — | -318,277 | 0.53 | — | -0.5% |
| v7_cm_monthly | REJECTED | 123 | 54% | 157% | -169,617 | 0.75 | 41% | +10.1% |
| v7_carry_monthly | REJECTED | 58 | 54% | 168% | -109,279 | 0.64 | 92% | +11.6% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v7_ccv_monthly | v7_cm_monthly | v7_carry_monthly |
|---|---|---|---|
| 2014.0 | -1.0% | +12.9% | -3.9% |
| 2015.0 | -13.2% | -0.9% | -6.9% |
| 2016.0 | +3.5% | +5.3% | +4.5% |
| 2017.0 | -4.9% | -9.0% | -4.0% |
| 2018.0 | -5.5% | +0.9% | +4.9% |
| 2019.0 | -0.4% | -4.1% | -1.0% |
| 2020.0 | -2.7% | -8.1% | -8.0% |
| 2021.0 | +1.0% | +2.2% | +3.8% |
| 2022.0 | +4.4% | +13.1% | -3.4% |
| 2023.0 | +3.3% | -1.5% | +2.4% |
| 2024.0 | -1.8% | +6.4% | +7.4% |
| 2025.0 | +1.4% | +3.2% | -3.2% |
| 2026.0 | -0.1% | +0.3% | +7.4% |

## 年別 Profit Factor（WF OOS）

| year | v7_ccv_monthly | v7_cm_monthly | v7_carry_monthly |
|---|---|---|---|
| 2014.0 | 0.00 | 7.63 | 0.00 |
| 2015.0 | 0.55 | 0.00 | 1.94 |
| 2016.0 | 2.79 | 1.77 | 0.77 |
| 2017.0 | 0.02 | 0.06 | 0.20 |
| 2018.0 | 0.38 | 1.58 | 5.32 |
| 2019.0 | 0.16 | 0.31 | 0.00 |
| 2020.0 | 2.83 | 0.17 | 0.07 |
| 2021.0 | 1.86 | 20.14 | 0.27 |
| 2022.0 | 1.76 | 1.53 | 3.09 |
| 2023.0 | 0.39 | 1.74 | 1.79 |
| 2024.0 | 0.33 | 0.55 | 0.00 |
| 2025.0 | 2.83 | 14.71 | 1.67 |
| 2026.0 | 0.28 | 0.26 | 4.25 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v7_ccv_monthly | AUDJPY | 13 | -11,621 | 0.88 | 23% | 77 | +10,019 |
| v7_ccv_monthly | AUDUSD | 18 | -66,010 | 0.40 | 22% | 130 | -10,681 |
| v7_ccv_monthly | EURJPY | 15 | -14,629 | 0.84 | 33% | 93 | +9,760 |
| v7_ccv_monthly | EURUSD | 13 | +69,647 | 2.81 | 46% | 54 | -4,190 |
| v7_ccv_monthly | GBPJPY | 13 | +136,747 | 3.65 | 54% | 70 | +10,051 |
| v7_ccv_monthly | GBPUSD | 10 | -10,764 | 0.77 | 30% | 77 | -7,523 |
| v7_ccv_monthly | NZDUSD | 15 | -89,293 | 0.15 | 20% | 127 | -3,834 |
| v7_ccv_monthly | USDCAD | 11 | -67,258 | 0.07 | 18% | 98 | -4,062 |
| v7_ccv_monthly | USDCHF | 12 | -14,786 | 0.65 | 42% | 119 | +13,837 |
| v7_ccv_monthly | USDJPY | 10 | +21,763 | 1.86 | 40% | 54 | +15,043 |
| v7_cm_monthly | AUDJPY | 16 | -44,143 | 0.67 | 25% | 160 | +21,106 |
| v7_cm_monthly | AUDUSD | 12 | -33,512 | 0.40 | 42% | 127 | -1,990 |
| v7_cm_monthly | EURJPY | 11 | -22,138 | 0.71 | 36% | 98 | +3,668 |
| v7_cm_monthly | EURUSD | 7 | +232,629 | 13.83 | 57% | 78 | +12,129 |
| v7_cm_monthly | GBPJPY | 15 | +218,727 | 9.61 | 80% | 149 | +27,905 |
| v7_cm_monthly | GBPUSD | 12 | -44,761 | 0.37 | 33% | 72 | -470 |
| v7_cm_monthly | NZDUSD | 11 | -48,442 | 0.37 | 36% | 240 | +2,085 |
| v7_cm_monthly | USDCAD | 11 | -56,923 | 0.20 | 36% | 207 | -762 |
| v7_cm_monthly | USDCHF | 15 | -72,335 | 0.28 | 27% | 129 | +23,029 |
| v7_cm_monthly | USDJPY | 13 | +167,469 | 4.34 | 38% | 71 | +34,713 |
| v7_carry_monthly | AUDJPY | 5 | -38,542 | 0.00 | 0% | 39 | +7,153 |
| v7_carry_monthly | AUDUSD | 7 | +3,793 | 1.13 | 43% | 89 | +1,952 |
| v7_carry_monthly | EURJPY | 7 | +23,480 | 1.44 | 29% | 85 | +13,090 |
| v7_carry_monthly | EURUSD | 6 | +43,744 | 2.01 | 17% | 60 | +14,902 |
| v7_carry_monthly | GBPJPY | 4 | +67,678 | 8.33 | 75% | 73 | +20,448 |
| v7_carry_monthly | GBPUSD | 4 | +8,355 | 1.36 | 25% | 40 | +1,913 |
| v7_carry_monthly | NZDUSD | 5 | +8,457 | 1.31 | 40% | 85 | +1,468 |
| v7_carry_monthly | USDCAD | 8 | -6,611 | 0.85 | 50% | 57 | +1,350 |
| v7_carry_monthly | USDCHF | 8 | +3,610 | 1.16 | 25% | 96 | +58,999 |
| v7_carry_monthly | USDJPY | 4 | +47,090 | 4.43 | 50% | 43 | +26,277 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v7_ccv_monthly | regime4h | HIGH_VOL | 14 | +17,796 | 21% | 1.15 |
| v7_ccv_monthly | regime4h | NEUTRAL | 31 | -47,222 | 23% | 0.74 |
| v7_ccv_monthly | regime4h | RANGE | 43 | +15,996 | 40% | 1.09 |
| v7_ccv_monthly | regime4h | TREND | 42 | -32,773 | 36% | 0.84 |
| v7_ccv_monthly | month_dir | DOWN | 21 | -70,086 | 24% | 0.55 |
| v7_ccv_monthly | month_dir | FLAT | 72 | +3,974 | 32% | 1.01 |
| v7_ccv_monthly | month_dir | UP | 37 | +19,908 | 38% | 1.10 |
| v7_ccv_monthly | month_vol | HIGH_VOL | 36 | +41,454 | 22% | 1.24 |
| v7_ccv_monthly | month_vol | LOW_VOL | 94 | -87,658 | 36% | 0.83 |
| v7_cm_monthly | regime4h | HIGH_VOL | 13 | +106,488 | 62% | 3.42 |
| v7_cm_monthly | regime4h | NEUTRAL | 25 | -53,869 | 36% | 0.58 |
| v7_cm_monthly | regime4h | RANGE | 33 | +106,445 | 45% | 1.69 |
| v7_cm_monthly | regime4h | TREND | 52 | +137,507 | 35% | 1.39 |
| v7_cm_monthly | month_dir | DOWN | 24 | +101,097 | 33% | 1.50 |
| v7_cm_monthly | month_dir | FLAT | 68 | -34,809 | 38% | 0.90 |
| v7_cm_monthly | month_dir | UP | 31 | +230,282 | 52% | 2.61 |
| v7_cm_monthly | month_vol | HIGH_VOL | 36 | -12,624 | 31% | 0.94 |
| v7_cm_monthly | month_vol | LOW_VOL | 87 | +309,194 | 45% | 1.64 |
| v7_carry_monthly | regime4h | HIGH_VOL | 19 | +178,939 | 42% | 2.90 |
| v7_carry_monthly | regime4h | NEUTRAL | 20 | -27,790 | 30% | 0.71 |
| v7_carry_monthly | regime4h | RANGE | 19 | +64,793 | 32% | 1.76 |
| v7_carry_monthly | regime4h | TREND | 34 | -72,199 | 32% | 0.62 |
| v7_carry_monthly | month_dir | DOWN | 16 | +14,558 | 31% | 1.15 |
| v7_carry_monthly | month_dir | FLAT | 50 | +34,393 | 28% | 1.13 |
| v7_carry_monthly | month_dir | UP | 26 | +94,793 | 46% | 1.92 |
| v7_carry_monthly | month_vol | HIGH_VOL | 44 | +80,227 | 34% | 1.36 |
| v7_carry_monthly | month_vol | LOW_VOL | 48 | +63,517 | 33% | 1.26 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v7_ccv_monthly | REJECTED | {"threshold": 0.5} | vol_target | 2026-09-26T07:01 | 1146711fcbe5 |
| v7_cm_monthly | REJECTED | {"threshold": 1.0} | vol_target | 2026-09-26T07:01 | 8bfedf5a6e2d |
| v7_carry_monthly | REJECTED | {"threshold": 1.0} | vol_target | 2026-09-26T07:01 | c4e84f7cb4ee |

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
USDJPY  4186               0.0219            0.2993             1.156               9             1 2013-06-06
EURUSD  4186               0.0254            0.3179             0.884               9             0 2011-10-07
GBPUSD  4186               0.0257            0.3183             1.817              11             1 2020-03-18
AUDUSD  4186               0.0303            0.3768             1.172              20             3 2020-03-12
NZDUSD  4186               0.0361            0.4023             1.450              23             2 2011-08-05
USDCAD  4186               0.0249            0.2947             0.895               9             0 2020-03-12
USDCHF  4186               0.0276            0.3102             1.041               8             1 2011-10-07
