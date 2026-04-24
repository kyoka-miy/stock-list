
import json
import redis
from app.config import settings


class RedisCache:
    def __init__(self):
        self.client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            decode_responses=True
        )
        self.ttl = settings.REDIS_TTL

    def get(self, key: str):
        value = self.client.get(key)
        
        if value is None:
            return None
        if not isinstance(value, str):
            return None
        
        return json.loads(value)

    def set(self, key: str, value):
        self.client.setex(key, self.ttl, json.dumps(value))

    def clear(self):
        self.client.flushdb()


redis_cache = RedisCache()
