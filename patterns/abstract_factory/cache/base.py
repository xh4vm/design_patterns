from abc import ABC, abstractmethod


class CacheStorage(ABC):
    @abstractmethod
    async def get(self, key: str, default: type | None = None):
        """Метод получения данные из кеша"""

    @abstractmethod
    async def set(self, key: str, value: type):
        """Метод установки данных в кеш"""

    def __init__(self, conn: type) -> None:
        self.conn = conn
