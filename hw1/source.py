import collections
from array import array


class iterator:

    def __init__(self, list, direct):
        self._list = list
        self._direct = direct
        self._ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._ind < len(self._list) and self._ind >= 0:
            yield self._list[self._ind]
            self._ind += self._direct
        else:
            raise StopIteration


class arraylist:

    def __init__(self, typ, data):
        self.capacity = len(data)
        self.typ = typ
        self.arraylist = array(typ, data)

    def __len__(self):
        return len(self.arraylist)

    def __contains__(self, item):
        if type(item) == self.typ:
            for x in self:
                if item == x:
                    return True
        return False

    def __getitem__(self, start, stop=None, step=1):
        index = self.indcheck(start)
        if stop == None:
            end = start + 1
        else:
            end = stop
        return self.__data[index:end:step]

    def __delitem__(self, index):
        x = self.indcheck(index)
        t = self.arraylist[:x]
        t = t + self.arraylist[x + 1:]
        self.arraylist = array(self.typ, t)
        self.capacity -= 1
        return self

    def __iadd__(self, data):
        if isinstance(data, collections.abc.Sized):
            amount = len(data)
            self.capacity += amount
            for i in range(amount):
                self.arraylist += array(self.typ, [data[i]])
        else:
            self.arraylist = array(self.typ, self.arraylist[:] + array(self.typ, [data]))
            self.capacity += 1
        return self

    def __setitem__(self, index, value):
        x = self.indcheck(index)
        t = self.arraylist[:x]
        v = array(self.typ, [value])
        t = t + v + self.arraylist[x + 1:]
        self.arraylist = array(self.typ, t)
        return self

    def __iter__(self):
        return iterator(self.arraylist, 1)

    def __reversed__(self):
        return iterator(self.arraylist, -1)

    def indcheck(self, index):
        x = 0
        if index < 0:
            x = self.capacity - (abs(index) % self.capacity)
        elif index > self.capacity:
            x = index % self.capacity
        return x

    def index(self, item):
        if type(item) == self.typ:
            for i, x in enumerate(self):
                if x == item:
                    return i
        return None

    def count(self, item):
        i = 0
        if self.typ == type(item):
            for x in self:
                if x == item:
                    i += 1
            return i
        else:
            return None

    def remove(self, item):
        a = self.arraylist.index(item)
        if a:
            t = self.arraylist[:a]
            t = t + self.arraylist[a + 1:]
            self.arraylist = array(self.typ, t)
        self.capacity -= 1

    def pop(self, index):
        x = self[self.indcheck(index)]
        self.remove(x)
        self.capacity -= 1
        return x

    def append(self, item):
        self.arraylist = array(self.typ, self.arraylist[:] + array(self.typ, [item]))
        self.capacity += 1

    def insert(self, i, item):
        index = self.indcheck(i)
        if index != 0:
            t = self.arraylist[index:]
            t = self.arraylist[:index] + array(self.typ, [item]) + t
        elif index == 0:
            t = array(self.typ, [item]) + self.arraylist[index:]
        self.arraylist = array(self.typ, t)
        self.capacity += 1

    def extend(self, data):
        if isinstance(data, collections.abc.Sized):
            amount = len(data)
            self.capacity += amount
            for i in range(amount):
                self.arraylist += array(self.typ, [data[i]])
        else:
            self.arraylist = array(self.typ, self.arraylist[:] + array(self.typ, [data]))
            self.capacity += 1
