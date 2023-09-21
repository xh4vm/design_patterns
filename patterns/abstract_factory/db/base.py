from abc import ABC, abstractmethod
from typing import Any
from pydantic._internal._model_construction import ModelMetaclass


class DBStorage(ABC):
    @abstractmethod
    async def one(self, *args, **kwargs) -> ModelMetaclass:
        """Метод получения одного экземпляра данных"""

    @abstractmethod
    async def get(self, *args, **kwargs) -> list[ModelMetaclass]:
        """Метод получения данных по условию"""

    @abstractmethod
    async def insert(self, *args, **kwargs) -> list[Any]:
        """Метод установки данных в хранилище"""

    def __init__(self, conn: type) -> None:
        self.conn = conn
