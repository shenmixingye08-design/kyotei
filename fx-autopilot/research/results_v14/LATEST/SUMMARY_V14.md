# FX AUTOPILOT V14 研究結果（2026-11-28 05:11 UTC、データ〜2026-11-27 21:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v14.yaml`

> **検証汚染の申告**: 期間・コスト・ゲートは既出。設計者は V1〜V13 の結果を知っている。符号（傾きが負に予測）は論文から登録時に固定、 パラメータは閾値 2 通りのみ。DSR は V1 からの累積試行数で補正。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v14_term_ratemom | REJECTED | 117 | -5.5% | -0.4% | 0.93 | -0.04 | -0.06 | -20.7% | -369 | 69 | — | 15 | 62% | 41% | -13.6% | +9.3% | 0.80 | 5 | 82% | 0.09 | 1 | profit_factor, sharpe, single_year_dependence, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |
| v14_term | REJECTED | 103 | -27.8% | -2.5% | 0.68 | -0.26 | -0.38 | -40.7% | -1,501 | 59 | — | 14 | 23% | 57% | -32.4% | +6.9% | 0.44 | 1 | 100% | 0.02 | 1 | profit_factor, sharpe, positive_years, single_year_dependence, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v14_term | REJECTED | 103 | — | — | -317,541 | 0.35 | — | +14.7% |
| v14_term_ratemom | REJECTED | 117 | — | — | -215,749 | 0.63 | — | +8.6% |

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
| 2026.0 | +1.4% | +2.1% |

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
| 2023.0 | 4.55 | 4.05 |
| 2024.0 | 2.00 | 13.22 |
| 2025.0 | 1.74 | 0.79 |
| 2026.0 | 0.14 | 2.19 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v14_term | AUDJPY | 12 | -70,052 | 0.09 | 8% | 37 | -19,821 |
| v14_term | AUDUSD | 12 | -3,585 | 0.94 | 33% | 74 | -1,096 |
| v14_term | EURJPY | 6 | -26,805 | 0.16 | 17% | 18 | -6,422 |
| v14_term | EURUSD | 13 | -2,287 | 0.96 | 31% | 22 | +6,863 |
| v14_term | GBPJPY | 7 | +49,798 | 3.71 | 43% | 112 | +10,661 |
| v14_term | GBPUSD | 15 | -19,701 | 0.61 | 33% | 57 | -7,304 |
| v14_term | NZDUSD | 10 | -15,277 | 0.62 | 40% | 75 | -954 |
| v14_term | USDCAD | 10 | -7,422 | 0.79 | 50% | 97 | -198 |
| v14_term | USDCHF | 8 | -19,043 | 0.44 | 25% | 80 | +1,646 |
| v14_term | USDJPY | 10 | -40,266 | 0.48 | 20% | 33 | -8,469 |
| v14_term_ratemom | AUDJPY | 11 | +4,194 | 1.07 | 36% | 69 | -9,531 |
| v14_term_ratemom | AUDUSD | 12 | -28,443 | 0.51 | 33% | 80 | +1,244 |
| v14_term_ratemom | EURJPY | 11 | +20,159 | 1.34 | 45% | 52 | -6,088 |
| v14_term_ratemom | EURUSD | 13 | +21,253 | 1.44 | 38% | 32 | +7,098 |
| v14_term_ratemom | GBPJPY | 10 | +18,209 | 1.37 | 30% | 64 | +2,657 |
| v14_term_ratemom | GBPUSD | 8 | +12,374 | 1.43 | 50% | 51 | -2,970 |
| v14_term_ratemom | NZDUSD | 13 | -3,812 | 0.94 | 38% | 103 | +2,960 |
| v14_term_ratemom | USDCAD | 9 | -9,776 | 0.73 | 44% | 88 | -1,111 |
| v14_term_ratemom | USDCHF | 16 | -13,107 | 0.85 | 44% | 109 | +1,877 |
| v14_term_ratemom | USDJPY | 14 | -64,252 | 0.30 | 29% | 36 | -3,660 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v14_term | regime4h | HIGH_VOL | 13 | -50,186 | 23% | 0.39 |
| v14_term | regime4h | NEUTRAL | 20 | -42,112 | 30% | 0.51 |
| v14_term | regime4h | RANGE | 37 | -62,942 | 30% | 0.61 |
| v14_term | regime4h | TREND | 33 | +597 | 33% | 1.00 |
| v14_term | month_dir | DOWN | 22 | +40,541 | 41% | 1.50 |
| v14_term | month_dir | FLAT | 52 | -186,309 | 25% | 0.30 |
| v14_term | month_dir | UP | 29 | -8,874 | 31% | 0.94 |
| v14_term | month_vol | HIGH_VOL | 35 | -24,256 | 34% | 0.84 |
| v14_term | month_vol | LOW_VOL | 68 | -130,386 | 28% | 0.62 |
| v14_term_ratemom | regime4h | HIGH_VOL | 14 | -17,494 | 29% | 0.82 |
| v14_term_ratemom | regime4h | NEUTRAL | 23 | +13,177 | 52% | 1.16 |
| v14_term_ratemom | regime4h | RANGE | 32 | +58,323 | 47% | 1.45 |
| v14_term_ratemom | regime4h | TREND | 48 | -97,206 | 29% | 0.64 |
| v14_term_ratemom | month_dir | DOWN | 20 | +135,156 | 70% | 3.94 |
| v14_term_ratemom | month_dir | FLAT | 64 | -158,958 | 34% | 0.54 |
| v14_term_ratemom | month_dir | UP | 33 | -19,398 | 27% | 0.90 |
| v14_term_ratemom | month_vol | HIGH_VOL | 35 | -94,177 | 31% | 0.43 |
| v14_term_ratemom | month_vol | LOW_VOL | 82 | +50,977 | 41% | 1.12 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v14_term | REJECTED | {"threshold": 0.5} | vol_target | 2026-09-26T10:16 | 3edf4710facf |
| v14_term_ratemom | REJECTED | {"threshold": 1.0} | vol_target | 2026-09-26T10:16 | daf5b3d93c01 |

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
