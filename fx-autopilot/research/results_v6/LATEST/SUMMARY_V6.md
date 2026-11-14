# FX AUTOPILOT V6 研究結果（2026-11-14 03:14 UTC、データ〜2026-11-13 21:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v6.yaml`

> **検証汚染の申告**: 規則・パラメータ・期間はすべて既出（v2_trend_carry / v3_carry_trend_7p / v4_carry_trend_daily と同一）。 新しいのは金利データだけ。したがって V6 は「新しい優位性の探索」ではなく「既存結果の頑健性チェック」。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v6_carry_trend_daily_mkt_7p | REJECTED | 233 | +26.4% | +1.8% | 2.30 | 0.50 | 0.69 | -8.1% | 1,226 | 40 | 0.04 | 10 | 69% | 24% | +5.4% | +20.0% | 1.69 | 5 | 77% | 0.95 | 1 | single_regime_dependence, top1_trade_dependence |
| v6_carry_trend_mkt_7p | REJECTED | 141 | +22.7% | +1.6% | 2.39 | 0.45 | 0.62 | -8.6% | 1,837 | 34 | 0.02 | 9 | 77% | 19% | +6.1% | +15.6% | 1.93 | 5 | 47% | 0.93 | 1 | top1_trade_dependence |
| v6_trend_carry_mkt_5p | REJECTED | 167 | +17.2% | +1.2% | 1.86 | 0.39 | 0.54 | -8.2% | 1,176 | 33 | 0.03 | 8 | 69% | 27% | +7.3% | +9.1% | 1.63 | 3 | 56% | 0.89 | 1 | sharpe, few_positive_pairs, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v6_trend_carry_mkt_5p | REJECTED | 167 | 64% | 132% | -63,727 | 0.72 | 13% | +1.1% |
| v6_carry_trend_mkt_7p | REJECTED | 141 | 48% | 100% | +136 | 1.00 | 17% | +7.0% |
| v6_carry_trend_daily_mkt_7p | REJECTED | 233 | 43% | 97% | +9,646 | 1.04 | 20% | +7.8% |

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
| 2026.0 | +1.2% | +2.2% | +0.3% |

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
| 2021.0 | 170.89 | 294.47 | 43.05 |
| 2022.0 | 2.44 | 0.63 | 4.18 |
| 2023.0 | 1.54 | 91.35 | 7.67 |
| 2024.0 | 0.16 | 0.00 | 0.00 |
| 2025.0 | 0.33 | 2.59 | 1.82 |
| 2026.0 | 1.36 | — | 0.24 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v6_trend_carry_mkt_5p | AUDUSD | 47 | -24,599 | 0.56 | 32% | 45 | -2,937 |
| v6_trend_carry_mkt_5p | EURJPY | 26 | +14,407 | 1.39 | 38% | 32 | +2,122 |
| v6_trend_carry_mkt_5p | EURUSD | 32 | +64,570 | 2.31 | 38% | 23 | +1,405 |
| v6_trend_carry_mkt_5p | GBPUSD | 36 | -124 | 1.00 | 39% | 35 | -6,662 |
| v6_trend_carry_mkt_5p | USDJPY | 26 | +142,173 | 5.05 | 38% | 22 | +31,067 |
| v6_carry_trend_mkt_7p | AUDJPY | 17 | +7,309 | 1.32 | 53% | 49 | +10,043 |
| v6_carry_trend_mkt_7p | AUDUSD | 30 | -19,632 | 0.48 | 37% | 41 | -1,682 |
| v6_carry_trend_mkt_7p | EURJPY | 16 | +32,616 | 2.99 | 50% | 31 | +3,511 |
| v6_carry_trend_mkt_7p | EURUSD | 22 | +84,326 | 4.14 | 45% | 23 | +597 |
| v6_carry_trend_mkt_7p | GBPJPY | 15 | -13,426 | 0.64 | 20% | 43 | +4,929 |
| v6_carry_trend_mkt_7p | GBPUSD | 17 | +25,313 | 2.62 | 59% | 34 | -4,617 |
| v6_carry_trend_mkt_7p | USDJPY | 24 | +142,492 | 5.86 | 33% | 23 | +31,623 |
| v6_carry_trend_daily_mkt_7p | AUDJPY | 33 | -2,965 | 0.93 | 24% | 44 | +10,197 |
| v6_carry_trend_daily_mkt_7p | AUDUSD | 55 | -8,727 | 0.81 | 40% | 49 | -1,297 |
| v6_carry_trend_daily_mkt_7p | EURJPY | 35 | +21,997 | 1.76 | 43% | 32 | +2,072 |
| v6_carry_trend_daily_mkt_7p | EURUSD | 29 | +81,568 | 3.55 | 62% | 25 | +1,261 |
| v6_carry_trend_daily_mkt_7p | GBPJPY | 17 | +42,189 | 3.11 | 24% | 50 | +15,928 |
| v6_carry_trend_daily_mkt_7p | GBPUSD | 27 | +32,650 | 2.91 | 56% | 47 | -4,844 |
| v6_carry_trend_daily_mkt_7p | USDJPY | 37 | +118,871 | 4.23 | 38% | 30 | +32,568 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v6_trend_carry_mkt_5p | regime4h | HIGH_VOL | 11 | +10,257 | 36% | 1.65 |
| v6_trend_carry_mkt_5p | regime4h | NEUTRAL | 40 | +15,937 | 40% | 1.37 |
| v6_trend_carry_mkt_5p | regime4h | RANGE | 42 | +109,647 | 40% | 2.84 |
| v6_trend_carry_mkt_5p | regime4h | TREND | 74 | +60,584 | 32% | 1.55 |
| v6_trend_carry_mkt_5p | month_dir | DOWN | 39 | -17,079 | 31% | 0.73 |
| v6_trend_carry_mkt_5p | month_dir | FLAT | 99 | +189,607 | 36% | 2.43 |
| v6_trend_carry_mkt_5p | month_dir | UP | 29 | +23,898 | 45% | 1.72 |
| v6_trend_carry_mkt_5p | month_vol | HIGH_VOL | 35 | +4,050 | 40% | 1.10 |
| v6_trend_carry_mkt_5p | month_vol | LOW_VOL | 132 | +192,375 | 36% | 2.03 |
| v6_carry_trend_mkt_7p | regime4h | HIGH_VOL | 11 | +4,900 | 45% | 1.31 |
| v6_carry_trend_mkt_7p | regime4h | NEUTRAL | 31 | +113,809 | 48% | 4.82 |
| v6_carry_trend_mkt_7p | regime4h | RANGE | 36 | +121,565 | 44% | 3.34 |
| v6_carry_trend_mkt_7p | regime4h | TREND | 63 | +18,724 | 37% | 1.21 |
| v6_carry_trend_mkt_7p | month_dir | DOWN | 34 | +5,199 | 41% | 1.11 |
| v6_carry_trend_mkt_7p | month_dir | FLAT | 81 | +245,903 | 40% | 3.49 |
| v6_carry_trend_mkt_7p | month_dir | UP | 26 | +7,896 | 50% | 1.20 |
| v6_carry_trend_mkt_7p | month_vol | HIGH_VOL | 40 | -2,208 | 42% | 0.97 |
| v6_carry_trend_mkt_7p | month_vol | LOW_VOL | 101 | +261,205 | 42% | 3.16 |
| v6_carry_trend_daily_mkt_7p | regime4h | HIGH_VOL | 15 | -15,249 | 27% | 0.41 |
| v6_carry_trend_daily_mkt_7p | regime4h | NEUTRAL | 67 | +230,175 | 45% | 5.35 |
| v6_carry_trend_daily_mkt_7p | regime4h | RANGE | 62 | +19,443 | 48% | 1.36 |
| v6_carry_trend_daily_mkt_7p | regime4h | TREND | 89 | +51,214 | 36% | 1.59 |
| v6_carry_trend_daily_mkt_7p | month_dir | DOWN | 51 | +11,825 | 51% | 1.21 |
| v6_carry_trend_daily_mkt_7p | month_dir | FLAT | 124 | +55,882 | 34% | 1.47 |
| v6_carry_trend_daily_mkt_7p | month_dir | UP | 58 | +217,875 | 48% | 5.96 |
| v6_carry_trend_daily_mkt_7p | month_vol | HIGH_VOL | 62 | +30,138 | 34% | 1.50 |
| v6_carry_trend_daily_mkt_7p | month_vol | LOW_VOL | 171 | +255,444 | 44% | 2.60 |

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
USDJPY  4215               0.0220            0.2986             1.156               9             1 2013-06-06
EURUSD  4215               0.0256            0.3172             0.884               9             0 2011-10-07
GBPUSD  4215               0.0257            0.3175             1.817              11             1 2020-03-18
AUDUSD  4215               0.0304            0.3766             1.172              20             3 2020-03-12
NZDUSD  4215               0.0365            0.4003             1.450              23             2 2011-08-05
USDCAD  4215               0.0250            0.2944             0.895               9             0 2020-03-12
USDCHF  4215               0.0278            0.3100             1.041               8             1 2011-10-07
