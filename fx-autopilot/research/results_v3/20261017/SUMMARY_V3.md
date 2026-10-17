# FX AUTOPILOT V3 研究結果（2026-10-17 01:32 UTC、データ〜2026-10-16 20:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v3.yaml`

> **検証汚染の申告**: 設計者は v1 と V2 の 2010〜2026 の結果（v2_trend_carry の composite だけが事前登録ゲートを通り、 利益が USDJPY と少数の大きなトレードに集中していたこと）を見たうえで V3 を設計している。 よって V3 の Walk-Forward 成績は「汚染あり」。新規ペア（AUDJPY / GBPJPY）は V1/V2 の設計に使っていないが、期間は同じ。 V3 の最終判断は LOCK 後の PAPER Forward のみ。V2 の LOCK（v2_trend_carry など）は変更しない。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v3_carry_trend_7p | REJECTED | 128 | +28.9% | +2.0% | 2.91 | 0.54 | 0.75 | -8.3% | 2,501 | 32 | 0.02 | 7 | 85% | 24% | +8.0% | +19.4% | 1.93 | 7 | 53% | 0.76 | 1 | top1_trade_dependence |
| v3_carry_trend_xs | REJECTED | 180 | +50.2% | +3.2% | 1.86 | 0.50 | 0.73 | -13.3% | 3,357 | 93 | 0.03 | 9 | 69% | 30% | +29.4% | +16.1% | 1.65 | 5 | 61% | 0.71 | 3 | top5_trade_dependence, top1_trade_dependence |
| v3_carry_only | REJECTED | 28 | +48.3% | +3.1% | 5.47 | 0.40 | 0.56 | -18.8% | 18,812 | 45 | 0.00 | 14 | 62% | 36% | -4.5% | +55.3% | 3.78 | 6 | 88% | 0.60 | 2 | trades, subperiod_not_positive, single_regime_dependence, top5_trade_dependence, top1_trade_dependence |
| v3_carry_trend_mh | REJECTED | 203 | +15.9% | +1.2% | 1.94 | 0.37 | 0.50 | -8.7% | 1,011 | 28 | 0.04 | 10 | 69% | 23% | +0.2% | +15.6% | 1.24 | 5 | 42% | 0.54 | 3 | sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v3_carry_trend_xs | REJECTED | 180 | 68% | 124% | -146,729 | 0.79 | 1% | +6.9% |
| v3_carry_trend_mh | REJECTED | 203 | 60% | 111% | -22,616 | 0.90 | 28% | +7.4% |
| v3_carry_trend_7p | REJECTED | 128 | 39% | 91% | +27,578 | 1.16 | 19% | +9.8% |
| v3_carry_only | REJECTED | 28 | 61% | 118% | -94,805 | 0.20 | 34% | +27.9% |

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
| 2026.0 | +0.2% | +0.5% | +2.2% | +2.8% |

## 年別 Profit Factor（WF OOS）

