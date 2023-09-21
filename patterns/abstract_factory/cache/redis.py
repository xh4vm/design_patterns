from loguru import logger

from .base import CacheStorage


class RedisCacheStorage(CacheStorage):
    async def get(self, key: str, default: type | None = None):
        message = "Get data from Redis cache storage"
        logger.info(message)

        return message

    async def set(self, key: str, value: type):
        message = "Set data into Redis cache storage"
        logger.info(message)

        return message
