"""戦略の共通インターフェースと登録簿。

各戦略は `generate(df, pair) -> DataFrame[SIG_COLS]` を返す。
  entry: +1 買い / -1 売り / 0（足 i の終値で判断、足 i+1 始値で約定）
  exit_long / exit_short: 決済シグナル
  sl_dist: SL 距離（価格、必須）/ tp_dist: TP 距離（NaN=なし）/ trail_dist: トレーリング距離 / max_bars: 時間切れ
シグナルは mid 価格の指標で作るが、損益は必ず bid/ask で計算される（backtest.py）。
パラメータの候補（grid）は評価前に固定する。grid を結果を見て変えることは禁止（新バージョンとして追加）。
"""
from __future__ import annotations

import itertools

import numpy as np
import pandas as pd

from .. import features as F

REGISTRY: dict = {}


def register(cls):
    REGISTRY[cls.name] = cls
    return cls


class Strategy:
    name = "base"
    family = ""
    version = "v1"
    grid: dict = {}
    needs_all_pairs = False

    def __init__(self, **params):
        self.params = {**self.defaults(), **params}

    @classmethod
    def defaults(cls) -> dict:
        return {k: v[0] for k, v in cls.grid.items()}

    @classmethod
    def param_grid(cls) -> list[dict]:
        keys = list(cls.grid)
        return [dict(zip(keys, vals)) for vals in itertools.product(*[cls.grid[k] for k in keys])]

    @property
    def id(self) -> str:
        ps = "_".join(f"{k}{v}" for k, v in sorted(self.params.items()))
        return f"{self.name}_{self.version}[{ps}]"

    def generate(self, df: pd.DataFrame, pair: str) -> pd.DataFrame:
        raise NotImplementedError

    @staticmethod
    def empty(index) -> pd.DataFrame:
        return pd.DataFrame({"entry": 0, "exit_long": False, "exit_short": False, "sl_dist": np.nan,
                             "tp_dist": np.nan, "trail_dist": np.nan, "max_bars": np.nan}, index=index)


def cross_up(a: pd.Series, b) -> pd.Series:
    return (a > b) & (a.shift(1) <= (b.shift(1) if isinstance(b, pd.Series) else b))


def cross_dn(a: pd.Series, b) -> pd.Series:
    return (a < b) & (a.shift(1) >= (b.shift(1) if isinstance(b, pd.Series) else b))


@register
class RandomBaseline(Strategy):
    """比較用: ランダムな方向に一定確率で入る（SL/TP は ATR 基準）。候補ではなくベンチマーク。"""
    name = "random"
    family = "baseline"
    grid = {"p": [0.01], "seed": [0]}

    def generate(self, df, pair):
        m = F.mid(df)
        a = F.atr(m, 14)
        rng = np.random.default_rng(int(self.params["seed"]) + sum(map(ord, pair)))
        out = self.empty(df.index)
        u = rng.random(len(df))
        side = np.where(rng.random(len(df)) < 0.5, 1, -1)
        out["entry"] = np.where(u < self.params["p"], side, 0)
        out["sl_dist"] = 2 * a
        out["tp_dist"] = 2 * a
        out["max_bars"] = 48
        out.loc[a.isna(), "entry"] = 0
        return out
