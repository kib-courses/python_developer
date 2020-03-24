import array


class Iterator:
    # включаем и начальнйы инлекси и конечный
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
        self.curr = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr == self.end:
            raise StopIteration
        curr_el = self.collection[self.curr]
        self.curr += self.step
        return curr_el


class ArrayList:
    def __init__(self, arr_type, data=None):
        self.type_dict = {int: 'i', float: 'f', str: 'u'}
        self.type = arr_type
        if data:
            self.array = array.array(self.type_dict[arr_type], data)
        else:
            self.array = array.array(self.type_dict[arr_type])

    def __getitem__(self, index):
        if isinstance(index, slice):
            return type(self)(self.type, self.array[index])
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

    def insert(self, index, value):
        temp = array.array(self.type_dict[self.type], [value])
        self.array = self.array[:index] + temp + self.array[index:]

    def index(self, value):
        for i, el in enumerate(self):
            if el == value:
                return i
        raise ValueError

    def count(self, value):
        counter = 0
        for el in self:
            if el == value:
                counter += 1
        return counter

    def append(self, value):
        self.array = self.array + array.array(self.type_dict[self.type], [value])

    def reverse(self):
        for i in range(len(self.array) // 2):
            self.array[i], self.array[len(self.array) - 1 - i] = self.array[len(self.array) - 1 - i], self.array[i]

    def extend(self, *iterable_sequence):
        for el in iterable_sequence:
            self.append(el)

    def pop(self, i=-1):
        element = self.array[i]
        if i != -1:
            self.array = self.array[:i] + self.array[i + 1:]
        else:
            self.array = self.array[:i]
        return element

    def remove(self, value):
        for i, el in enumerate(self):
            if el == value:
                self.array = self.array[:i] + self.array[i + 1:]

    def __iadd__(self, other):
        self.array = self.array + other.array
        return self

    def __str__(self):
        str_arr = str(self.array)
        str_type = {int: 'int', float: 'float', str: 'unicode'}
        return f"({str_type[self.type]}, {str_arr[str_arr.find('['):str_arr.rfind(']') + 1]})"

    def __repr__(self):
        return self.array.__repr__()


if __name__ == '__main__':
    print('TESTS')
    print('append')
    arr1 = ArrayList(int)
    arr1.append(1)
    print(arr1)
    print('--------------')
    print('extend')
    arr1.extend(2, 3)
    print(arr1)
    print('--------------')
    print('iter')
    for el in arr1:
        print(el, end=' ')
    # \n
    print('')
    print('--------------')
    print('insert')
    arr1.insert(2, 42)
    print(arr1)
    print('--------------')
    print('reversed')
    for el in reversed(arr1):
        print(el, end=' ')
        # \n
        print('')
    print('--------------')
    print('reverse')
    arr1.reverse()
    print(arr1)
    print('--------------')
    print('remove')
    arr1.remove(42)
    print(arr1)
    print('--------------')
    print('pop')
    arr1.append(43)
    print(arr1)
    arr1.pop(-2)
    print(arr1)
    print('--------------')
    print('count')
    arr1.extend(1, 1, 1)
    print(arr1.count(1))
    print('--------------')
    print('index')
    print(arr1)
    print(arr1.index(1))
    print('--------------')
    print('get set del')
    print(arr1[3])
    arr1[3] = 44
    print(arr1)
    del arr1[3]
    print(arr1)
    print('--------------')
    print('contain')
    if 43 in arr1:
        print('43 in arr1')
    print('--------------')
    print('init from iterable, +=')
    arr2 = ArrayList(int, [44, 45, 46])
    arr2 += arr1
    print(arr2)
