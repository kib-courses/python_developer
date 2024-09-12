from array import array


class Iterator:
    def __iter__(self):
        return self

    def __init__(self, collection, rev, counter):
        self.collection = collection
        self.rev = rev
        self.counter = counter

    def __next__(self):
        if self.rev:
            self.counter += 1
        else:
            self.counter -= 1
        if -1 < self.counter < len(self.collection):
            return self.collection[self.counter]
        else:
            raise StopIteration


class Sequence:
    def __init__(self, element_type, *elements):
        self.lst = array(element_type, elements)

    def __getitem__(self, ind):
        if isinstance(ind, slice):
            first_el, *elements = self.lst[ind]
            return (first_el, *elements)
        return self.lst[ind]

    def __len__(self):
        return len(self.lst)

    def __contains__(self, elem):
        if self.lst.count(elem) == 0:
            return False
        else:
            return True

    def __iter__(self):
        counter = -1
        self.it = Iterator(self.lst, True, counter)
        return self.it

    def __reversed__(self):
        counter = len(self.lst)
        self.it = Iterator(self.lst, False, counter)
        return self.it

    def index(self, elem):
        return self.lst.index(elem)

    def count(self, elem):
        return self.lst.count(elem)


#x = Sequence('u', 'a', 'b', 'e', 'd', 'e')
x = Sequence('i', 1, 2, 3, 2, 4)
print(x[:3])
print(len(x))
print(3 in x)
for i in x:
    print(i, end=' ')
print()
for i in reversed(x):
    print(i, end=' ')
print()
print(x.index(1))
print(x.count(2))
