import time

import RedisClient

if __name__ == '__main__':
    redisClient = RedisClient.RedisClient("39.107.143.174")
    redisClient.set("key", "value", 1)
    time.sleep(0.5)
    print(redisClient.get("key"))