from array import array
class Iterator: #additional class for __iter__()
    def __init__(self, collection):
        self.cursor = -1
        self._collection = collection
    def __next__(self,default=None):
        if self.cursor + 1 >= len(self._collection):
            self.cursor = -1
            raise StopIteration
        self.cursor +=1
        return self._collection[self.cursor]

types_dict = {int: 'i', str: 'u', float: 'd'} #matching dict
class ArrayList:
    def __init__(self,datatype,initializer=()):
        typecode = types_dict[datatype]
        for x in initializer:
            if type(x) != datatype:
                raise Exception("Wrong initializer datatype") #fixed
        self._arr = array(typecode, initializer)
        self._iterator = Iterator(self._arr)

    def __getitem__(self, key): #fixed (slice added) - working only for int type
        cls = type(self)
        if isinstance(key,slice):
            return cls(int,self._arr[key])
        elif isinstance(key,int):
            return self._arr[key]
        else:
            raise IndexError

    def __repr__(self):
        return f"{self._arr}"

    def __len__(self):
        return self._arr.buffer_info()[1] # buffer_info return a tuple (address, length)

    def __contains__(self, elem):
        for x in range(self.__len__()): #fixed
            if self._arr[x] == elem:
                return True

    def __iter__(self):
        return self._iterator
        # for i in range(self._arr.buffer_info()[1]):
        #     yield self._arr[i]

    def __reversed__(self):
        return self._arr[::-1]

    def __index__(self,item):
        for i, x in enumerate(self._arr):
            if x == item:
                return i

    def __count__(self, item):
        c = 0
        for x in self._arr:
            if x == item:
                c += 1
        return c



#int
print('int tests: ')
print()
a = ArrayList(int, (1,4,5,4,3,5,64,43,6))

print('slice test: ', a[0:3])
print('getitem test: ', a.__getitem__(3))
print('len test: ', a.__len__())
print('contains test: ', a.__contains__(64))
print('iter test: ')
for k in a:
    print(k, end=' ')
print()
print('reversed test: ')
print(a.__reversed__())
print('index test: ',a.__index__(64))
print('count test: ',a.__count__(4))

#str
print('str tests: ')
print()
a1 = ArrayList(str, ('x','y','z','x','z','p','q'))

print('getitem test: ', a1.__getitem__(3))
print('len test: ', a1.__len__())
print('contains test: ', a1.__contains__('x'))
print('iter test: ')
for k in a1:
    print(k, end=' ')
print()
print('reversed test: ')
print(a1.__reversed__())
print('index test: ',a1.__index__('q'))
print('count test: ',a1.__count__('x'))

#float
print('float tests: ')
print()
a2 = ArrayList(float, (1.1,1.2,1.3,1.4,1.4,1.5,1.2,1.7))

print('getitem test: ', a2.__getitem__(3))
print('len test: ', a2.__len__())
print('contains test: ', a2.__contains__(1.7))
print('iter test: ')
for k in a2:
    print(k, end=' ')
print()
print()
print('reversed test: ')
print(a2.__reversed__())
print('index test: ',a2.__index__(1.1))
print('count test: ',a2.__count__(1.4))
