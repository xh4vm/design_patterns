from aiosqlite import Connection as SQLiteConnectio
from cassandra.cluster import Session as CassandraConnection

from .base import AbstractFactory
from ..cache.cassandra import CassandraCacheStorage, CacheStorage
from ..db.sqlite import SQLiteDBStorage, DBStorage


class SqliteCassandraFactory(AbstractFactory):
    async def create_cache_storage(
        self, conn: CassandraConnection | None = None
    ) -> CacheStorage:
        conn = conn or None
        return CassandraCacheStorage(conn=conn)

    async def create_db_storage(self, conn: SQLiteConnectio | None = None) -> DBStorage:
        conn = conn or None
        return SQLiteDBStorage(conn=conn)
