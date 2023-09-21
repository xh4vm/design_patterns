from aiosqlite import Connection

from .base import DBFactory
from ...db.sqlite import DBStorage, SQLiteDBStorage


class SQLiteDBFactory(DBFactory):
    async def factory_method(self, conn: Connection | None = None) -> DBStorage:
        conn = conn or None
        return SQLiteDBStorage(conn=conn)
