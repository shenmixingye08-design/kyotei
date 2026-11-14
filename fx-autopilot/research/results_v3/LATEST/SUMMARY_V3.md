# FX AUTOPILOT V3 研究結果（2026-11-14 03:13 UTC、データ〜2026-11-13 21:00:00+00:00）

**PAPER / BACKTEST のみ。利益を保証しません。** 事前登録: `config/research_plan_v3.yaml`

> **検証汚染の申告**: 設計者は v1 と V2 の 2010〜2026 の結果（v2_trend_carry の composite だけが事前登録ゲートを通り、 利益が USDJPY と少数の大きなトレードに集中していたこと）を見たうえで V3 を設計している。 よって V3 の Walk-Forward 成績は「汚染あり」。新規ペア（AUDJPY / GBPJPY）は V1/V2 の設計に使っていないが、期間は同じ。 V3 の最終判断は LOCK 後の PAPER Forward のみ。V2 の LOCK（v2_trend_carry など）は変更しない。

コスト: bid/ask 実効スプレッド（実測と原則固定の大きい方）+ スリッページ + 手数料 + スワップ（政策金利差, 1か月ラグ）+ 1本の執行遅延。
単位: 5 ペアのポートフォリオ（同一パラメータ）。WF: 拡張窓（2010〜Y-1 で選択 → Y 年）、2014〜2026（2026 は部分年）。

## 候補一覧（WF OOS 連結・コスト込み）

| candidate | status | n_trades | net_return | cagr | profit_factor | sharpe | sortino | max_drawdown | expectancy_jpy | cost_per_trade_jpy | cost_ratio | max_consecutive_losses | positive_year_ratio | max_single_year_share | ret_A | ret_B | stress_pf | positive_pairs | max_regime_share | dsr | param_changes | gate_fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v3_carry_trend_7p | REJECTED | 128 | +30.0% | +2.1% | 2.97 | 0.55 | 0.76 | -8.3% | 2,583 | 32 | 0.02 | 7 | 85% | 23% | +8.0% | +20.4% | 1.96 | 7 | 51% | 0.77 | 1 | top1_trade_dependence |
| v3_carry_trend_xs | REJECTED | 181 | +51.3% | +3.3% | 1.87 | 0.51 | 0.74 | -13.3% | 3,394 | 92 | 0.03 | 9 | 69% | 30% | +29.4% | +16.9% | 1.66 | 5 | 61% | 0.71 | 3 | top5_trade_dependence, top1_trade_dependence |
| v3_carry_only | REJECTED | 28 | +50.2% | +3.2% | 5.62 | 0.41 | 0.57 | -18.8% | 19,442 | 45 | 0.00 | 14 | 62% | 35% | -4.5% | +57.2% | 3.89 | 6 | 87% | 0.61 | 2 | trades, subperiod_not_positive, single_regime_dependence, top5_trade_dependence, top1_trade_dependence |
| v3_carry_trend_mh | REJECTED | 203 | +16.5% | +1.2% | 1.97 | 0.38 | 0.52 | -8.7% | 1,044 | 28 | 0.04 | 10 | 69% | 22% | +0.2% | +16.2% | 1.26 | 5 | 43% | 0.55 | 3 | sharpe, top5_trade_dependence, top1_trade_dependence |

ret_A = 2014〜2021、ret_B = 2022〜2026（部分年）。max_single_year_share = プラス年の利益に占める最大年の割合（40% 超は単年依存）。

## 診断（報告のみ・ゲート外）: 少数トレードへの利益集中・スワップ依存・直近

| candidate | status | n_trades | diag_top1_share | diag_top5_share | diag_pnl_ex_top5 | diag_pf_ex_top5 | diag_swap_share | diag_ret_2024_2026 |
|---|---|---|---|---|---|---|---|---|
| v3_carry_trend_xs | REJECTED | 181 | 67% | 122% | -137,488 | 0.80 | 1% | +7.7% |
| v3_carry_trend_mh | REJECTED | 203 | 60% | 109% | -19,080 | 0.91 | 27% | +8.0% |
| v3_carry_trend_7p | REJECTED | 128 | 39% | 90% | +33,448 | 1.20 | 19% | +10.6% |
| v3_carry_only | REJECTED | 28 | 60% | 117% | -94,805 | 0.20 | 34% | +29.5% |

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
| 2026.0 | +1.0% | +1.0% | +3.1% | +4.1% |

## 年別 Profit Factor（WF OOS）

