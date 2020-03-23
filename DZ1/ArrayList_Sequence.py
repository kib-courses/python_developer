
from array import array

class ArrayList():
    def __init__(self, type, init_list=[]):
        try:
            self.data=array(type, init_list)
        except TypeError as er:
            self.data=array(type)
            print(er)

    def __getitem__(self, item):
        try:
            return self.data[item]
        except IndexError as er:
            print(er)
        except TypeError as er:
            print(er)

    def __len__(self):
        return len(self.data)


    def __contains__(self, item):
        for i in range(len(self.data)):
            if item==self.data[i]:
                return True
        return False

    def __iter__(self):
        return (self.data[i] for i in range(len(self.data)))

    def __reversed__(self):
        return self.data[::-1]

    def index(self, item):
        for i in range(len(self.data)):
            if item == self.data[i]:
                return i
        raise ValueError

    def count(self, item):
        return len([self.data[i] for i in range(len(self.data)) if item==self.data[i]])


if __name__=="__main__":
    my_array1 = ArrayList('l',[1,2,2,3,4,5])
    my_array2 = ArrayList('d', [1.5, 7.7, 123.1])
    my_array3 = ArrayList('u', ['s','t','r','i','n','g'])

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
    print('1.5 in [1.5, 7.7, 123.1] -> {}'.format(1.5in my_array2))
    print("'g' in ['s','t','r','i','n','g'] -> {}".format('g' in my_array3))

    # Проверка итераторов
    for v in my_array1:
        print(v, end='  ')
    print()
    for v in my_array2:
        print(v, end='  ')
    print()
    for v in my_array3:
        print(v, end='  ')
    print()

    # Переворот массивов
    print("Reversed [1,2,2,3,4,5] is {}".format(reversed(my_array1)))
    print("Reversed [1.5, 7.7, 123.1] is {}".format(reversed(my_array2)))
    print("Reversed ['s','t','r','i','n','g'] is {}".format(reversed(my_array3)))

    # Проверка вхождений индекса
    print("3 on the {} place in [1,2,2,3,4,5]".format(my_array1.index(3)))
    print("7.7 on the {} place in [1.5, 7.7, 123.1]".format(my_array2.index(7.7)))
    print("i on the {} place in ['s','t','r','i','n','g']".format(my_array3.index('i')))

    # Проверка количества элементов
    print("count of 2 in [1,2,2,3,4,5] is {}".format(my_array1.count(2)))
    print("count of 1.1 in [1.5, 7.7, 123.1] is {}".format(my_array2.count(1.1)))
    print("count of n in ['s','t','r','i','n','g'] is {}".format(my_array3.count('n')))
