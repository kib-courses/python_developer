from array import array as arr

''' 
'''
class Iter_for_arr():
    def __init__(self, my_arr):
        self._my_arr = my_arr
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if (self._index < len(self._my_arr)):
            self._index += 1
            return self._my_arr[self._index - 1]
        else:
            raise StopIteration

class My_arr():

    def __init__(self, type_arr, vx_list=list()):
        self.type = type_arr
        self.__type = self.__what_it_is()
        self.__my_arr = arr(self.__what_it_is(), vx_list)
        return

    def __what_it_is(self):
        if self.type == int:
            return 'i'
        if self.type == float:
            return 'd'
        if self.type == str:
            return 'u'
        else:
            raise TypeError

    def __iter__(self):
        return Iter_for_arr(self)

    def __len__(self):
        return len(self.__my_arr)

    def __setitem__(self, key, value):
        self.__my_arr[key] = value
        return

    def __getitem__(self, key):
        if isinstance(key, slice):
            start = key.start if key.start is not None else 0
            stop = key.stop if key.stop is not None else len(self)
            step = key.step if key.step is not None else 1

            if start < 0:
                start += len(self)+1
            else:
                start
            if stop < 0:
                stop += len(self)
            else:
                stop
            if step < 0:
                start, stop= stop-1, start-1

            sl_arr = list()
            for i in range(start, stop, step):
                sl_arr.append(self.__my_arr[i])

            return My_arr(self.type, sl_arr)
        return self.__my_arr[key]


    def __delitem__(self, index):
        del self.__my_arr[index]

# переопределение метода +=
    def __iadd__(self, other):
        self.__my_arr = self.__my_arr + other.__my_arr
        return self

    def __str__(self):
        return str(list(self.__my_arr))

    def __reversed__(self):
        return iter(self[::-1])

    def __contains__(self, elem):
        for indx in range(len(self)):
            if self[indx] == elem:
                return True
        return False

    def count(self, value):
        count = 0
        for elem in self:
            if elem == value:
                count += 1
        return count

    def extend(self, arr_2):
        arr_list = arr(self.__type, arr_2)
        self.__my_arr = self.__my_arr + arr_list
        return

    def pop(self, index=-1):
        return_val = self[index]
        del self[index]
        return return_val

    def remove(self, value):
        del_indx = -1
        for indx in range(0, len(self.__my_arr)):
            if self.__my_arr[indx] == value:
                del_indx = indx
                break
        if del_indx >= 0:
            del self[del_indx]
            return
        else:
            raise ValueError

    def append(self, data):
        self.__my_arr = self.__my_arr + arr(self.__type, [data])
        return

    def insert(self, index, value):
        self.__my_arr = self[:index].__my_arr + arr(self.__type, [value]) + self[index:].__my_arr

    def reverse(self):
        self.__my_arr = self[::-1].__my_arr
        return

    def index(self, val, start=0, stop=None):
        if not stop:
            end = len(self)

        for indx, elem in enumerate(self[start:stop]):
            if val == elem:
                return indx + start

        raise ValueError


if __name__ == '__main__':

    int_example = My_arr(int, [-1, 5, -2, 14])
    float_example = My_arr(float, [-2.8, 6.4])
    str_example = My_arr(str, ['y', 'u', '5'])

#test __iter__
    print('__iter__ for', int_example)
    for el in int_example:
        print(el)
    print('__iter__ for:', float_example)
    for el in float_example:
        print(el)
    print('__iter__ for:', str_example)
    for el in str_example:
        print(el)
    print('\n')

#test __len__
    print('__len__ for', int_example, 'is: ', len(int_example))
    print('__len__ for', float_example, 'is: ', len(float_example))
    print('__len__ for', str_example, 'is: ', len(str_example),)
    print('\n')

#test __setitem
    print('__setitem__ for ', int_example, '([-1] = 7), ([0] = 20) is: ')
    int_example[-1] = 7
    int_example[0] = 20
    print(int_example)
    print('__setitem__ for ', float_example, '([-1] = -3.5), ([0] = 9.8) is: ')
    float_example[-1] = -3.5
    float_example[0] = 9.8
    print(float_example)
    print('__setitem__ for ', str_example, '([-2] = ы), ([0] = s) is: ')
    str_example[-2] = 'ы'
    str_example[0] = 's'
    print(str_example)
    print('\n')

#test __getitem__
    print('__getitem__ for', int_example, ' [3] and [-4] is: ', int_example[3],'and',int_example[-4])
    print('__getitem__ for', float_example, ' [0] and [-1] is: ', float_example[0], 'and', float_example[-1])
    print('__getitem__ for', str_example, ' [2] and [-2] is: ', str_example[2], 'and', str_example[-2])
    print('\n')

