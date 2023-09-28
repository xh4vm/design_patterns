from abc import ABC, abstractmethod
from patterns.bridge.color.base import BaseColor


class BaseShape(ABC):
    def __init__(self, color: BaseColor) -> None:
        self.color = color

    @abstractmethod
    def draw(self) -> None:
        """Метод отрисовки фигуры"""
