from abc import ABC, abstractmethod


class BaseColor(ABC):

    @abstractmethod
    def get(self):
        """Возвращает цвет объекта"""
