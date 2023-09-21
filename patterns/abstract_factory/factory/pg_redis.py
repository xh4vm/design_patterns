from asyncpg import Connection as PGConnection
from redis.asyncio import Connection as RedisConnection

from .base import AbstractFactory
from ..cache.redis import RedisCacheStorage, CacheStorage
from ..db.postgres import PostgresDBStorage, DBStorage


class PGRedisFactory(AbstractFactory):
    async def create_cache_storage(
        self, conn: RedisConnection | None = None
    ) -> CacheStorage:
        conn = conn or None
        return RedisCacheStorage(conn=conn)

    async def create_db_storage(self, conn: PGConnection | None = None) -> DBStorage:
        conn = conn or None
        return PostgresDBStorage(conn=conn)
