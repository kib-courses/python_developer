from homework1 import Sequence

array = Sequence('f', 1.0, 2.2, 3.4, 4.7, 5.8)
array2 = Sequence('f', 15.5, 16.8, 17.9)

def iterate():
    d = [i for i in array]
    print(d)

def reverse():
    b = reversed(array)
    c = [i for i in b]
    print(c)


def length():
    print(len(array))


def gets(i, j=3):
    print(array[i])
    if i<j:
        print(array[i:j])

def sets(i, val):
    array[i] = val
    d = [i for i in array]
    print(d)

def deletes(i):
    d = [i for i in array]
    del d[i]
    print(d)

def adds():
    d = [i for i in array]
    e = [i for i in array2]
    d += e
    print(d)

def index_test(i):
    print(array.index(i))

def count_test(i):
    print(array.count(i))

def app_end(*i):
    array.append(i)
    print(*array)


iterate()
reverse()
length()
gets(2)
sets(2, 9)
deletes(3)
adds()
index_test(4)
count_test(1)
app_end(7)