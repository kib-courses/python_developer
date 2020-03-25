from array import array


def _int(item) -> bool:
    return type(item) == int


def _u_int(item) -> bool:
    return type(item) == int and item >= 0


def _float(item) -> bool:
    return type(item) == float


def _char(item) -> bool:
    return type(item) == str and len(item) == 1


# This dict calls functions defined above,
# in method _is_correct_object which checks that
# all items in iterable object have same types


_type_codes = {
    'b': _int,
    'B': _u_int,
    'u': _char,
    'h': _int,
    'H': _u_int,
    'i': _int,
    'I': _u_int,
    'l': _int,
    'L': _u_int,
    'q': _int,
    'Q': _u_int,
    'f': _float,
    'd': _float
}


class ArrayIterator:
    _array: array
    _position: int

    def __init__(self, _arr: array):
        self._array = _arr
        self._position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._position not in range(len(self._array)):
            raise StopIteration
        self._position += 1
        return self._array[self._position-1]


class ArrayList:
    _data: array
    _type: str

    def __init__(self, _type: str, *args):
        if _type in _type_codes:
            self._type = _type
            self._is_correct_object(*args)  # Raise if args incorrect
            self._data = array(_type, args)
        else:
            raise TypeError("'{}' type is not provided.".format(_type))

    def __getitem__(self, index: int):
        return self._data[index]

    def __setitem__(self, index: int, value):
        self._is_correct_object(value)
        self._data[index] = value

    def __delitem__(self, index: int):
        # self._data = self._data.remove(index)
        self._data = self._data[:index] + self._data[index+1:]

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return self._data.__str__().replace('array', 'ArrayList', 1)

    def __contains__(self, item):
        return item in self._data

    def __iter__(self):
        return ArrayIterator(self._data)

    def __reversed__(self):
        return ArrayIterator(self._data[::-1])

    def __add__(self, other):
        return self.extend(ArrayList(other._type, *other))

    def __iadd__(self, other):
        return self.extend(other)

    def insert(self, index: int, value):
        self._is_correct_object(value)
        item = array(self._type, [value])
        self._data = self._data[:index] + item + self._data[index:]

    def index(self, item):
        for index in range(self.__len__()):
            if self._data[index] == item:
                return index
        raise IndexError("No such item({}) in ArrayList".format(item))

    def count(self, value):
        return sum(1 if value == item else 0 for item in self._data)

    def append(self, value):
        self._is_correct_object(value)
        self._data += array(self._type, [value])

    def reverse(self):
        return self._data[::-1]

    def extend(self, oth):
        if self._type == oth._type:
            return self._data + oth._data
        raise TypeError(f"Expected '{self._type}', not '{oth._type}'")

    def pop(self, index: int):
        value = self._data[index]
        self._data = self._data[:index] + self._data[index+1:]
        return value

    def remove(self, value):
        for i in range(self.__len__()):
            if self._data[i] == value:
                self._data = self._data[:i] + self._data[i+1:]
                return None

    def clear(self):
        self._data = array(self._type)

    # Throws 'TypeError' if elements don`t have same types
    def _is_correct_object(self, *args):
        for elem in args:
            if not _type_codes[self._type](elem):
                raise TypeError("Invalid type")
