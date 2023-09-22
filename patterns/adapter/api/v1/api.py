from loguru import logger

from .base import BaseOldAPI


class API(BaseOldAPI):
    def old_request(self, *args, **kwargs) -> list[type]:
        message = "Getting data from old external api"
        logger.info(message)

        return message
