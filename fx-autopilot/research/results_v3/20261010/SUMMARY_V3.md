# FX AUTOPILOT V3 研究結果（2026-10-10 02:45 UTC、データ〜2026-10-09 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v3.yaml`

> **検証汚染の申告**: 設計者は v1 と V2 の 2010〜2026 の結果（v2_trend_carry の composite だけが事前登録ゲートを通り、 利益が USDJPY と少数の大きなトレードに集中していたこと）を見たうえで V3 を設計している。 よって V3 の Walk-Forward 成績は「汚染あり」。新規ペア（AUDJPY / GBPJPY）は V1/V2 の設計に使っていないが、期間は同じ。 V3 の最終判断は LOCK 後の PAPER Forward のみ。V2 の LOCK（v2_trend_carry など）は変更しない。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v3_carry_trend_7p | REJECTED | 128 | +29.1% | +2.0% | 2.92 | 0.54 | 0.75 | -8.3% | 2,510 | 32 | 0.02 | 7 | 85% | 24% | +8.0% | +19.6% | 1.93 | 7 | 52% | 0.77 | 1 | top1_trade_dependence |
| v3_carry_trend_xs | REJECTED | 179 | +50.3% | +3.2% | 1.86 | 0.50 | 0.73 | -13.3% | 3,378 | 93 | 0.03 | 9 | 69% | 30% | +29.4% | +16.1% | 1.65 | 5 | 61% | 0.71 | 3 | top5_trade_dependence, top1_trade_dependence |
| v3_carry_only | REJECTED | 28 | +48.0% | +3.1% | 5.44 | 0.40 | 0.56 | -18.8% | 18,719 | 45 | 0.00 | 14 | 62% | 36% | -4.5% | +55.0% | 3.76 | 6 | 88% | 0.60 | 2 | trades, subperiod_not_positive, single_regime_dependence, top5_trade_dependence, top1_trade_dependence |
| v3_carry_trend_mh | REJECTED | 202 | +16.0% | +1.2% | 1.94 | 0.37 | 0.50 | -8.7% | 1,019 | 28 | 0.04 | 10 | 69% | 23% | +0.2% | +15.7% | 1.24 | 5 | 42% | 0.54 | 3 | sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v3_carry_trend_xs | REJECTED | 179 | 68% | 124% | -145,097 | 0.79 | 1% | +7.0% |
| v3_carry_trend_mh | REJECTED | 202 | 60% | 111% | -21,963 | 0.90 | 27% | +7.5% |
| v3_carry_trend_7p | REJECTED | 128 | 39% | 91% | +29,546 | 1.18 | 19% | +9.9% |
| v3_carry_only | REJECTED | 28 | 60% | 118% | -94,805 | 0.20 | 34% | +27.6% |

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
| 2026.0 | +0.2% | +0.5% | +2.3% | +2.6% |

## 年別 Profit Factor（WF OOS）

