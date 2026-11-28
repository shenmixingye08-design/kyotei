# FX AUTOPILOT V7 研究結果（2026-11-28 05:09 UTC、データ〜2026-11-27 21:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v7.yaml`

> **検証汚染の申告**: 期間（2010〜2026）・コスト・ゲートは既出。設計者は V2〜V6 の結果（トレンド×キャリーは少数トレード依存・2022 年の円安が大きい）を 知った上でこの枠組みを選んでいる。ファクターの定義は文献の標準形をそのまま使い、閾値以外のパラメータは持たない（グリッドは閾値 2 通りのみ）。 文献の数値の多くはコスト抜き・1970〜2000 年代・新興国通貨を含むため、ここで同じ効果が出る保証はない。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v7_cm_monthly | REJECTED | 125 | +19.6% | +1.4% | 1.45 | 0.23 | 0.32 | -21.7% | 2,256 | 132 | 0.08 | 11 | 62% | 31% | -2.1% | +22.1% | 1.19 | 3 | 37% | 0.68 | 1 | sharpe, subperiod_not_positive, few_positive_pairs, top5_trade_dependence, top1_trade_dependence |
| v7_carry_monthly | REJECTED | 57 | -0.2% | -0.0% | 1.32 | 0.04 | 0.05 | -18.6% | 1,760 | 67 | — | 7 | 38% | 35% | -10.2% | +11.1% | 0.95 | 5 | 94% | 0.42 | 2 | trades, sharpe, positive_years, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |
| v7_ccv_monthly | REJECTED | 98 | -5.5% | -0.4% | 0.80 | -0.06 | -0.08 | -19.1% | -1,073 | 98 | — | 10 | 38% | 30% | -8.8% | +3.6% | 0.61 | 4 | 100% | 0.29 | 2 | trades, profit_factor, sharpe, positive_years, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v7_ccv_monthly | REJECTED | 98 | — | — | -346,189 | 0.33 | — | +1.6% |
| v7_cm_monthly | REJECTED | 125 | 57% | 155% | -154,118 | 0.76 | 35% | +10.4% |
| v7_carry_monthly | REJECTED | 57 | 87% | 272% | -172,237 | 0.45 | 136% | +13.7% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v7_ccv_monthly | v7_cm_monthly | v7_carry_monthly |
|---|---|---|---|
| 2014.0 | -1.0% | +13.0% | -3.9% |
| 2015.0 | -0.3% | -0.4% | -6.9% |
| 2016.0 | +3.4% | +5.0% | +4.5% |
| 2017.0 | -4.9% | -8.8% | -4.0% |
| 2018.0 | -4.4% | +0.7% | +4.9% |
| 2019.0 | -0.4% | -4.2% | -1.0% |
| 2020.0 | -2.6% | -7.9% | -8.0% |
| 2021.0 | +1.3% | +2.2% | +4.7% |
| 2022.0 | -1.3% | +13.7% | -2.2% |
| 2023.0 | +3.3% | -2.7% | -0.0% |
| 2024.0 | -1.8% | +4.8% | +12.0% |
| 2025.0 | +2.0% | +3.5% | -5.8% |
| 2026.0 | +1.5% | +1.8% | +7.8% |

## 年別 Profit Factor（WF OOS）

