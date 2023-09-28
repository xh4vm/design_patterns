from loguru import logger

from .base import BaseShape


class RoundShape(BaseShape):
    def draw(self) -> None:
        message = f"Drawing round shape with {self.color.get()}"
        logger.info(message)

        return message
