from abc import ABC, abstractmethod

from ..cache.base import CacheStorage
from ..db.base import DBStorage


class AbstractFactory(ABC):
    @abstractmethod
    async def create_cache_storage(self) -> CacheStorage:
        """Метод создания кеш хранилища"""

    @abstractmethod
    async def create_db_storage(self) -> DBStorage:
        """Метод создания базы данных"""
