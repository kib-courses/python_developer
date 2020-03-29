from array import array


class Iterator:
    """Итератор для прохождения по коллекции"""

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

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.end:
            raise StopIteration
        current = self.collection[self.current]
        self.current += self.step
        return current


class ArrayList:
    def __init__(self, type, init_list=[]):
        self.data = array(type, init_list)

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        for i in range(len(self.data)):
            if item == self.data[i]:
                return True
        return False

    def __iter__(self):
        return Iterator(self.data)
        # return (self.data[i] for i in range(len(self.data)))

    def __reversed__(self):
        # for i in range(len(self.data)):
        #    yield self.data[len(self.data)-i]
        #return (self.data[len(self.data) - 1 - i] for i in range(len(self.data)))
        return Iterator(self.data, -1, 0, -1)

    def index(self, item):
        for i in range(len(self.data)):
            if item == self.data[i]:
                return i
        raise ValueError

    def count(self, item):
        counter = 0
        for i in range(len(self.data)):
            if self.data[i] == item:
                counter += 1
        return counter


if __name__ == "__main__":
    my_array1 = ArrayList('l', [1, 2, 2, 3, 4, 5])
    my_array2 = ArrayList('d', [1.5, 7.7, 123.1])
    my_array3 = ArrayList('u', ['s', 't', 'r', 'i', 'n', 'g'])

    # Проверка получения значения по индексу
    print('my_array1[0] = {}'.format(my_array1[0]))
    print('my_array2[1] = {}'.format(my_array2[1]))
    print('my_array3[2] = {}'.format(my_array3[2]))

    # Проверка длины
    print('len my_array1 = {}'.format(len(my_array1)))
    print('len my_array2 = {}'.format(len(my_array2)))
    print('len my_array3 = {}'.format(len(my_array3)))

    # Проверка вхождения элементов
    print('10 in [1,2,2,3,4,5] -> {}'.format(10 in my_array1))
    print('1.5 in [1.5, 7.7, 123.1] -> {}'.format(1.5 in my_array2))
    print("'g' in ['s','t','r','i','n','g'] -> {}".format('g' in my_array3))

    # Проверка итераторов
    for v in my_array1:
        print(v, end=' ')
    print()
    for v in my_array2:
        print(v, end=' ')
    print()
    for v in my_array3:
        print(v, end=' ')
    print()
    itr = iter(my_array1)
    while True:
        try:
            print(next(itr), end=' ')
        except StopIteration:
            break
    print()

    # Переворот массивов
    print("Reversed [1,2,2,3,4,5] is {}".format(list(reversed(my_array1))))
    print("Reversed [1.5, 7.7, 123.1] is {}".format(list(reversed(my_array2))))
    print("Reversed ['s','t','r','i','n','g'] is {}".format(list(reversed(my_array3))))

    # Проверка вхождений индекса
    print("3 on the {} place in [1,2,2,3,4,5]".format(my_array1.index(3)))
    print("7.7 on the {} place in [1.5, 7.7, 123.1]".format(my_array2.index(7.7)))
    print("i on the {} place in ['s','t','r','i','n','g']".format(my_array3.index('i')))

    # Проверка количества элементов
    print("count of 2 in [1,2,2,3,4,5] is {}".format(my_array1.count(2)))
    print("count of 1.1 in [1.5, 7.7, 123.1] is {}".format(my_array2.count(1.1)))
    print("count of n in ['s','t','r','i','n','g'] is {}".format(my_array3.count('n')))
