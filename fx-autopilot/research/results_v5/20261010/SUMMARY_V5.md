# FX AUTOPILOT V5 研究結果（2026-10-10 02:47 UTC、データ〜2026-10-09 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v5.yaml`

> **検証汚染の申告**: 期間（2010〜2026）は V1〜V4 と同じで、設計者は既存 7 ペアの結果を見ている。新規 3 ペアの成績だけが 「設計に使っていないデータ」だが、同じ期間の同じ相場環境を共有している点に注意。最終判断は LOCK 後の PAPER Forward のみ。 NZD / CAD / CHF の政策金利は変更月ベースの近似表（fxap/swap.py）。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v5_carry_trend_daily_10p | REJECTED | 291 | +8.9% | +0.7% | 1.34 | 0.20 | 0.27 | -10.1% | 372 | 45 | 0.18 | 26 | 46% | 31% | -1.2% | +10.2% | 1.04 | 4 | 94% | 0.71 | 1 | sharpe, positive_years, subperiod_not_positive, few_positive_pairs, single_regime_dependence, top5_trade_dependence, top1_trade_dependence |
| v5_carry_trend_weekly_10p | REJECTED | 156 | +1.7% | +0.1% | 1.16 | 0.07 | 0.09 | -8.8% | 229 | 35 | 0.76 | 13 | 62% | 32% | -3.6% | +5.6% | 0.80 | 3 | 49% | 0.53 | 1 | sharpe, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v5_carry_trend_weekly_10p | REJECTED | 156 | 175% | 372% | -96,950 | 0.58 | 95% | +2.0% |
| v5_carry_trend_daily_10p | REJECTED | 291 | 114% | 213% | -122,180 | 0.62 | 46% | +2.9% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v5_carry_trend_weekly_10p | v5_carry_trend_daily_10p |
|---|---|---|
| 2014.0 | +1.4% | +3.7% |
| 2015.0 | -2.5% | -0.1% |
| 2016.0 | -0.9% | +1.9% |
| 2017.0 | -2.4% | -1.7% |
| 2018.0 | -1.0% | -2.9% |
| 2019.0 | +0.5% | -2.1% |
| 2020.0 | +0.4% | +0.4% |
| 2021.0 | +0.9% | -0.2% |
| 2022.0 | +2.8% | +5.1% |
| 2023.0 | +0.7% | +1.9% |
| 2024.0 | +3.9% | +5.8% |
| 2025.0 | -3.5% | -2.6% |
| 2026.0 | +1.6% | -0.2% |

## 年別 Profit Factor（WF OOS）