| year | v7_ccv_monthly | v7_cm_monthly | v7_carry_monthly |
|---|---|---|---|
| 2014.0 | 0.00 | 8.41 | 0.00 |
| 2015.0 | 0.19 | 0.00 | 1.94 |
| 2016.0 | 2.79 | 1.69 | 0.77 |
| 2017.0 | 0.02 | 0.07 | 0.20 |
| 2018.0 | 0.00 | 1.45 | 5.32 |
| 2019.0 | 0.16 | 0.31 | 0.00 |
| 2020.0 | 0.42 | 0.16 | 0.07 |
| 2021.0 | 2.00 | 20.14 | 0.27 |
| 2022.0 | 1.69 | 1.53 | 3.13 |
| 2023.0 | 0.39 | 1.06 | 0.22 |
| 2024.0 | 0.33 | 0.63 | 0.00 |
| 2025.0 | 3.22 | 19.69 | 1.34 |
| 2026.0 | 1.48 | 1.28 | — |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v7_ccv_monthly | AUDJPY | 10 | -62,099 | 0.26 | 10% | 45 | +15,461 |
| v7_ccv_monthly | AUDUSD | 12 | -44,456 | 0.36 | 17% | 138 | -7,953 |
| v7_ccv_monthly | EURJPY | 8 | -2,325 | 0.96 | 25% | 148 | +10,484 |
| v7_ccv_monthly | EURUSD | 10 | +78,204 | 3.41 | 40% | 52 | +550 |
| v7_ccv_monthly | GBPJPY | 10 | +34,281 | 1.70 | 40% | 100 | +774 |
| v7_ccv_monthly | GBPUSD | 8 | -24,739 | 0.28 | 25% | 65 | -5,333 |
| v7_ccv_monthly | NZDUSD | 15 | -74,537 | 0.23 | 20% | 123 | -4,005 |
| v7_ccv_monthly | USDCAD | 7 | -47,563 | 0.02 | 14% | 105 | -2,005 |
| v7_ccv_monthly | USDCHF | 8 | +12,834 | 1.70 | 38% | 136 | +13,578 |
| v7_ccv_monthly | USDJPY | 10 | +25,232 | 2.13 | 40% | 58 | +14,898 |
| v7_cm_monthly | AUDJPY | 16 | -61,042 | 0.54 | 25% | 158 | +20,010 |
| v7_cm_monthly | AUDUSD | 12 | -29,935 | 0.41 | 42% | 120 | -1,776 |
| v7_cm_monthly | EURJPY | 11 | -20,944 | 0.70 | 36% | 93 | +3,947 |
| v7_cm_monthly | EURUSD | 8 | +238,456 | 14.15 | 62% | 72 | +9,348 |
| v7_cm_monthly | GBPJPY | 15 | +180,666 | 9.70 | 80% | 161 | +15,911 |
| v7_cm_monthly | GBPUSD | 12 | -39,229 | 0.40 | 33% | 69 | -372 |
| v7_cm_monthly | NZDUSD | 12 | -28,827 | 0.59 | 42% | 223 | +2,097 |
| v7_cm_monthly | USDCAD | 11 | -53,811 | 0.20 | 36% | 198 | -671 |
| v7_cm_monthly | USDCHF | 15 | -55,499 | 0.37 | 27% | 115 | +23,553 |
| v7_cm_monthly | USDJPY | 13 | +152,150 | 4.04 | 38% | 82 | +26,036 |
| v7_carry_monthly | AUDJPY | 5 | -46,622 | 0.00 | 0% | 46 | +7,761 |
| v7_carry_monthly | AUDUSD | 9 | -2,880 | 0.93 | 44% | 89 | +2,073 |
| v7_carry_monthly | EURJPY | 6 | -6,323 | 0.88 | 17% | 76 | +5,878 |
| v7_carry_monthly | EURUSD | 6 | +43,744 | 2.01 | 17% | 60 | +14,902 |
| v7_carry_monthly | GBPJPY | 4 | +67,921 | 8.35 | 75% | 73 | +20,739 |
| v7_carry_monthly | GBPUSD | 4 | +8,355 | 1.36 | 25% | 40 | +1,913 |
| v7_carry_monthly | NZDUSD | 5 | +13,490 | 1.49 | 40% | 85 | +1,428 |
| v7_carry_monthly | USDCAD | 7 | -24,341 | 0.45 | 43% | 53 | +1,382 |
| v7_carry_monthly | USDCHF | 7 | -2,096 | 0.86 | 29% | 79 | +53,443 |
| v7_carry_monthly | USDJPY | 4 | +49,088 | 4.57 | 50% | 43 | +26,571 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v7_ccv_monthly | regime4h | HIGH_VOL | 10 | +36,122 | 20% | 1.62 |
| v7_ccv_monthly | regime4h | NEUTRAL | 27 | -99,381 | 22% | 0.39 |
| v7_ccv_monthly | regime4h | RANGE | 29 | -25,469 | 31% | 0.82 |
| v7_ccv_monthly | regime4h | TREND | 32 | -16,439 | 28% | 0.89 |
| v7_ccv_monthly | month_dir | DOWN | 18 | -52,976 | 17% | 0.60 |
| v7_ccv_monthly | month_dir | FLAT | 56 | -7,507 | 27% | 0.97 |
| v7_ccv_monthly | month_dir | UP | 24 | -44,684 | 33% | 0.65 |
| v7_ccv_monthly | month_vol | HIGH_VOL | 22 | +29,066 | 18% | 1.33 |
| v7_ccv_monthly | month_vol | LOW_VOL | 76 | -134,233 | 29% | 0.69 |
| v7_cm_monthly | regime4h | HIGH_VOL | 13 | +110,244 | 62% | 3.89 |
| v7_cm_monthly | regime4h | NEUTRAL | 26 | -50,327 | 38% | 0.58 |
| v7_cm_monthly | regime4h | RANGE | 34 | +122,431 | 47% | 1.83 |
| v7_cm_monthly | regime4h | TREND | 52 | +99,637 | 35% | 1.30 |
| v7_cm_monthly | month_dir | DOWN | 25 | +110,699 | 36% | 1.59 |
| v7_cm_monthly | month_dir | FLAT | 69 | -17,596 | 39% | 0.94 |
| v7_cm_monthly | month_dir | UP | 31 | +188,881 | 52% | 2.39 |
| v7_cm_monthly | month_vol | HIGH_VOL | 36 | -8,942 | 31% | 0.95 |
| v7_cm_monthly | month_vol | LOW_VOL | 89 | +290,926 | 46% | 1.66 |
| v7_carry_monthly | regime4h | HIGH_VOL | 13 | +160,010 | 46% | 3.10 |
| v7_carry_monthly | regime4h | NEUTRAL | 15 | -72,340 | 13% | 0.10 |
| v7_carry_monthly | regime4h | RANGE | 17 | -10,482 | 24% | 0.90 |
| v7_carry_monthly | regime4h | TREND | 30 | +11,039 | 40% | 1.08 |
| v7_carry_monthly | month_dir | DOWN | 11 | +42,496 | 36% | 1.67 |
| v7_carry_monthly | month_dir | FLAT | 42 | -45,680 | 26% | 0.83 |
| v7_carry_monthly | month_dir | UP | 22 | +91,411 | 41% | 2.13 |
| v7_carry_monthly | month_vol | HIGH_VOL | 36 | +91,023 | 36% | 1.47 |
| v7_carry_monthly | month_vol | LOW_VOL | 39 | -2,797 | 28% | 0.99 |

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
