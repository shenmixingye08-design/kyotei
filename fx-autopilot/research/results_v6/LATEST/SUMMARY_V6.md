# FX AUTOPILOT V6 研究結果（2026-10-24 01:52 UTC、データ〜2026-10-23 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v6.yaml`

> **検証汚染の申告**: 規則・パラメータ・期間はすべて既出（v2_trend_carry / v3_carry_trend_7p / v4_carry_trend_daily と同一）。 新しいのは金利データだけ。したがって V6 は「新しい優位性の探索」ではなく「既存結果の頑健性チェック」。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v6_carry_trend_daily_mkt_7p | REJECTED | 233 | +25.6% | +1.8% | 2.26 | 0.49 | 0.68 | -8.1% | 1,189 | 39 | 0.04 | 10 | 62% | 24% | +5.4% | +19.2% | 1.66 | 5 | 77% | 0.94 | 1 | single_regime_dependence, top1_trade_dependence |
| v6_carry_trend_mkt_7p | REJECTED | 141 | +21.9% | +1.6% | 2.34 | 0.44 | 0.61 | -8.6% | 1,778 | 34 | 0.02 | 9 | 77% | 19% | +6.1% | +14.9% | 1.89 | 5 | 46% | 0.92 | 1 | top5_trade_dependence, top1_trade_dependence |
| v6_trend_carry_mkt_5p | REJECTED | 165 | +16.1% | +1.2% | 1.81 | 0.37 | 0.51 | -8.2% | 1,124 | 32 | 0.03 | 8 | 69% | 28% | +7.3% | +8.2% | 1.59 | 3 | 56% | 0.88 | 1 | sharpe, few_positive_pairs, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v6_trend_carry_mkt_5p | REJECTED | 165 | 64% | 137% | -68,767 | 0.70 | 13% | +0.2% |
| v6_carry_trend_mkt_7p | REJECTED | 141 | 47% | 101% | -3,720 | 0.98 | 17% | +6.3% |
| v6_carry_trend_daily_mkt_7p | REJECTED | 233 | 43% | 97% | +7,986 | 1.04 | 20% | +7.1% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v6_trend_carry_mkt_5p | v6_carry_trend_mkt_7p | v6_carry_trend_daily_mkt_7p |
|---|---|---|---|
| 2014.0 | +4.7% | +4.4% | +2.0% |
| 2015.0 | +2.2% | +1.0% | +1.9% |
| 2016.0 | +1.6% | +1.3% | +3.1% |
| 2017.0 | -0.7% | -0.2% | -0.6% |
| 2018.0 | -1.5% | -1.8% | -0.9% |
| 2019.0 | +0.1% | +0.6% | -0.4% |
| 2020.0 | -0.0% | -0.7% | -1.2% |
| 2021.0 | +0.8% | +1.4% | +1.5% |
| 2022.0 | +5.6% | +3.6% | +6.4% |
| 2023.0 | +2.2% | +4.3% | +4.6% |
| 2024.0 | +2.4% | +4.4% | +6.6% |
| 2025.0 | -2.4% | +0.3% | +0.9% |
| 2026.0 | +0.2% | +1.5% | -0.4% |

## 年別 Profit Factor（WF OOS）

