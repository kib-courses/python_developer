from main import Arr

array = Arr("u", "1", "2", "1", "4", "1")


def reverse():
    b = reversed(array)
    c = [_ for _ in b]
    print(b)
    print(c)


def iterate():
    d = [_ for _ in array]
    print(d)


def length():
    print(len(array))


def get_it(i):
    print(array[3])
    c = [_ for _ in array[1:3]]
    print(c)


def index_test(i):
    print(array.index(i))


def count_test(i):
    print(array.count(i))


reverse()
iterate()
length()
get_it(3)
index_test("4")
count_test("1")
array["4"] = "3"
iterate()
del array[3]
iterate()

