from . import base, meanrev, ml, regime, trend, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15  # noqa: F401  （登録のための import）
from .base import REGISTRY, Strategy  # noqa: F401


def get(name: str, **params) -> Strategy:
    return REGISTRY[name](**params)
