import pytest

from patterns.bridge.shape.square import SquareShape
from patterns.bridge.shape.round import RoundShape
from patterns.bridge.color.red import RedColor
from patterns.bridge.color.blue import BlueColor


pytestmark = pytest.mark.asyncio


async def test_bridge_red_square_shape_create():
    color = RedColor()
    square = SquareShape(color=color)

    result = square.draw()

    assert result == "Drawing square shape with Red color"


async def test_bridge_red_round_shape_create():
    color = RedColor()
    round = RoundShape(color=color)

    result = round.draw()

    assert result == "Drawing round shape with Red color"


async def test_bridge_blue_square_shape_create():
    color = BlueColor()
    square = SquareShape(color=color)

    result = square.draw()

    assert result == "Drawing square shape with Blue color"


async def test_bridge_blue_round_shape_create():
    color = BlueColor()
    round = RoundShape(color=color)

    result = round.draw()

    assert result == "Drawing round shape with Blue color"
