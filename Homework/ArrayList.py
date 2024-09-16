from array import array, ArrayType
from typing import TypeVar, Iterable
from copy import deepcopy

T = TypeVar("T")


class ArrayList(object):
    class Iterator(object):
        __data: ArrayType
        __index: int

        def __init__(self, data: ArrayType):
            self.__data = data
            self.__index = -1

        def __iter__(self) -> 'ArrayList.Iterator':
            return self

        def __next__(self) -> T:
            if self.__index > len(self.__data) - 2:
                raise StopIteration()

            self.__index += 1
            return self.__data[self.__index]

    class ReverseIterator(object):
        __data: ArrayType
        __index: int

        def __init__(self, data: ArrayType):
            self.__data = data
            self.__index = len(data)

        def __iter__(self) -> 'ArrayList.Iterator':
            return self

        def __next__(self):
            if self.__index == 0:
                raise StopIteration()

            self.__index -= 1
            return self.__data[self.__index]

    __array: ArrayType

    def __init__(self, type_char: str, *args) -> None:
        self.__array = array(type_char, args)

    def __str__(self) -> str:
        return self.__array.__str__()

    def __getitem__(self, index: int) -> T:
        return self.__array[index]

    def __len__(self) -> int:
        return len(self.__array)

    def __contains__(self, target: T) -> bool:
        for item in self.__array:
            if target == item:
                return True

        return False

    def __add__(self, other: "ArrayList") -> "ArrayList":
        copy = deepcopy(self)
        copy += other
        return copy

    def __iadd__(self, other: "ArrayList") -> "ArrayList":
        self.__array += other.__array
        return self

    def __lt__(self, other: "ArrayList") -> bool:
        if len(self.__array) < len(other.__array):
            return True

        elif len(self.__array) > len(other.__array):
            return False

        else:
            not_equal = False

            for i, elem in enumerate(self.__array):
                if elem > other.__array[i]:
                    return False

                if elem < other.__array[i]:
                    not_equal = True

            return not_equal

    def __eq__(self, other: "ArrayList") -> bool:
        if len(self.__array) != len(other.__array):
            return False

        else:
            for i, elem in enumerate(self.__array):
                if elem != other.__array[i]:
                    return False
            return True

    def __le__(self, other: "ArrayList") -> bool:
        if self < other:
            return True
        elif self == other:
            return True

        return False

    def __ne__(self, other: "ArrayList") -> bool:
        return not self == other

    def __gt__(self, other: "ArrayList") -> bool:
        return not self <= other

    def __ge__(self, other: "ArrayList") -> bool:
        return not self < other

    def __mul__(self, mult: int) -> "ArrayList":
        result = deepcopy(self)
        result *= mult

        return result

    def __imul__(self, mult: int) -> "ArrayList":
        old_len = len(self.__array)
        new_len = old_len * mult
        new_array = array(self.__array.typecode, [0 for _ in range(new_len)])

        for i in range(new_len):
            new_array[i] = self.__array[i % old_len]

        self.__array = new_array
        return self

    def append(self, item: T) -> None:
        self.__array += array(self.__array.typecode, [item])

    def count(self, item: T) -> int:
        count = 0

        for elem in self.__array:
            if elem == item:
                count += 1

        return count

    def index(self, target: T, start=0, stop=None) -> int:
        stop = stop if stop is not None else len(self.__array)
        for i in range(start, stop):
            if self.__array[i] == target:
                return i

        raise ValueError

    def extend(self, *args: Iterable) -> None:
        for elem in args:
            self.__array += array(self.__array.typecode, elem)

    def insert(self, index: int, item: T) -> None:
        if index == -1:
            self.append(item)
            return

        elif index < 0:
            index = len(self.__array) + index + 1

        old_array = self.__array
        self.__array = array(old_array.typecode)

        for i, elem in enumerate(old_array):
            if i == index:
                self.append(item)
                self.append(elem)

            else:
                self.append(elem)

    def __iter__(self) -> 'ArrayList.Iterator':
        return ArrayList.Iterator(self.__array)

    def pop(self, index=-1) -> T:
        if index < 0:
            index = len(self.__array) + index

        if index > len(self.__array) - 1:
            raise IndexError

        new_array = array(self.__array.typecode, [0 for _ in range(len(self.__array) - 1)])

        i = 0
        is_found = False
        for elem in self.__array:
            if i == index and not is_found:
                item = self.__array[i]
                is_found = True
                continue

            new_array[i] = elem
            i += 1

        self.__array = new_array

        return item

    def remove(self, target: T) -> None:
        index = self.index(target)
        self.pop(index)

    def __reversed__(self) -> 'ArrayList.ReverseIterator':
        return ArrayList.ReverseIterator(self.__array)

    def __setitem__(self, key: int, value: T) -> None:
        self.__array[key] = value

    def __delitem__(self, key: int) -> None:
        self.pop(key)