| year | v3_carry_trend_xs | v3_carry_trend_mh | v3_carry_trend_7p | v3_carry_only |
|---|---|---|---|---|
| 2014.0 | 5.87 | 1.56 | 5.21 | 0.00 |
| 2015.0 | 1.51 | 1.17 | 0.61 | 0.55 |
| 2016.0 | 0.26 | 0.94 | 0.81 | 0.00 |
| 2017.0 | 0.47 | 0.57 | 2.27 | 0.00 |
| 2018.0 | 0.72 | 0.63 | 0.86 | 7.40 |
| 2019.0 | 0.14 | 0.05 | 0.46 | — |
| 2020.0 | 1.45 | 6.27 | 2.73 | — |
| 2021.0 | 2.63 | 14.92 | — | — |
| 2022.0 | 0.93 | 0.28 | 0.57 | 30.54 |
| 2023.0 | 49.03 | 26.32 | 197.93 | — |
| 2024.0 | 1.97 | 0.07 | 0.00 | 0.00 |
| 2025.0 | 2.61 | 7.67 | 1.60 | — |
| 2026.0 | 0.00 | 0.00 | — | — |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v3_carry_trend_xs | AUDJPY | 29 | +21,668 | 1.20 | 41% | 108 | +14,894 |
| v3_carry_trend_xs | AUDUSD | 32 | -71,833 | 0.39 | 44% | 102 | -80 |
| v3_carry_trend_xs | EURJPY | 30 | +22,443 | 1.27 | 27% | 64 | +1,350 |
| v3_carry_trend_xs | EURUSD | 19 | +491,861 | 15.78 | 63% | 81 | -13,459 |
| v3_carry_trend_xs | GBPJPY | 21 | +107,936 | 1.68 | 33% | 162 | +7,595 |
| v3_carry_trend_xs | GBPUSD | 25 | +64,520 | 1.92 | 44% | 76 | -10,964 |
| v3_carry_trend_xs | USDJPY | 23 | -31,927 | 0.76 | 35% | 64 | +8,226 |
| v3_carry_trend_mh | AUDJPY | 38 | +4,948 | 1.11 | 39% | 36 | +10,552 |
| v3_carry_trend_mh | AUDUSD | 39 | -2,522 | 0.93 | 28% | 38 | -1,656 |
| v3_carry_trend_mh | EURJPY | 26 | +26,685 | 1.84 | 35% | 24 | +5,004 |
| v3_carry_trend_mh | EURUSD | 29 | +32,820 | 2.44 | 45% | 18 | +327 |
| v3_carry_trend_mh | GBPJPY | 15 | -3,692 | 0.87 | 27% | 37 | +9,237 |
| v3_carry_trend_mh | GBPUSD | 27 | +7,399 | 1.29 | 48% | 25 | -2,957 |
| v3_carry_trend_mh | USDJPY | 28 | +140,252 | 6.05 | 46% | 17 | +35,766 |
| v3_carry_trend_7p | AUDJPY | 18 | +7,080 | 1.31 | 44% | 44 | +10,124 |
| v3_carry_trend_7p | AUDUSD | 24 | +3,297 | 1.12 | 38% | 38 | -1,499 |
| v3_carry_trend_7p | EURJPY | 16 | +25,094 | 2.28 | 50% | 27 | +4,445 |
| v3_carry_trend_7p | EURUSD | 21 | +88,051 | 4.09 | 43% | 24 | +179 |
| v3_carry_trend_7p | GBPJPY | 12 | +36,353 | 2.42 | 25% | 50 | +18,460 |
| v3_carry_trend_7p | GBPUSD | 15 | +22,156 | 2.91 | 60% | 31 | -3,982 |
| v3_carry_trend_7p | USDJPY | 22 | +139,270 | 5.36 | 27% | 19 | +34,210 |
| v3_carry_only | AUDJPY | 2 | -23,160 | 0.00 | 0% | 54 | +4,287 |
| v3_carry_only | AUDUSD | 6 | +3,892 | 1.23 | 33% | 49 | +965 |
| v3_carry_only | EURJPY | 1 | +61,369 | — | 100% | 50 | +4,132 |
| v3_carry_only | EURUSD | 5 | +80,099 | 5.76 | 20% | 17 | +29,848 |
| v3_carry_only | GBPJPY | 1 | +316,426 | — | 100% | 96 | +90,558 |
| v3_carry_only | GBPUSD | 4 | +42,814 | 4.22 | 25% | 47 | +1,749 |
| v3_carry_only | USDJPY | 9 | +42,684 | 1.90 | 22% | 47 | +49,172 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v3_carry_trend_xs | regime4h | HIGH_VOL | 14 | +62,429 | 64% | 2.49 |
| v3_carry_trend_xs | regime4h | NEUTRAL | 66 | +263,338 | 36% | 2.10 |
| v3_carry_trend_xs | regime4h | RANGE | 66 | +98,327 | 44% | 1.33 |
| v3_carry_trend_xs | regime4h | TREND | 111 | +666,913 | 37% | 2.25 |
| v3_carry_trend_xs | month_dir | DOWN | 64 | -43,143 | 39% | 0.88 |
| v3_carry_trend_xs | month_dir | FLAT | 135 | +989,029 | 36% | 2.77 |
| v3_carry_trend_xs | month_dir | UP | 58 | +145,122 | 50% | 1.75 |
| v3_carry_trend_xs | month_vol | HIGH_VOL | 76 | +230,331 | 42% | 1.53 |
| v3_carry_trend_xs | month_vol | LOW_VOL | 181 | +860,677 | 39% | 2.27 |
| v3_carry_trend_mh | regime4h | HIGH_VOL | 27 | +13,144 | 33% | 1.39 |
| v3_carry_trend_mh | regime4h | NEUTRAL | 49 | +101,085 | 49% | 3.03 |
| v3_carry_trend_mh | regime4h | RANGE | 72 | +105,006 | 35% | 2.27 |
| v3_carry_trend_mh | regime4h | TREND | 122 | +29,662 | 41% | 1.24 |
| v3_carry_trend_mh | month_dir | DOWN | 64 | +12,491 | 36% | 1.16 |
| v3_carry_trend_mh | month_dir | FLAT | 141 | +168,794 | 39% | 2.13 |
| v3_carry_trend_mh | month_dir | UP | 65 | +67,612 | 46% | 2.08 |
| v3_carry_trend_mh | month_vol | HIGH_VOL | 79 | +2,084 | 35% | 1.02 |
| v3_carry_trend_mh | month_vol | LOW_VOL | 191 | +246,813 | 42% | 2.25 |
| v3_carry_trend_7p | regime4h | HIGH_VOL | 9 | +13,221 | 56% | 2.63 |
| v3_carry_trend_7p | regime4h | NEUTRAL | 32 | +167,706 | 47% | 5.86 |
| v3_carry_trend_7p | regime4h | RANGE | 29 | +107,687 | 38% | 3.56 |
| v3_carry_trend_7p | regime4h | TREND | 58 | +32,687 | 36% | 1.39 |
| v3_carry_trend_7p | month_dir | DOWN | 29 | +27,097 | 52% | 1.66 |
| v3_carry_trend_7p | month_dir | FLAT | 71 | +234,582 | 35% | 3.72 |
| v3_carry_trend_7p | month_dir | UP | 28 | +59,621 | 43% | 2.48 |
| v3_carry_trend_7p | month_vol | HIGH_VOL | 35 | +5,225 | 37% | 1.09 |
| v3_carry_trend_7p | month_vol | LOW_VOL | 93 | +316,076 | 42% | 3.89 |
| v3_carry_only | regime4h | HIGH_VOL | 8 | +453,273 | 50% | 20.36 |
| v3_carry_only | regime4h | NEUTRAL | 3 | -13,033 | 0% | 0.00 |
| v3_carry_only | regime4h | RANGE | 5 | -23,310 | 0% | 0.00 |
| v3_carry_only | regime4h | TREND | 18 | +64,336 | 22% | 1.64 |
| v3_carry_only | month_dir | DOWN | 8 | -45,847 | 0% | 0.00 |
| v3_carry_only | month_dir | FLAT | 18 | +19,146 | 22% | 1.21 |
| v3_carry_only | month_dir | UP | 8 | +507,968 | 50% | 23.21 |
| v3_carry_only | month_vol | HIGH_VOL | 20 | +464,189 | 35% | 6.73 |
| v3_carry_only | month_vol | LOW_VOL | 14 | +17,078 | 7% | 1.21 |

## 比較: sizing（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | sizing | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v3_carry_only | risk_stop | 37 | +8.4% | 1.79 | 0.22 | -0.28 | 0.84 | -10.8% |
| v3_carry_only | vol_target | 32 | +37.5% | 2.23 | 0.26 | -0.24 | 0.84 | -30.3% |
| v3_carry_trend_xs | risk_stop | 201 | +23.8% | 1.98 | 0.50 | 0.22 | 0.81 | -6.1% |
| v3_carry_trend_xs | vol_target | 237 | +126.6% | 1.75 | 0.50 | 0.24 | 0.84 | -25.0% |

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
USDJPY  4191               0.0219            0.2991             1.156               9             1 2013-06-06
EURUSD  4191               0.0254            0.3177             0.884               9             0 2011-10-07
GBPUSD  4191               0.0257            0.3183             1.817              11             1 2020-03-18
AUDUSD  4191               0.0303            0.3768             1.172              20             3 2020-03-12
NZDUSD  4191               0.0362            0.4022             1.450              23             2 2011-08-05
USDCAD  4191               0.0250            0.2946             0.895               9             0 2020-03-12
USDCHF  4191               0.0277            0.3102             1.041               8             1 2011-10-07
