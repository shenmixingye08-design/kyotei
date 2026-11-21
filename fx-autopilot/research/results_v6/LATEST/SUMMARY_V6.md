# FX AUTOPILOT V6 研究結果（2026-11-21 04:23 UTC、データ〜2026-11-20 21:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v6.yaml`

> **検証汚染の申告**: 規則・パラメータ・期間はすべて既出（v2_trend_carry / v3_carry_trend_7p / v4_carry_trend_daily と同一）。 新しいのは金利データだけ。したがって V6 は「新しい優位性の探索」ではなく「既存結果の頑健性チェック」。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v6_carry_trend_daily_mkt_7p | REJECTED | 234 | +25.9% | +1.8% | 2.28 | 0.49 | 0.68 | -8.1% | 1,199 | 39 | 0.04 | 10 | 62% | 24% | +5.4% | +19.5% | 1.67 | 5 | 77% | 0.95 | 1 | single_regime_dependence, top1_trade_dependence |
| v6_carry_trend_mkt_7p | REJECTED | 141 | +22.1% | +1.6% | 2.36 | 0.44 | 0.61 | -8.6% | 1,795 | 34 | 0.02 | 9 | 77% | 19% | +6.1% | +15.1% | 1.90 | 5 | 47% | 0.93 | 1 | top5_trade_dependence, top1_trade_dependence |
| v6_trend_carry_mkt_5p | REJECTED | 167 | +17.3% | +1.2% | 1.86 | 0.39 | 0.54 | -8.2% | 1,183 | 33 | 0.03 | 8 | 69% | 27% | +7.3% | +9.2% | 1.64 | 4 | 54% | 0.90 | 1 | sharpe, few_positive_pairs, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v6_trend_carry_mkt_5p | REJECTED | 167 | 62% | 131% | -60,371 | 0.74 | 13% | +1.2% |
| v6_carry_trend_mkt_7p | REJECTED | 141 | 48% | 101% | -3,453 | 0.98 | 18% | +6.5% |
| v6_carry_trend_daily_mkt_7p | REJECTED | 234 | 43% | 96% | +10,604 | 1.05 | 20% | +7.4% |

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
| 2026.0 | +1.3% | +1.7% | -0.1% |

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
| 2021.0 | 168.26 | 290.12 | 42.44 |
| 2022.0 | 2.44 | 0.63 | 4.18 |
| 2023.0 | 1.54 | 91.35 | 7.31 |
| 2024.0 | 0.16 | 0.00 | 0.00 |
| 2025.0 | 0.33 | 2.33 | 1.76 |
| 2026.0 | 1.55 | — | 0.34 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v6_trend_carry_mkt_5p | AUDUSD | 46 | -26,026 | 0.53 | 30% | 46 | -2,907 |
| v6_trend_carry_mkt_5p | EURJPY | 26 | +16,516 | 1.45 | 38% | 32 | +2,095 |
| v6_trend_carry_mkt_5p | EURUSD | 32 | +65,392 | 2.33 | 38% | 23 | +1,454 |
| v6_trend_carry_mkt_5p | GBPUSD | 37 | +1,727 | 1.03 | 41% | 35 | -6,675 |
| v6_trend_carry_mkt_5p | USDJPY | 26 | +139,915 | 4.98 | 38% | 22 | +31,135 |
| v6_carry_trend_mkt_7p | AUDJPY | 17 | +6,472 | 1.28 | 53% | 49 | +10,059 |
| v6_carry_trend_mkt_7p | AUDUSD | 30 | -19,632 | 0.48 | 37% | 41 | -1,682 |
| v6_carry_trend_mkt_7p | EURJPY | 16 | +32,616 | 2.99 | 50% | 31 | +3,511 |
| v6_carry_trend_mkt_7p | EURUSD | 22 | +85,148 | 4.17 | 45% | 23 | +646 |
| v6_carry_trend_mkt_7p | GBPJPY | 15 | -16,999 | 0.54 | 20% | 43 | +4,943 |
| v6_carry_trend_mkt_7p | GBPUSD | 17 | +25,313 | 2.62 | 59% | 34 | -4,617 |
| v6_carry_trend_mkt_7p | USDJPY | 24 | +140,234 | 5.79 | 33% | 23 | +31,692 |
| v6_carry_trend_daily_mkt_7p | AUDJPY | 33 | -3,803 | 0.90 | 24% | 44 | +10,213 |
| v6_carry_trend_daily_mkt_7p | AUDUSD | 55 | -8,727 | 0.81 | 40% | 49 | -1,297 |
| v6_carry_trend_daily_mkt_7p | EURJPY | 36 | +22,913 | 1.79 | 44% | 31 | +2,040 |
| v6_carry_trend_daily_mkt_7p | EURUSD | 29 | +82,447 | 3.58 | 62% | 25 | +1,310 |
| v6_carry_trend_daily_mkt_7p | GBPJPY | 17 | +38,550 | 2.93 | 24% | 50 | +15,937 |
| v6_carry_trend_daily_mkt_7p | GBPUSD | 27 | +32,650 | 2.91 | 56% | 47 | -4,844 |
| v6_carry_trend_daily_mkt_7p | USDJPY | 37 | +116,614 | 4.16 | 38% | 30 | +32,636 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v6_trend_carry_mkt_5p | regime4h | HIGH_VOL | 11 | +10,257 | 36% | 1.65 |
| v6_trend_carry_mkt_5p | regime4h | NEUTRAL | 40 | +18,046 | 40% | 1.42 |
| v6_trend_carry_mkt_5p | regime4h | RANGE | 42 | +107,390 | 40% | 2.81 |
| v6_trend_carry_mkt_5p | regime4h | TREND | 74 | +61,830 | 32% | 1.56 |
| v6_trend_carry_mkt_5p | month_dir | DOWN | 40 | -15,607 | 32% | 0.75 |
| v6_trend_carry_mkt_5p | month_dir | FLAT | 98 | +189,234 | 36% | 2.43 |
| v6_trend_carry_mkt_5p | month_dir | UP | 29 | +23,898 | 45% | 1.72 |
| v6_trend_carry_mkt_5p | month_vol | HIGH_VOL | 35 | +4,050 | 40% | 1.10 |
| v6_trend_carry_mkt_5p | month_vol | LOW_VOL | 132 | +193,474 | 36% | 2.04 |
| v6_carry_trend_mkt_7p | regime4h | HIGH_VOL | 11 | +4,900 | 45% | 1.31 |
| v6_carry_trend_mkt_7p | regime4h | NEUTRAL | 31 | +109,398 | 48% | 4.67 |
| v6_carry_trend_mkt_7p | regime4h | RANGE | 36 | +119,308 | 44% | 3.30 |
| v6_carry_trend_mkt_7p | regime4h | TREND | 63 | +19,546 | 37% | 1.22 |
| v6_carry_trend_mkt_7p | month_dir | DOWN | 34 | +5,199 | 41% | 1.11 |
| v6_carry_trend_mkt_7p | month_dir | FLAT | 81 | +240,057 | 40% | 3.43 |
| v6_carry_trend_mkt_7p | month_dir | UP | 26 | +7,896 | 50% | 1.20 |
| v6_carry_trend_mkt_7p | month_vol | HIGH_VOL | 40 | -3,045 | 42% | 0.95 |
| v6_carry_trend_mkt_7p | month_vol | LOW_VOL | 101 | +256,197 | 42% | 3.12 |
| v6_carry_trend_daily_mkt_7p | regime4h | HIGH_VOL | 15 | -15,249 | 27% | 0.41 |
| v6_carry_trend_daily_mkt_7p | regime4h | NEUTRAL | 67 | +227,080 | 45% | 5.29 |
| v6_carry_trend_daily_mkt_7p | regime4h | RANGE | 62 | +20,321 | 48% | 1.38 |
| v6_carry_trend_daily_mkt_7p | regime4h | TREND | 90 | +48,492 | 37% | 1.56 |
| v6_carry_trend_daily_mkt_7p | month_dir | DOWN | 51 | +11,825 | 51% | 1.21 |
| v6_carry_trend_daily_mkt_7p | month_dir | FLAT | 125 | +56,840 | 34% | 1.48 |
| v6_carry_trend_daily_mkt_7p | month_dir | UP | 58 | +211,979 | 48% | 5.82 |
| v6_carry_trend_daily_mkt_7p | month_vol | HIGH_VOL | 62 | +29,301 | 34% | 1.49 |
| v6_carry_trend_daily_mkt_7p | month_vol | LOW_VOL | 172 | +251,343 | 44% | 2.58 |

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
