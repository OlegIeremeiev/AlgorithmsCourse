from AlgorithmsCourse.Practice3.abstractstructure import AbstractStructure
from AlgorithmsCourse.Practice1.abstract_object import AbstractObject
from collections.abc import Iterable


class StructureExample(AbstractStructure):
    """Класс реалізації структури на основі list і основних його методів
    """

    def __init__(self, *args: Iterable[AbstractObject]):
        self.__list = []
        self.__iter_index = 0
        if args and isinstance(args, tuple):
            for element in args:
                self.__list += element

    def __repr__(self) -> str:
        return str(self.__list)

    def __len__(self) -> int:
        return len(self.__list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__iter_index >= len(self.__list):
            raise StopIteration
        result = self.__list[self.__iter_index]
        self.__iter_index += 1
        return result

    def __getitem__(self, item):
        try:
            return self.__list[item]
        except IndexError:
            raise IndexError("getitem: Для наочності ")

    def __setitem__(self, key, value):
        try:
            self.__list[key] = value
        except IndexError:
            raise IndexError("setitem: Для наочності ")

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
        except IndexError:
            raise IndexError("index: Для наочності ")

    def count(self, value: AbstractObject) -> int:
        return self.__list.count(value)


class ArrayParts(AbstractStructure):
    __array: list
    __size: int
    __reserved: int

    def __init__(self, *args: AbstractObject|Iterable[AbstractObject]):
        self.clear()
        self.__iter_index =-1

        if len(args) == 1 and isinstance(args, Iterable):
            for element in args[0]:
                self.append(element)

    def __size_extending(self, max_size = -1):
        while self.__reserved < max(max_size, self.__reserved * 2):
            self.__reserved *= 2
        tmp = [None] * self.__reserved
        tmp[0:self.__size] = self.__array
        self.__array = tmp
        self.__reserved = len(self.__array)

    def __len__(self) -> int:
        return self.__size

    def __getitem__(self, item):
        if isinstance(item, int) and item >= self.__size:
            raise IndexError("Out of index")

        if isinstance(item, slice):
            if item.step is None or item.step >= 0:
                if item.stop is None:
                    item = slice(item.start, self.__size, item.step)
                elif item.stop > self.__size:
                    raise IndexError("Out of index")
            else:
                if item.start is None:
                    item = slice(
                        self.__size-1 if item.start is None else item.start, item.stop, item.step)
                elif item.start > self.__size-1:
                    raise IndexError("Out of index")
        return self.__array[item]

    def __setitem__(self, key, value):
        self.__array[key] = value

    def append(self, value: AbstractObject) -> None:
        if self.__size >= self.__reserved - 1:
            self.__size_extending()
        self.__array[self.__size] = value
        self.__size += 1