| year | v6_trend_carry_mkt_5p | v6_carry_trend_mkt_7p | v6_carry_trend_daily_mkt_7p |
|---|---|---|---|
| 2014.0 | 8.03 | 7.01 | 3.38 |
| 2015.0 | 0.88 | 0.61 | 0.87 |
| 2016.0 | 0.84 | 0.80 | 1.64 |
| 2017.0 | 1.98 | 1.14 | 0.95 |
| 2018.0 | 0.57 | 0.71 | 0.78 |
| 2019.0 | 0.38 | 0.22 | 0.56 |
| 2020.0 | 1.26 | 1.67 | 1.06 |
| 2021.0 | 163.97 | 282.99 | 41.42 |
| 2022.0 | 2.44 | 0.63 | 4.18 |
| 2023.0 | 1.54 | 91.35 | 7.54 |
| 2024.0 | 0.16 | 0.00 | 0.00 |
| 2025.0 | 0.33 | 2.63 | 1.97 |
| 2026.0 | 1.09 | — | 0.07 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v6_trend_carry_mkt_5p | AUDUSD | 46 | -26,028 | 0.53 | 30% | 46 | -2,908 |
| v6_trend_carry_mkt_5p | EURJPY | 26 | +14,945 | 1.40 | 38% | 26 | +2,264 |
| v6_trend_carry_mkt_5p | EURUSD | 32 | +61,467 | 2.25 | 38% | 23 | +1,317 |
| v6_trend_carry_mkt_5p | GBPUSD | 35 | -1,171 | 0.98 | 37% | 36 | -6,630 |
| v6_trend_carry_mkt_5p | USDJPY | 26 | +136,215 | 4.88 | 38% | 22 | +30,827 |
| v6_carry_trend_mkt_7p | AUDJPY | 17 | +9,368 | 1.40 | 53% | 49 | +9,925 |
| v6_carry_trend_mkt_7p | AUDUSD | 30 | -19,632 | 0.48 | 37% | 41 | -1,682 |
| v6_carry_trend_mkt_7p | EURJPY | 16 | +32,616 | 2.99 | 50% | 31 | +3,511 |
| v6_carry_trend_mkt_7p | EURUSD | 22 | +81,224 | 4.02 | 45% | 23 | +508 |
| v6_carry_trend_mkt_7p | GBPJPY | 15 | -14,789 | 0.60 | 20% | 43 | +4,795 |
| v6_carry_trend_mkt_7p | GBPUSD | 17 | +25,313 | 2.62 | 59% | 34 | -4,617 |
| v6_carry_trend_mkt_7p | USDJPY | 24 | +136,534 | 5.66 | 33% | 23 | +31,383 |
| v6_carry_trend_daily_mkt_7p | AUDJPY | 33 | -907 | 0.98 | 24% | 44 | +10,079 |
| v6_carry_trend_daily_mkt_7p | AUDUSD | 55 | -8,727 | 0.81 | 40% | 49 | -1,297 |
| v6_carry_trend_daily_mkt_7p | EURJPY | 35 | +21,997 | 1.76 | 43% | 32 | +2,072 |
| v6_carry_trend_daily_mkt_7p | EURUSD | 29 | +78,595 | 3.46 | 62% | 25 | +1,173 |
| v6_carry_trend_daily_mkt_7p | GBPJPY | 17 | +40,827 | 3.05 | 24% | 50 | +15,795 |
| v6_carry_trend_daily_mkt_7p | GBPUSD | 27 | +32,434 | 2.87 | 56% | 45 | -4,844 |
| v6_carry_trend_daily_mkt_7p | USDJPY | 37 | +112,913 | 4.06 | 38% | 30 | +32,328 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v6_trend_carry_mkt_5p | regime4h | HIGH_VOL | 11 | +10,257 | 36% | 1.65 |
| v6_trend_carry_mkt_5p | regime4h | NEUTRAL | 40 | +16,475 | 40% | 1.39 |
| v6_trend_carry_mkt_5p | regime4h | RANGE | 42 | +103,690 | 40% | 2.74 |
| v6_trend_carry_mkt_5p | regime4h | TREND | 72 | +55,005 | 31% | 1.50 |
| v6_trend_carry_mkt_5p | month_dir | DOWN | 38 | -18,508 | 29% | 0.70 |
| v6_trend_carry_mkt_5p | month_dir | FLAT | 98 | +180,038 | 36% | 2.36 |
| v6_trend_carry_mkt_5p | month_dir | UP | 29 | +23,898 | 45% | 1.72 |
| v6_trend_carry_mkt_5p | month_vol | HIGH_VOL | 35 | +4,050 | 40% | 1.10 |
| v6_trend_carry_mkt_5p | month_vol | LOW_VOL | 130 | +181,377 | 35% | 1.97 |
| v6_carry_trend_mkt_7p | regime4h | HIGH_VOL | 11 | +4,900 | 45% | 1.31 |
| v6_carry_trend_mkt_7p | regime4h | NEUTRAL | 31 | +114,505 | 48% | 4.84 |
| v6_carry_trend_mkt_7p | regime4h | RANGE | 36 | +115,607 | 44% | 3.22 |
| v6_carry_trend_mkt_7p | regime4h | TREND | 63 | +15,621 | 37% | 1.18 |
| v6_carry_trend_mkt_7p | month_dir | DOWN | 34 | +5,199 | 41% | 1.11 |
| v6_carry_trend_mkt_7p | month_dir | FLAT | 81 | +237,538 | 40% | 3.40 |
| v6_carry_trend_mkt_7p | month_dir | UP | 26 | +7,896 | 50% | 1.20 |
| v6_carry_trend_mkt_7p | month_vol | HIGH_VOL | 40 | -149 | 42% | 1.00 |
| v6_carry_trend_mkt_7p | month_vol | LOW_VOL | 101 | +250,783 | 42% | 3.08 |
| v6_carry_trend_daily_mkt_7p | regime4h | HIGH_VOL | 15 | -15,249 | 27% | 0.41 |
| v6_carry_trend_daily_mkt_7p | regime4h | NEUTRAL | 67 | +226,059 | 45% | 5.25 |
| v6_carry_trend_daily_mkt_7p | regime4h | RANGE | 62 | +16,470 | 48% | 1.31 |
| v6_carry_trend_daily_mkt_7p | regime4h | TREND | 89 | +49,851 | 36% | 1.57 |
| v6_carry_trend_daily_mkt_7p | month_dir | DOWN | 51 | +11,825 | 51% | 1.21 |
| v6_carry_trend_daily_mkt_7p | month_dir | FLAT | 124 | +54,751 | 34% | 1.46 |
| v6_carry_trend_daily_mkt_7p | month_dir | UP | 58 | +210,555 | 48% | 5.79 |
| v6_carry_trend_daily_mkt_7p | month_vol | HIGH_VOL | 62 | +32,197 | 34% | 1.53 |
| v6_carry_trend_daily_mkt_7p | month_vol | LOW_VOL | 171 | +244,934 | 44% | 2.53 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v6_trend_carry_mkt_5p | REJECTED | {"mode": "composite", "sizing": "risk_stop"} | risk_stop | 2026-09-26T06:02 | ec40f7329345 |
| v6_carry_trend_mkt_7p | REJECTED | {"sizing": "risk_stop"} | risk_stop | 2026-09-26T06:02 | ceebd60a3757 |
| v6_carry_trend_daily_mkt_7p | REJECTED | {"threshold": 0.5} | risk_stop | 2026-09-26T06:02 | 3945f68170cf |

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
USDJPY  4200               0.0220            0.2987             1.156               9             1 2013-06-06
EURUSD  4200               0.0256            0.3174             0.884               9             0 2011-10-07
GBPUSD  4200               0.0257            0.3181             1.817              11             1 2020-03-18
AUDUSD  4200               0.0304            0.3768             1.172              20             3 2020-03-12
NZDUSD  4200               0.0365            0.4021             1.450              23             2 2011-08-05
USDCAD  4200               0.0250            0.2945             0.895               9             0 2020-03-12
USDCHF  4200               0.0278            0.3102             1.041               8             1 2011-10-07
