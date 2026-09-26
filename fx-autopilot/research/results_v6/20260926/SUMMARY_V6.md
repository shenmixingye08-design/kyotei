# FX AUTOPILOT V6 研究結果（2026-09-26 06:02 UTC、データ〜2026-09-25 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v6.yaml`

> **検証汚染の申告**: 規則・パラメータ・期間はすべて既出（v2_trend_carry / v3_carry_trend_7p / v4_carry_trend_daily と同一）。 新しいのは金利データだけ。したがって V6 は「新しい優位性の探索」ではなく「既存結果の頑健性チェック」。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v6_carry_trend_daily_mkt_7p | REJECTED | 224 | +27.5% | +1.9% | 2.48 | 0.52 | 0.73 | -8.1% | 1,320 | 36 | 0.03 | 10 | 69% | 23% | +5.2% | +21.2% | 1.71 | 6 | 76% | 0.96 | 1 | single_regime_dependence, top1_trade_dependence |
| v6_carry_trend_mkt_7p | REJECTED | 141 | +21.4% | +1.5% | 2.30 | 0.43 | 0.59 | -8.7% | 1,742 | 34 | 0.02 | 7 | 77% | 20% | +6.1% | +14.4% | 1.50 | 5 | 48% | 0.92 | 1 | top5_trade_dependence, top1_trade_dependence |
| v6_trend_carry_mkt_5p | REJECTED | 157 | +17.5% | +1.3% | 1.95 | 0.40 | 0.55 | -8.3% | 1,270 | 32 | 0.03 | 7 | 69% | 27% | +7.2% | +9.6% | 1.67 | 4 | 58% | 0.90 | 1 | sharpe, few_positive_pairs, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v6_trend_carry_mkt_5p | REJECTED | 157 | 61% | 128% | -56,550 | 0.73 | 13% | +1.6% |
| v6_carry_trend_mkt_7p | REJECTED | 141 | 49% | 105% | -11,092 | 0.94 | 19% | +5.9% |
| v6_carry_trend_daily_mkt_7p | REJECTED | 224 | 41% | 92% | +23,602 | 1.12 | 20% | +8.8% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v6_trend_carry_mkt_5p | v6_carry_trend_mkt_7p | v6_carry_trend_daily_mkt_7p |
|---|---|---|---|
| 2014.0 | +4.7% | +4.4% | +2.1% |
| 2015.0 | +2.2% | +1.0% | +1.6% |
| 2016.0 | +1.6% | +1.3% | +3.1% |
| 2017.0 | -0.7% | -0.2% | -0.6% |
| 2018.0 | -1.5% | -1.8% | -0.9% |
| 2019.0 | +0.1% | +0.6% | -0.4% |
| 2020.0 | -0.2% | -0.7% | -1.2% |
| 2021.0 | +0.8% | +1.4% | +1.5% |
| 2022.0 | +5.6% | +3.6% | +6.4% |
| 2023.0 | +2.2% | +4.3% | +4.6% |
| 2024.0 | +2.4% | +4.2% | +6.6% |
| 2025.0 | -1.6% | +0.4% | +1.6% |
| 2026.0 | +0.7% | +1.3% | +0.5% |

## 年別 Profit Factor（WF OOS）

