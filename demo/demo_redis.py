from easy_redis.redis_conn import EasyRedis


def demo_redis():
    redis_conn = EasyRedis('../conf/conf.yml').redis_conn
    redis_conn.set('demo', 'value')
    print(redis_conn.keys('*'))


if __name__ == "__main__":
    demo_redis()
