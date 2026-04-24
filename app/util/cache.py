import time
from typing import Any, Optional


class SimpleCache:
    def __init__(self, ttl_seconds: int = 600):
        self.ttl = ttl_seconds
        self._cache = {}

    def get(self, key: str) -> Optional[Any]:
        entry = self._cache.get(key)
        if not entry:
            return None
        value, expires = entry
        if expires < time.time():
            del self._cache[key]
            return None
        return value

    def set(self, key: str, value: Any):
        expires = time.time() + self.ttl
        self._cache[key] = (value, expires)

    def clear(self):
        self._cache.clear()


cache = SimpleCache(ttl_seconds=600)
