from AlgorithmsCourse.Practice3.abstractstructure import AbstractStructure
from AlgorithmsCourse.Practice1.abstract_object import AbstractObject
from collections.abc import Iterable


class StructureExample(AbstractStructure):
    """Класс реалізації структури на основі list і основних його методів
    """

    def __init__(self, *args: Iterable[AbstractObject]):
        self.__list = []
        if args and isinstance(args, tuple):
            for element in args:
                self.__list += element

    def __repr__(self) -> str:
        return str(self.__list)

    def __len__(self) -> int:
        return len(self.__list)

    def __getitem__(self, item):
        try:
            return self.__list[item]
        except IndexError:
            raise ValueError("getitem: Для наочності ")

    def __setitem__(self, key, value):
        try:
            self.__list[key] = value
        except IndexError:
            raise ValueError("setitem: Для наочності ")

    def __delitem__(self, key):
        try:
            del self.__list[key]
        except ValueError:
            raise ValueError("delitem: Для наочності ")
    
    def append(self, value: AbstractObject) -> None:
        self.__list.append(value)

    def insert(self, index: int, value: AbstractObject) -> None:
        self.__list.insert(index, value)

    def extend(self, values: Iterable[AbstractObject]) -> None:
        self.__list.extend(values)

    def clear(self) -> None:
        self.__list.clear()

    def remove(self, value: AbstractObject) -> None:
        try:
            self.__list.remove(value)
        except ValueError:
            raise ValueError("remove: Для наочності ")

    def pop(self, index: int = -1) -> AbstractObject:
        try:
            return self.__list.pop(index)
        except IndexError:
            raise IndexError("pop: Для наочності ")

    def copy(self) -> list[AbstractObject]:
        return self.__list.copy()

    def reverse(self) -> None:
        self.__list.reverse()

    def index(self, value: AbstractObject, start: int = 0, stop: int = -1) -> int:
        if stop == -1:
            stop = len(self.__list)
        try:
            return self.__list.index(value, start, stop)
        except ValueError:
            raise ValueError("index: Для наочності ")

    def count(self, value: AbstractObject) -> int:
        return self.__list.count(value)