| year | v3_carry_trend_xs | v3_carry_trend_mh | v3_carry_trend_7p | v3_carry_only |
|---|---|---|---|---|
| 2014.0 | 5.87 | 1.56 | 5.21 | 0.00 |
| 2015.0 | 1.51 | 1.17 | 0.61 | 0.55 |
| 2016.0 | 0.26 | 0.94 | 0.81 | 0.00 |
| 2017.0 | 0.47 | 0.57 | 2.27 | 0.00 |
| 2018.0 | 0.72 | 0.63 | 0.86 | 8.00 |
| 2019.0 | 0.14 | 0.05 | 0.46 | — |
| 2020.0 | 1.45 | 6.27 | 2.73 | — |
| 2021.0 | 2.63 | 15.25 | — | — |
| 2022.0 | 0.93 | 0.28 | 0.57 | 31.27 |
| 2023.0 | 49.86 | 26.32 | 203.12 | — |
| 2024.0 | 1.97 | 0.07 | 0.00 | 0.00 |
| 2025.0 | 2.72 | 7.64 | 1.47 | — |
| 2026.0 | 0.52 | 0.53 | — | — |

## 通貨ペア別（WF OOS）

| candidate | pair | trades | pnl_jpy | profit_factor | win_rate | avg_cost_jpy | swap_jpy |
|---|---|---|---|---|---|---|---|
| v3_carry_trend_xs | AUDJPY | 29 | +21,809 | 1.21 | 41% | 108 | +15,015 |
| v3_carry_trend_xs | AUDUSD | 33 | -68,953 | 0.41 | 45% | 100 | -115 |
| v3_carry_trend_xs | EURJPY | 30 | +22,443 | 1.27 | 27% | 64 | +1,350 |
| v3_carry_trend_xs | EURUSD | 20 | +494,744 | 15.87 | 65% | 78 | -13,365 |
| v3_carry_trend_xs | GBPJPY | 21 | +109,913 | 1.69 | 33% | 162 | +8,058 |
| v3_carry_trend_xs | GBPUSD | 25 | +64,520 | 1.92 | 44% | 76 | -10,964 |
| v3_carry_trend_xs | USDJPY | 23 | -30,221 | 0.78 | 35% | 64 | +8,521 |
| v3_carry_trend_mh | AUDJPY | 38 | +2,795 | 1.06 | 39% | 36 | +10,755 |
| v3_carry_trend_mh | AUDUSD | 39 | -2,522 | 0.93 | 28% | 38 | -1,656 |
| v3_carry_trend_mh | EURJPY | 26 | +26,685 | 1.84 | 35% | 24 | +5,004 |
| v3_carry_trend_mh | EURUSD | 30 | +35,702 | 2.56 | 47% | 18 | +421 |
| v3_carry_trend_mh | GBPJPY | 15 | -1,714 | 0.94 | 27% | 37 | +9,700 |
| v3_carry_trend_mh | GBPUSD | 27 | +7,399 | 1.29 | 48% | 25 | -2,957 |
| v3_carry_trend_mh | USDJPY | 28 | +143,665 | 6.17 | 46% | 17 | +36,356 |
| v3_carry_trend_7p | AUDJPY | 18 | +4,927 | 1.22 | 44% | 44 | +10,327 |
| v3_carry_trend_7p | AUDUSD | 24 | +3,297 | 1.12 | 38% | 38 | -1,499 |
| v3_carry_trend_7p | EURJPY | 16 | +25,094 | 2.28 | 50% | 27 | +4,445 |
| v3_carry_trend_7p | EURUSD | 21 | +94,106 | 4.30 | 43% | 24 | +373 |
| v3_carry_trend_7p | GBPJPY | 12 | +38,331 | 2.50 | 25% | 50 | +18,923 |
| v3_carry_trend_7p | GBPUSD | 15 | +22,156 | 2.91 | 60% | 31 | -3,982 |
| v3_carry_trend_7p | USDJPY | 22 | +142,682 | 5.46 | 27% | 19 | +34,800 |
| v3_carry_only | AUDJPY | 2 | -23,160 | 0.00 | 0% | 54 | +4,287 |
| v3_carry_only | AUDUSD | 6 | +3,892 | 1.23 | 33% | 49 | +965 |
| v3_carry_only | EURJPY | 1 | +57,812 | — | 100% | 49 | +4,364 |
| v3_carry_only | EURUSD | 5 | +92,569 | 6.50 | 20% | 18 | +30,236 |
| v3_carry_only | GBPJPY | 1 | +324,338 | — | 100% | 104 | +92,410 |
| v3_carry_only | GBPUSD | 4 | +42,814 | 4.22 | 25% | 47 | +1,749 |
| v3_carry_only | USDJPY | 9 | +46,096 | 1.97 | 22% | 47 | +49,763 |

## レジーム別（WF OOS、エントリー時点の 4H レジーム / 月次の方向・ボラ）

