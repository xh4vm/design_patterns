from abc import abstractmethod
from aiosqlite import Connection

from ..base import Factory
from ...db.sqlite import DBStorage


class DBFactory(Factory):
    @abstractmethod
    async def factory_method(self, conn: Connection | None = None) -> DBStorage:
        """Создание хранилища данных"""
