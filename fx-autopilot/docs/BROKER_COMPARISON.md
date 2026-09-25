# FX Broker / API 比較（日本居住者の個人・2026-09 調査）

> 調査方法: Web 検索結果（公式サイト・公式ドキュメントのスニペット中心）。この環境からは一部の公式ページ本文を取得できなかったため、
> **数値は口座開設前に必ず公式ページで再確認**すること。確認できなかった項目は **未確認** と明記。口座開設・登録・契約・入金は一切行っていない。

## 前提（規制・税）

- 個人の FX 証拠金は想定元本の 4% 以上 → **最大 25 倍**（金融先物取引業協会 https://www.ffaj.or.jp/regulation/customers/ ）。本システムの PAPER 既定は最大 5 倍
- 店頭 FX の利益は「先物取引に係る雑所得等」**申告分離課税 20.315%**、損失は **3 年繰越可**（国税庁 No.1521 / 1523）。給与とは損益通算不可
  → `fxap/sweep.py` は年初来の確定損益（スワップ含む）× 20.315% を税金として確保する

## 比較表

| 項目 | GMOコイン 外国為替FX | OANDA証券 (v20) | IBKR 証券 (IBSJ, Forex CFD) | サクソバンク証券 (OpenAPI) | 楽天 MT4 |
|---|---|---|---|---|---|
| 公式 API | REST + WebSocket（https://api.coin.z.com/fxdocs/ ） | REST + HTTP ストリーム | TWS API / Client Portal Web API | REST + ストリーミング / FIX | MQL4（EA）のみ |
| DEMO × API | **なし**（本番少額で検証） | fxTrade Practice（ただし本番口座で API 条件を満たす必要） | ペーパー口座（IBSJ での条件は未確認） | **シミュレーション環境あり** | MT4 デモ |
| 注文 | 成行/指値/逆指値・OCO/IFD/IFDOCO（トレーリングは未確認） | 成行/指値/逆指値/MIT + SL/TP/トレーリング | 最多（トレーリング・ブラケット・OCA） | 豊富（未確認） | EA で実装 |
| 変更・決済・建玉・約定・残高 | 可（細部未確認） | 可 | 可 | 可 | 可 |
| USD/JPY スプレッド | 0.2 銭 原則固定 | 変動（NY プロは広め・未確認） | 変動（IDEALPRO 連動） | 未確認 | 0.5 銭 |
| 手数料 | API 手数料 約定額 × 0.002%（=0.2bp） | なし | 0.2bp（最低 USD2 前後・要確認） | 未確認 | なし |
| 最小単位 | 100 通貨（API） | 1 通貨 | 未確認 | 未確認 | 1,000 通貨 |
| API 利用条件 | 口座のみ | 残高 25 万円 + Gold 会員 + NY プロコース | 口座 | 口座 | 口座 |
| 24h 自動運用 | API キーで容易 | トークンで容易 | Gateway 日次再起動 + 週 1 回 2FA | OAuth リフレッシュ | Windows/VPS 必須 |
| 出金 API | 確認できず | なし | Account Management API にあるが個人 IBSJ で使えるか未確認 | 未確認 | なし |

外為どっとコム・SBI FXトレード・みんなのFX・GMOクリック証券（FXネオ）は **個人向け公開取引 API が確認できず** 対象外。
MetaTrader5 の Python パッケージは Windows 専用。

## 推奨

**(a) いま（PAPER / DEMO 開発）**: 内部シミュレータ `PaperBroker`（Dukascopy bid/ask で約定再現）で運用中。外部 DEMO 接続の第一候補は
**Saxo OpenAPI シミュレーション**（口座なしで開発者トークン取得可・要本人登録）、次点 **IBKR ペーパー**（将来の利益移動先と同じ）。

**(b) 将来の LIVE 候補**（本人の明示承認後のみ）: **GMOコイン 外国為替FX**（利用条件が緩い・0.2 銭・100 通貨・OCO/IFD を API で・API キーで 24h 運用）
→ 次点 **OANDA 証券**（API 成熟・1 通貨単位。残高 25 万円と Gold 維持条件がリスク）。
IBKR Forex CFD は最低手数料のため小ロットでは割高だが、利益の移動先（IBKR 長期運用）と同じ口座系で完結できる。

## Profit Sweep の結論

**国内 FX 業者で公式の自動出金 API は確認できなかった。** FX → IBKR の資金移動は当面「本人が手動で出金 → IBKR に入金」。
システムは移動候補額の**計算のみ**を行い、資金移動は実行しない（`fxap/sweep.py`）。

## 本人にしかできない作業（未実施）

口座開設・本人確認・2FA・API 利用規約への同意・（GMOコインは）少額入金・API キー発行・Saxo 開発者登録。
キーは GitHub Secrets に本人が登録する（本 repo は public のため、キーをファイルに書かないこと）。

主要出典: ffaj.or.jp / nta.go.jp No.1521・1523 / api.coin.z.com/fxdocs / coin.z.com/jp/news/2025/04/14320 /
help.oanda.jp/oanda/faq/show/720・226 / developer.oanda.com/rest-live-v20/best-practices /
interactivebrokers.co.jp/en/trading/ibkr-forex-cfds.php / interactivebrokers.com/docs (reauthentication, external-cash-transfers) /
developer.saxo/openapi/learn/environments / rakuten-sec.co.jp/web/fx/mt4/commission.html
