# FX AUTOPILOT V4 研究結果（2026-10-24 01:51 UTC、データ〜2026-10-23 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v4.yaml`

> **検証汚染の申告**: 設計者は v1〜V3 の 2010〜2026 の結果（週次のトレンド×キャリーだけが残り、1 時間足の高頻度戦略はコスト負け）を見たうえで V4 を設計している。V4 の Walk-Forward 成績は「汚染あり」。最終判断は LOCK 後の PAPER Forward のみ。V1〜V3 の LOCK は変更しない。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v4_carry_trend_daily | REJECTED | 253 | +26.2% | +1.8% | 2.31 | 0.50 | 0.70 | -7.6% | 1,132 | 36 | 0.04 | 18 | 69% | 24% | +3.8% | +21.5% | 1.46 | 6 | 83% | 0.86 | 2 | single_regime_dependence, top1_trade_dependence |
| v4_carry_trend_h4 | REJECTED | 1958 | -2.2% | -0.2% | 0.98 | -0.05 | -0.06 | -8.5% | -7 | 15 | — | 21 | 46% | 39% | -5.7% | +3.7% | 0.93 | 2 | 100% | 0.19 | 2 | profit_factor, sharpe, positive_years, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |
| v4_carry_trend_daily_fast | REJECTED | 502 | -3.3% | -0.3% | 0.95 | -0.08 | -0.11 | -9.8% | -35 | 35 | — | 16 | 46% | 32% | -6.0% | +2.8% | 0.79 | 4 | 74% | 0.15 | 2 | profit_factor, sharpe, positive_years, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v4_carry_trend_daily | REJECTED | 253 | 42% | 93% | +20,230 | 1.09 | 22% | +9.9% |
| v4_carry_trend_daily_fast | REJECTED | 502 | — | — | -92,477 | 0.75 | — | +2.6% |
| v4_carry_trend_h4 | REJECTED | 1958 | — | — | -71,419 | 0.89 | — | +1.1% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v4_carry_trend_daily | v4_carry_trend_daily_fast | v4_carry_trend_h4 |
|---|---|---|---|
| 2014.0 | +1.8% | +1.3% | +0.1% |
| 2015.0 | +1.7% | -0.4% | -0.7% |
| 2016.0 | +2.8% | +0.2% | +1.1% |
| 2017.0 | -0.4% | -3.1% | -1.5% |
| 2018.0 | -2.1% | +0.0% | -0.1% |
| 2019.0 | -0.7% | -1.0% | -1.4% |
| 2020.0 | -0.7% | -2.5% | -2.5% |
| 2021.0 | +1.5% | -0.7% | -0.8% |
| 2022.0 | +5.4% | -0.9% | +1.5% |
| 2023.0 | +5.0% | +1.1% | +1.0% |
| 2024.0 | +6.5% | +2.0% | +2.8% |
| 2025.0 | +2.5% | +1.6% | +0.5% |
| 2026.0 | +0.6% | -1.0% | -2.2% |

## 年別 Profit Factor（WF OOS）

