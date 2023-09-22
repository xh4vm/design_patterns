from loguru import logger

from ..v1.api import API as OldAPI


class NewAPIAdapter(OldAPI):
    def new_request(self, *args, **kwargs) -> list[type]:
        message = self.old_request()
        logger.info(message)

        return message