| year | v5_carry_trend_weekly_10p | v5_carry_trend_daily_10p |
|---|---|---|
| 2014.0 | 1.66 | 3.75 |
| 2015.0 | 0.52 | 0.76 |
| 2016.0 | 0.46 | 1.22 |
| 2017.0 | 0.27 | 0.76 |
| 2018.0 | 0.97 | 0.49 |
| 2019.0 | 0.58 | 0.11 |
| 2020.0 | 2.36 | 1.58 |
| 2021.0 | 112.73 | 14.82 |
| 2022.0 | 0.04 | 0.94 |
| 2023.0 | 0.65 | 0.34 |
| 2024.0 | 0.14 | 0.39 |
| 2025.0 | 0.96 | 0.89 |
| 2026.0 | 3.41 | 0.49 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v5_carry_trend_weekly_10p | AUDJPY | 14 | -8,615 | 0.65 | 29% | 40 | +9,083 |
| v5_carry_trend_weekly_10p | AUDUSD | 27 | -7,175 | 0.72 | 37% | 42 | -1,925 |
| v5_carry_trend_weekly_10p | EURJPY | 12 | +15,257 | 2.32 | 50% | 26 | +424 |
| v5_carry_trend_weekly_10p | EURUSD | 15 | +56,443 | 4.52 | 53% | 22 | +1,235 |
| v5_carry_trend_weekly_10p | GBPJPY | 4 | -16,086 | 0.00 | 0% | 35 | -229 |
| v5_carry_trend_weekly_10p | GBPUSD | 9 | -14,450 | 0.03 | 22% | 40 | -895 |
| v5_carry_trend_weekly_10p | NZDUSD | 15 | -6,900 | 0.66 | 40% | 49 | -47 |
| v5_carry_trend_weekly_10p | USDCAD | 29 | -18,815 | 0.54 | 28% | 38 | -1,958 |
| v5_carry_trend_weekly_10p | USDCHF | 16 | -17,451 | 0.38 | 31% | 35 | +11,739 |
| v5_carry_trend_weekly_10p | USDJPY | 15 | +53,444 | 2.77 | 20% | 16 | +16,522 |
| v5_carry_trend_daily_10p | AUDJPY | 20 | -10,721 | 0.56 | 25% | 42 | +7,077 |
| v5_carry_trend_daily_10p | AUDUSD | 40 | +2,363 | 1.08 | 35% | 46 | -1,537 |
| v5_carry_trend_daily_10p | EURJPY | 25 | +4,978 | 1.24 | 24% | 32 | +242 |
| v5_carry_trend_daily_10p | EURUSD | 27 | +85,404 | 4.56 | 56% | 22 | +96 |
| v5_carry_trend_daily_10p | GBPJPY | 9 | -2,802 | 0.83 | 11% | 53 | +4,682 |
| v5_carry_trend_daily_10p | GBPUSD | 28 | -22,355 | 0.42 | 25% | 43 | -4,133 |
| v5_carry_trend_daily_10p | NZDUSD | 27 | -25,890 | 0.36 | 15% | 77 | -43 |
| v5_carry_trend_daily_10p | USDCAD | 52 | -9,022 | 0.79 | 38% | 46 | -2,029 |
| v5_carry_trend_daily_10p | USDCHF | 30 | -19,927 | 0.49 | 27% | 65 | +10,311 |
| v5_carry_trend_daily_10p | USDJPY | 33 | +106,243 | 3.38 | 24% | 25 | +34,730 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v5_carry_trend_weekly_10p | regime4h | HIGH_VOL | 8 | +18,309 | 38% | 3.87 |
| v5_carry_trend_weekly_10p | regime4h | NEUTRAL | 27 | +7,232 | 37% | 1.22 |
| v5_carry_trend_weekly_10p | regime4h | RANGE | 49 | +12,059 | 29% | 1.13 |
| v5_carry_trend_weekly_10p | regime4h | TREND | 72 | -1,948 | 35% | 0.98 |
| v5_carry_trend_weekly_10p | month_dir | DOWN | 34 | +18,404 | 47% | 1.43 |
| v5_carry_trend_weekly_10p | month_dir | FLAT | 85 | +22,708 | 27% | 1.17 |
| v5_carry_trend_weekly_10p | month_dir | UP | 37 | -5,460 | 35% | 0.90 |
| v5_carry_trend_weekly_10p | month_vol | HIGH_VOL | 42 | -9,354 | 33% | 0.85 |
| v5_carry_trend_weekly_10p | month_vol | LOW_VOL | 114 | +45,006 | 33% | 1.27 |
| v5_carry_trend_daily_10p | regime4h | HIGH_VOL | 18 | +11,923 | 39% | 2.15 |
| v5_carry_trend_daily_10p | regime4h | NEUTRAL | 75 | +182,861 | 33% | 3.65 |
| v5_carry_trend_daily_10p | regime4h | RANGE | 67 | -36,950 | 31% | 0.53 |
| v5_carry_trend_daily_10p | regime4h | TREND | 131 | -49,563 | 27% | 0.70 |
| v5_carry_trend_daily_10p | month_dir | DOWN | 58 | -26,986 | 36% | 0.64 |
| v5_carry_trend_daily_10p | month_dir | FLAT | 168 | +24,345 | 26% | 1.14 |
| v5_carry_trend_daily_10p | month_dir | UP | 65 | +110,911 | 37% | 2.52 |
| v5_carry_trend_daily_10p | month_vol | HIGH_VOL | 80 | -3,881 | 30% | 0.95 |
| v5_carry_trend_daily_10p | month_vol | LOW_VOL | 211 | +112,152 | 30% | 1.48 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v5_carry_trend_weekly_10p | REJECTED | {"sizing": "risk_stop"} | risk_stop | 2026-09-26T03:39 | 0a4be932bd57 |
| v5_carry_trend_daily_10p | REJECTED | {"threshold": 0.5} | risk_stop | 2026-09-26T03:39 | 28d7511bea23 |

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
USDJPY  4191               0.0219            0.2991             1.156               9             1 2013-06-06
EURUSD  4191               0.0254            0.3177             0.884               9             0 2011-10-07
GBPUSD  4191               0.0257            0.3183             1.817              11             1 2020-03-18
AUDUSD  4191               0.0303            0.3768             1.172              20             3 2020-03-12
NZDUSD  4191               0.0362            0.4022             1.450              23             2 2011-08-05
USDCAD  4191               0.0250            0.2946             0.895               9             0 2020-03-12
USDCHF  4191               0.0277            0.3102             1.041               8             1 2011-10-07