| year | v4_carry_trend_daily | v4_carry_trend_daily_fast | v4_carry_trend_h4 |
|---|---|---|---|
| 2014.0 | 2.66 | 2.01 | 1.22 |
| 2015.0 | 1.04 | 0.80 | 0.74 |
| 2016.0 | 1.34 | 1.06 | 1.28 |
| 2017.0 | 1.11 | 0.38 | 0.80 |
| 2018.0 | 0.47 | 1.01 | 0.91 |
| 2019.0 | 0.42 | 0.55 | 0.67 |
| 2020.0 | 1.37 | 0.72 | 0.68 |
| 2021.0 | 46.16 | 0.78 | 0.85 |
| 2022.0 | 1.92 | 1.14 | 1.51 |
| 2023.0 | 8.16 | 2.17 | 1.61 |
| 2024.0 | 0.00 | 0.60 | 1.60 |
| 2025.0 | 5.04 | 3.70 | 1.29 |
| 2026.0 | 0.00 | 0.28 | 0.55 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v4_carry_trend_daily | AUDJPY | 37 | +4,303 | 1.12 | 22% | 41 | +10,568 |
| v4_carry_trend_daily | AUDUSD | 47 | -7,897 | 0.82 | 36% | 47 | -1,559 |
| v4_carry_trend_daily | EURJPY | 41 | +40,344 | 2.75 | 39% | 32 | +3,734 |
| v4_carry_trend_daily | EURUSD | 32 | +71,431 | 3.46 | 56% | 19 | +1,093 |
| v4_carry_trend_daily | GBPJPY | 20 | +52,586 | 3.65 | 30% | 55 | +18,233 |
| v4_carry_trend_daily | GBPUSD | 35 | +24,294 | 2.53 | 49% | 40 | -4,173 |
| v4_carry_trend_daily | USDJPY | 41 | +101,243 | 3.02 | 22% | 25 | +35,270 |
| v4_carry_trend_daily_fast | AUDJPY | 65 | +3,489 | 1.06 | 28% | 33 | +8,354 |
| v4_carry_trend_daily_fast | AUDUSD | 111 | -9,236 | 0.86 | 32% | 47 | -1,338 |
| v4_carry_trend_daily_fast | EURJPY | 60 | +1,681 | 1.04 | 35% | 37 | +3,329 |
| v4_carry_trend_daily_fast | EURUSD | 88 | +12,073 | 1.22 | 36% | 21 | +2,334 |
| v4_carry_trend_daily_fast | GBPJPY | 37 | -9,472 | 0.74 | 32% | 61 | +6,365 |
| v4_carry_trend_daily_fast | GBPUSD | 71 | -28,929 | 0.48 | 25% | 32 | -1,900 |
| v4_carry_trend_daily_fast | USDJPY | 70 | +12,679 | 1.25 | 30% | 25 | +10,169 |
| v4_carry_trend_h4 | AUDJPY | 360 | -1,284 | 0.99 | 29% | 14 | +9,016 |
| v4_carry_trend_h4 | AUDUSD | 389 | -11,937 | 0.89 | 33% | 19 | -791 |
| v4_carry_trend_h4 | EURJPY | 286 | -24,768 | 0.76 | 28% | 12 | +1,954 |
| v4_carry_trend_h4 | EURUSD | 337 | +6,290 | 1.06 | 31% | 10 | +2,557 |
| v4_carry_trend_h4 | GBPJPY | 114 | -1,447 | 0.97 | 35% | 20 | +5,151 |
| v4_carry_trend_h4 | GBPUSD | 222 | -12,083 | 0.85 | 28% | 19 | -2,823 |
| v4_carry_trend_h4 | USDJPY | 250 | +30,631 | 1.35 | 28% | 10 | +9,543 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v4_carry_trend_daily | regime4h | HIGH_VOL | 16 | -785 | 38% | 0.95 |
| v4_carry_trend_daily | regime4h | NEUTRAL | 78 | +277,174 | 42% | 5.81 |
| v4_carry_trend_daily | regime4h | RANGE | 75 | +18,800 | 40% | 1.29 |
| v4_carry_trend_daily | regime4h | TREND | 118 | +36,709 | 31% | 1.32 |
| v4_carry_trend_daily | month_dir | DOWN | 56 | +7,215 | 45% | 1.13 |
| v4_carry_trend_daily | month_dir | FLAT | 158 | +70,578 | 31% | 1.51 |
| v4_carry_trend_daily | month_dir | UP | 73 | +254,104 | 42% | 5.22 |
| v4_carry_trend_daily | month_vol | HIGH_VOL | 73 | +36,738 | 30% | 1.53 |
| v4_carry_trend_daily | month_vol | LOW_VOL | 214 | +295,159 | 39% | 2.60 |
| v4_carry_trend_daily_fast | regime4h | HIGH_VOL | 65 | +10,418 | 42% | 1.21 |
| v4_carry_trend_daily_fast | regime4h | NEUTRAL | 162 | +29,236 | 29% | 1.29 |
| v4_carry_trend_daily_fast | regime4h | RANGE | 194 | -27 | 32% | 1.00 |
| v4_carry_trend_daily_fast | regime4h | TREND | 363 | -110,853 | 29% | 0.64 |
| v4_carry_trend_daily_fast | month_dir | DOWN | 184 | +772 | 33% | 1.01 |
| v4_carry_trend_daily_fast | month_dir | FLAT | 424 | -169,652 | 26% | 0.48 |
| v4_carry_trend_daily_fast | month_dir | UP | 176 | +97,654 | 41% | 1.80 |
| v4_carry_trend_daily_fast | month_vol | HIGH_VOL | 185 | +41,296 | 35% | 1.26 |
| v4_carry_trend_daily_fast | month_vol | LOW_VOL | 599 | -112,522 | 30% | 0.74 |
| v4_carry_trend_h4 | regime4h | HIGH_VOL | 104 | -3,021 | 28% | 0.93 |
| v4_carry_trend_h4 | regime4h | NEUTRAL | 442 | -9,323 | 30% | 0.93 |
| v4_carry_trend_h4 | regime4h | RANGE | 648 | +11,224 | 35% | 1.05 |
| v4_carry_trend_h4 | regime4h | TREND | 866 | -12,652 | 27% | 0.96 |
| v4_carry_trend_h4 | month_dir | DOWN | 457 | +24,700 | 33% | 1.17 |
| v4_carry_trend_h4 | month_dir | FLAT | 1161 | -121,992 | 27% | 0.69 |
| v4_carry_trend_h4 | month_dir | UP | 442 | +83,520 | 36% | 1.60 |
| v4_carry_trend_h4 | month_vol | HIGH_VOL | 476 | -16,844 | 32% | 0.91 |
| v4_carry_trend_h4 | month_vol | LOW_VOL | 1584 | +3,072 | 29% | 1.01 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v4_carry_trend_daily | REJECTED | {"threshold": 0.5} | risk_stop | 2026-09-25T20:26 | 8f8ea5b61317 |
| v4_carry_trend_daily_fast | REJECTED | {"threshold": 1.0} | risk_stop | 2026-09-25T20:26 | e06c9e4506e9 |
| v4_carry_trend_h4 | REJECTED | {"threshold": 1.0} | risk_stop | 2026-09-25T20:26 | 21f421b1286c |

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
