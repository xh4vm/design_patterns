from abc import ABC, abstractmethod


class BaseOldAPI(ABC):
    @abstractmethod
    def old_request(self, *args, **kwargs) -> list[type]:
        """Метод запроса по внешнему апи"""
