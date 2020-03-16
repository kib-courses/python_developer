from array import array


class Array:
    def __init__(self, *items):
        self.data = array('i', items)

    def __iter__(self):
        for i in range(len(self.data)):
            yield self.data[i]

    def __contains__(self, item):
        for i in range(len(self.data)):
            if self.data[i] == item:
                return True
            return False

    def __len__(self):
        return len(self.data)

    def __reversed__(self):
        for i in range(len(self.data)):
            yield self.data[len(self.data) - i - 1]

    def __getitem__(self, item):
        return self.data[item]

    def index(self, item):
        for i in range(len(self.data)):
            if self.data[i] == item:
                return i
        return -1

    def count(self, item):
        return sum([1 for i in self if i == item])

