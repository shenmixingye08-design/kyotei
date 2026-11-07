# FX AUTOPILOT V13 研究結果（2026-11-07 03:10 UTC、データ〜2026-11-06 21:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v13.yaml`

> **検証汚染の申告**: 期間・コスト・ゲートは既出。設計者は V1〜V12 の結果（キャリー系が 2022〜24 の円安に依存）を知っている。 2022〜24 は米国の利上げ・日本の据え置きで、金利モメンタムもドル買い・円売りになるため同じ相場への依存が出る可能性がある。 パラメータは閾値 2 通りのみ（6 か月は登録時に固定）。DSR は V1 からの累積試行数で補正。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v13_carry_ratemom | REJECTED | 106 | -11.2% | -0.9% | 0.90 | -0.14 | -0.19 | -28.2% | -499 | 85 | — | 9 | 38% | 35% | -14.2% | +3.5% | 0.77 | 7 | 100% | 0.11 | 2 | profit_factor, sharpe, positive_years, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |
| v13_ratemom | REJECTED | 152 | -26.1% | -2.3% | 0.70 | -0.34 | -0.46 | -32.0% | -1,781 | 78 | — | 12 | 38% | 33% | -10.5% | -17.5% | 0.61 | 2 | 100% | 0.03 | 2 | profit_factor, sharpe, positive_years, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v13_ratemom | REJECTED | 152 | — | — | -445,653 | 0.50 | — | -13.4% |
| v13_carry_ratemom | REJECTED | 106 | — | — | -244,603 | 0.55 | — | +4.2% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v13_ratemom | v13_carry_ratemom |
|---|---|---|
| 2014.0 | -1.6% | -1.6% |
| 2015.0 | +5.5% | -3.0% |
| 2016.0 | -5.5% | -4.6% |
| 2017.0 | -13.5% | -12.8% |
| 2018.0 | +7.0% | +3.4% |
| 2019.0 | +2.9% | +0.4% |
| 2020.0 | +3.4% | +4.6% |
| 2021.0 | -7.3% | -0.5% |
| 2022.0 | -6.9% | -4.6% |
| 2023.0 | +2.3% | +4.1% |
| 2024.0 | -1.1% | +6.8% |
| 2025.0 | -9.7% | -1.3% |
| 2026.0 | -3.1% | -1.2% |

## 年別 Profit Factor（WF OOS）

