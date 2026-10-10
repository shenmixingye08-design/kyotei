# FX AUTOPILOT V6 研究結果（2026-10-10 02:47 UTC、データ〜2026-10-09 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v6.yaml`

> **検証汚染の申告**: 規則・パラメータ・期間はすべて既出（v2_trend_carry / v3_carry_trend_7p / v4_carry_trend_daily と同一）。 新しいのは金利データだけ。したがって V6 は「新しい優位性の探索」ではなく「既存結果の頑健性チェック」。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v6_carry_trend_daily_mkt_7p | REJECTED | 230 | +26.4% | +1.9% | 2.35 | 0.50 | 0.70 | -8.1% | 1,238 | 39 | 0.04 | 10 | 62% | 24% | +5.2% | +20.2% | 1.68 | 5 | 77% | 0.95 | 1 | single_regime_dependence, top1_trade_dependence |
| v6_carry_trend_mkt_7p | REJECTED | 139 | +22.1% | +1.6% | 2.36 | 0.44 | 0.61 | -8.6% | 1,820 | 35 | 0.02 | 7 | 77% | 19% | +6.1% | +15.1% | 1.63 | 5 | 42% | 0.92 | 1 | top5_trade_dependence, top1_trade_dependence |
| v6_trend_carry_mkt_5p | REJECTED | 163 | +16.9% | +1.2% | 1.88 | 0.38 | 0.54 | -8.3% | 1,185 | 32 | 0.03 | 7 | 69% | 28% | +7.2% | +9.1% | 1.61 | 3 | 58% | 0.89 | 1 | sharpe, few_positive_pairs, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v6_trend_carry_mkt_5p | REJECTED | 163 | 63% | 133% | -63,738 | 0.71 | 13% | +1.0% |
| v6_carry_trend_mkt_7p | REJECTED | 139 | 48% | 102% | -4,262 | 0.98 | 18% | +6.5% |
| v6_carry_trend_daily_mkt_7p | REJECTED | 230 | 42% | 95% | +13,025 | 1.06 | 19% | +7.9% |

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
| 2024.0 | +2.4% | +4.4% | +6.6% |
| 2025.0 | -1.9% | +0.2% | +1.3% |
| 2026.0 | +0.5% | +1.8% | -0.1% |

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
| 2021.0 | 167.19 | 288.34 | 42.18 |
| 2022.0 | 2.44 | 0.63 | 4.18 |
| 2023.0 | 1.54 | 91.35 | 7.50 |
| 2024.0 | 0.16 | 0.00 | 0.00 |
| 2025.0 | 0.41 | 2.70 | 3.48 |
| 2026.0 | 1.14 | — | 0.04 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v6_trend_carry_mkt_5p | AUDUSD | 46 | -26,027 | 0.53 | 30% | 46 | -2,907 |
| v6_trend_carry_mkt_5p | EURJPY | 24 | +19,418 | 1.62 | 38% | 27 | +2,152 |
| v6_trend_carry_mkt_5p | EURUSD | 32 | +61,494 | 2.25 | 38% | 23 | +1,260 |
| v6_trend_carry_mkt_5p | GBPUSD | 35 | -568 | 0.99 | 40% | 35 | -6,649 |
| v6_trend_carry_mkt_5p | USDJPY | 26 | +138,916 | 4.95 | 38% | 22 | +30,564 |
| v6_carry_trend_mkt_7p | AUDJPY | 17 | +9,488 | 1.41 | 53% | 49 | +9,865 |
| v6_carry_trend_mkt_7p | AUDUSD | 28 | -18,648 | 0.49 | 39% | 40 | -1,631 |
| v6_carry_trend_mkt_7p | EURJPY | 16 | +27,308 | 2.66 | 50% | 31 | +3,446 |
| v6_carry_trend_mkt_7p | EURUSD | 22 | +81,250 | 4.02 | 45% | 23 | +451 |
| v6_carry_trend_mkt_7p | GBPJPY | 15 | -11,033 | 0.70 | 20% | 49 | +6,067 |
| v6_carry_trend_mkt_7p | GBPUSD | 17 | +25,313 | 2.62 | 59% | 34 | -4,617 |
| v6_carry_trend_mkt_7p | USDJPY | 24 | +139,310 | 5.75 | 33% | 23 | +31,263 |
| v6_carry_trend_daily_mkt_7p | AUDJPY | 33 | -787 | 0.98 | 24% | 44 | +10,019 |
| v6_carry_trend_daily_mkt_7p | AUDUSD | 56 | -8,866 | 0.80 | 39% | 49 | -1,317 |
| v6_carry_trend_daily_mkt_7p | EURJPY | 35 | +21,817 | 1.74 | 43% | 31 | +2,078 |
| v6_carry_trend_daily_mkt_7p | EURUSD | 26 | +85,431 | 4.47 | 65% | 21 | +1,148 |
| v6_carry_trend_daily_mkt_7p | GBPJPY | 16 | +41,197 | 3.14 | 25% | 46 | +15,771 |
| v6_carry_trend_daily_mkt_7p | GBPUSD | 27 | +30,239 | 2.90 | 56% | 45 | -4,758 |
| v6_carry_trend_daily_mkt_7p | USDJPY | 37 | +115,689 | 4.14 | 38% | 30 | +32,207 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v6_trend_carry_mkt_5p | regime4h | HIGH_VOL | 11 | +10,257 | 36% | 1.65 |
| v6_trend_carry_mkt_5p | regime4h | NEUTRAL | 39 | +15,014 | 38% | 1.35 |
| v6_trend_carry_mkt_5p | regime4h | RANGE | 42 | +112,063 | 43% | 2.95 |
| v6_trend_carry_mkt_5p | regime4h | TREND | 71 | +55,898 | 31% | 1.53 |
| v6_trend_carry_mkt_5p | month_dir | DOWN | 38 | -18,504 | 29% | 0.70 |
| v6_trend_carry_mkt_5p | month_dir | FLAT | 96 | +189,735 | 36% | 2.52 |
| v6_trend_carry_mkt_5p | month_dir | UP | 29 | +22,002 | 45% | 1.66 |
| v6_trend_carry_mkt_5p | month_vol | HIGH_VOL | 36 | +2,613 | 42% | 1.06 |
| v6_trend_carry_mkt_5p | month_vol | LOW_VOL | 127 | +190,619 | 35% | 2.07 |
| v6_carry_trend_mkt_7p | regime4h | HIGH_VOL | 11 | +4,900 | 45% | 1.31 |
| v6_carry_trend_mkt_7p | regime4h | NEUTRAL | 29 | +102,712 | 48% | 4.52 |
| v6_carry_trend_mkt_7p | regime4h | RANGE | 35 | +106,603 | 43% | 3.05 |
| v6_carry_trend_mkt_7p | regime4h | TREND | 64 | +38,772 | 39% | 1.44 |
| v6_carry_trend_mkt_7p | month_dir | DOWN | 32 | +6,183 | 44% | 1.13 |
| v6_carry_trend_mkt_7p | month_dir | FLAT | 80 | +232,437 | 39% | 3.35 |
| v6_carry_trend_mkt_7p | month_dir | UP | 27 | +14,368 | 52% | 1.37 |
| v6_carry_trend_mkt_7p | month_vol | HIGH_VOL | 40 | -29 | 42% | 1.00 |
| v6_carry_trend_mkt_7p | month_vol | LOW_VOL | 99 | +253,017 | 42% | 3.11 |
| v6_carry_trend_daily_mkt_7p | regime4h | HIGH_VOL | 14 | -9,301 | 29% | 0.53 |
| v6_carry_trend_daily_mkt_7p | regime4h | NEUTRAL | 65 | +226,335 | 45% | 5.48 |
| v6_carry_trend_daily_mkt_7p | regime4h | RANGE | 64 | +15,147 | 47% | 1.27 |
| v6_carry_trend_daily_mkt_7p | regime4h | TREND | 87 | +52,540 | 37% | 1.62 |
| v6_carry_trend_daily_mkt_7p | month_dir | DOWN | 50 | +9,043 | 52% | 1.16 |
| v6_carry_trend_daily_mkt_7p | month_dir | FLAT | 123 | +56,840 | 33% | 1.49 |
| v6_carry_trend_daily_mkt_7p | month_dir | UP | 57 | +218,837 | 49% | 6.74 |
| v6_carry_trend_daily_mkt_7p | month_vol | HIGH_VOL | 59 | +40,371 | 36% | 1.77 |
| v6_carry_trend_daily_mkt_7p | month_vol | LOW_VOL | 171 | +244,350 | 43% | 2.54 |

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
