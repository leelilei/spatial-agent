"""API 结果缓存模块。"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

try:
    from diskcache import Cache
except ImportError:  # pragma: no cover - dependency exists in project env
    Cache = None


class ResponseCache:
    """LLM 调用结果的轻量磁盘缓存。"""

    def __init__(self, cache_dir: str | Path) -> None:
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self._cache = Cache(str(self.cache_dir)) if Cache is not None else None

    def make_key(self, payload: dict[str, Any]) -> str:
        serialized = json.dumps(payload, ensure_ascii=False, sort_keys=True)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()

    def get(self, key: str) -> dict[str, Any] | None:
        if self._cache is None:
            return None
        return self._cache.get(key)

    def set(self, key: str, value: dict[str, Any]) -> None:
        if self._cache is None:
            return
        self._cache.set(key, value)
