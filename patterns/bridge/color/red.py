from loguru import logger
from .base import BaseColor


class RedColor(BaseColor):

    def get(self):
        message = "Red color"
        logger.info(message)
        return message
