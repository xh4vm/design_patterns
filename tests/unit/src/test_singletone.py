import pytest

from patterns.singleton import Singleton


pytestmark = pytest.mark.asyncio


async def test_adapter_create_success():
    s1 = Singleton()
    s2 = Singleton()

    assert s1 == s2
