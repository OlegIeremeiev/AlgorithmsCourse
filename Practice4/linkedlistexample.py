from typing import Iterable
from AlgorithmsCourse.Practice1.abstract_object import AbstractObject
from AlgorithmsCourse.Practice3.abstractstructure import AbstractStructure
from AlgorithmsCourse.Practice4.node import Node


class LinkedList(AbstractStructure):

    def __init__(self, *args: Iterable[AbstractObject]):
        self.__head = None
        self.__tail = None
        self.__size = 0
        self.__iter_link = self.__head
        if args and isinstance(args, Iterable):
            for element in args[0]:
                self.append(element)

    def __len__(self) -> int:
        return self.__size

    def __repr__(self) -> str:
        pass

    def __iter__(self) -> Iterable:
        return self

    def __next__(self) -> AbstractObject:
        if isinstance(self.__iter_link, Node):
            self.__iter_link = self.__iter_link.next
            return self.__iter_link.data
        raise StopIteration("Ending linkedlist")

    def __getitem__(self, item):

        if isinstance(item,slice):
            raise NotImplemented

        # some text
        link = self.__head
        counter = 0
        while link is not None and counter < item:
            link = link.next
            counter += 1

        if link is not None:
            return link.data
        raise IndexError("Out of linkedlist")

    def append(self, value: AbstractObject) -> None:
        if self.__head is None:
            self.__head = Node(value)
            self.__tail = self.__head
        else:
            self.__tail.next = Node(value)
            self.__tail = self.__tail.next
        self.__size += 1
