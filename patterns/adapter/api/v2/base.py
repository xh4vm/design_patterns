from abc import ABC, abstractmethod


class BaseNewAPI(ABC):
    @abstractmethod
    def new_request(self, *args, **kwargs) -> list[type]:
        """Метод запроса по внешнему апи"""
