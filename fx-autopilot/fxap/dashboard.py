"""スマホ向けダッシュボード（public/index.html）と GitHub で読める DASHBOARD.md を生成する。"""
from __future__ import annotations

import html
import json
import math

import pandas as pd

from . import metrics, sweep
from .common import OUT, PAPER_DIR, PUBLIC, RESULTS, settings, utcnow
from .paper_engine import load_paper
from .research import load_locked


def _f(v, fmt="{:,.0f}", none="—"):
    if v is None or (isinstance(v, float) and not math.isfinite(v)):
        return none
    try:
        return fmt.format(v)
    except (ValueError, TypeError):
        return str(v)


def _window_pnl(eq: pd.Series, days: int | None):
    if eq.empty:
        return None
    if days is None:
        return float(eq.iloc[-1] - eq.iloc[0])
    t0 = eq.index[-1] - pd.Timedelta(days=days)
    base = eq[eq.index <= t0]
    ref = float(base.iloc[-1]) if len(base) else float(eq.iloc[0])
    return float(eq.iloc[-1] - ref)


def paper_summary(spec: dict, initial: float) -> dict:
    p = load_paper(spec["spec_id"])
    eq, tr, st = p["equity"], p["trades"], p["state"]
    if eq.empty:
        return {"spec_id": spec["spec_id"], "started": False, "equity": initial}
    full = pd.concat([pd.Series([initial], index=[eq.index[0] - pd.Timedelta(hours=1)]), eq])
    m = metrics.compute(full, tr if len(tr) else pd.DataFrame(), None, initial) if len(full) > 2 else {}
    bs = st.get("broker_state", {})
    rs = st.get("risk_state", {})
    positions = bs.get("positions", {})
    gross = sum(v.get("notional_jpy", 0) for v in positions.values())
    e = float(eq.iloc[-1])
    today = _window_pnl(full, 1)
    dls = settings()["risk"]["daily_loss_limit"]
    day_start = rs.get("day_start_equity") or e
    realized = float(tr["pnl_jpy"].sum()) if len(tr) else 0.0
    return {
        "spec_id": spec["spec_id"], "started": True, "last_bar": str(eq.index[-1]), "equity": e,
        "cash": bs.get("cash"), "available": e - gross / 25.0, "open_positions": len(positions),
        "positions": positions, "exposure_jpy": gross, "leverage": gross / e if e > 0 else None,
        "drawdown": 1 - e / max(rs.get("hwm", e), e), "pnl_today": today, "pnl_7d": _window_pnl(full, 7),
        "pnl_30d": _window_pnl(full, 30), "pnl_total": e - initial, "realized": realized,
        "daily_loss_used": max(0.0, -(e / day_start - 1)) / dls if day_start else 0.0,
        "trades": int(len(tr)), "win_rate": m.get("win_rate"), "profit_factor": m.get("profit_factor"),
        "sharpe": m.get("sharpe") if len(full) > 30 * 24 else None, "halted": st.get("halted"),
        "kill_reason": rs.get("kill_reason"), "pairs": list(spec.get("trade_pairs") or spec["pairs"]),
    }


def build() -> dict:
    cfg = settings()
    initial = float(cfg["account"]["initial_equity"])
    specs = load_locked()
    tour = json.loads((PAPER_DIR / "tournament.json").read_text()) if (PAPER_DIR / "tournament.json").exists() else {}
    status = {r["spec_id"]: r for r in tour.get("specs", [])}
    papers = [paper_summary(s, initial) for s in specs]
    s2p = RESULTS / "LATEST" / "stage2.csv"
    s2 = pd.read_csv(s2p) if s2p.exists() else pd.DataFrame()
    champ = tour.get("champion")
    ch = next((p for p in papers if p["spec_id"] == champ), None)
    sw = None
    if ch and ch.get("started"):
        unreal = ch["equity"] - (ch["cash"] or ch["equity"])
        sw = sweep.compute(ch["equity"], ch["realized"], unreal, max(ch["equity"], initial))
    data = {"generated_at": utcnow().isoformat(), "mode": cfg["mode"], "live": cfg["live_trading_enabled"],
            "champion": champ, "champion_note": tour.get("champion_note"), "papers": papers,
            "status": status, "sweep": sw, "live_candidates": tour.get("live_candidates", [])}
    PUBLIC.mkdir(parents=True, exist_ok=True)
    (PUBLIC / "index.html").write_text(render_html(data, s2), encoding="utf-8")
    (OUT / "DASHBOARD.md").write_text(render_md(data, s2), encoding="utf-8")
    (PUBLIC / "status.json").write_text(json.dumps(data, indent=2, ensure_ascii=False, default=str))
    return data


