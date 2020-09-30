import os

import yaml

from .redis_log import EasyRedisLog


class EasyRedisConfig:
    server = '127.0.0.1'
    port = 6379
    topic_subscribe = ['demo_topic']
    topic_produce = 'demo_topic'
    logger = EasyRedisLog.logger()

    def __init__(self, yml_path):
        """
        yml config file
        :param yml_path:
        """
        if not os.path.exists(yml_path):
            raise FileNotFoundError('yml config not found')
        # parse
        with open(yml_path, encoding='UTF-8') as f:
            data = f.read()
            conf = yaml.load(data, Loader=yaml.FullLoader)
            self.server = conf['redis']['server']
            self.port = conf['redis']['port']
            self.topic_subscribe = conf['redis']['topic_subscribe']
            self.topic_produce = conf['redis']['topic_produce']
            self.logger.info('EasyRedisConfig: yml parse done')