#test __delitem__
    print('__delitem__ for', int_example, ' [-3] is: ')
    del int_example[-3]
    print(int_example)
    print('__delitem__ for', float_example, ' [1] is: ')
    del float_example[1]
    print(float_example)
    print('__delitem__ for', str_example, ' [-1] is: ')
    del str_example[-1]
    print(str_example)
    print('\n')

#test __iadd__
    test_int = My_arr(int, [-2, -3])
    test_float = My_arr(float, [5.2, -7.3])
    test_str = My_arr(str, ['d', 'ц', 'ы', 'w', 'ы'])
    print('__iadd__ for', int_example, 'and', test_int, 'is: ')
    int_example += test_int
    print(int_example)
    print('__iadd__ for', float_example, 'and', test_float, 'is: ')
    float_example += test_float
    print(float_example)
    print('__iadd__ for', str_example, 'and', test_str, 'is: ')
    str_example += test_str
    print(str_example)
    print('\n')

# test __str__
    print('__str__ for int_ex:', int_example)
    print('__str__ for float_ex:', float_example)
    print('__str__ for str_ex:', str_example)
    print('\n')

#test __reversed__
    print('__reversed__ for', int_example, 'is: ', My_arr(int, reversed(int_example)))
    print('__reversed__ for', float_example, 'is: ', My_arr(float, reversed(float_example)))
    print('__reversed__ for', str_example, 'is: ', My_arr(str, reversed(str_example)))
    print('\n')

#test __contains__
    print('__contains__ for', int_example, 'elem (7): ', 7 in int_example)
    print('__contains__ for', float_example, 'elem (20.5): ', 20.5 in float_example)
    print('__contains__ for', str_example, 'elem (ы): ', 'ы' in str_example)
    print('\n')

#test count
    print('count for', int_example, 'elem (-2): ', int_example.count(-2))
    print('count for', float_example, 'elem (3.14): ', float_example.count(3.14))
    print('count for', str_example, 'elem (ы): ', str_example.count('ы'))
    print('\n')

#test extend
    print('extend for', int_example, 'extd arr:', test_int, 'res: ', )
    int_example.extend(test_int)
    print(int_example)
    print('extend for', float_example, 'extd arr:', test_float, 'res: ', )
    float_example.extend(test_float)
    print(float_example)
    print('extend for', str_example, 'extd arr:', test_str, 'res: ', )
    str_example.extend(test_str)
    print(str_example)
    print('\n')

#test pop
    print('pop for', int_example, 'elem (-1) and () : ')
    int_example.pop(-1)
    int_example.pop()
    print(int_example)
    print('pop for', float_example, 'elem (0) and (-3) : ')
    float_example.pop(0)
    float_example.pop(-3)
    print(float_example)
    print('pop for', str_example, 'elem (4) and (-5) : ')
    str_example.pop(4)
    str_example.pop(-5)
    print(str_example)
    print('\n')

#test remove   так так, а это у нас ломается. Тут было бы в идеале все обернуть в исключения но мне лень
    print('remove for', int_example, 'elem (0) and (-2): ')
    try:
        int_example.remove(0)
        print(int_example)
    except:
        print('value error')
    int_example.remove(-2)
    print(int_example)
    print('remove for', float_example, 'elem (5.2) and (4.15): ')
    float_example.remove(5.2)
    print(float_example)
    try:
        float_example.remove(4.15)
        print(float_example)
    except:
        print('value error')
    print('remove for', str_example, 'elem (w) and (ы): ')
    str_example.remove('w')
    print(str_example)
    str_example.remove('ы')
    print(str_example)
    print('\n')

#test append
    print('append for', int_example, 'elem (4) and (-5): ')
    int_example.append(4)
    int_example.append(-5)
    print(int_example)
    print('append for', float_example, 'elem (7.321): ')
    float_example.append(7.321)
    print(float_example)
    print('append for', str_example, 'elem (2) and (Q): ')
    str_example.append('2')
    str_example.append('Q')
    print(str_example)
    print('\n')

#test insert
    print('inser for', int_example, 'elem (40) on [-2]')
    int_example.insert(-2, 40)
    print(int_example)
    print('inser for', float_example, 'elem (24) on [0]')
    float_example.insert(0, 24)
    print(float_example)
    print('inser for', str_example, 'elem (t) on [3]')
    str_example.insert(3, 't')
    print(str_example)
    print('\n')

#test reverse
    print('reverse for', int_example, ': ')
    int_example.reverse()
    print(int_example)
    print('reverse for', float_example, ': ')
    float_example.reverse()
    print(float_example)
    print('reverse for', str_example, ': ')
    str_example.reverse()
    print(str_example)

#test index
    print('index for', int_example, 'elem(-3): ')
    try:
        print(int_example.index(-3))
    except:
        print('value error')
    print('index for', float_example, 'elem(44.4): ')
    try:
        print(float_example.index(44.4))
    except:
        print('value error')
    print('index for', str_example, 'elem(ы): ')
    try:
        print(str_example.index('ы'))
    except:
        print('value error')