| year | v6_trend_carry_mkt_5p | v6_carry_trend_mkt_7p | v6_carry_trend_daily_mkt_7p |
|---|---|---|---|
| 2014.0 | 8.03 | 7.01 | 3.38 |
| 2015.0 | 0.88 | 0.61 | 0.80 |
| 2016.0 | 0.84 | 0.80 | 1.64 |
| 2017.0 | 1.98 | 1.14 | 0.94 |
| 2018.0 | 0.57 | 0.71 | 0.78 |
| 2019.0 | 0.38 | 0.22 | 0.56 |
| 2020.0 | 1.14 | 1.67 | 1.08 |
| 2021.0 | 166.20 | 286.71 | 41.95 |
| 2022.0 | 2.44 | 0.62 | 4.36 |
| 2023.0 | 1.53 | 90.99 | 7.57 |
| 2024.0 | 0.16 | 0.05 | 0.00 |
| 2025.0 | 0.42 | 2.56 | 4.12 |
| 2026.0 | 1.60 | — | 0.00 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v6_trend_carry_mkt_5p | AUDUSD | 45 | -24,302 | 0.55 | 31% | 44 | -2,894 |
| v6_trend_carry_mkt_5p | EURJPY | 24 | +17,773 | 1.57 | 38% | 26 | +2,472 |
| v6_trend_carry_mkt_5p | EURUSD | 29 | +66,196 | 2.56 | 38% | 23 | +1,517 |
| v6_trend_carry_mkt_5p | GBPUSD | 33 | +1,731 | 1.04 | 42% | 35 | -6,444 |
| v6_trend_carry_mkt_5p | USDJPY | 26 | +138,068 | 4.93 | 38% | 22 | +31,812 |
| v6_carry_trend_mkt_7p | AUDJPY | 17 | +9,813 | 1.42 | 53% | 49 | +10,266 |
| v6_carry_trend_mkt_7p | AUDUSD | 30 | -19,743 | 0.48 | 37% | 39 | -1,700 |
| v6_carry_trend_mkt_7p | EURJPY | 16 | +30,957 | 2.88 | 50% | 30 | +3,816 |
| v6_carry_trend_mkt_7p | EURUSD | 22 | +77,533 | 3.82 | 45% | 23 | +270 |
| v6_carry_trend_mkt_7p | GBPJPY | 15 | -14,861 | 0.60 | 20% | 43 | +6,177 |
| v6_carry_trend_mkt_7p | GBPUSD | 17 | +23,428 | 2.33 | 59% | 32 | -4,552 |
| v6_carry_trend_mkt_7p | USDJPY | 24 | +138,462 | 5.73 | 33% | 23 | +32,511 |
| v6_carry_trend_daily_mkt_7p | AUDJPY | 33 | +683 | 1.02 | 24% | 45 | +10,420 |
| v6_carry_trend_daily_mkt_7p | AUDUSD | 54 | -5,693 | 0.86 | 41% | 42 | -1,228 |
| v6_carry_trend_daily_mkt_7p | EURJPY | 34 | +27,584 | 2.20 | 44% | 26 | +2,382 |
| v6_carry_trend_daily_mkt_7p | EURUSD | 25 | +84,755 | 4.43 | 64% | 20 | +1,071 |
| v6_carry_trend_daily_mkt_7p | GBPJPY | 16 | +41,992 | 3.18 | 25% | 46 | +17,734 |
| v6_carry_trend_daily_mkt_7p | GBPUSD | 25 | +31,467 | 3.15 | 56% | 44 | -4,680 |
| v6_carry_trend_daily_mkt_7p | USDJPY | 37 | +114,841 | 4.12 | 38% | 30 | +33,455 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v6_trend_carry_mkt_5p | regime4h | HIGH_VOL | 11 | +10,193 | 36% | 1.65 |
| v6_trend_carry_mkt_5p | regime4h | NEUTRAL | 37 | +22,597 | 41% | 1.65 |
| v6_trend_carry_mkt_5p | regime4h | RANGE | 40 | +115,931 | 45% | 3.27 |
| v6_trend_carry_mkt_5p | regime4h | TREND | 69 | +50,747 | 30% | 1.47 |
| v6_trend_carry_mkt_5p | month_dir | DOWN | 38 | -21,093 | 29% | 0.68 |
| v6_trend_carry_mkt_5p | month_dir | FLAT | 90 | +201,263 | 38% | 2.85 |
| v6_trend_carry_mkt_5p | month_dir | UP | 29 | +19,298 | 45% | 1.54 |
| v6_trend_carry_mkt_5p | month_vol | HIGH_VOL | 36 | +2,510 | 42% | 1.06 |
| v6_trend_carry_mkt_5p | month_vol | LOW_VOL | 121 | +196,957 | 36% | 2.18 |
| v6_carry_trend_mkt_7p | regime4h | HIGH_VOL | 10 | +8,876 | 50% | 1.74 |
| v6_carry_trend_mkt_7p | regime4h | NEUTRAL | 33 | +110,824 | 48% | 4.22 |
| v6_carry_trend_mkt_7p | regime4h | RANGE | 36 | +116,735 | 44% | 3.28 |
| v6_carry_trend_mkt_7p | regime4h | TREND | 62 | +9,153 | 35% | 1.10 |
| v6_carry_trend_mkt_7p | month_dir | DOWN | 34 | -571 | 38% | 0.99 |
| v6_carry_trend_mkt_7p | month_dir | FLAT | 81 | +240,971 | 41% | 3.57 |
| v6_carry_trend_mkt_7p | month_dir | UP | 26 | +5,187 | 50% | 1.13 |
| v6_carry_trend_mkt_7p | month_vol | HIGH_VOL | 41 | +364 | 44% | 1.01 |
| v6_carry_trend_mkt_7p | month_vol | LOW_VOL | 100 | +245,224 | 41% | 3.00 |
| v6_carry_trend_daily_mkt_7p | regime4h | HIGH_VOL | 14 | -9,377 | 29% | 0.53 |
| v6_carry_trend_daily_mkt_7p | regime4h | NEUTRAL | 62 | +231,974 | 45% | 6.24 |
| v6_carry_trend_daily_mkt_7p | regime4h | RANGE | 62 | +15,952 | 47% | 1.29 |
| v6_carry_trend_daily_mkt_7p | regime4h | TREND | 86 | +57,080 | 37% | 1.71 |
| v6_carry_trend_daily_mkt_7p | month_dir | DOWN | 45 | +17,567 | 53% | 1.38 |
| v6_carry_trend_daily_mkt_7p | month_dir | FLAT | 122 | +58,754 | 34% | 1.51 |
| v6_carry_trend_daily_mkt_7p | month_dir | UP | 57 | +219,308 | 49% | 6.76 |
| v6_carry_trend_daily_mkt_7p | month_vol | HIGH_VOL | 59 | +43,039 | 36% | 1.84 |
| v6_carry_trend_daily_mkt_7p | month_vol | LOW_VOL | 165 | +252,590 | 44% | 2.70 |

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
USD     199     2026-08        -0.117             0.143            1.225
EUR     169     2024-01        -0.228             0.242            1.176
JPY     168     2023-12        -0.139             0.139            0.350
GBP     169     2024-01        -0.152             0.159            1.140
AUD     200     2026-08        -0.167             0.197            0.910
NZD     200     2026-08        -0.173             0.181            0.680
CAD     200     2026-08         0.052             0.084            0.422
CHF     200     2026-08         0.034             0.066            0.353
```

## データ品質: Dukascopy と米連銀 H.10 正午レートの突き合わせ（日次）

  pair  days  median_abs_diff_pct  p99_abs_diff_pct  max_abs_diff_pct  days_gt_0_5pct  days_gt_1pct  worst_day
USDJPY  4181               0.0219            0.2995             1.156               9             1 2013-06-06
EURUSD  4181               0.0253            0.3181             0.884               9             0 2011-10-07
GBPUSD  4181               0.0257            0.3184             1.817              11             1 2020-03-18
AUDUSD  4181               0.0303            0.3768             1.172              20             3 2020-03-12
NZDUSD  4181               0.0361            0.4023             1.450              23             2 2011-08-05
USDCAD  4181               0.0248            0.2948             0.895               9             0 2020-03-12
USDCHF  4181               0.0276            0.3103             1.041               8             1 2011-10-07
