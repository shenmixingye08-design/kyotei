# FX AUTOPILOT — FX 専用 研究・PAPER 自動売買基盤

**PAPER / DEMO / BACKTEST / FORWARD TEST のみ。LIVE（実資金）注文・入出金・資金移動は本人の明示承認まで行いません。
LIVE の発注経路はコードに存在せず、`fxap/safety.py` が設定・環境変数・承認ファイルのどれかが LIVE を示した時点で停止します。利益は保証しません。**

役割: FX = 資本成長を狙う攻め側 → 確定利益から税・予備資金を確保 → 余剰を IBKR 長期運用（守り側、別 repo `ai-investment-research`）へ移す。
FX の研究・戦略は長期投資ロジックと混ぜません（コードも repo も分離。指標計算の式だけ `aiquant/metrics.py` から移植）。

## 構成

```
Market Data (Dukascopy bid/ask H1, 2010〜) ─ 品質検査（価格帯・スプレッド・欠損・逆転気配）→ NG なら研究停止
  ↓
Signal Engine (fxap/strategies: 9 戦略 × 事前登録パラメータ)
  ↓
Risk Engine (fxap/risk.py: 口座残高ベースのサイズ計算・レバ/通貨別上限・日次/週次損失・DD Kill Switch・スプレッド/データ鮮度)
  ↓
Order Engine (fxap/paper_engine.py: 冪等 client_order_id・発注失敗/切断時の停止)
  ↓
Broker Adapter (fxap/broker: PaperBroker。外部 DEMO は docs/BROKER_COMPARISON.md 参照)
  ↓
Execution Confirmation → Position Manager（SL/TP/トレーリング/時間切れ）→ PnL / Drawdown
  ↓
Logging（paper_forward/<spec>/ledger.jsonl ハッシュチェーン）→ Research DB（equity.csv / trades.csv / research/results）
  ↓
Tournament（Champion / Challenger）→ Dashboard（public/index.html・DASHBOARD.md）→ Profit Sweep 計算
```

| 系統 | 戦略 ID | 内容 |
|---|---|---|
| A Trend | `trend_ema_adx` / `trend_donchian` / `trend_tsmom` | EMA クロス + ADX / Donchian ブレイクアウト / ボラ正規化モメンタム |
| B Mean Reversion | `mr_rsi_bb` / `mr_zscore` | RSI + Bollinger（ADX<25 のみ）/ EMA 乖離 z |
| C Regime | `regime_switch` | 4H ADX・ATR 順位で TREND / RANGE / HIGH_VOL を判定し戦略切替 |
| D Multi Timeframe | `mtf_pullback` | 4H 環境 → 1H 方向 → 1H RSI 押し目 |
| F ML | `ml_logit` / `ml_lgbm` | 毎年再学習（パージ付き拡張窓）。Deep Learning は未採用 |
| ベンチマーク | `random` | ランダム売買（同じ SL/TP・コスト） |

E（Market Microstructure）: 時間帯別の実測スプレッド・値幅を `microstructure.csv` に出し、Risk Engine が異常スプレッド時の新規を禁止。
Tick / 板情報は Dukascopy では出来高のみのため戦略化していない。

## 検証の手順（`config/research_plan.yaml` に事前登録）

1. TRAIN 2010–2018 / VALIDATION 2019–2021 / TEST 2022–2025-06 / FORWARD 2025-07〜
2. Stage 1: **データを 2021-12-31 で切り詰めてから**全戦略 × パラメータ × ペアを評価。Walk-Forward（4 年 → 1 年、2014–2021）
3. LOCK（`config/locked/*.json`: パラメータ・Risk・コスト・コードハッシュ）。同じ ID で変更不可 → 改善は `_v2`
4. Stage 2: LOCK 済み仕様だけを TEST / FORWARD で評価（コスト 2 倍・IBKR コスト・レバレッジ none/low/medium・年別・局面別・イベント別）
5. ゲート A（WF + VALIDATION）→ ゲート B（TEST・FORWARD・コスト耐性・DD）→ LOCK 後 PAPER（3 か月・20 取引・プラス・乖離）
   → LIVE 候補として**報告するだけ**。LIVE 開始は本人の承認が必須

コスト: 実効スプレッド = max(Dukascopy 実測, 国内業者の原則固定) + スリッページ（成行 0.2 / 逆指値 0.5 pip）+ スワップ（政策金利差 − 年 1%）
+ 足 1 本の執行遅延（足 i の終値で判断 → 足 i+1 の始値で約定）。同じ足で SL と TP に触れたら SL。Mid での勝敗判定はしない。

## 使い方

```bash
cd fx-autopilot && pip install -r requirements.txt
python -m unittest discover -s tests      # 合成データ・ネット不要
python -m fxap.cli ingest                 # 市場データ（外部ネット必要。GitHub Actions で実行）
python -m fxap.cli research               # Stage1 → LOCK → Stage2 → Tournament → research/results/LATEST/SUMMARY.md
python -m fxap.cli paper                  # PAPER Forward（LOCK 後の新しい足だけ）→ dashboard → 台帳検証
python -m fxap.cli kill-switch status --spec trend_ema_adx_v1
python -m fxap.cli kill-switch release --spec ... --by <本人> --reason ...   # 解除は本人・対話端末のみ
```

GitHub Actions（`.github/workflows/fx-autopilot.yml`）: push 時 = テスト + 研究 + PAPER。
**schedule（平日 3 時間ごと PAPER・金曜夜 研究）は main にマージされてから有効**になります。生データは commit しません（Actions cache）。

## 本人にしかできない作業

Broker 口座開設・本人確認・2FA・API 規約同意・API キー発行（→ GitHub Secrets）・入金・**LIVE 開始の承認**・FX→IBKR の送金。
