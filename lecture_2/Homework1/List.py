from array import array
from math import fabs


class Ptr:
    def __init__(self, data):
        self.data = data
        self.ptr = 0

    def __next__(self):
        if self.ptr == len(self.data)-1:
            raise StopIteration
        self.ptr += 1
        return self.data[self.ptr]

    def prev(self):
        if fabs(self.ptr) == len(self.data)-1:
            raise StopIteration
        self.ptr -= 1
        return self.data[self.ptr]

    def __iadd__(self, num):
        if (self.ptr+num) >= len(self.data):
            raise StopIteration
        self.ptr += num
        return self.data[self.ptr]

    def __isub__(self, num):
        if fabs(self.ptr - num) >= len(self.data):
            raise StopIteration
        self.ptr -= num
        return self.data[self.ptr]


class List:
    def __init__(self, itemtype, *args):
        self.data = array(itemtype, args)

    def __str__(self):
        return self.data.__str__()

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return self.data.__len__()

    def __contains__(self, item):
        for it in self.data:
            if (item == it):
                return True
        return False

    def __add__(self, other):
        return self.data + other

    def __iadd__(self, other):
        self.data += other

    def __lt__(self, other):
        # <
        if self.data.__len__() < other.data.__len__():
            return True
        elif self.data.__len__() > other.data.__len__():
            return False
        else:
            notR = False
            for i, elem in enumerate(self.data):
                if elem > other.data[i]:
                    return False
                if elem < other.data[i]:
                    notR = True
            return notR

    def __le__(self, other):
        # <=
        if self.data.__len__() < other.data.__len__():
            return True
        elif self.data.__len__() > other.data.__len__():
            return False
        else:
            for i, elem in enumerate(self.data):
                if elem > other.data[i]:
                    return False
            return True

    def __eq__(self, other):
        # ==
        if self.data.__len__() != other.data.__len__():
            return False
        else:
            for i, elem in enumerate(self.data):
                if elem != other.data[i]:
                    return False
            return True

    def __ne__(self, other):
        # !=
        if self.data.__len__() != other.data.__len__():
            return True
        else:
            for i, elem in enumerate(self.data):
                if elem != other.data[i]:
                    return True
            return False

    def __gt__(self, other):
        # >
        if self.data.__len__() > other.data.__len__():
            return True
        elif self.data.__len__() < other.data.__len__():
            return False
        else:
            notR = False
            for i, elem in enumerate(self.data):
                if elem < other.data[i]:
                    return False
                if elem > other.data[i]:
                    notR = True
            return notR

    def __ge__(self, other):
        # >=
        if self.data.__len__() > other.data.__len__():
            return True
        elif self.data.__len__() < other.data.__len__():
            return False
        else:
            for i, elem in enumerate(self.data):
                if elem < other.data[i]:
                    return False
            return True

    def __mul__(self, num):
        # *
        temp = List(self.data.typecode)
        if num == 0:
            temp.data.clear()
        else:
            i = 0
            while i != num:
                temp.data.extend(self.data)
                i += 1
        return temp

    def __imul__(self, num):
        # *=
        temp = self.data
        if num == 0:
            self.data = array(self.data.typecode)
        else:
            i = 1
            while i != num:
                self.data += temp
                i += 1
        return self

    def append(self, item):
        self.data += array(self.data.typecode, [item])

    def count(self, item):
        cou = 0
        for elem in self.data:
            if elem == item:
                cou += 1
        return cou

    def extend(self, *args):
        for item in args:
            self.data += array(self.data.typecode, item)

    def insert(self, idx, x):
        old = self.data
        self.data = array(old.typecode)
        for i, item in enumerate(old):
            if i < idx or i > idx:
                self.append(item)
            elif i == idx:
                self.append(x)
                self.append(item)

    def __iter__(self):
        self.ptr = Ptr(self.data)
        return self.ptr

    def __next__(self):
        return self.data.__next__()

    def pop(self, i=-1):
        if i == -1:
            i = self.data.__len__() - 1
        temp = self.data
        self.data = array(self.data.typecode)
        for dx, item in enumerate(temp):
            if dx != i:
                self.append(item)
        return temp[i]

    def remove(self, x):
        temp = self.data
        if self.data.typecode == 'u':
            self.data = array(self.data.typecode, ['0' for i in range(len(temp)-1)])
        else:
            self.data = array(self.data.typecode, [0 for i in range(len(temp) - 1)])
        found = False
        for i,item in enumerate(temp):
            if item == x and not found:
                found = True
            else:
                if found:
                    self.data[i-1] = item
                else:
                    self.data[i] = item
        if not found:
            raise ValueError

    def __reversed__(self):
        old = self.data
        self.data = array(self.data.typecode)
        for i in range(old.__len__() - 1, -1, -1):
            self.append(old[i])

    def clear(self):
        self.data = array(self.data.typecode)

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        if key >= len(self):
            raise IndexError

        temp = self.data
        if self.data.typecode == 'u':
            self.data = array(self.data.typecode, ['0' for i in range(len(temp) - 1)])
        else:
            self.data = array(self.data.typecode, [0 for i in range(len(temp) - 1)])
        for i, item in enumerate(temp):
            if i < key:
                self.data[i] = item
            elif i>key:
                self.data[i-1] = item

# def __main__():
#     print("start")