| year | v3_carry_trend_xs | v3_carry_trend_mh | v3_carry_trend_7p | v3_carry_only |
|---|---|---|---|---|
| 2014.0 | 5.87 | 1.56 | 5.21 | 0.00 |
| 2015.0 | 1.51 | 1.17 | 0.61 | 0.55 |
| 2016.0 | 0.26 | 0.94 | 0.81 | 0.00 |
| 2017.0 | 0.47 | 0.57 | 2.27 | 0.00 |
| 2018.0 | 0.72 | 0.63 | 0.86 | 7.28 |
| 2019.0 | 0.14 | 0.05 | 0.46 | — |
| 2020.0 | 1.45 | 6.27 | 2.73 | — |
| 2021.0 | 2.63 | 14.88 | — | — |
| 2022.0 | 0.93 | 0.28 | 0.57 | 30.96 |
| 2023.0 | 49.52 | 26.32 | 200.97 | — |
| 2024.0 | 1.97 | 0.07 | 0.00 | 0.00 |
| 2025.0 | 2.55 | 7.75 | 1.55 | — |
| 2026.0 | 0.00 | 0.00 | — | — |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v3_carry_trend_xs | AUDJPY | 29 | +20,888 | 1.20 | 41% | 108 | +14,932 |
| v3_carry_trend_xs | AUDUSD | 32 | -71,833 | 0.39 | 44% | 102 | -80 |
| v3_carry_trend_xs | EURJPY | 30 | +22,443 | 1.27 | 27% | 64 | +1,350 |
| v3_carry_trend_xs | EURUSD | 20 | +491,208 | 15.48 | 60% | 78 | -13,444 |
| v3_carry_trend_xs | GBPJPY | 21 | +109,094 | 1.69 | 33% | 162 | +7,681 |
| v3_carry_trend_xs | GBPUSD | 25 | +64,520 | 1.92 | 44% | 76 | -10,964 |
| v3_carry_trend_xs | USDJPY | 23 | -32,126 | 0.76 | 35% | 64 | +8,281 |
| v3_carry_trend_mh | AUDJPY | 38 | +4,168 | 1.09 | 39% | 36 | +10,590 |
| v3_carry_trend_mh | AUDUSD | 39 | -2,522 | 0.93 | 28% | 38 | -1,656 |
| v3_carry_trend_mh | EURJPY | 26 | +26,685 | 1.84 | 35% | 24 | +5,004 |
| v3_carry_trend_mh | EURUSD | 30 | +32,167 | 2.37 | 43% | 18 | +343 |
| v3_carry_trend_mh | GBPJPY | 15 | -2,534 | 0.91 | 27% | 37 | +9,323 |
| v3_carry_trend_mh | GBPUSD | 27 | +7,399 | 1.29 | 48% | 25 | -2,957 |
| v3_carry_trend_mh | USDJPY | 28 | +139,855 | 6.03 | 46% | 17 | +35,877 |
| v3_carry_trend_7p | AUDJPY | 18 | +6,300 | 1.28 | 44% | 44 | +10,162 |
| v3_carry_trend_7p | AUDUSD | 24 | +3,297 | 1.12 | 38% | 38 | -1,499 |
| v3_carry_trend_7p | EURJPY | 16 | +25,094 | 2.28 | 50% | 27 | +4,445 |
| v3_carry_trend_7p | EURUSD | 21 | +86,863 | 4.04 | 43% | 24 | +215 |
| v3_carry_trend_7p | GBPJPY | 12 | +37,511 | 2.47 | 25% | 50 | +18,546 |
| v3_carry_trend_7p | GBPUSD | 15 | +22,156 | 2.91 | 60% | 31 | -3,982 |
| v3_carry_trend_7p | USDJPY | 22 | +138,872 | 5.35 | 27% | 19 | +34,320 |
| v3_carry_only | AUDJPY | 2 | -23,160 | 0.00 | 0% | 54 | +4,287 |
| v3_carry_only | AUDUSD | 6 | +3,892 | 1.23 | 33% | 49 | +965 |
| v3_carry_only | EURJPY | 1 | +62,177 | — | 100% | 51 | +4,175 |
| v3_carry_only | EURUSD | 5 | +77,656 | 5.62 | 20% | 18 | +29,921 |
| v3_carry_only | GBPJPY | 1 | +321,059 | — | 100% | 98 | +90,903 |
| v3_carry_only | GBPUSD | 4 | +42,814 | 4.22 | 25% | 47 | +1,749 |
| v3_carry_only | USDJPY | 9 | +42,287 | 1.89 | 22% | 47 | +49,283 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v3_carry_trend_xs | regime4h | HIGH_VOL | 14 | +62,429 | 64% | 2.49 |
| v3_carry_trend_xs | regime4h | NEUTRAL | 67 | +263,063 | 36% | 2.10 |
| v3_carry_trend_xs | regime4h | RANGE | 66 | +98,129 | 44% | 1.33 |
| v3_carry_trend_xs | regime4h | TREND | 111 | +666,913 | 37% | 2.25 |
| v3_carry_trend_xs | month_dir | DOWN | 64 | -43,143 | 39% | 0.88 |
| v3_carry_trend_xs | month_dir | FLAT | 136 | +987,397 | 36% | 2.77 |
| v3_carry_trend_xs | month_dir | UP | 58 | +146,280 | 50% | 1.76 |
| v3_carry_trend_xs | month_vol | HIGH_VOL | 76 | +229,551 | 42% | 1.52 |
| v3_carry_trend_xs | month_vol | LOW_VOL | 182 | +860,983 | 39% | 2.27 |
| v3_carry_trend_mh | regime4h | HIGH_VOL | 27 | +13,144 | 33% | 1.39 |
| v3_carry_trend_mh | regime4h | NEUTRAL | 50 | +99,652 | 48% | 2.97 |
| v3_carry_trend_mh | regime4h | RANGE | 72 | +104,608 | 35% | 2.26 |
| v3_carry_trend_mh | regime4h | TREND | 122 | +30,820 | 41% | 1.24 |
| v3_carry_trend_mh | month_dir | DOWN | 64 | +12,491 | 36% | 1.16 |
| v3_carry_trend_mh | month_dir | FLAT | 142 | +168,121 | 39% | 2.12 |
| v3_carry_trend_mh | month_dir | UP | 65 | +67,612 | 46% | 2.08 |
| v3_carry_trend_mh | month_vol | HIGH_VOL | 79 | +1,304 | 35% | 1.01 |
| v3_carry_trend_mh | month_vol | LOW_VOL | 192 | +246,920 | 42% | 2.25 |
| v3_carry_trend_7p | regime4h | HIGH_VOL | 9 | +13,221 | 56% | 2.63 |
| v3_carry_trend_7p | regime4h | NEUTRAL | 32 | +168,085 | 47% | 5.87 |
| v3_carry_trend_7p | regime4h | RANGE | 29 | +107,289 | 38% | 3.55 |
| v3_carry_trend_7p | regime4h | TREND | 58 | +31,499 | 36% | 1.38 |
| v3_carry_trend_7p | month_dir | DOWN | 29 | +27,097 | 52% | 1.66 |
| v3_carry_trend_7p | month_dir | FLAT | 71 | +232,217 | 35% | 3.69 |
| v3_carry_trend_7p | month_dir | UP | 28 | +60,779 | 43% | 2.51 |
| v3_carry_trend_7p | month_vol | HIGH_VOL | 35 | +4,445 | 37% | 1.08 |
| v3_carry_trend_7p | month_vol | LOW_VOL | 93 | +315,649 | 42% | 3.89 |
| v3_carry_only | regime4h | HIGH_VOL | 8 | +456,272 | 50% | 20.49 |
| v3_carry_only | regime4h | NEUTRAL | 3 | -13,033 | 0% | 0.00 |
| v3_carry_only | regime4h | RANGE | 5 | -23,310 | 0% | 0.00 |
| v3_carry_only | regime4h | TREND | 18 | +63,939 | 22% | 1.63 |
| v3_carry_only | month_dir | DOWN | 8 | -45,847 | 0% | 0.00 |
| v3_carry_only | month_dir | FLAT | 18 | +18,748 | 22% | 1.20 |
| v3_carry_only | month_dir | UP | 8 | +510,966 | 50% | 23.35 |
| v3_carry_only | month_vol | HIGH_VOL | 20 | +469,232 | 35% | 6.80 |
| v3_carry_only | month_vol | LOW_VOL | 14 | +14,636 | 7% | 1.18 |

## 比較: sizing（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | sizing | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v3_carry_only | risk_stop | 37 | +8.3% | 1.79 | 0.22 | -0.28 | 0.83 | -10.8% |
| v3_carry_only | vol_target | 32 | +37.8% | 2.24 | 0.26 | -0.24 | 0.85 | -30.3% |
| v3_carry_trend_xs | risk_stop | 202 | +23.8% | 1.98 | 0.50 | 0.22 | 0.81 | -6.1% |
| v3_carry_trend_xs | vol_target | 238 | +125.9% | 1.74 | 0.50 | 0.24 | 0.84 | -25.0% |

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
USDJPY  4196               0.0219            0.2988             1.156               9             1 2013-06-06
EURUSD  4196               0.0255            0.3175             0.884               9             0 2011-10-07
GBPUSD  4196               0.0257            0.3182             1.817              11             1 2020-03-18
AUDUSD  4196               0.0303            0.3768             1.172              20             3 2020-03-12
NZDUSD  4196               0.0364            0.4022             1.450              23             2 2011-08-05
USDCAD  4196               0.0250            0.2946             0.895               9             0 2020-03-12
USDCHF  4196               0.0278            0.3102             1.041               8             1 2011-10-07
