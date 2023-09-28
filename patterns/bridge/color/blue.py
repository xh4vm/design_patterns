from loguru import logger
from .base import BaseColor


class BlueColor(BaseColor):

    def get(self):
        message = "Blue color"
        logger.info(message)
        return message
