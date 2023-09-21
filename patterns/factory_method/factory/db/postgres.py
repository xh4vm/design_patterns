from aiosqlite import Connection

from .base import DBFactory
from ...db.postgres import DBStorage, PostgresDBStorage


class PostgresDBFactory(DBFactory):
    async def factory_method(self, conn: Connection | None = None) -> DBStorage:
        conn = conn or None
        return PostgresDBStorage(conn=conn)
