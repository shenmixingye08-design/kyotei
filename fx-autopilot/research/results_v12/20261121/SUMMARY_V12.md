# FX AUTOPILOT V12 研究結果（2026-11-21 04:25 UTC、データ〜2026-11-20 21:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v12.yaml`

> **検証汚染の申告**: 期間・コスト・ゲートは既出。V7 のキャリーのみ（フィルターなし）は -2.3% で不合格、前半（2014〜2021）がマイナスだった。 フィルターは論文由来、期間は 3 か月 / 6 か月の 2 通りのみ。V7 の結果を見た後の登録であることを申告する。 DSR は V1 からの累積試行数で補正。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v12_carry_timed | REJECTED | 97 | +7.0% | +0.5% | 1.19 | 0.13 | 0.18 | -14.5% | 824 | 92 | 0.49 | 13 | 54% | 30% | -4.0% | +11.4% | 0.89 | 4 | 64% | 0.61 | 2 | trades, sharpe, positive_years, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v12_carry_timed | REJECTED | 97 | 72% | 259% | -127,163 | 0.70 | 88% | +10.2% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v12_carry_timed |
|---|---|
| 2014.0 | -3.7% |
| 2015.0 | -2.7% |
| 2016.0 | +6.4% |
| 2017.0 | -3.5% |
| 2018.0 | +0.5% |
| 2019.0 | -0.4% |
| 2020.0 | -3.6% |
| 2021.0 | +3.5% |
| 2022.0 | +5.1% |
| 2023.0 | -3.9% |
| 2024.0 | +1.4% |
| 2025.0 | +1.1% |
| 2026.0 | +7.5% |

## 年別 Profit Factor（WF OOS）

| year | v12_carry_timed |
|---|---|
| 2014.0 | 0.00 |
| 2015.0 | 0.14 |
| 2016.0 | 3.41 |
| 2017.0 | 0.07 |
| 2018.0 | 1.32 |
| 2019.0 | 1.22 |
| 2020.0 | 0.08 |
| 2021.0 | 2.56 |
| 2022.0 | 1.96 |
| 2023.0 | 0.07 |
| 2024.0 | 3.28 |
| 2025.0 | 1.11 |
| 2026.0 | 8.80 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v12_carry_timed | AUDJPY | 10 | -12,224 | 0.77 | 30% | 99 | +13,806 |
| v12_carry_timed | AUDUSD | 10 | -29,781 | 0.44 | 20% | 119 | +2,445 |
| v12_carry_timed | EURJPY | 9 | -58,145 | 0.18 | 22% | 107 | +2,592 |
| v12_carry_timed | EURUSD | 15 | +110,372 | 3.49 | 60% | 49 | +9,399 |
| v12_carry_timed | GBPJPY | 9 | -9,680 | 0.68 | 33% | 80 | +13,758 |
| v12_carry_timed | GBPUSD | 7 | -10,635 | 0.54 | 71% | 54 | +7 |
| v12_carry_timed | NZDUSD | 9 | -44,619 | 0.43 | 11% | 126 | +4,631 |
| v12_carry_timed | USDCAD | 8 | +27,307 | 2.31 | 50% | 73 | +284 |
| v12_carry_timed | USDCHF | 10 | +70,102 | 7.25 | 70% | 158 | +8,139 |
| v12_carry_timed | USDJPY | 10 | +37,277 | 2.13 | 70% | 63 | +15,477 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v12_carry_timed | regime4h | HIGH_VOL | 10 | +27,829 | 30% | 1.37 |
| v12_carry_timed | regime4h | NEUTRAL | 22 | +22,832 | 59% | 1.34 |
| v12_carry_timed | regime4h | RANGE | 36 | -100,839 | 36% | 0.48 |
| v12_carry_timed | regime4h | TREND | 47 | +90,107 | 45% | 1.47 |
| v12_carry_timed | month_dir | DOWN | 20 | -112,848 | 20% | 0.27 |
| v12_carry_timed | month_dir | FLAT | 70 | +146,831 | 49% | 1.57 |
| v12_carry_timed | month_dir | UP | 25 | +5,945 | 48% | 1.05 |
| v12_carry_timed | month_vol | HIGH_VOL | 34 | -20,664 | 32% | 0.88 |
| v12_carry_timed | month_vol | LOW_VOL | 81 | +60,593 | 48% | 1.17 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v12_carry_timed | REJECTED | {"lookback": 126} | vol_target | 2026-09-26T09:28 | f16f02e79d3e |

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
