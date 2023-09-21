from aiosqlite import Connection as SQLiteConnectio
from redis.asyncio import Connection as RedisConnection

from .base import AbstractFactory
from ..cache.redis import RedisCacheStorage, CacheStorage
from ..db.sqlite import SQLiteDBStorage, DBStorage


class SQLiteRedisFactory(AbstractFactory):
    async def create_cache_storage(
        self, conn: RedisConnection | None = None
    ) -> CacheStorage:
        conn = conn or None
        return RedisCacheStorage(conn=conn)

    async def create_db_storage(self, conn: SQLiteConnectio | None = None) -> DBStorage:
        conn = conn or None
        return SQLiteDBStorage(conn=conn)
