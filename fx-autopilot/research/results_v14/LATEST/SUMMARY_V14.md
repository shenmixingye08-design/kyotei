# FX AUTOPILOT V14 研究結果（2026-11-07 03:10 UTC、データ〜2026-11-06 21:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v14.yaml`

> **検証汚染の申告**: 期間・コスト・ゲートは既出。設計者は V1〜V13 の結果を知っている。符号（傾きが負に予測）は論文から登録時に固定、 パラメータは閾値 2 通りのみ。DSR は V1 からの累積試行数で補正。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v14_term_ratemom | REJECTED | 115 | -8.0% | -0.6% | 0.88 | -0.08 | -0.12 | -20.7% | -590 | 70 | — | 15 | 54% | 43% | -13.6% | +6.4% | 0.77 | 5 | 98% | 0.09 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |
| v14_term | REJECTED | 103 | -28.1% | -2.5% | 0.67 | -0.27 | -0.39 | -40.7% | -1,537 | 59 | — | 14 | 23% | 58% | -32.4% | +6.4% | 0.43 | 1 | 100% | 0.03 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v14_term | REJECTED | 103 | — | — | -319,964 | 0.34 | — | +14.2% |
| v14_term_ratemom | REJECTED | 115 | — | — | -240,422 | 0.58 | — | +5.7% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v14_term | v14_term_ratemom |
|---|---|---|
| 2014.0 | -11.5% | -14.1% |
| 2015.0 | -8.8% | +2.9% |
| 2016.0 | -4.3% | +0.5% |
| 2017.0 | -1.2% | -5.0% |
| 2018.0 | +9.3% | +13.3% |
| 2019.0 | -3.7% | +0.7% |
| 2020.0 | -4.4% | +1.1% |
| 2021.0 | -12.0% | -11.2% |
| 2022.0 | -6.2% | -4.0% |
| 2023.0 | -0.7% | +4.9% |
| 2024.0 | +14.1% | +7.2% |
| 2025.0 | -0.9% | -0.9% |
| 2026.0 | +0.9% | -0.6% |

## 年別 Profit Factor（WF OOS）

