import json

from easy_redis.redis_consumer import EasyRedisConsumer


def start_consumer():
    redis_consumer = EasyRedisConsumer('../conf/conf.yml')
    print('consumer iterator started')
    for record in redis_consumer:
        if record['type'] == 'message':
            print('data', json.loads(record['data']))
        else:
            print('subscribe', record)


if __name__ == "__main__":
    start_consumer()
