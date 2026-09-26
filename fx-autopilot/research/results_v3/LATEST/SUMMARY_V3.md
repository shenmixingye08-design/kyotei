# FX AUTOPILOT V3 研究結果（2026-09-26 06:59 UTC、データ〜2026-09-25 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v3.yaml`

> **検証汚染の申告**: 設計者は v1 と V2 の 2010〜2026 の結果（v2_trend_carry の composite だけが事前登録ゲートを通り、 利益が USDJPY と少数の大きなトレードに集中していたこと）を見たうえで V3 を設計している。 よって V3 の Walk-Forward 成績は「汚染あり」。新規ペア（AUDJPY / GBPJPY）は V1/V2 の設計に使っていないが、期間は同じ。 V3 の最終判断は LOCK 後の PAPER Forward のみ。V2 の LOCK（v2_trend_carry など）は変更しない。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v3_carry_trend_7p | REJECTED | 128 | +28.1% | +2.0% | 2.86 | 0.53 | 0.73 | -8.3% | 2,432 | 32 | 0.02 | 7 | 85% | 24% | +8.0% | +18.7% | 1.90 | 7 | 53% | 0.75 | 1 | top1_trade_dependence |
| v3_carry_trend_xs | REJECTED | 179 | +50.0% | +3.2% | 1.86 | 0.50 | 0.73 | -13.3% | 3,363 | 93 | 0.03 | 9 | 69% | 30% | +29.4% | +15.9% | 1.64 | 5 | 61% | 0.70 | 3 | top5_trade_dependence, top1_trade_dependence |
| v3_carry_only | REJECTED | 28 | +46.4% | +3.0% | 5.32 | 0.39 | 0.55 | -18.8% | 18,190 | 45 | 0.00 | 14 | 62% | 36% | -4.5% | +53.3% | 3.66 | 6 | 88% | 0.59 | 2 | trades, sharpe, subperiod_not_positive, single_regime_dependence, top5_trade_dependence, top1_trade_dependence |
| v3_carry_trend_mh | REJECTED | 202 | +15.8% | +1.2% | 1.94 | 0.37 | 0.50 | -8.7% | 1,010 | 28 | 0.04 | 10 | 69% | 23% | +0.2% | +15.5% | 1.24 | 5 | 42% | 0.54 | 3 | sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v3_carry_trend_xs | REJECTED | 179 | 68% | 124% | -146,407 | 0.79 | 1% | +6.7% |
| v3_carry_trend_mh | REJECTED | 202 | 60% | 110% | -20,143 | 0.91 | 27% | +7.3% |
| v3_carry_trend_7p | REJECTED | 128 | 39% | 93% | +23,246 | 1.14 | 20% | +9.1% |
| v3_carry_only | REJECTED | 28 | 61% | 119% | -94,805 | 0.20 | 35% | +26.3% |

上位 5 トレードを除くと赤字になる候補は、少数の大相場（例: 2022 年の円安）に依存している可能性が高い。

## 年別 Return（WF OOS）

| year | v3_carry_trend_xs | v3_carry_trend_mh | v3_carry_trend_7p | v3_carry_only |
|---|---|---|---|---|
| 2014.0 | +14.4% | +0.7% | +4.3% | -0.2% |
| 2015.0 | +10.5% | +1.0% | +0.8% | -2.0% |
| 2016.0 | +4.0% | -0.3% | +1.4% | -0.4% |
| 2017.0 | -0.9% | -1.8% | -0.1% | -3.5% |
| 2018.0 | -1.9% | -1.5% | -1.3% | +3.5% |
| 2019.0 | -1.3% | +0.5% | +0.5% | +0.1% |
| 2020.0 | -1.0% | +1.7% | +0.7% | -6.2% |
| 2021.0 | +3.6% | -0.0% | +1.4% | +4.6% |
| 2022.0 | +4.3% | +3.2% | +3.4% | +6.6% |
| 2023.0 | +4.1% | +4.3% | +5.2% | +13.9% |
| 2024.0 | +5.2% | +4.2% | +6.5% | +19.6% |
| 2025.0 | +1.4% | +2.6% | +0.8% | +4.0% |
| 2026.0 | +0.1% | +0.4% | +1.6% | +1.5% |

## 年別 Profit Factor（WF OOS）

