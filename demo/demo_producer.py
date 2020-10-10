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
