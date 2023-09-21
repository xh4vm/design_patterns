from pydantic._internal._model_construction import ModelMetaclass
from loguru import logger
from typing import Any

from .base import DBStorage


class SQLiteDBStorage(DBStorage):
    async def one(self, *args, **kwargs) -> ModelMetaclass:
        message = "Get one instance data from sqlite"
        logger.info(message)

        return message

    async def get(self, *args, **kwargs) -> list[ModelMetaclass]:
        message = "Get data from sqlite"
        logger.info(message)

        return message

    async def insert(self, *args, **kwargs) -> list[Any]:
        message = "Insert data into sqlite"
        logger.info(message)

        return message
