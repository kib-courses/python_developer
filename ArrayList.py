import array as arr
from typing import Iterable, Any, Type


class ArrayList:
    def __init__(self, typecode: str, data=None) -> None:
        '''
        Функция для инициализации объекта класса

        :param typecode: тип
        :param data: данные
        '''
        if typecode in ['i', 'f', 'u'] and type(data) == list and data is not None:
            self.__type = typecode
            self.array = arr.array(typecode, data)
        elif typecode in ['i', 'f', 'u'] and data is None:
            self.__type = typecode
            self.array = arr.array(typecode)
        else:
            raise Exception('Wrong init parameters.')

        self.__type_dict = {'i': int, 'f': float, 'u': str}[typecode]
        super().__init__()

    def __getitem__(self, index):
        if isinstance(index, slice):
            return type(self)(self.__type, self.array[index])
        else:
            return self.array[index]

    def __setitem__(self, key, value):
        self.array[key] = value

    def __delitem__(self, key):
        self.array = self.array[:key] + self.array[key + 1:]

    def __contains__(self, item):
        for i in range(len(self.array)):
            if self.array[i] == item:
                return True
        return False

    def __iter__(self):
        return Iterator(self.array)

    def __reversed__(self):
        return Iterator(self.array, -1, 0, -1)

    def __len__(self):
        return len(self.array)

    def __iadd__(self, ArrayList):
        self.array = self.array + ArrayList.array
        return self

    def __str__(self) -> str:
        return 'ArrayList' + str(self.array)[5:]

    def __repr__(self):
        return self.array.__repr__()

    def __sizeof__(self) -> int:
        return self.array.__sizeof__()

    def __dir__(self) -> Iterable[str]:
        return self.__dir__()

    def append(self, value):
        '''
        Добавление в конец списка

        :param value: значение
        :return: None
        '''
        if self.__type_dict is type(value):
            self.array = self.array + arr.array(self.__type, [value])
        else:
            raise Exception('Wrong type of value.')

    def insert(self, index: int, value):
        '''
        Добавление значения по индексу

        :param index: индекс
        :param value: значение
        :return: None
        '''
        if type(index) is int and type(value) is self.__type_dict:
            if index >= self.__len__():
                self.append(value)
            elif index <= 0:
                self.array = arr.array(self.__type, [value]) + self.array
            else:
                tmp = arr.array(self.__type, [value])
                self.array = self.array[:index] + tmp + self.array[index:]
        else:
            raise Exception('Wrong index and value.')

    def count(self, value):
        '''
        Подсчет одинаннаковых значений

        :param value: значение
        :return: None
        '''
        counter = 0
        for el in self.array:
            if el == value:
                counter += 1
        return counter

    def reverse(self):
        '''
        Разворот списка

        :return: список на оборот
        '''
        self.array = self.array[::-1]

    def remove(self, value):
        '''
        Удаление элемента

        :param value: значение
        :return: None
        '''
        for i, el in enumerate(self):
            if el == value:
                self.array = self.array[:i] + self.array[i + 1:]

    def pop(self, i=None):
        '''
        Удаление элемента по индексу

        :param i: индекс
        :return: удаленный элемент
        '''
        if i is None:
            i = -1

        el = self.array[i]
        if i != -1:
            self.array = self.array[:i] + self.array[i + 1:]
        else:
            self.array = self.array[:i]
        return el

    def index(self, value):
        '''
        Возвращение индекса

        :param value: элемент
        :return: индекс по элементу
        '''
        for i, el in enumerate(self.array):
            if el == value:
                return i
        raise Exception('Value not found.')

    def extend(self, arrayList):
        '''
        Добавление списка к существующему

        :param arrayList:
        :return: None
        '''
        for el in arrayList:
            self.array.append(el)


class Iterator:
    def __init__(self, collection, start=0, end=-1, step=1):
        self.collection = collection
        if start < 0:
            self.start = len(collection) + start
        else:
            self.start = start
        if end < 0:
            self.end = len(collection) + end + step
        else:
            self.end = end + step
        self.step = step
        self.current = self.start

    def __next__(self):
        if self.current == self.end:
            raise StopIteration

        c_el = self.collection[self.current]
        self.current += self.step
        return c_el

    def __iter__(self):
        return self
