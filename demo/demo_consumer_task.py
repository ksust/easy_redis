import json

from easy_redis.redis_consumer import EasyRedisConsumer
from easy_redis.redis_producer import EasyRedisProducer

redis_producer = EasyRedisProducer('../conf/conf.yml')


def consumer_task(record):
    """
    consumer callback
    :param record: object
    :return:
    """
    print('consumer_task', (
        'received type: {},topic: {}, msg: {}'.format(record['type'], record['channel'], record['data'])))
    if record['type'] == 'message':
        print('data', json.loads(record['data']))
    if record['channel'] == 'topic1':
        redis_producer.produce_msg({'type': 'task result'})


def start_consumer():
    redis_consumer = EasyRedisConsumer('../conf/conf.yml')
    print('consumer task started')
    redis_consumer.subscribe(fn=consumer_task)


if __name__ == "__main__":
    start_consumer()