| candidate | dimension | state | trades | pnl_jpy | win_rate | profit_factor |
|---|---|---|---|---|---|---|
| v3_carry_trend_xs | regime4h | HIGH_VOL | 14 | +62,429 | 64% | 2.49 |
| v3_carry_trend_xs | regime4h | NEUTRAL | 67 | +268,340 | 37% | 2.12 |
| v3_carry_trend_xs | regime4h | RANGE | 66 | +100,034 | 44% | 1.33 |
| v3_carry_trend_xs | regime4h | TREND | 112 | +669,793 | 38% | 2.25 |
| v3_carry_trend_xs | month_dir | DOWN | 65 | -40,263 | 40% | 0.89 |
| v3_carry_trend_xs | month_dir | FLAT | 136 | +993,758 | 37% | 2.78 |
| v3_carry_trend_xs | month_dir | UP | 58 | +147,100 | 50% | 1.76 |
| v3_carry_trend_xs | month_vol | HIGH_VOL | 76 | +230,472 | 42% | 1.53 |
| v3_carry_trend_xs | month_vol | LOW_VOL | 183 | +870,123 | 40% | 2.29 |
| v3_carry_trend_mh | regime4h | HIGH_VOL | 27 | +13,144 | 33% | 1.39 |
| v3_carry_trend_mh | regime4h | NEUTRAL | 50 | +101,815 | 50% | 3.04 |
| v3_carry_trend_mh | regime4h | RANGE | 72 | +108,418 | 35% | 2.31 |
| v3_carry_trend_mh | regime4h | TREND | 122 | +31,640 | 41% | 1.25 |
| v3_carry_trend_mh | month_dir | DOWN | 64 | +12,491 | 36% | 1.16 |
| v3_carry_trend_mh | month_dir | FLAT | 142 | +174,913 | 39% | 2.17 |
| v3_carry_trend_mh | month_dir | UP | 65 | +67,612 | 46% | 2.08 |
| v3_carry_trend_mh | month_vol | HIGH_VOL | 79 | -69 | 35% | 1.00 |
| v3_carry_trend_mh | month_vol | LOW_VOL | 192 | +255,085 | 42% | 2.29 |
| v3_carry_trend_7p | regime4h | HIGH_VOL | 9 | +13,221 | 56% | 2.63 |
| v3_carry_trend_7p | regime4h | NEUTRAL | 32 | +167,531 | 47% | 5.85 |
| v3_carry_trend_7p | regime4h | RANGE | 29 | +111,099 | 38% | 3.64 |
| v3_carry_trend_7p | regime4h | TREND | 58 | +38,742 | 36% | 1.47 |
| v3_carry_trend_7p | month_dir | DOWN | 29 | +27,097 | 52% | 1.66 |
| v3_carry_trend_7p | month_dir | FLAT | 71 | +241,897 | 35% | 3.80 |
| v3_carry_trend_7p | month_dir | UP | 28 | +61,599 | 43% | 2.53 |
| v3_carry_trend_7p | month_vol | HIGH_VOL | 35 | +3,072 | 37% | 1.05 |
| v3_carry_trend_7p | month_vol | LOW_VOL | 93 | +327,521 | 42% | 3.99 |
| v3_carry_only | regime4h | HIGH_VOL | 8 | +470,099 | 50% | 21.08 |
| v3_carry_only | regime4h | NEUTRAL | 3 | -13,033 | 0% | 0.00 |
| v3_carry_only | regime4h | RANGE | 5 | -23,310 | 0% | 0.00 |
| v3_carry_only | regime4h | TREND | 18 | +67,748 | 22% | 1.67 |
| v3_carry_only | month_dir | DOWN | 8 | -45,847 | 0% | 0.00 |
| v3_carry_only | month_dir | FLAT | 18 | +22,558 | 22% | 1.25 |
| v3_carry_only | month_dir | UP | 8 | +524,794 | 50% | 23.95 |
| v3_carry_only | month_vol | HIGH_VOL | 20 | +471,956 | 35% | 6.83 |
| v3_carry_only | month_vol | LOW_VOL | 14 | +29,549 | 7% | 1.37 |

## 比較: sizing（グリッド全点・非 WF・他の次元で平均。事前登録した全候補を表示）

| candidate | sizing | trades | full_ret | full_pf | full_sharpe | A_sharpe | B_sharpe | max_dd |
|---|---|---|---|---|---|---|---|---|
| v3_carry_only | risk_stop | 37 | +8.8% | 1.84 | 0.23 | -0.28 | 0.85 | -10.8% |
| v3_carry_only | vol_target | 32 | +39.5% | 2.30 | 0.27 | -0.24 | 0.86 | -30.3% |
| v3_carry_trend_xs | risk_stop | 203 | +24.4% | 2.00 | 0.51 | 0.22 | 0.84 | -6.1% |
| v3_carry_trend_xs | vol_target | 240 | +132.3% | 1.78 | 0.51 | 0.24 | 0.88 | -25.0% |

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
