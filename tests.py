from homework1 import Sequence

array = Sequence('f', 1.0, 2.2, 3.4, 4.6, 5.57)
array2 = Sequence('f', 15.9, 16.6, 17.7)

array3 = Sequence('i', 1, 2, 3, 4, 5)
array4 = Sequence('i', 15, 16, 17)

array5 = Sequence('u', 'a', 'b', 'c', 'd', 'e')
array6 = Sequence('u', 'g', 'h', 'k')

def iterate(array):
    d = [i for i in array]
    print(d)

def reverse(array):
    b = reversed(array)
    c = [i for i in b]
    print(c)


def length(array):
    print(len(array))


def gets(array, i, j=3):
    print(array[i])
    if i<j:
        print(array[i:j])

def sets(array, i, val):
    array[i] = val
    d = [i for i in array]
    print(d)

def deletes(array, i):
    d = [i for i in array]
    del d[i]
    print(d)

def adds(array, array2):
    d = [i for i in array]
    e = [i for i in array2]
    d += e
    print(d)

def index_test(array, i):
    print(array.index(i))

def count_test(array, i):
    print(array.count(i))

def app_end(array, *i):
    array.append(i)
    print(*array)


iterate(array)
reverse(array)
length(array)
gets(array, 2)
sets(array, 2, 9)
deletes(array, 3)
adds(array, array2)
index_test(array, 1)
count_test(array, 1)
app_end(array, 7)

iterate(array3)
reverse(array3)
length(array3)
gets(array3, 2)
sets(array3, 2, 9)
deletes(array3, 3)
adds(array3, array4)
index_test(array3, 1)
count_test(array3, 1)
app_end(array3, 7)

iterate(array5)
reverse(array5)
length(array5)
gets(array5, 2)
sets(array5, 2, 'j')
deletes(array5, 3)
adds(array5, array6)
index_test(array5, 'e')
count_test(array5, 'a')
app_end(array5, 'z')