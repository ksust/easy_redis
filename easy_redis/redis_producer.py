import json

from .redis_config import EasyRedisConfig
from .redis_conn import EasyRedis
from .redis_log import EasyRedisLog


class EasyRedisProducer:
    __config_dic = {}
    logger = EasyRedisLog.logger()

    def __init__(self, config_or_yml_path):
        """
        init, require config
        :param config_or_yml_path: yml path or EasyRedisConfig
        """
        if isinstance(config_or_yml_path, EasyRedisConfig):
            self.__config_dic = config_or_yml_path.__dict__
        elif isinstance(config_or_yml_path, str):
            self.__config_dic = EasyRedisConfig(config_or_yml_path).__dict__
        else:
            raise TypeError('config_or_yml_path: need str or EasyRedisConfig')
        self.redis_conn = EasyRedis(config_or_yml_path).redis_conn
        self.topic = self.__config_dic['topic_produce']
        self.logger.info('producer started[topic: %s]' % self.topic)

    def produce_msg(self, msg):
        """
        produce msg with default topic
        :param msg:json or dic
        :return:
        """
        self.produce_msg_topic(self.topic, msg)

    def produce_msg_topic(self, topic: str, msg):
        """
        produce msg with topic
        :param topic:
        :param msg:json or dic
        :return:
        """
        self.redis_conn.publish(topic, json.dumps(msg))
