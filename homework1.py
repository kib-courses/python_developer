from array import array


class Sequence:
    def __init__(self, element_type, *elements):

        self.data = array(element_type, elements)

    def __getitem__(self, item):
        if isinstance(item, slice):
            # return self.data[item]
            first_el, *elements = self.data[item]
            return [first_el, *elements]
        else:
            return self.data[item]

    def __setitem__(self, item, value):
        self.data[item] = value

    def __delitem__(self, item):
        del self.data[item]

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        for i in range(len(self.data)):
            if self.data[i] == item:
                return True
            return False

    def __iter__(self):
        return Iterator(self.data)

    def __reversed__(self):
        return Iterator(self.data, -1)

    def __iadd__(self, other):
        if isinstance(other, Sequence):
            self.data += other.data

    def index(self, item):
        for i in range(len(self.data)):
            if self.data[i] == item:
                return i
        return -1

    def count(self, item):
        counter = 0
        for i in range(len(self.data)):
            if self.data[i] == item:
                counter += 1
        return counter

    def append(self, item):
        self.data += array(self.data.typecode, [*item])



class Iterator:
    def __iter__(self):
        return self

    def __init__(self, collection, cursor=1):
        self.collection = collection
        self.cursor = cursor
        if cursor == 1:
            self._cursor = -1
            self.step = 1
        if cursor == -1:
            self._cursor = len(self.collection)
            self.step = -1

    def __next__(self):
        self._cursor += self.step
        if self._cursor < 0 or self._cursor >= len(self.collection):
            raise StopIteration()
        return self.collection[self._cursor]