| year | v13_ratemom | v13_carry_ratemom |
|---|---|---|
| 2014.0 | 2.38 | 0.32 |
| 2015.0 | 0.79 | 0.32 |
| 2016.0 | 0.32 | 0.14 |
| 2017.0 | 0.00 | 0.09 |
| 2018.0 | 4.35 | 4.37 |
| 2019.0 | 0.65 | 0.89 |
| 2020.0 | 2.94 | 4.13 |
| 2021.0 | 0.25 | 0.72 |
| 2022.0 | 1.30 | 1.84 |
| 2023.0 | 0.35 | 0.65 |
| 2024.0 | 0.46 | 1.72 |
| 2025.0 | 0.12 | 0.25 |
| 2026.0 | 0.63 | 0.68 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v13_ratemom | AUDJPY | 9 | -26,701 | 0.60 | 22% | 75 | -4,769 |
| v13_ratemom | AUDUSD | 15 | +28,462 | 1.40 | 47% | 109 | -14,943 |
| v13_ratemom | EURJPY | 9 | -5,113 | 0.91 | 33% | 63 | -2,577 |
| v13_ratemom | EURUSD | 22 | -5,543 | 0.96 | 32% | 46 | -15,686 |
| v13_ratemom | GBPJPY | 13 | -48,401 | 0.42 | 15% | 86 | -3,610 |
| v13_ratemom | GBPUSD | 19 | -51,387 | 0.55 | 37% | 50 | -8,891 |
| v13_ratemom | NZDUSD | 14 | -58,088 | 0.34 | 29% | 129 | -3,711 |
| v13_ratemom | USDCAD | 22 | -72,735 | 0.37 | 32% | 89 | -8,209 |
| v13_ratemom | USDCHF | 14 | +3,212 | 1.05 | 36% | 116 | -15,908 |
| v13_ratemom | USDJPY | 15 | -34,400 | 0.68 | 33% | 31 | -5,030 |
| v13_carry_ratemom | AUDJPY | 15 | -67,916 | 0.39 | 13% | 71 | +11,556 |
| v13_carry_ratemom | AUDUSD | 16 | +16,228 | 1.27 | 44% | 95 | -4,255 |
| v13_carry_ratemom | EURJPY | 3 | +7,821 | 1.39 | 33% | 93 | +4,051 |
| v13_carry_ratemom | EURUSD | 13 | +2,539 | 1.04 | 46% | 33 | +8,106 |
| v13_carry_ratemom | GBPJPY | 5 | +10,206 | 1.40 | 20% | 61 | +8,476 |
| v13_carry_ratemom | GBPUSD | 9 | +5,990 | 1.11 | 33% | 44 | +367 |
| v13_carry_ratemom | NZDUSD | 9 | -37,120 | 0.46 | 33% | 120 | +143 |
| v13_carry_ratemom | USDCAD | 15 | -13,267 | 0.75 | 53% | 112 | -3,425 |
| v13_carry_ratemom | USDCHF | 15 | +13,203 | 1.23 | 47% | 136 | +26,098 |
| v13_carry_ratemom | USDJPY | 6 | +9,392 | 1.28 | 50% | 33 | +8,939 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v13_ratemom | regime4h | HIGH_VOL | 17 | +14,497 | 29% | 1.14 |
| v13_ratemom | regime4h | NEUTRAL | 46 | -131,977 | 30% | 0.54 |
| v13_ratemom | regime4h | RANGE | 59 | -105,377 | 32% | 0.69 |
| v13_ratemom | regime4h | TREND | 64 | -95,502 | 41% | 0.72 |
| v13_ratemom | month_dir | DOWN | 40 | -35,711 | 35% | 0.85 |
| v13_ratemom | month_dir | FLAT | 104 | -269,765 | 32% | 0.54 |
| v13_ratemom | month_dir | UP | 42 | -12,883 | 40% | 0.95 |
| v13_ratemom | month_vol | HIGH_VOL | 66 | -140,091 | 39% | 0.61 |
| v13_ratemom | month_vol | LOW_VOL | 120 | -178,268 | 32% | 0.75 |
| v13_carry_ratemom | regime4h | HIGH_VOL | 18 | +151,146 | 50% | 2.66 |
| v13_carry_ratemom | regime4h | NEUTRAL | 42 | -34,050 | 40% | 0.84 |
| v13_carry_ratemom | regime4h | RANGE | 41 | -2,730 | 44% | 0.99 |
| v13_carry_ratemom | regime4h | TREND | 63 | -151,356 | 32% | 0.54 |
| v13_carry_ratemom | month_dir | DOWN | 35 | -20,233 | 29% | 0.91 |
| v13_carry_ratemom | month_dir | FLAT | 80 | +6,978 | 41% | 1.02 |
| v13_carry_ratemom | month_dir | UP | 49 | -23,736 | 43% | 0.90 |
| v13_carry_ratemom | month_vol | HIGH_VOL | 61 | -29,682 | 34% | 0.92 |
| v13_carry_ratemom | month_vol | LOW_VOL | 103 | -7,309 | 42% | 0.98 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v13_ratemom | REJECTED | {"threshold": 0.5} | vol_target | 2026-09-26T09:49 | 46b7a171be92 |
| v13_carry_ratemom | REJECTED | {"threshold": 1.0} | vol_target | 2026-09-26T09:49 | 820965d2eb31 |

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
USDJPY  4210               0.0220            0.2986             1.156               9             1 2013-06-06
EURUSD  4210               0.0257            0.3173             0.884               9             0 2011-10-07
GBPUSD  4210               0.0258            0.3177             1.817              11             1 2020-03-18
AUDUSD  4210               0.0304            0.3767             1.172              20             3 2020-03-12
NZDUSD  4210               0.0365            0.4009             1.450              23             2 2011-08-05
USDCAD  4210               0.0251            0.2945             0.895               9             0 2020-03-12
USDCHF  4210               0.0279            0.3100             1.041               8             1 2011-10-07
