# FX AUTOPILOT V7 研究結果（2026-10-31 02:49 UTC、データ〜2026-10-30 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v7.yaml`

> **検証汚染の申告**: 期間（2010〜2026）・コスト・ゲートは既出。設計者は V2〜V6 の結果（トレンド×キャリーは少数トレード依存・2022 年の円安が大きい）を 知った上でこの枠組みを選んでいる。ファクターの定義は文献の標準形をそのまま使い、閾値以外のパラメータは持たない（グリッドは閾値 2 通りのみ）。 文献の数値の多くはコスト抜き・1970〜2000 年代・新興国通貨を含むため、ここで同じ効果が出る保証はない。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v7_cm_monthly | REJECTED | 123 | +17.5% | +1.3% | 1.41 | 0.21 | 0.29 | -21.7% | 2,100 | 128 | 0.09 | 11 | 54% | 32% | -2.1% | +20.0% | 1.17 | 3 | 36% | 0.66 | 1 | sharpe, positive_years, subperiod_not_positive, few_positive_pairs, top5_trade_dependence, top1_trade_dependence |
| v7_carry_monthly | REJECTED | 57 | -2.9% | -0.2% | 1.26 | 0.01 | 0.01 | -18.6% | 1,465 | 67 | — | 7 | 38% | 39% | -10.2% | +8.2% | 0.90 | 5 | 100% | 0.38 | 2 | trades, sharpe, positive_years, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |
| v7_ccv_monthly | REJECTED | 96 | -6.7% | -0.5% | 0.76 | -0.08 | -0.11 | -19.1% | -1,302 | 96 | — | 10 | 38% | 34% | -8.8% | +2.3% | 0.58 | 4 | 100% | 0.27 | 2 | trades, profit_factor, sharpe, positive_years, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v7_ccv_monthly | REJECTED | 96 | — | — | -379,599 | 0.26 | — | +0.3% |
| v7_cm_monthly | REJECTED | 123 | 62% | 169% | -178,166 | 0.72 | 37% | +8.4% |
| v7_carry_monthly | REJECTED | 57 | 104% | 326% | -188,828 | 0.40 | 162% | +10.6% |

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
| 2026.0 | +0.1% | -0.0% | +4.9% |

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
| 2025.0 | 3.54 | 22.35 | 0.86 |
| 2026.0 | 0.25 | 0.24 | — |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v7_ccv_monthly | AUDJPY | 10 | -48,484 | 0.42 | 10% | 45 | +14,926 |
| v7_ccv_monthly | AUDUSD | 12 | -44,456 | 0.36 | 17% | 138 | -7,953 |
| v7_ccv_monthly | EURJPY | 8 | -2,325 | 0.96 | 25% | 148 | +10,484 |
| v7_ccv_monthly | EURUSD | 9 | +65,583 | 3.02 | 33% | 54 | +108 |
| v7_ccv_monthly | GBPJPY | 10 | +34,478 | 1.70 | 40% | 83 | +775 |
| v7_ccv_monthly | GBPUSD | 8 | -24,739 | 0.28 | 25% | 65 | -5,333 |
| v7_ccv_monthly | NZDUSD | 14 | -86,349 | 0.11 | 14% | 122 | -3,961 |
| v7_ccv_monthly | USDCAD | 7 | -47,563 | 0.02 | 14% | 105 | -2,005 |
| v7_ccv_monthly | USDCHF | 8 | +7,953 | 1.43 | 38% | 136 | +12,806 |
| v7_ccv_monthly | USDJPY | 10 | +20,939 | 1.94 | 40% | 58 | +14,573 |
| v7_cm_monthly | AUDJPY | 16 | -47,426 | 0.64 | 25% | 158 | +19,474 |
| v7_cm_monthly | AUDUSD | 12 | -29,935 | 0.41 | 42% | 120 | -1,776 |
| v7_cm_monthly | EURJPY | 11 | -20,944 | 0.70 | 36% | 93 | +3,947 |
| v7_cm_monthly | EURUSD | 7 | +221,628 | 13.23 | 57% | 76 | +8,759 |
| v7_cm_monthly | GBPJPY | 15 | +181,060 | 9.72 | 80% | 139 | +15,913 |
| v7_cm_monthly | GBPUSD | 12 | -39,229 | 0.40 | 33% | 69 | -372 |
| v7_cm_monthly | NZDUSD | 11 | -43,002 | 0.38 | 36% | 230 | +2,149 |
| v7_cm_monthly | USDCAD | 11 | -53,811 | 0.20 | 36% | 198 | -671 |
| v7_cm_monthly | USDCHF | 15 | -62,821 | 0.29 | 27% | 115 | +22,395 |
| v7_cm_monthly | USDJPY | 13 | +152,811 | 4.05 | 38% | 68 | +26,037 |
| v7_carry_monthly | AUDJPY | 5 | -46,622 | 0.00 | 0% | 46 | +7,761 |
| v7_carry_monthly | AUDUSD | 9 | -2,880 | 0.93 | 44% | 89 | +2,073 |
| v7_carry_monthly | EURJPY | 6 | -6,323 | 0.88 | 17% | 76 | +5,878 |
| v7_carry_monthly | EURUSD | 6 | +43,744 | 2.01 | 17% | 60 | +14,902 |
| v7_carry_monthly | GBPJPY | 4 | +69,818 | 8.56 | 75% | 73 | +20,590 |
| v7_carry_monthly | GBPUSD | 4 | +8,355 | 1.36 | 25% | 40 | +1,913 |
| v7_carry_monthly | NZDUSD | 5 | +8,098 | 1.30 | 40% | 85 | +1,445 |
| v7_carry_monthly | USDCAD | 7 | -30,658 | 0.31 | 43% | 53 | +1,218 |
| v7_carry_monthly | USDCHF | 7 | -6,977 | 0.52 | 29% | 79 | +52,671 |
| v7_carry_monthly | USDJPY | 4 | +46,942 | 4.42 | 50% | 43 | +26,408 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v7_ccv_monthly | regime4h | HIGH_VOL | 10 | +36,122 | 20% | 1.62 |
| v7_ccv_monthly | regime4h | NEUTRAL | 26 | -97,578 | 19% | 0.40 |
| v7_ccv_monthly | regime4h | RANGE | 28 | -42,187 | 29% | 0.70 |
| v7_ccv_monthly | regime4h | TREND | 32 | -21,320 | 28% | 0.86 |
| v7_ccv_monthly | month_dir | DOWN | 17 | -64,788 | 12% | 0.51 |
| v7_ccv_monthly | month_dir | FLAT | 55 | -10,609 | 25% | 0.96 |
| v7_ccv_monthly | month_dir | UP | 24 | -49,565 | 33% | 0.61 |
| v7_ccv_monthly | month_vol | HIGH_VOL | 22 | +29,066 | 18% | 1.33 |
| v7_ccv_monthly | month_vol | LOW_VOL | 74 | -154,028 | 27% | 0.64 |
| v7_cm_monthly | regime4h | HIGH_VOL | 13 | +110,244 | 62% | 3.89 |
| v7_cm_monthly | regime4h | NEUTRAL | 25 | -50,886 | 36% | 0.57 |
| v7_cm_monthly | regime4h | RANGE | 33 | +106,658 | 45% | 1.72 |
| v7_cm_monthly | regime4h | TREND | 52 | +92,316 | 35% | 1.28 |
| v7_cm_monthly | month_dir | DOWN | 24 | +96,525 | 33% | 1.51 |
| v7_cm_monthly | month_dir | FLAT | 68 | -20,147 | 38% | 0.93 |
| v7_cm_monthly | month_dir | UP | 31 | +181,953 | 52% | 2.34 |
| v7_cm_monthly | month_vol | HIGH_VOL | 36 | -8,548 | 31% | 0.95 |
| v7_cm_monthly | month_vol | LOW_VOL | 87 | +266,879 | 45% | 1.60 |
| v7_carry_monthly | regime4h | HIGH_VOL | 13 | +159,761 | 46% | 3.10 |
| v7_carry_monthly | regime4h | NEUTRAL | 15 | -72,340 | 13% | 0.10 |
| v7_carry_monthly | regime4h | RANGE | 17 | -15,875 | 24% | 0.85 |
| v7_carry_monthly | regime4h | TREND | 30 | -160 | 40% | 1.00 |
| v7_carry_monthly | month_dir | DOWN | 11 | +40,349 | 36% | 1.63 |
| v7_carry_monthly | month_dir | FLAT | 42 | -51,998 | 26% | 0.80 |
| v7_carry_monthly | month_dir | UP | 22 | +83,035 | 41% | 2.03 |
| v7_carry_monthly | month_vol | HIGH_VOL | 36 | +90,774 | 36% | 1.47 |
| v7_carry_monthly | month_vol | LOW_VOL | 39 | -19,388 | 28% | 0.91 |

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
