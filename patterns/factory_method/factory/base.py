from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    async def factory_method(self, *args, **kwargs) -> type:
        """Создание класса"""
