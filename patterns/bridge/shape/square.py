from loguru import logger

from .base import BaseShape


class SquareShape(BaseShape):

    def draw(self) -> None:
        message = f"Drawing square shape with {self.color.get()}"
        logger.info(message)

        return message
