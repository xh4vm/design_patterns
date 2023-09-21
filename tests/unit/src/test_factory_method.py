import pytest

from patterns.factory_method.factory.db.sqlite import SQLiteDBFactory
from patterns.factory_method.factory.db.postgres import PostgresDBFactory


pytestmark = pytest.mark.asyncio


async def test_pg_factory_create_success():
    factory = PostgresDBFactory()

    db = await factory.factory_method()

    assert await db.get() == "Get data from postgresql"
    assert await db.one() == "Get one instance data from postgresql"
    assert await db.insert() == "Insert data into postgresql"


async def test_sqlite_factory_create_success():
    factory = SQLiteDBFactory()

    db = await factory.factory_method()

    assert await db.get() == "Get data from sqlite"
    assert await db.one() == "Get one instance data from sqlite"
    assert await db.insert() == "Insert data into sqlite"