| year | v3_carry_trend_xs | v3_carry_trend_mh | v3_carry_trend_7p | v3_carry_only |
|---|---|---|---|---|
| 2014.0 | 5.87 | 1.56 | 5.21 | 0.00 |
| 2015.0 | 1.51 | 1.17 | 0.61 | 0.55 |
| 2016.0 | 0.26 | 0.94 | 0.81 | 0.00 |
| 2017.0 | 0.47 | 0.57 | 2.27 | 0.00 |
| 2018.0 | 0.72 | 0.63 | 0.86 | 6.79 |
| 2019.0 | 0.14 | 0.05 | 0.46 | — |
| 2020.0 | 1.45 | 6.27 | 2.73 | — |
| 2021.0 | 2.63 | 14.69 | — | — |
| 2022.0 | 0.93 | 0.28 | 0.57 | 30.04 |
| 2023.0 | 48.47 | 26.39 | 194.41 | — |
| 2024.0 | 1.97 | 0.07 | 0.00 | 0.00 |
| 2025.0 | 2.53 | 7.38 | 1.59 | — |
| 2026.0 | 0.00 | 0.00 | — | — |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v3_carry_trend_xs | AUDJPY | 29 | +21,516 | 1.20 | 41% | 108 | +14,818 |
| v3_carry_trend_xs | AUDUSD | 32 | -71,833 | 0.39 | 44% | 102 | -80 |
| v3_carry_trend_xs | EURJPY | 30 | +22,443 | 1.27 | 27% | 64 | +1,350 |
| v3_carry_trend_xs | EURUSD | 19 | +491,861 | 15.78 | 63% | 81 | -13,459 |
| v3_carry_trend_xs | GBPJPY | 21 | +106,596 | 1.67 | 33% | 162 | +7,424 |
| v3_carry_trend_xs | GBPUSD | 25 | +64,520 | 1.92 | 44% | 76 | -10,964 |
| v3_carry_trend_xs | USDJPY | 23 | -33,085 | 0.75 | 35% | 64 | +8,115 |
| v3_carry_trend_mh | AUDJPY | 38 | +4,796 | 1.10 | 39% | 36 | +10,476 |
| v3_carry_trend_mh | AUDUSD | 39 | -702 | 0.98 | 28% | 38 | -1,644 |
| v3_carry_trend_mh | EURJPY | 26 | +26,796 | 1.85 | 35% | 20 | +5,004 |
| v3_carry_trend_mh | EURUSD | 29 | +32,820 | 2.44 | 45% | 18 | +327 |
| v3_carry_trend_mh | GBPJPY | 15 | -5,032 | 0.82 | 27% | 37 | +9,066 |
| v3_carry_trend_mh | GBPUSD | 27 | +7,399 | 1.29 | 48% | 25 | -2,957 |
| v3_carry_trend_mh | USDJPY | 28 | +137,936 | 5.97 | 46% | 17 | +35,546 |
| v3_carry_trend_7p | AUDJPY | 18 | +6,928 | 1.30 | 44% | 44 | +10,048 |
| v3_carry_trend_7p | AUDUSD | 24 | +3,297 | 1.12 | 38% | 38 | -1,499 |
| v3_carry_trend_7p | EURJPY | 16 | +25,094 | 2.28 | 50% | 27 | +4,445 |
| v3_carry_trend_7p | EURUSD | 21 | +81,903 | 3.87 | 43% | 24 | +106 |
| v3_carry_trend_7p | GBPJPY | 12 | +35,013 | 2.37 | 25% | 50 | +18,288 |
| v3_carry_trend_7p | GBPUSD | 15 | +22,156 | 2.91 | 60% | 31 | -3,982 |
| v3_carry_trend_7p | USDJPY | 22 | +136,953 | 5.29 | 27% | 19 | +33,989 |
| v3_carry_only | AUDJPY | 2 | -23,160 | 0.00 | 0% | 54 | +4,287 |
| v3_carry_only | AUDUSD | 6 | +3,892 | 1.23 | 33% | 49 | +965 |
| v3_carry_only | EURJPY | 1 | +66,786 | — | 100% | 54 | +4,044 |
| v3_carry_only | EURUSD | 5 | +67,562 | 5.02 | 20% | 18 | +29,702 |
| v3_carry_only | GBPJPY | 1 | +311,068 | — | 100% | 98 | +89,872 |
| v3_carry_only | GBPUSD | 4 | +42,814 | 4.22 | 25% | 47 | +1,749 |
| v3_carry_only | USDJPY | 9 | +40,368 | 1.85 | 22% | 48 | +48,952 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v3_carry_trend_xs | regime4h | HIGH_VOL | 14 | +62,429 | 64% | 2.49 |
| v3_carry_trend_xs | regime4h | NEUTRAL | 66 | +261,847 | 36% | 2.10 |
| v3_carry_trend_xs | regime4h | RANGE | 66 | +97,169 | 44% | 1.33 |
| v3_carry_trend_xs | regime4h | TREND | 111 | +666,913 | 37% | 2.25 |
| v3_carry_trend_xs | month_dir | DOWN | 64 | -43,143 | 39% | 0.88 |
| v3_carry_trend_xs | month_dir | FLAT | 135 | +987,718 | 36% | 2.77 |
| v3_carry_trend_xs | month_dir | UP | 58 | +143,782 | 50% | 1.74 |
| v3_carry_trend_xs | month_vol | HIGH_VOL | 76 | +230,179 | 42% | 1.53 |
| v3_carry_trend_xs | month_vol | LOW_VOL | 181 | +858,179 | 39% | 2.27 |
| v3_carry_trend_mh | regime4h | HIGH_VOL | 27 | +13,144 | 33% | 1.39 |
| v3_carry_trend_mh | regime4h | NEUTRAL | 49 | +101,045 | 49% | 3.03 |
| v3_carry_trend_mh | regime4h | RANGE | 72 | +102,689 | 35% | 2.24 |
| v3_carry_trend_mh | regime4h | TREND | 122 | +30,142 | 41% | 1.24 |
| v3_carry_trend_mh | month_dir | DOWN | 64 | +14,311 | 36% | 1.18 |
| v3_carry_trend_mh | month_dir | FLAT | 141 | +164,986 | 39% | 2.10 |
| v3_carry_trend_mh | month_dir | UP | 65 | +67,723 | 46% | 2.08 |
| v3_carry_trend_mh | month_vol | HIGH_VOL | 79 | +1,932 | 35% | 1.02 |
| v3_carry_trend_mh | month_vol | LOW_VOL | 191 | +245,088 | 42% | 2.25 |
| v3_carry_trend_7p | regime4h | HIGH_VOL | 9 | +13,221 | 56% | 2.63 |
| v3_carry_trend_7p | regime4h | NEUTRAL | 32 | +166,215 | 47% | 5.81 |
| v3_carry_trend_7p | regime4h | RANGE | 29 | +105,370 | 38% | 3.50 |
| v3_carry_trend_7p | regime4h | TREND | 58 | +26,539 | 36% | 1.32 |
| v3_carry_trend_7p | month_dir | DOWN | 29 | +27,097 | 52% | 1.66 |
| v3_carry_trend_7p | month_dir | FLAT | 71 | +225,966 | 35% | 3.62 |
| v3_carry_trend_7p | month_dir | UP | 28 | +58,282 | 43% | 2.45 |
| v3_carry_trend_7p | month_vol | HIGH_VOL | 35 | +5,073 | 37% | 1.09 |
| v3_carry_trend_7p | month_vol | LOW_VOL | 93 | +306,272 | 42% | 3.80 |
| v3_carry_only | regime4h | HIGH_VOL | 8 | +440,795 | 50% | 19.82 |
| v3_carry_only | regime4h | NEUTRAL | 3 | -13,033 | 0% | 0.00 |
| v3_carry_only | regime4h | RANGE | 5 | -23,310 | 0% | 0.00 |
| v3_carry_only | regime4h | TREND | 18 | +62,020 | 22% | 1.61 |
| v3_carry_only | month_dir | DOWN | 8 | -45,847 | 0% | 0.00 |
| v3_carry_only | month_dir | FLAT | 18 | +16,829 | 22% | 1.18 |
| v3_carry_only | month_dir | UP | 8 | +495,490 | 50% | 22.67 |
| v3_carry_only | month_vol | HIGH_VOL | 20 | +461,931 | 35% | 6.71 |
| v3_carry_only | month_vol | LOW_VOL | 14 | +4,541 | 7% | 1.06 |

