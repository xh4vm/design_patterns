from loguru import logger

from .base import BaseNewAPI


class API(BaseNewAPI):
    def new_request(self, *args, **kwargs) -> list[type]:
        message = "Getting data from new external api"
        logger.info(message)

        return message