| year | v14_term | v14_term_ratemom |
|---|---|---|
| 2014.0 | 0.00 | 0.18 |
| 2015.0 | 0.25 | 3.98 |
| 2016.0 | 0.69 | 0.06 |
| 2017.0 | 0.24 | 0.73 |
| 2018.0 | 9.84 | 12.08 |
| 2019.0 | 0.04 | 2.05 |
| 2020.0 | 0.18 | 0.51 |
| 2021.0 | 0.00 | 0.00 |
| 2022.0 | 1.91 | 1.10 |
| 2023.0 | 4.49 | 4.05 |
| 2024.0 | 2.00 | 13.22 |
| 2025.0 | 1.49 | 0.79 |
| 2026.0 | 0.17 | 0.49 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v14_term | AUDJPY | 12 | -66,758 | 0.09 | 8% | 36 | -19,929 |
| v14_term | AUDUSD | 12 | -1,673 | 0.97 | 33% | 73 | -1,115 |
| v14_term | EURJPY | 6 | -26,805 | 0.16 | 17% | 18 | -6,422 |
| v14_term | EURUSD | 13 | -5,778 | 0.91 | 31% | 22 | +6,746 |
| v14_term | GBPJPY | 7 | +49,798 | 3.71 | 43% | 112 | +10,661 |
| v14_term | GBPUSD | 15 | -19,701 | 0.61 | 33% | 57 | -7,304 |
| v14_term | NZDUSD | 10 | -16,624 | 0.59 | 40% | 75 | -948 |
| v14_term | USDCAD | 10 | -10,213 | 0.70 | 50% | 97 | -325 |
| v14_term | USDCHF | 8 | -19,043 | 0.44 | 25% | 80 | +1,646 |
| v14_term | USDJPY | 10 | -41,483 | 0.46 | 20% | 33 | -8,589 |
| v14_term_ratemom | AUDJPY | 11 | +4,194 | 1.07 | 36% | 69 | -9,531 |
| v14_term_ratemom | AUDUSD | 12 | -28,480 | 0.51 | 33% | 80 | +1,208 |
| v14_term_ratemom | EURJPY | 10 | +16,101 | 1.27 | 40% | 55 | -5,725 |
| v14_term_ratemom | EURUSD | 13 | +10,979 | 1.23 | 38% | 32 | +6,749 |
| v14_term_ratemom | GBPJPY | 9 | +15,960 | 1.33 | 22% | 69 | +3,147 |
| v14_term_ratemom | GBPUSD | 8 | +4,320 | 1.15 | 50% | 51 | -2,842 |
| v14_term_ratemom | NZDUSD | 13 | -3,812 | 0.94 | 38% | 103 | +2,960 |
| v14_term_ratemom | USDCAD | 9 | -9,776 | 0.73 | 44% | 88 | -1,111 |
| v14_term_ratemom | USDCHF | 16 | -13,107 | 0.85 | 44% | 109 | +1,877 |
| v14_term_ratemom | USDJPY | 14 | -64,252 | 0.30 | 29% | 36 | -3,660 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v14_term | regime4h | HIGH_VOL | 13 | -50,186 | 23% | 0.39 |
| v14_term | regime4h | NEUTRAL | 20 | -42,112 | 30% | 0.51 |
| v14_term | regime4h | RANGE | 37 | -62,377 | 30% | 0.61 |
| v14_term | regime4h | TREND | 33 | -3,607 | 33% | 0.98 |
| v14_term | month_dir | DOWN | 21 | +43,643 | 43% | 1.59 |
| v14_term | month_dir | FLAT | 53 | -192,399 | 25% | 0.29 |
| v14_term | month_dir | UP | 29 | -9,526 | 31% | 0.93 |
| v14_term | month_vol | HIGH_VOL | 36 | -27,554 | 33% | 0.82 |
| v14_term | month_vol | LOW_VOL | 67 | -130,727 | 28% | 0.61 |
| v14_term_ratemom | regime4h | HIGH_VOL | 14 | -17,494 | 29% | 0.82 |
| v14_term_ratemom | regime4h | NEUTRAL | 22 | +1,028 | 50% | 1.01 |
| v14_term_ratemom | regime4h | RANGE | 31 | +45,800 | 45% | 1.35 |
| v14_term_ratemom | regime4h | TREND | 48 | -97,206 | 29% | 0.64 |
| v14_term_ratemom | month_dir | DOWN | 19 | +125,423 | 68% | 3.73 |
| v14_term_ratemom | month_dir | FLAT | 63 | -173,897 | 33% | 0.49 |
| v14_term_ratemom | month_dir | UP | 33 | -19,398 | 27% | 0.90 |
| v14_term_ratemom | month_vol | HIGH_VOL | 35 | -94,177 | 31% | 0.43 |
| v14_term_ratemom | month_vol | LOW_VOL | 80 | +26,304 | 40% | 1.06 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v14_term | REJECTED | {"threshold": 0.5} | vol_target | 2026-09-26T10:16 | 3edf4710facf |
| v14_term_ratemom | REJECTED | {"threshold": 1.0} | vol_target | 2026-09-26T10:16 | daf5b3d93c01 |

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
USDJPY  4210               0.0220            0.2986             1.156               9             1 2013-06-06
EURUSD  4210               0.0257            0.3173             0.884               9             0 2011-10-07
GBPUSD  4210               0.0258            0.3177             1.817              11             1 2020-03-18
AUDUSD  4210               0.0304            0.3767             1.172              20             3 2020-03-12
NZDUSD  4210               0.0365            0.4009             1.450              23             2 2011-08-05
USDCAD  4210               0.0251            0.2945             0.895               9             0 2020-03-12
USDCHF  4210               0.0279            0.3100             1.041               8             1 2011-10-07
