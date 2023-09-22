import pytest

from patterns.adapter.api.adapters.new_api import NewAPIAdapter
from patterns.adapter.api.v2.api import API as NewAPI
from patterns.adapter.api.v1.api import API as OldAPI


pytestmark = pytest.mark.asyncio


async def test_adapter_create_success():
    api = NewAPIAdapter()

    data = api.new_request()
    assert data == "Getting data from old external api"


async def test_adapter_new_api_create_success():
    new_api = NewAPI()

    new_api_data = new_api.new_request()
    assert new_api_data == "Getting data from new external api"


async def test_adapter_old_api_create_success():
    old_api = OldAPI()

    old_api_data = old_api.old_request()
    assert old_api_data == "Getting data from old external api"
