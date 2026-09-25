"""Profit Sweep（FX 利益を IBKR 長期運用へ移す額の計算）。**計算のみ。送金・出金は実行しない。**

Base FX Capital → FX Trading → 確定利益 → Tax Reserve → Margin / Emergency Reserve → Excess Profit → IBKR 移動候補

- 対象は**確定損益のみ**（含み益は対象外）。含み損がある場合はその分を差し引く（保守的）
- 税: 年初来の確定損益（スワップ含む）× 20.315%（先物取引に係る雑所得等・申告分離課税）。損失年は 0。
  過去 3 年の損失繰越は carryforward_loss として入力（自動では推定しない）
- 口座の DD が sweep_only_if_drawdown_below 以上のときは移動候補 0（まず回復を優先）
- 自動送金 API は国内 FX 業者で確認できていない（docs/BROKER_COMPARISON.md）。本人が手動で出金 → IBKR 入金する
"""
from __future__ import annotations

from .common import settings


def compute(equity: float, realized_ytd: float, unrealized: float, hwm: float,
            already_swept_ytd: float = 0.0, tax_paid_ytd: float = 0.0, carryforward_loss: float = 0.0,
            cfg: dict | None = None) -> dict:
    c = (cfg or settings())["sweep"]
    base = float(c["base_capital"])
    taxable = max(0.0, realized_ytd - carryforward_loss)
    tax_reserve = max(0.0, taxable * c["tax_rate"] - tax_paid_ytd)
    margin_reserve = base * c["margin_reserve_ratio"]
    emergency = float(c["emergency_reserve"])
    keep_in_fx = base + margin_reserve + emergency + tax_reserve
    dd = 1 - equity / hwm if hwm > 0 else 0.0
    # 含み損は確定益から差し引く（含み益は加えない）
    cash_like = equity - max(0.0, unrealized)
    excess = cash_like - keep_in_fx
    blocked = []
    if dd >= c["sweep_only_if_drawdown_below"]:
        blocked.append(f"drawdown {dd:.1%} >= {c['sweep_only_if_drawdown_below']:.0%}")
    if realized_ytd <= 0:
        blocked.append("年初来の確定損益がマイナスまたはゼロ")
    candidate = max(0.0, excess) if not blocked else 0.0
    if candidate < c["min_sweep_amount"]:
        if candidate > 0:
            blocked.append(f"移動候補額が最小額 {c['min_sweep_amount']:,} 円未満")
        candidate = 0.0
    return {
        "equity": round(equity, 0), "realized_pnl_ytd_pre_tax": round(realized_ytd, 0),
        "unrealized_pnl": round(unrealized, 0), "drawdown": round(dd, 4),
        "tax_reserve": round(tax_reserve, 0), "margin_reserve": round(margin_reserve, 0),
        "emergency_reserve": round(emergency, 0), "base_capital": round(base, 0),
        "keep_in_fx_account": round(keep_in_fx, 0), "movable_profit": round(max(0.0, excess), 0),
        "ibkr_transfer_candidate": round(candidate, 0), "already_swept_ytd": round(already_swept_ytd, 0),
        "blocked_reasons": blocked,
        "execution": "NOT EXECUTED — 送金は本人のみ（自動送金 API 未確認・LIVE 未承認）",
    }
