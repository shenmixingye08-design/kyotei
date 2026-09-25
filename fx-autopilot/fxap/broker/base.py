"""Broker Adapter の共通インターフェース（PAPER / DEMO 専用）。

実装:
  PaperBroker        : 内部シミュレータ（既定）。Dukascopy の bid/ask 足で約定を再現
  OandaPracticeBroker: OANDA v20 fxTrade Practice（デモ）。本番ホストへの接続はコードで拒否。未検証（口座条件あり）
LIVE 用の実装は存在しない（本人の明示承認後に別途実装・検証する）。
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field


class BrokerError(RuntimeError):
    pass


class BrokerDisconnected(BrokerError):
    pass


@dataclass
class OrderRequest:
    client_order_id: str          # 冪等キー（spec・ペア・判断足・方向のハッシュ）。同じ ID は二度送らない
    pair: str
    side: int                     # +1 買い / -1 売り
    units: float
    kind: str = "MARKET"          # MARKET（新規・決済とも成行）
    sl: float | None = None       # SL 距離（価格）。新規は必須
    tp: float | None = None       # TP 距離（価格）
    trail: float | None = None    # トレーリング距離
    max_bars: float | None = None
    reason: str = "entry"         # entry | exit:<reason>
    decided_at: str = ""
    meta: dict = field(default_factory=dict)

    def to_dict(self):
        return asdict(self)


@dataclass
class Fill:
    client_order_id: str
    pair: str
    side: int
    units: float
    price: float
    time: str
    kind: str                     # open | close
    reason: str
    cost_spread_jpy: float = 0.0
    cost_slip_jpy: float = 0.0
    commission_jpy: float = 0.0
    realized_pnl_jpy: float = 0.0
    trade: dict | None = None


class BrokerAdapter:
    name = "base"
    is_paper = True

    def is_connected(self) -> bool: ...
    def get_account(self) -> dict: ...
    def get_positions(self) -> list[dict]: ...
    def get_quote(self, pair: str) -> dict: ...
    def place_order(self, req: OrderRequest) -> dict: ...
    def modify_stop(self, pair: str, new_sl_price: float) -> dict: ...
    def close_position(self, pair: str, reason: str, client_order_id: str) -> dict: ...
    def get_fills(self, since: str | None = None) -> list[Fill]: ...
    def known_client_ids(self) -> set: ...
