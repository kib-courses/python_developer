from array import array


class Array_list:
    def __init__(self, *args):
        if not args:
            self.arr_type = None
            self.data = None
        elif (type(args[0]) == int):
            for i in args:
                if type(i) != int:
                    raise Exception("Wrong type of input data")
            self.arr_type = type(args[0])
            self.data = array('i', args)
        elif (type(args[0]) == float):
            for i in args:
                if type(i) != float:
                    raise Exception("Wrong type of input data")
            self.arr_type = type(args[0])
            self.data = array('d', args)
        elif (type(args[0]) == str):
            for i in args:
                if type(i) != str:
                    raise Exception("Wrong type of input data")
            self.arr_type = type(args[0])
            self.data = array('u', args)

    def __iter__(self):
        if self.data is not None:
            for i in range(self.data.buffer_info()[1]):
                yield self.data[i]

    def __len__(self):
        k = 0
        if self.data is not None:
            for i in self.data:
                k += 1
            return k
        return 0

    def __contains__(self, item):
        if self.data is None:
            raise Exception("Item does not exist")
        elif type(item) != self.arr_type:
            raise Exception("Wrong type of input data")
        return item in self.data

    def __getitem__(self, index):
        if self.data is None:
            raise Exception("Item does not exist")
        elif index >= len(self.data):
            raise Exception("Index out of range")
        return self.data[index]

    def __setitem__(self, index, item):
        if self.data is None:
            raise Exception("Item does not exist")
        elif type(item) != self.arr_type:
            raise Exception("Wrong type of input data")
        elif index >= len(self.data):
            raise Exception("Index out of range")
        self.data[index] = item

    def __reversed__(self):
        if self.data is not None:
            return self.data[::-1]

    def __delitem__(self, index):
        if self.data is None:
            raise Exception("Index does not exist")
        elif index >= len(self.data):
            raise Exception("Index out of range")
        del self.data[index]

    def __iadd__(self, other):
        if other.data is None:
            return self
        elif self.data is None:
            self.arr_type = other.arr_type
            self.data = other.data
            return self
        elif self.arr_type == type(other[0]):
            self.data = self.data + other.data
            return self
        else:
            raise Exception("Wrong type of input data")

    def index(self, item):
        if self.data is None:
            raise Exception("Item does not exist")
        elif type(item) != self.arr_type:
            raise Exception("Wrong type of input data")
        i = None
        for i, k in enumerate(self.data):
            if k == item:
                return i
        if i is None:
            raise Exception("Item does not exist")

    def count(self, item):
        if self.data is None:
            return 0
        elif type(item) != self.arr_type:
            raise Exception("Wrong type of input data")
        i = 0
        for k in self.data:
            if k == item:
                i += 1
        return i

    def append(self, item):
        if self.data is None:
            self.arr_type = type(item)
            if (type(item) == int):
                self.data = array('i', [item])
                return
            elif (type(item) == float):
                self.data = array('d', [item])
                return
            elif (type(item) == str):
                self.data = array('u', [item])
                return
        elif type(item) != self.arr_type:
            raise Exception("Wrong type of input data")
        else:
            self.data = self.data + Array_list(item).data
            return

    def clear(self):
        self.data = None
        self.arr_type = None
        return self

    def extend(self, other):
        return self.__iadd__(other)

    def pop(self, index):
        if self.data is None:
            raise Exception("Item does not exist")
        elif index >= len(self.data):
            raise Exception("Index out of range")
        x = self.data[index]
        del self.data[index]
        return x

    def remove(self, item):
        if self.data is None:
            raise Exception("Item does not exist")
        elif type(item) != self.arr_type:
            raise Exception("Wrong type of input data")
        else:
            i = None
            for i, k in enumerate(self.data):
                if k == item:
                    self.pop(i)
                    return
            if i is None:
                raise Exception("Item does not exist")