## 比較: sizing（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | sizing | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v3_carry_only | risk_stop | 37 | +7.8% | 1.74 | 0.20 | -0.28 | 0.80 | -10.8% |
| v3_carry_only | vol_target | 32 | +36.0% | 2.18 | 0.25 | -0.24 | 0.83 | -30.3% |
| v3_carry_trend_xs | risk_stop | 201 | +23.7% | 1.97 | 0.50 | 0.22 | 0.81 | -6.1% |
| v3_carry_trend_xs | vol_target | 237 | +125.6% | 1.74 | 0.50 | 0.24 | 0.84 | -25.0% |

## LOCK（V2・PAPER Forward 用）

| spec_id | status | params | sizing | locked_at | spec_hash |
|---|---|---|---|---|---|
| v3_carry_trend_xs | REJECTED | {"sizing": "risk_stop", "top_k": 4} | risk_stop | 2026-09-25T16:24 | 50fc34f2c499 |
| v3_carry_trend_mh | REJECTED | {"threshold": 0.5, "trail": "none"} | risk_stop | 2026-09-25T16:24 | b98a8484c660 |
| v3_carry_trend_7p | REJECTED | {"sizing": "risk_stop"} | risk_stop | 2026-09-25T16:24 | 63611c77fd67 |
| v3_carry_only | REJECTED | {"sizing": "vol_target"} | vol_target | 2026-09-25T16:24 | 596cd352face |

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
USDJPY  4181               0.0219            0.2995             1.156               9             1 2013-06-06
EURUSD  4181               0.0253            0.3181             0.884               9             0 2011-10-07
GBPUSD  4181               0.0257            0.3184             1.817              11             1 2020-03-18
AUDUSD  4181               0.0303            0.3768             1.172              20             3 2020-03-12
NZDUSD  4181               0.0361            0.4023             1.450              23             2 2011-08-05
USDCAD  4181               0.0248            0.2948             0.895               9             0 2020-03-12
USDCHF  4181               0.0276            0.3103             1.041               8             1 2011-10-07
