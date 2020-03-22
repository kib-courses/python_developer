from array import array


class ArrayIterator:
    def __init__(self, collection, length):
        self.collection = collection
        self.length = length
        self.pos = 0
        
    def __next__(self):
        if (self.pos < self.length):
            self.pos += 1
            return self.collection[self.pos-1]
        else:
            raise StopIteration
        
    def __iter__(self):
        return self
        
# для array используем только repr, len, индексацию и объединение, трактууем как сишный массив

types = {'i' : "<class 'int'>", 'f' : "<class 'float'>", 'u' : "<class 'str'>"}

# для инициализации испольуем буковки i, f или u. Как для оригинальных array
class ArrayList:
    def __init__(self, initial_capacity, initial_type, initial_length = 0):
        if (initial_capacity > 0):
            self.capacity = initial_capacity
            self.length = initial_length
            self.array = array(initial_type, [])
            self.type = types[initial_type]
        else:
            raise ValueError("Capacity can't be less, than 0")

    def __str__(self):
        result = ''
        for i in range(self.length):
            result += str(self.array[i]) + ' '
        return result

    def __repr__(self):
        return repr(self.array)

    # добавление элементов(с возможностью добавления сразу нескольких(но минимум одного))
    def append(self, el, *keys):
        if (self.length < self.capacity):
            if (str(type(el)) == self.type):
                self.array += array(self.array.typecode, [el])
                self.length += 1
            else:
                raise TypeError('Incorrect key type')
        else:
            raise IndexError('Array is full')
        for key in keys:
            self.append(key)

    # вставка на определенную позицию
    def insert(self, pos, el):
        if (self.length < self.capacity):
            if (str(type(el)) == self.type):
                self.array = array(self.array.typecode, self.array[0:pos] +
                array(self.array.typecode, [el]) + self.array[pos:self.length])
                self.length += 1
            else:
                raise TypeError('Incorrect key type')
        else:
            raise IndexError('Array is full')

    def pop(self):
        if (self.length > 0):
            self.array = self.array[:-1]
            self.length += -1
        else:
            raise IndexError('Array is empty')

    def remove(self, el):
        if (self.length > 0):
            pos = None
            for i in range(self.length):
                if (self.array[i] == el):
                    pos = i
                    break
            if (pos is not None):
                self.array = self.array[:pos] + self.array[pos+1:]
                self.length += -1
            else:
                print('No such key in Array')
                return
                #raise KeyError('No such key in Array')
        else:
            raise IndexError('Array is empty')

    def __len__(self):
        return self.length

    def __getitem__(self, pos):
        return self.array[pos]

    def __iter__(self):
        return ArrayIterator(self.array, self.length)

    def count(self, el):
        counter = 0
        for  i in range(self.length):
            if (self.array[i] == el): counter += 1
        return counter

    def index(self, el):
        for  i in range(self.length):
            if (self.array[i] == el): return i
        return 'No such element'

    #def __add__(self, other):
        if isinstance(other, ArrayList):
            if (other.type == self.type):
                return ArrayList(other.capacity + self.capacity, self.type,
                other.length + self.length, other.array + self.array)
            else:
                raise ValueError('Different types')
        else:
            raise ValueError('Different types of objects')

    def __contains__(self, el):
        for  i in range(self.length):
            if (self.array[i] == el): return True
        return False


if __name__ == '__main__':
    # инициализация
    list1 = ArrayList(5, 'i')
    # [. . . . .]
    #вставляем элементы
    list1.append(0, 2, 3)
    # [0 2 3 . .]
    # insert in position
    list1.insert(1, 1)
    # [0 1 2 3 .]
    print(list1)
    # pop last
    list1.pop()
    # [0 1 2 . .]
    list1.remove(1)
    print(list1)
    # [0 2 . . .]
    list1.remove(16)
    print(list1)
    # working with iterator:
    for i in list1:
        print('i = ', i)
