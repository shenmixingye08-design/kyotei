# FX AUTOPILOT V4 研究結果（2026-11-21 04:23 UTC、データ〜2026-11-20 21:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v4.yaml`

> **検証汚染の申告**: 設計者は v1〜V3 の 2010〜2026 の結果（週次のトレンド×キャリーだけが残り、1 時間足の高頻度戦略はコスト負け）を見たうえで V4 を設計している。V4 の Walk-Forward 成績は「汚染あり」。最終判断は LOCK 後の PAPER Forward のみ。V1〜V3 の LOCK は変更しない。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v4_carry_trend_daily | REJECTED | 254 | +26.8% | +1.9% | 2.34 | 0.51 | 0.71 | -7.6% | 1,150 | 37 | 0.04 | 18 | 69% | 23% | +3.8% | +22.1% | 1.47 | 6 | 83% | 0.86 | 2 | single_regime_dependence, top1_trade_dependence |
| v4_carry_trend_h4 | REJECTED | 1972 | -2.4% | -0.2% | 0.97 | -0.05 | -0.07 | -8.5% | -8 | 15 | — | 21 | 46% | 39% | -5.7% | +3.5% | 0.93 | 2 | 100% | 0.17 | 2 | profit_factor, sharpe, positive_years, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |
| v4_carry_trend_daily_fast | REJECTED | 507 | -2.8% | -0.2% | 0.97 | -0.07 | -0.09 | -9.8% | -24 | 35 | — | 16 | 46% | 32% | -6.0% | +3.4% | 0.80 | 4 | 65% | 0.16 | 2 | profit_factor, sharpe, positive_years, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v4_carry_trend_daily | REJECTED | 254 | 43% | 92% | +24,510 | 1.11 | 22% | +10.3% |
| v4_carry_trend_daily_fast | REJECTED | 507 | — | — | -86,982 | 0.77 | — | +3.2% |
| v4_carry_trend_h4 | REJECTED | 1972 | — | — | -73,566 | 0.89 | — | +0.9% |

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
| 2026.0 | +1.0% | -0.5% | -2.4% |

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
| 2021.0 | 47.29 | 0.78 | 0.85 |
| 2022.0 | 1.92 | 1.14 | 1.51 |
| 2023.0 | 7.95 | 2.17 | 1.61 |
| 2024.0 | 0.00 | 0.60 | 1.60 |
| 2025.0 | 4.67 | 3.70 | 1.29 |
| 2026.0 | 1.32 | 0.56 | 0.58 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v4_carry_trend_daily | AUDJPY | 37 | +1,406 | 1.04 | 22% | 41 | +10,701 |
| v4_carry_trend_daily | AUDUSD | 48 | -4,971 | 0.89 | 38% | 47 | -1,587 |
| v4_carry_trend_daily | EURJPY | 41 | +40,344 | 2.75 | 39% | 32 | +3,734 |
| v4_carry_trend_daily | EURUSD | 32 | +75,221 | 3.60 | 59% | 19 | +1,175 |
| v4_carry_trend_daily | GBPJPY | 20 | +50,619 | 3.56 | 30% | 55 | +18,623 |
| v4_carry_trend_daily | GBPUSD | 35 | +24,229 | 2.52 | 49% | 43 | -4,173 |
| v4_carry_trend_daily | USDJPY | 41 | +105,134 | 3.09 | 22% | 25 | +35,769 |
| v4_carry_trend_daily_fast | AUDJPY | 66 | +1,819 | 1.03 | 27% | 33 | +8,393 |
| v4_carry_trend_daily_fast | AUDUSD | 112 | -6,348 | 0.90 | 32% | 47 | -1,364 |
| v4_carry_trend_daily_fast | EURJPY | 60 | +1,681 | 1.04 | 35% | 37 | +3,329 |
| v4_carry_trend_daily_fast | EURUSD | 88 | +15,862 | 1.28 | 38% | 21 | +2,416 |
| v4_carry_trend_daily_fast | GBPJPY | 38 | -9,878 | 0.73 | 32% | 61 | +6,669 |
| v4_carry_trend_daily_fast | GBPUSD | 72 | -28,832 | 0.48 | 26% | 32 | -1,916 |
| v4_carry_trend_daily_fast | USDJPY | 71 | +13,476 | 1.26 | 31% | 24 | +10,364 |
| v4_carry_trend_h4 | AUDJPY | 364 | -4,221 | 0.97 | 29% | 14 | +9,112 |
| v4_carry_trend_h4 | AUDUSD | 391 | -9,290 | 0.91 | 34% | 19 | -823 |
| v4_carry_trend_h4 | EURJPY | 286 | -24,768 | 0.76 | 28% | 12 | +1,954 |
| v4_carry_trend_h4 | EURUSD | 341 | +7,747 | 1.07 | 31% | 10 | +2,614 |
| v4_carry_trend_h4 | GBPJPY | 115 | -4,096 | 0.91 | 35% | 20 | +5,470 |
| v4_carry_trend_h4 | GBPUSD | 225 | -14,693 | 0.82 | 28% | 19 | -2,845 |
| v4_carry_trend_h4 | USDJPY | 250 | +32,577 | 1.37 | 28% | 10 | +9,792 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v4_carry_trend_daily | regime4h | HIGH_VOL | 16 | -785 | 38% | 0.95 |
| v4_carry_trend_daily | regime4h | NEUTRAL | 78 | +279,925 | 44% | 5.86 |
| v4_carry_trend_daily | regime4h | RANGE | 75 | +18,800 | 40% | 1.29 |
| v4_carry_trend_daily | regime4h | TREND | 119 | +39,635 | 31% | 1.35 |
| v4_carry_trend_daily | month_dir | DOWN | 57 | +10,141 | 46% | 1.18 |
| v4_carry_trend_daily | month_dir | FLAT | 158 | +71,406 | 32% | 1.52 |
| v4_carry_trend_daily | month_dir | UP | 73 | +256,027 | 42% | 5.25 |
| v4_carry_trend_daily | month_vol | HIGH_VOL | 73 | +33,841 | 30% | 1.49 |
| v4_carry_trend_daily | month_vol | LOW_VOL | 215 | +303,734 | 40% | 2.65 |
| v4_carry_trend_daily_fast | regime4h | HIGH_VOL | 65 | +10,418 | 42% | 1.21 |
| v4_carry_trend_daily_fast | regime4h | NEUTRAL | 164 | +30,709 | 30% | 1.30 |
| v4_carry_trend_daily_fast | regime4h | RANGE | 197 | +6,077 | 33% | 1.04 |
| v4_carry_trend_daily_fast | regime4h | TREND | 373 | -111,624 | 29% | 0.64 |
| v4_carry_trend_daily_fast | month_dir | DOWN | 191 | -2,012 | 33% | 0.99 |
| v4_carry_trend_daily_fast | month_dir | FLAT | 430 | -162,542 | 27% | 0.51 |
| v4_carry_trend_daily_fast | month_dir | UP | 178 | +100,135 | 41% | 1.82 |
| v4_carry_trend_daily_fast | month_vol | HIGH_VOL | 189 | +45,522 | 35% | 1.28 |
| v4_carry_trend_daily_fast | month_vol | LOW_VOL | 610 | -109,942 | 30% | 0.76 |
| v4_carry_trend_h4 | regime4h | HIGH_VOL | 104 | -3,021 | 28% | 0.93 |
| v4_carry_trend_h4 | regime4h | NEUTRAL | 445 | -8,337 | 30% | 0.94 |
| v4_carry_trend_h4 | regime4h | RANGE | 650 | +11,712 | 35% | 1.06 |
| v4_carry_trend_h4 | regime4h | TREND | 875 | -16,273 | 27% | 0.95 |
| v4_carry_trend_h4 | month_dir | DOWN | 466 | +23,237 | 33% | 1.16 |
| v4_carry_trend_h4 | month_dir | FLAT | 1166 | -122,676 | 27% | 0.69 |
| v4_carry_trend_h4 | month_dir | UP | 442 | +83,520 | 36% | 1.60 |
| v4_carry_trend_h4 | month_vol | HIGH_VOL | 476 | -16,844 | 32% | 0.91 |
| v4_carry_trend_h4 | month_vol | LOW_VOL | 1598 | +924 | 29% | 1.00 |

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
