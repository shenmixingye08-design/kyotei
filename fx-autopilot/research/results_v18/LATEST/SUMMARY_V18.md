# FX AUTOPILOT V18 研究結果（2026-10-10 14:46 UTC、データ〜2026-10-09 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v18.yaml`

> **検証汚染の申告**: これはバグ（執行タイミングの不備）の修正による再評価で、新しい優位性の探索ではない。対象は V3/V4/V6 で最も合格に近かった trend×carry であり、結果を知った上で選んでいる。ゲートは同一、保持本数 4 は登録時に固定（グリッドなし）。 DSR は V1 からの累積試行数で補正。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v18_carry_trend_daily_hold | REJECTED | 280 | +27.1% | +1.9% | 2.20 | 0.51 | 0.70 | -8.1% | 1,054 | 38 | 0.04 | 17 | 77% | 22% | +5.0% | +21.0% | 1.75 | 5 | 53% | 0.89 | 1 | top1_trade_dependence |
| v18_carry_trend_weekly_hold | REJECTED | 164 | +19.8% | +1.4% | 1.99 | 0.40 | 0.54 | -9.0% | 1,393 | 32 | 0.03 | 9 | 77% | 22% | +2.1% | +17.3% | 1.80 | 4 | 58% | 0.79 | 1 | sharpe, few_positive_pairs, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v18_carry_trend_daily_hold | REJECTED | 280 | 43% | 96% | +13,046 | 1.05 | 18% | +8.4% |
| v18_carry_trend_weekly_hold | REJECTED | 164 | 55% | 109% | -20,381 | 0.91 | 19% | +7.8% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v18_carry_trend_daily_hold | v18_carry_trend_weekly_hold |
|---|---|---|
| 2014.0 | +3.3% | +2.1% |
| 2015.0 | +1.6% | +0.6% |
| 2016.0 | +2.9% | +1.5% |
| 2017.0 | +0.2% | -0.2% |
| 2018.0 | -2.1% | -2.2% |
| 2019.0 | -1.1% | +0.9% |
| 2020.0 | -1.8% | -1.4% |
| 2021.0 | +2.2% | +0.8% |
| 2022.0 | +6.3% | +4.2% |
| 2023.0 | +5.0% | +4.4% |
| 2024.0 | +6.5% | +4.9% |
| 2025.0 | +1.2% | +1.3% |
| 2026.0 | +0.6% | +1.4% |

## 年別 Profit Factor（WF OOS）

| year | v18_carry_trend_daily_hold | v18_carry_trend_weekly_hold |
|---|---|---|
| 2014.0 | 3.99 | 3.70 |
| 2015.0 | 0.84 | 0.58 |
| 2016.0 | 1.24 | 0.90 |
| 2017.0 | 2.29 | 1.14 |
| 2018.0 | 0.42 | 0.60 |
| 2019.0 | 0.42 | 0.48 |
| 2020.0 | 0.89 | 1.06 |
| 2021.0 | 16.26 | 8.73 |
| 2022.0 | 3.89 | 0.78 |
| 2023.0 | 11.82 | 90.13 |
| 2024.0 | 0.00 | 0.13 |
| 2025.0 | 2.25 | 4.66 |
| 2026.0 | 0.46 | 2.03 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v18_carry_trend_daily_hold | AUDJPY | 42 | -1,047 | 0.98 | 26% | 39 | +9,982 |
| v18_carry_trend_daily_hold | AUDUSD | 63 | -10,796 | 0.78 | 35% | 49 | -1,362 |
| v18_carry_trend_daily_hold | EURJPY | 40 | +12,037 | 1.31 | 28% | 32 | +2,490 |
| v18_carry_trend_daily_hold | EURUSD | 37 | +84,018 | 3.45 | 57% | 21 | +1,028 |
| v18_carry_trend_daily_hold | GBPJPY | 20 | +46,435 | 3.15 | 40% | 49 | +15,636 |
| v18_carry_trend_daily_hold | GBPUSD | 32 | +33,707 | 2.74 | 56% | 47 | -5,233 |
| v18_carry_trend_daily_hold | USDJPY | 46 | +130,894 | 4.14 | 39% | 27 | +31,569 |
| v18_carry_trend_weekly_hold | AUDJPY | 22 | -599 | 0.98 | 41% | 46 | +9,857 |
| v18_carry_trend_weekly_hold | AUDUSD | 29 | -20,458 | 0.45 | 34% | 36 | -1,511 |
| v18_carry_trend_weekly_hold | EURJPY | 22 | +30,730 | 1.93 | 45% | 33 | +2,747 |
| v18_carry_trend_weekly_hold | EURUSD | 25 | +93,020 | 4.70 | 52% | 20 | +1,112 |
| v18_carry_trend_weekly_hold | GBPJPY | 15 | -9,847 | 0.72 | 27% | 46 | +4,704 |
| v18_carry_trend_weekly_hold | GBPUSD | 20 | +21,532 | 2.04 | 50% | 33 | -5,341 |
| v18_carry_trend_weekly_hold | USDJPY | 31 | +114,097 | 3.40 | 39% | 22 | +31,801 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v18_carry_trend_daily_hold | regime4h | HIGH_VOL | 24 | -18,204 | 21% | 0.51 |
| v18_carry_trend_daily_hold | regime4h | NEUTRAL | 62 | +167,538 | 35% | 4.43 |
| v18_carry_trend_daily_hold | regime4h | RANGE | 63 | +35,172 | 44% | 1.63 |
| v18_carry_trend_daily_hold | regime4h | TREND | 131 | +110,743 | 41% | 2.05 |
| v18_carry_trend_daily_hold | month_dir | DOWN | 59 | +50,456 | 51% | 1.81 |
| v18_carry_trend_daily_hold | month_dir | FLAT | 157 | +19,620 | 32% | 1.14 |
| v18_carry_trend_daily_hold | month_dir | UP | 64 | +225,172 | 45% | 5.84 |
| v18_carry_trend_daily_hold | month_vol | HIGH_VOL | 73 | +25,467 | 36% | 1.40 |
| v18_carry_trend_daily_hold | month_vol | LOW_VOL | 207 | +269,781 | 40% | 2.47 |
| v18_carry_trend_weekly_hold | regime4h | HIGH_VOL | 12 | +11,396 | 50% | 1.79 |
| v18_carry_trend_weekly_hold | regime4h | NEUTRAL | 32 | +132,006 | 31% | 3.99 |
| v18_carry_trend_weekly_hold | regime4h | RANGE | 48 | +31,125 | 46% | 1.43 |
| v18_carry_trend_weekly_hold | regime4h | TREND | 72 | +53,948 | 42% | 1.54 |
| v18_carry_trend_weekly_hold | month_dir | DOWN | 37 | +32,924 | 49% | 1.62 |
| v18_carry_trend_weekly_hold | month_dir | FLAT | 94 | +40,844 | 33% | 1.30 |
| v18_carry_trend_weekly_hold | month_dir | UP | 33 | +154,707 | 58% | 4.71 |
| v18_carry_trend_weekly_hold | month_vol | HIGH_VOL | 42 | +22,845 | 45% | 1.35 |
| v18_carry_trend_weekly_hold | month_vol | LOW_VOL | 122 | +205,631 | 40% | 2.24 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v18_carry_trend_daily_hold | REJECTED | {"threshold": 0.5} | risk_stop | 2026-10-10T14:46 | 5d8c54263e0c |
| v18_carry_trend_weekly_hold | REJECTED | {"sizing": "risk_stop"} | risk_stop | 2026-10-10T14:46 | 3e03a9025fcc |

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
