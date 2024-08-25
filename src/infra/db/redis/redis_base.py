""" This module defines Redis Base Class
"""

# Natives
import logging

# Third-parties
from redis import Redis

# Locals
from configs import config


class BaseRedis:
    def __init__(self) -> None:
        self._redis = Redis(host=config.REDIS_HOST, port=config.REDIS_PORT)

    def get_redis_client(self) -> Redis:
        return self._redis

    def check_connection(self) -> None:
        try:
            self._redis.ping()
            logging.info("Redis connection success")
        except ConnectionRefusedError as conn_ref_error:
            logging.error(f"Socket connection error: {conn_ref_error}")
            return conn_ref_error
        except ConnectionError as conn_exception:
            logging.error(f"Redis connection error: {conn_exception}")
            return conn_exception
        except Exception as exception:
            logging.error(f"Redis connection error: {exception}")
            return exception


redis_instance = BaseRedis()
redis_instance.check_connection()
RedisClient = redis_instance.get_redis_client()
