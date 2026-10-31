# FX AUTOPILOT V6 研究結果（2026-10-31 02:48 UTC、データ〜2026-10-30 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v6.yaml`

> **検証汚染の申告**: 規則・パラメータ・期間はすべて既出（v2_trend_carry / v3_carry_trend_7p / v4_carry_trend_daily と同一）。 新しいのは金利データだけ。したがって V6 は「新しい優位性の探索」ではなく「既存結果の頑健性チェック」。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v6_carry_trend_daily_mkt_7p | REJECTED | 233 | +26.0% | +1.8% | 2.28 | 0.50 | 0.69 | -8.1% | 1,206 | 39 | 0.04 | 10 | 62% | 24% | +5.4% | +19.6% | 1.68 | 5 | 77% | 0.95 | 1 | single_regime_dependence, top1_trade_dependence |
| v6_carry_trend_mkt_7p | REJECTED | 141 | +22.3% | +1.6% | 2.36 | 0.45 | 0.61 | -8.6% | 1,806 | 34 | 0.02 | 9 | 77% | 19% | +6.1% | +15.2% | 1.91 | 5 | 46% | 0.92 | 1 | top5_trade_dependence, top1_trade_dependence |
| v6_trend_carry_mkt_5p | REJECTED | 165 | +16.3% | +1.2% | 1.82 | 0.37 | 0.52 | -8.2% | 1,136 | 32 | 0.03 | 8 | 69% | 28% | +7.3% | +8.3% | 1.60 | 3 | 56% | 0.88 | 1 | sharpe, few_positive_pairs, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v6_trend_carry_mkt_5p | REJECTED | 165 | 64% | 136% | -68,218 | 0.70 | 13% | +0.4% |
| v6_carry_trend_mkt_7p | REJECTED | 141 | 47% | 101% | -1,758 | 0.99 | 17% | +6.7% |
| v6_carry_trend_daily_mkt_7p | REJECTED | 233 | 43% | 97% | +8,671 | 1.04 | 20% | +7.4% |

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
| 2026.0 | +0.4% | +1.9% | -0.1% |

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
| 2021.0 | 165.73 | 285.92 | 41.84 |
| 2022.0 | 2.44 | 0.63 | 4.18 |
| 2023.0 | 1.54 | 91.35 | 7.66 |
| 2024.0 | 0.16 | 0.00 | 0.00 |
| 2025.0 | 0.33 | 2.73 | 2.01 |
| 2026.0 | 1.12 | — | 0.11 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v6_trend_carry_mkt_5p | AUDUSD | 46 | -26,028 | 0.53 | 30% | 46 | -2,908 |
| v6_trend_carry_mkt_5p | EURJPY | 26 | +14,778 | 1.40 | 38% | 26 | +2,221 |
| v6_trend_carry_mkt_5p | EURUSD | 32 | +62,183 | 2.26 | 38% | 23 | +1,343 |
| v6_trend_carry_mkt_5p | GBPUSD | 35 | -1,171 | 0.98 | 37% | 36 | -6,630 |
| v6_trend_carry_mkt_5p | USDJPY | 26 | +137,732 | 4.92 | 38% | 22 | +30,898 |
| v6_carry_trend_mkt_7p | AUDJPY | 17 | +9,837 | 1.43 | 53% | 49 | +9,960 |
| v6_carry_trend_mkt_7p | AUDUSD | 30 | -19,632 | 0.48 | 37% | 41 | -1,682 |
| v6_carry_trend_mkt_7p | EURJPY | 16 | +32,616 | 2.99 | 50% | 31 | +3,511 |
| v6_carry_trend_mkt_7p | EURUSD | 22 | +81,940 | 4.05 | 45% | 23 | +535 |
| v6_carry_trend_mkt_7p | GBPJPY | 15 | -13,542 | 0.64 | 20% | 43 | +4,835 |
| v6_carry_trend_mkt_7p | GBPUSD | 17 | +25,313 | 2.62 | 59% | 34 | -4,617 |
| v6_carry_trend_mkt_7p | USDJPY | 24 | +138,051 | 5.71 | 33% | 23 | +31,455 |
| v6_carry_trend_daily_mkt_7p | AUDJPY | 33 | -437 | 0.99 | 24% | 44 | +10,115 |
| v6_carry_trend_daily_mkt_7p | AUDUSD | 55 | -8,727 | 0.81 | 40% | 49 | -1,297 |
| v6_carry_trend_daily_mkt_7p | EURJPY | 35 | +21,997 | 1.76 | 43% | 32 | +2,072 |
| v6_carry_trend_daily_mkt_7p | EURUSD | 29 | +79,280 | 3.48 | 62% | 25 | +1,199 |
| v6_carry_trend_daily_mkt_7p | GBPJPY | 17 | +42,073 | 3.11 | 24% | 50 | +15,835 |
| v6_carry_trend_daily_mkt_7p | GBPUSD | 27 | +32,434 | 2.87 | 56% | 45 | -4,844 |
| v6_carry_trend_daily_mkt_7p | USDJPY | 37 | +114,431 | 4.11 | 38% | 30 | +32,399 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v6_trend_carry_mkt_5p | regime4h | HIGH_VOL | 11 | +10,257 | 36% | 1.65 |
| v6_trend_carry_mkt_5p | regime4h | NEUTRAL | 40 | +16,309 | 40% | 1.38 |
| v6_trend_carry_mkt_5p | regime4h | RANGE | 42 | +105,207 | 40% | 2.77 |
| v6_trend_carry_mkt_5p | regime4h | TREND | 72 | +55,721 | 31% | 1.50 |
| v6_trend_carry_mkt_5p | month_dir | DOWN | 38 | -18,508 | 29% | 0.70 |
| v6_trend_carry_mkt_5p | month_dir | FLAT | 98 | +182,104 | 36% | 2.38 |
| v6_trend_carry_mkt_5p | month_dir | UP | 29 | +23,898 | 45% | 1.72 |
| v6_trend_carry_mkt_5p | month_vol | HIGH_VOL | 35 | +4,050 | 40% | 1.10 |
| v6_trend_carry_mkt_5p | month_vol | LOW_VOL | 130 | +183,444 | 35% | 1.99 |
| v6_carry_trend_mkt_7p | regime4h | HIGH_VOL | 11 | +4,900 | 45% | 1.31 |
| v6_carry_trend_mkt_7p | regime4h | NEUTRAL | 31 | +116,221 | 48% | 4.90 |
| v6_carry_trend_mkt_7p | regime4h | RANGE | 36 | +117,125 | 44% | 3.25 |
| v6_carry_trend_mkt_7p | regime4h | TREND | 63 | +16,337 | 37% | 1.18 |
| v6_carry_trend_mkt_7p | month_dir | DOWN | 34 | +5,199 | 41% | 1.11 |
| v6_carry_trend_mkt_7p | month_dir | FLAT | 81 | +241,488 | 40% | 3.44 |
| v6_carry_trend_mkt_7p | month_dir | UP | 26 | +7,896 | 50% | 1.20 |
| v6_carry_trend_mkt_7p | month_vol | HIGH_VOL | 40 | +320 | 42% | 1.00 |
| v6_carry_trend_mkt_7p | month_vol | LOW_VOL | 101 | +254,263 | 42% | 3.11 |
| v6_carry_trend_daily_mkt_7p | regime4h | HIGH_VOL | 15 | -15,249 | 27% | 0.41 |
| v6_carry_trend_daily_mkt_7p | regime4h | NEUTRAL | 67 | +228,046 | 45% | 5.29 |
| v6_carry_trend_daily_mkt_7p | regime4h | RANGE | 62 | +17,155 | 48% | 1.32 |
| v6_carry_trend_daily_mkt_7p | regime4h | TREND | 89 | +51,098 | 36% | 1.58 |
| v6_carry_trend_daily_mkt_7p | month_dir | DOWN | 51 | +11,825 | 51% | 1.21 |
| v6_carry_trend_daily_mkt_7p | month_dir | FLAT | 124 | +55,906 | 34% | 1.47 |
| v6_carry_trend_daily_mkt_7p | month_dir | UP | 58 | +213,319 | 48% | 5.85 |
| v6_carry_trend_daily_mkt_7p | month_vol | HIGH_VOL | 62 | +32,666 | 34% | 1.54 |
| v6_carry_trend_daily_mkt_7p | month_vol | LOW_VOL | 171 | +248,384 | 44% | 2.56 |

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
USDJPY  4205               0.0220            0.2986             1.156               9             1 2013-06-06
EURUSD  4205               0.0256            0.3173             0.884               9             0 2011-10-07
GBPUSD  4205               0.0258            0.3179             1.817              11             1 2020-03-18
AUDUSD  4205               0.0304            0.3767             1.172              20             3 2020-03-12
NZDUSD  4205               0.0365            0.4016             1.450              23             2 2011-08-05
USDCAD  4205               0.0250            0.2945             0.895               9             0 2020-03-12
USDCHF  4205               0.0279            0.3101             1.041               8             1 2011-10-07
