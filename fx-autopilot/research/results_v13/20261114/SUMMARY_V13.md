# FX AUTOPILOT V13 研究結果（2026-11-14 03:16 UTC、データ〜2026-11-13 21:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v13.yaml`

> **検証汚染の申告**: 期間・コスト・ゲートは既出。設計者は V1〜V12 の結果（キャリー系が 2022〜24 の円安に依存）を知っている。 2022〜24 は米国の利上げ・日本の据え置きで、金利モメンタムもドル買い・円売りになるため同じ相場への依存が出る可能性がある。 パラメータは閾値 2 通りのみ（6 か月は登録時に固定）。DSR は V1 からの累積試行数で補正。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v13_carry_ratemom | REJECTED | 106 | -10.2% | -0.8% | 0.92 | -0.12 | -0.17 | -28.2% | -391 | 85 | — | 9 | 38% | 35% | -14.2% | +4.7% | 0.80 | 7 | 98% | 0.12 | 2 | profit_factor, sharpe, positive_years, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |
| v13_ratemom | REJECTED | 152 | -24.6% | -2.2% | 0.72 | -0.31 | -0.43 | -32.0% | -1,664 | 78 | — | 12 | 38% | 33% | -10.5% | -15.8% | 0.62 | 3 | 100% | 0.03 | 2 | profit_factor, sharpe, positive_years, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v13_ratemom | REJECTED | 152 | — | — | -427,833 | 0.52 | — | -11.6% |
| v13_carry_ratemom | REJECTED | 106 | — | — | -233,166 | 0.57 | — | +5.3% |

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
| 2026.0 | -1.1% | -0.1% |

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
| 2026.0 | 1.22 | 1.44 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v13_ratemom | AUDJPY | 9 | -26,701 | 0.60 | 22% | 75 | -4,769 |
| v13_ratemom | AUDUSD | 15 | +28,462 | 1.40 | 47% | 109 | -14,943 |
| v13_ratemom | EURJPY | 9 | -4,003 | 0.93 | 33% | 63 | -2,677 |
| v13_ratemom | EURUSD | 22 | +418 | 1.00 | 32% | 46 | -15,593 |
| v13_ratemom | GBPJPY | 13 | -47,882 | 0.42 | 23% | 86 | -3,738 |
| v13_ratemom | GBPUSD | 19 | -46,977 | 0.59 | 37% | 50 | -8,954 |
| v13_ratemom | NZDUSD | 14 | -59,538 | 0.34 | 29% | 129 | -3,834 |
| v13_ratemom | USDCAD | 22 | -72,735 | 0.37 | 32% | 89 | -8,209 |
| v13_ratemom | USDCHF | 14 | +10,482 | 1.15 | 36% | 116 | -15,726 |
| v13_ratemom | USDJPY | 15 | -34,400 | 0.68 | 33% | 31 | -5,030 |
| v13_carry_ratemom | AUDJPY | 15 | -69,680 | 0.38 | 13% | 71 | +11,678 |
| v13_carry_ratemom | AUDUSD | 16 | +16,228 | 1.27 | 44% | 95 | -4,255 |
| v13_carry_ratemom | EURJPY | 3 | +7,821 | 1.39 | 33% | 93 | +4,051 |
| v13_carry_ratemom | EURUSD | 13 | +8,500 | 1.14 | 46% | 34 | +8,199 |
| v13_carry_ratemom | GBPJPY | 5 | +10,206 | 1.40 | 20% | 61 | +8,476 |
| v13_carry_ratemom | GBPUSD | 9 | +5,990 | 1.11 | 33% | 44 | +367 |
| v13_carry_ratemom | NZDUSD | 9 | -37,120 | 0.46 | 33% | 120 | +143 |
| v13_carry_ratemom | USDCAD | 15 | -13,267 | 0.75 | 53% | 112 | -3,425 |
| v13_carry_ratemom | USDCHF | 15 | +20,445 | 1.35 | 47% | 136 | +26,280 |
| v13_carry_ratemom | USDJPY | 6 | +9,392 | 1.28 | 50% | 33 | +8,939 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v13_ratemom | regime4h | HIGH_VOL | 17 | +13,047 | 29% | 1.13 |
| v13_ratemom | regime4h | NEUTRAL | 46 | -121,426 | 33% | 0.58 |
| v13_ratemom | regime4h | RANGE | 59 | -98,898 | 34% | 0.71 |
| v13_ratemom | regime4h | TREND | 64 | -75,441 | 41% | 0.78 |
| v13_ratemom | month_dir | DOWN | 40 | -35,711 | 35% | 0.85 |
| v13_ratemom | month_dir | FLAT | 104 | -235,234 | 34% | 0.60 |
| v13_ratemom | month_dir | UP | 42 | -11,773 | 40% | 0.95 |
| v13_ratemom | month_vol | HIGH_VOL | 66 | -114,661 | 41% | 0.68 |
| v13_ratemom | month_vol | LOW_VOL | 120 | -168,057 | 32% | 0.76 |
| v13_carry_ratemom | regime4h | HIGH_VOL | 18 | +151,146 | 50% | 2.66 |
| v13_carry_ratemom | regime4h | NEUTRAL | 42 | -34,050 | 40% | 0.84 |
| v13_carry_ratemom | regime4h | RANGE | 41 | +3,230 | 44% | 1.02 |
| v13_carry_ratemom | regime4h | TREND | 63 | -145,879 | 32% | 0.56 |
| v13_carry_ratemom | month_dir | DOWN | 36 | -26,945 | 28% | 0.89 |
| v13_carry_ratemom | month_dir | FLAT | 79 | +17,886 | 42% | 1.05 |
| v13_carry_ratemom | month_dir | UP | 49 | -16,495 | 43% | 0.93 |
| v13_carry_ratemom | month_vol | HIGH_VOL | 60 | -24,735 | 35% | 0.93 |
| v13_carry_ratemom | month_vol | LOW_VOL | 104 | -820 | 41% | 1.00 |

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
USDJPY  4215               0.0220            0.2986             1.156               9             1 2013-06-06
EURUSD  4215               0.0256            0.3172             0.884               9             0 2011-10-07
GBPUSD  4215               0.0257            0.3175             1.817              11             1 2020-03-18
AUDUSD  4215               0.0304            0.3766             1.172              20             3 2020-03-12
NZDUSD  4215               0.0365            0.4003             1.450              23             2 2011-08-05
USDCAD  4215               0.0250            0.2944             0.895               9             0 2020-03-12
USDCHF  4215               0.0278            0.3100             1.041               8             1 2011-10-07