def _s2(s2, sid, period, col, variant="portfolio"):
    if s2 is None or not len(s2):
        return None
    r = s2[(s2.spec_id == sid) & (s2.period == period) & (s2.variant == variant)]
    if not len(r):
        return None
    v = r.iloc[0][col]
    return None if pd.isna(v) else v


def render_md(d: dict, s2: pd.DataFrame) -> str:
    L = ["# FX AUTOPILOT ダッシュボード（PAPER ONLY）", "",
         f"更新: {d['generated_at'][:16]} UTC ／ モード: **{d['mode']}** ／ LIVE: **無効**（本人の明示承認まで開始しない）", "",
         f"**Champion:** {d['champion'] or 'CASH（取引しない）'}" + (f" — {d['champion_note']}" if d.get("champion_note") else ""),
         f"**LIVE 候補:** {', '.join(d['live_candidates']) or 'なし'}", "",
         "## PAPER 口座（LOCK 後の Forward。各 ¥1,000,000 の仮想口座）", "",
         "| 戦略 | 状態 | 残高 | 今日 | 7D | 30D | 累計 | DD | 建玉 | Lev | 取引 | 勝率 | PF |",
         "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for p in d["papers"]:
        st = d["status"].get(p["spec_id"], {}).get("status", "—")
        if not p.get("started"):
            L.append(f"| {p['spec_id']} | {st} | 未開始 | | | | | | | | | | |")
            continue
        L.append(f"| {p['spec_id']} | {st}{' / KILL' if p['halted'] else ''} | {_f(p['equity'])} | {_f(p['pnl_today'], '{:+,.0f}')} | "
                 f"{_f(p['pnl_7d'], '{:+,.0f}')} | {_f(p['pnl_30d'], '{:+,.0f}')} | {_f(p['pnl_total'], '{:+,.0f}')} | "
                 f"{_f(p['drawdown'], '{:.1%}')} | {p['open_positions']} | {_f(p['leverage'], '{:.2f}')} | {p['trades']} | "
                 f"{_f(p['win_rate'], '{:.0%}')} | {_f(p['profit_factor'], '{:.2f}')} |")
    L += ["", "## バックテスト（LOCK 後に 1 回だけ評価。コスト込み・retail_jp）", "",
          "| 戦略 | 状態 | TEST 取引 | TEST 収益 | TEST PF | TEST Sharpe | TEST MaxDD | FWD 収益 | FWD PF | FWD Sharpe | 2倍コスト PF |",
          "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for p in d["papers"]:
        sid = p["spec_id"]
        st = d["status"].get(sid, {}).get("status", "—")
        L.append(f"| {sid} | {st} | {_f(_s2(s2, sid, 'TEST', 'n_trades'))} | {_f(_s2(s2, sid, 'TEST', 'net_return'), '{:+.1%}')} | "
                 f"{_f(_s2(s2, sid, 'TEST', 'profit_factor'), '{:.2f}')} | {_f(_s2(s2, sid, 'TEST', 'sharpe'), '{:.2f}')} | "
                 f"{_f(_s2(s2, sid, 'TEST', 'max_drawdown'), '{:.1%}')} | {_f(_s2(s2, sid, 'FORWARD', 'net_return'), '{:+.1%}')} | "
                 f"{_f(_s2(s2, sid, 'FORWARD', 'profit_factor'), '{:.2f}')} | {_f(_s2(s2, sid, 'FORWARD', 'sharpe'), '{:.2f}')} | "
                 f"{_f(_s2(s2, sid, 'TEST', 'profit_factor', 'portfolio_stress_2x'), '{:.2f}')} |")
    if d.get("sweep"):
        sw = d["sweep"]
        L += ["", "## Profit Sweep（計算のみ・送金しない）", "",
              f"確定損益(税引前) {_f(sw['realized_pnl_ytd_pre_tax'])} ／ 税金積立 {_f(sw['tax_reserve'])} ／ "
              f"FX に残す額 {_f(sw['keep_in_fx_account'])} ／ **IBKR 移動候補 {_f(sw['ibkr_transfer_candidate'])} 円**",
              f"停止理由: {', '.join(sw['blocked_reasons']) or 'なし'}"]
    L += ["", "詳細: `research/results/LATEST/SUMMARY.md` ／ 台帳: `paper_forward/<spec>/ledger.jsonl`（ハッシュチェーン）", ""]
    return "\n".join(L)


CSS = """
:root{--bg:#f7f7f5;--card:#fff;--ink:#1d1d1b;--mut:#6b6b66;--line:#e4e4df;--pos:#1a7f4b;--neg:#b42318;--acc:#2f5bd3;--warn:#9a6700}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#121212;--card:#1c1c1c;--ink:#ecece8;--mut:#9d9d97;--line:#2e2e2b;--pos:#4ac383;--neg:#f07167;--acc:#8fb0ff;--warn:#e3b341}}
:root[data-theme=dark]{--bg:#121212;--card:#1c1c1c;--ink:#ecece8;--mut:#9d9d97;--line:#2e2e2b;--pos:#4ac383;--neg:#f07167;--acc:#8fb0ff;--warn:#e3b341}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.5 -apple-system,system-ui,"Hiragino Sans","Noto Sans JP",sans-serif}
main{max-width:960px;margin:0 auto;padding:16px}h1{font-size:18px;margin:4px 0}h2{font-size:15px;margin:22px 0 8px}
.banner{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--warn);padding:10px 12px;border-radius:8px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:8px}
.k{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px}.k b{display:block;font-size:17px;font-variant-numeric:tabular-nums}
.k span{color:var(--mut);font-size:12px}.pos{color:var(--pos)}.neg{color:var(--neg)}.mut{color:var(--mut)}
.tw{overflow-x:auto;background:var(--card);border:1px solid var(--line);border-radius:8px}
table{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums}th,td{padding:6px 8px;border-bottom:1px solid var(--line);text-align:right;white-space:nowrap}
th:first-child,td:first-child{text-align:left}th{color:var(--mut);font-weight:600;font-size:12px}.tag{font-size:11px;padding:1px 6px;border-radius:10px;border:1px solid var(--line)}
"""


def _cls(v):
    return "" if v is None else ("pos" if v > 0 else "neg" if v < 0 else "")


def render_html(d: dict, s2: pd.DataFrame) -> str:
    e = html.escape
    champ = next((p for p in d["papers"] if p["spec_id"] == d["champion"]), None)
    head = f"""<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>FX Autopilot Paper</title><style>{CSS}</style></head><body><main>
<h1>FX AUTOPILOT <span class="tag">PAPER ONLY</span></h1>
<div class="banner">LIVE 取引は無効です（本人の明示承認まで開始しません）。表示はすべて仮想口座・バックテストで、利益を保証しません。<br>
<span class="mut">更新 {e(d['generated_at'][:16])} UTC</span></div>"""
    parts = [head, f"<h2>Champion: {e(d['champion'] or 'CASH（取引しない）')}</h2>"]
    if d.get("champion_note"):
        parts.append(f"<p class='mut'>{e(d['champion_note'])}</p>")
    src = champ or next((p for p in d["papers"] if p.get("started")), None)
    if src and src.get("started"):
        cards = [("Today PnL", src["pnl_today"], "{:+,.0f}"), ("7D", src["pnl_7d"], "{:+,.0f}"), ("30D", src["pnl_30d"], "{:+,.0f}"),
                 ("Total", src["pnl_total"], "{:+,.0f}"), ("Account Equity", src["equity"], "{:,.0f}"),
                 ("Available Cash", src["available"], "{:,.0f}"), ("Open Positions", src["open_positions"], "{:d}"),
                 ("Exposure", src["exposure_jpy"], "{:,.0f}"), ("Current Leverage", src["leverage"], "{:.2f}x"),
                 ("Drawdown", -src["drawdown"], "{:.1%}"), ("Daily Loss Limit 使用率", src["daily_loss_used"], "{:.0%}"),
                 ("Trades", src["trades"], "{:d}"), ("Win Rate", src["win_rate"], "{:.0%}"),
                 ("Profit Factor", src["profit_factor"], "{:.2f}"), ("Sharpe", src["sharpe"], "{:.2f}")]
        parts.append(f"<p class='mut'>表示中の口座: {e(src['spec_id'])}（{e(', '.join(src['pairs']))}）"
                     f"{' — Champion 不在のため先頭の観測口座' if not champ else ''}</p><div class='grid'>")
        for k, v, fmt in cards:
            c = _cls(v) if k in ("Today PnL", "7D", "30D", "Total") else ""
            parts.append(f"<div class='k'><span>{e(k)}</span><b class='{c}'>{e(_f(v, fmt))}</b></div>")
        parts.append("</div>")
    parts.append("<h2>Champion / Challengers（LOCK 後 PAPER Forward）</h2><div class='tw'><table><tr><th>Strategy</th><th>状態</th>"
                 "<th>Pairs</th><th>Equity</th><th>Total</th><th>DD</th><th>Trades</th><th>Win</th><th>PF</th><th>Forward Status</th></tr>")
    for p in d["papers"]:
        st = d["status"].get(p["spec_id"], {})
        fwd = "未開始" if not p.get("started") else ("KILL" if p.get("halted") else f"{p['trades']} trades / {', '.join(st.get('paper_gate_fail', [])) or '合格'}")
        name = ("★ " if p["spec_id"] == d["champion"] else "") + p["spec_id"]
        if not p.get("started"):
            parts.append(f"<tr><td>{e(name)}</td><td>{e(st.get('status', '—'))}</td><td colspan=8 class='mut'>{e(fwd)}</td></tr>")
            continue
        parts.append(f"<tr><td>{e(name)}</td><td>{e(st.get('status', '—'))}</td><td>{e(' '.join(p['pairs']))}</td><td>{_f(p['equity'])}</td>"
                     f"<td class='{_cls(p['pnl_total'])}'>{_f(p['pnl_total'], '{:+,.0f}')}</td><td>{_f(p['drawdown'], '{:.1%}')}</td>"
                     f"<td>{p['trades']}</td><td>{_f(p['win_rate'], '{:.0%}')}</td><td>{_f(p['profit_factor'], '{:.2f}')}</td><td>{e(fwd)}</td></tr>")
    parts.append("</table></div>")
    parts.append("<h2>バックテスト（コスト込み・LOCK 後に 1 回だけ評価）</h2><div class='tw'><table><tr><th>Strategy</th><th>TEST trades</th>"
                 "<th>TEST ret</th><th>PF</th><th>Sharpe</th><th>MaxDD</th><th>FWD ret</th><th>FWD PF</th><th>FWD Sharpe</th><th>2x cost PF</th></tr>")
    for p in d["papers"]:
        sid = p["spec_id"]
        tr = _s2(s2, sid, "TEST", "net_return")
        fr = _s2(s2, sid, "FORWARD", "net_return")
        parts.append(f"<tr><td>{e(sid)}</td><td>{_f(_s2(s2, sid, 'TEST', 'n_trades'))}</td><td class='{_cls(tr)}'>{_f(tr, '{:+.1%}')}</td>"
                     f"<td>{_f(_s2(s2, sid, 'TEST', 'profit_factor'), '{:.2f}')}</td><td>{_f(_s2(s2, sid, 'TEST', 'sharpe'), '{:.2f}')}</td>"
                     f"<td>{_f(_s2(s2, sid, 'TEST', 'max_drawdown'), '{:.1%}')}</td><td class='{_cls(fr)}'>{_f(fr, '{:+.1%}')}</td>"
                     f"<td>{_f(_s2(s2, sid, 'FORWARD', 'profit_factor'), '{:.2f}')}</td><td>{_f(_s2(s2, sid, 'FORWARD', 'sharpe'), '{:.2f}')}</td>"
                     f"<td>{_f(_s2(s2, sid, 'TEST', 'profit_factor', 'portfolio_stress_2x'), '{:.2f}')}</td></tr>")
    parts.append("</table></div>")
    if d.get("sweep"):
        sw = d["sweep"]
        parts.append("<h2>Profit Sweep（計算のみ・送金は実行しない）</h2><div class='grid'>")
        for k, key in (("確定損益(税引前)", "realized_pnl_ytd_pre_tax"), ("税金積立", "tax_reserve"),
                       ("FX に残す額", "keep_in_fx_account"), ("IBKR 移動候補", "ibkr_transfer_candidate")):
            parts.append(f"<div class='k'><span>{e(k)}</span><b>{_f(sw[key])}</b></div>")
        parts.append(f"</div><p class='mut'>{e(', '.join(sw['blocked_reasons']) or '')}</p>")
    parts.append("</main></body></html>")
    return "\n".join(parts)
