from abc import ABC, abstractmethod
from collections.abc import Iterable
from AlgorithmsCourse.Practice1.abstract_object import AbstractObject


class AbstractStructure(ABC):
    """Абстрактний клас - шаблон класу з переліком необхідних до реалізації базових методів структур даних без самої їх
    реалізації"""

    # Обов'язкові до реалізації методи
    @abstractmethod
    def __init__(self, *args: Iterable[AbstractObject]):
        """Метод ініціалізації класу і наповнення його елементами структури args
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __getitem__(self, item):
        pass

    @abstractmethod
    def __setitem__(self, key, value):
        pass

    @abstractmethod
    def append(self, value: AbstractObject) -> None:
        pass

    @abstractmethod
    def insert(self, index: int, value: AbstractObject) -> None:
        pass

    @abstractmethod
    def index(self, value: AbstractObject, start: int, stop: int) -> int:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def remove(self, value: AbstractObject) -> None:
        pass

    @abstractmethod
    def copy(self) -> list[AbstractObject]:
        pass

    @abstractmethod
    def __iter__(self) -> Iterable:
        pass

    @abstractmethod
    def __next__(self) -> AbstractObject:
        pass

    # Не обов'язкові методи
    #
    @abstractmethod
    def __delitem__(self, key):
        pass

    @abstractmethod
    def extend(self, values: Iterable[AbstractObject]) -> None:
        pass

    @abstractmethod
    def count(self, value: AbstractObject) -> int:
        pass

    @abstractmethod
    def pop(self, index: int) -> AbstractObject:
        pass

    @abstractmethod
    def reverse(self) -> None:
        pass

    # @abstractmethod
    # def min(self) -> AbstractObject:
    #     pass
    #
    # @abstractmethod
    # def max(self) -> AbstractObject:
    #     pass
    #
    # @abstractmethod
    # def __add__(self,other) -> AbstractStructure|list:
    #     """Об'єднання елементів у єдину структуру"""
    #     pass
    #
    # @abstractmethod
    # def __mul__(self,other) -> AbstractStructure|list:
    #     """Множення на ціле число дублює елемелт або структуру задану кількість разів"""
    #     pass
