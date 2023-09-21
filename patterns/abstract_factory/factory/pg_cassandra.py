from asyncpg import Connection as PGConnection
from cassandra.cluster import Session as CassandraConnection

from .base import AbstractFactory
from ..cache.cassandra import CassandraCacheStorage, CacheStorage
from ..db.postgres import PostgresDBStorage, DBStorage


class PGCassandraFactory(AbstractFactory):
    async def create_cache_storage(
        self, conn: CassandraConnection | None = None
    ) -> CacheStorage:
        conn = conn or None
        return CassandraCacheStorage(conn=conn)

    async def create_db_storage(self, conn: PGConnection | None = None) -> DBStorage:
        conn = conn or None
        return PostgresDBStorage(conn=conn)
