import redis

class RedisClient:
    def __init__(self, host: str, port: int = 6379, decode_responses: bool = False):
        self.pool = redis.ConnectionPool(host=host, port=port, decode_responses=decode_responses)

    def get(self, key: str) -> str:
        r = redis.Redis(connection_pool=self.pool)
        return r.get(key)

    def set(self, key: str, value: str, time: int = 180) -> bool:
        r = redis.Redis(connection_pool=self.pool)
        return r.set(key, value, ex=time)
