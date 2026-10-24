# FX AUTOPILOT V10 研究結果（2026-10-24 01:54 UTC、データ〜2026-10-23 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v10.yaml`

> **検証汚染の申告**: 期間・コスト・ゲートは既出。V3 のキャリーのみ（フィルターなし、7 ペア）は 28 トレード・前半マイナスで不合格。 フィルターの考え方は論文由来で、閾値は中央値 / 80 パーセンタイルの 2 通りだけ。ペアは結果で選ばず 10 ペアすべて。 DSR は V1 からの累積試行数で補正。最終判断は LOCK 後の PAPER Forward。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v10_carry_vix | REJECTED | 504 | -12.9% | -1.1% | 0.89 | -0.17 | -0.23 | -29.2% | -216 | 108 | — | 13 | 54% | 27% | -21.5% | +11.0% | 0.73 | 3 | 76% | 0.16 | 2 | profit_factor, sharpe, positive_years, max_drawdown, subperiod_not_positive, fragile_to_cost_2x, few_positive_pairs, single_regime_dependence, deflated_sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v10_carry_vix | REJECTED | 504 | — | — | -194,834 | 0.79 | — | +14.4% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v10_carry_vix |
|---|---|
| 2014.0 | -8.0% |
| 2015.0 | -6.6% |
| 2016.0 | +2.3% |
| 2017.0 | -6.3% |
| 2018.0 | -4.4% |
| 2019.0 | -4.7% |
| 2020.0 | +0.6% |
| 2021.0 | +4.0% |
| 2022.0 | -5.2% |
| 2023.0 | +2.4% |
| 2024.0 | +6.4% |
| 2025.0 | +5.5% |
| 2026.0 | +1.9% |

## 年別 Profit Factor（WF OOS）

| year | v10_carry_vix |
|---|---|
| 2014.0 | 0.53 |
| 2015.0 | 0.35 |
| 2016.0 | 1.01 |
| 2017.0 | 0.71 |
| 2018.0 | 0.52 |
| 2019.0 | 0.74 |
| 2020.0 | 0.64 |
| 2021.0 | 3.10 |
| 2022.0 | 0.32 |
| 2023.0 | 2.00 |
| 2024.0 | 1.13 |
| 2025.0 | 2.75 |
| 2026.0 | 1.11 |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v10_carry_vix | AUDJPY | 59 | -32,904 | 0.74 | 47% | 90 | +13,812 |
| v10_carry_vix | AUDUSD | 62 | -36,264 | 0.73 | 47% | 122 | +4,044 |
| v10_carry_vix | EURJPY | 25 | +24,703 | 1.84 | 48% | 130 | +5,991 |
| v10_carry_vix | EURUSD | 70 | +1,785 | 1.01 | 53% | 51 | +7,519 |
| v10_carry_vix | GBPJPY | 40 | +10,935 | 1.21 | 50% | 153 | +9,089 |
| v10_carry_vix | GBPUSD | 23 | -8,970 | 0.79 | 43% | 79 | +107 |
| v10_carry_vix | NZDUSD | 62 | -41,690 | 0.70 | 42% | 143 | +7,093 |
| v10_carry_vix | USDCAD | 53 | -10,564 | 0.90 | 49% | 141 | +63 |
| v10_carry_vix | USDCHF | 62 | -14,878 | 0.87 | 53% | 133 | +9,653 |
| v10_carry_vix | USDJPY | 48 | -1,022 | 0.99 | 54% | 43 | +10,557 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v10_carry_vix | regime4h | HIGH_VOL | 36 | -45,669 | 44% | 0.53 |
| v10_carry_vix | regime4h | NEUTRAL | 116 | +9,488 | 50% | 1.05 |
| v10_carry_vix | regime4h | RANGE | 199 | +29,631 | 55% | 1.09 |
| v10_carry_vix | regime4h | TREND | 253 | -162,755 | 45% | 0.70 |
| v10_carry_vix | month_dir | DOWN | 120 | -139,795 | 42% | 0.54 |
| v10_carry_vix | month_dir | FLAT | 353 | -6,498 | 52% | 0.99 |
| v10_carry_vix | month_dir | UP | 131 | -23,012 | 49% | 0.91 |
| v10_carry_vix | month_vol | HIGH_VOL | 173 | -60,991 | 50% | 0.82 |
| v10_carry_vix | month_vol | LOW_VOL | 431 | -108,314 | 49% | 0.87 |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v10_carry_vix | REJECTED | {"calm": "below_median"} | vol_target | 2026-09-26T08:26 | 41e3a2922b91 |

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
