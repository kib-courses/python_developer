from main import Arr

array = Arr('i', 1, 2, 1, 4, 1)


def reverse():
    b = reversed(array)
    print(b)
    c = [_ for _ in b]
    print(c)


def iterate():
    d = [_ for _ in array]
    print(d)


def length():
    print(len(array))


def get_it(i):
    print(array[3])
    print(array[1:3])


def index_test(i):
    print(array.index(i))


def count_test(i):
    print(array.count(i))


reverse()
iterate()
length()
get_it(3)
index_test(4)
count_test(1)
