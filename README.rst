easy_redis
^^^^^^^^^^
Easy to use python redis(for kb first)

Compared with kafka, redis has the following characteristics in publishing and subscribing:

* Produced messages are immediately consumed by consumers.
* Fast speed, small data( < 10KB).
* Allow message loss.
* No need to save sent messages.

Quick Start
-----------
**Installation**: pip install easy_redis

1.config
>>>>>>>>
Edit conf/conf.yml
::

    redis: # redis config
      server: 127.0.0.1 # redis server
      port: 6379
      channel_subscribe: # channel if need, multiple
        - channel_1
        - channel_2
      channel_produce: channel_1_result # producer default channel

2.demo-consumer
>>>>>>>>>>>>>>>>>>
::

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

3.demo-consumer-task
>>>>>>>>>>>>>>>>>>>>>>>>>
::

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
            'received type: {}, channel: {}, msg: {}'.format(record['type'], record['channel'], record['data'])))
        if record['type'] == 'message':
            print('data', json.loads(record['data']))
        if record['channel'] == 'channel_1':
            redis_producer.produce_msg({'type': 'task result'})


    def start_consumer():
        redis_consumer = EasyRedisConsumer('../conf/conf.yml')
        print('consumer task started')
        redis_consumer.subscribe(fn=consumer_task)


    if __name__ == "__main__":
        start_consumer()

4.demo-producer
>>>>>>>>>>>>>>>>>>>>>>>>>
::

    from easy_redis.redis_config import EasyRedisConfig
    from easy_redis.redis_producer import EasyRedisProducer


    def demo_produce_msg():
        redis_producer = EasyRedisProducer('../conf/conf.yml')
        redis_producer.produce_msg({'name': 'ksust'})


    def demo_produce_msg_with_config():
        config = EasyRedisConfig('../conf/conf.yml')
        print('config', config.__dict__)
        redis_producer = EasyRedisProducer(config)
        redis_producer.produce_msg({'name': 'ksust'})
        redis_producer.produce_msg_channel('channel_1', {'name': 'ksust'})


    if __name__ == "__main__":
        demo_produce_msg()
        demo_produce_msg_with_config()

5.demo-redis_conn
>>>>>>>>>>>>>>>>>>>>>>>>>
::

    from easy_redis.redis_conn import EasyRedis
    def demo_redis():
        redis_conn = EasyRedis('../conf/conf.yml').redis_conn
        redis_conn.set('demo', 'value')
        print(redis_conn.keys('*'))


    if __name__ == "__main__":
        demo_redis()