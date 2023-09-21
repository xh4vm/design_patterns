import pytest

from patterns.abstract_factory.factory.sqlite_redis import SQLiteRedisFactory
from patterns.abstract_factory.factory.sqlite_cassandra import SqliteCassandraFactory
from patterns.abstract_factory.factory.pg_redis import PGRedisFactory
from patterns.abstract_factory.factory.pg_cassandra import PGCassandraFactory


pytestmark = pytest.mark.asyncio


async def test_pg_redis_factory_create_success():
    factory = PGRedisFactory()

    db = await factory.create_db_storage()

    assert await db.get() == "Get data from postgresql"
    assert await db.one() == "Get one instance data from postgresql"
    assert await db.insert() == "Insert data into postgresql"

    cache = await factory.create_cache_storage()

    assert await cache.get(key="test") == "Get data from Redis cache storage"
    assert (
        await cache.set(key="key", value="value") == "Set data into Redis cache storage"
    )


async def test_pg_cassandra_factory_create_success():
    factory = PGCassandraFactory()

    db = await factory.create_db_storage()

    assert await db.get() == "Get data from postgresql"
    assert await db.one() == "Get one instance data from postgresql"
    assert await db.insert() == "Insert data into postgresql"

    cache = await factory.create_cache_storage()

    assert await cache.get(key="test") == "Get data from Cassandra cache storage"
    assert (
        await cache.set(key="key", value="value")
        == "Set data into Cassandra cache storage"
    )


async def test_sqlite_redis_factory_create_success():
    factory = SQLiteRedisFactory()

    db = await factory.create_db_storage()

    assert await db.get() == "Get data from sqlite"
    assert await db.one() == "Get one instance data from sqlite"
    assert await db.insert() == "Insert data into sqlite"

    cache = await factory.create_cache_storage()

    assert await cache.get(key="test") == "Get data from Redis cache storage"
    assert (
        await cache.set(key="key", value="value") == "Set data into Redis cache storage"
    )


async def test_sqlite_cassandra_factory_create_success():
    factory = SqliteCassandraFactory()

    db = await factory.create_db_storage()

    assert await db.get() == "Get data from sqlite"
    assert await db.one() == "Get one instance data from sqlite"
    assert await db.insert() == "Insert data into sqlite"

    cache = await factory.create_cache_storage()

    assert await cache.get(key="test") == "Get data from Cassandra cache storage"
    assert (
        await cache.set(key="key", value="value")
        == "Set data into Cassandra cache storage"
    )
