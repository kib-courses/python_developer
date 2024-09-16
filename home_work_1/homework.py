from array import array


class ArrayListIterator:
    def __init__(self, arraylist):
        self._arraylist = arraylist
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._arraylist):
            self._index += 1
            return self._arraylist[self._index - 1]
        else:
            raise StopIteration


class ArrayList:
    # ok
    def __init__(self, type_obj, init_list=list()):
        self.type = type_obj
        self.__type = self.__get_type_char()
        self.__arraylist = array(self.__get_type_char(), init_list)
        return

    # ok
    def __iter__(self):
        return ArrayListIterator(self)

    # ok
    def __str__(self):
        return str(list(self.__arraylist))

    # ok
    def __len__(self):
        return len(self.__arraylist)

    # ok
    def __getitem__(self, key):
        if type(key) == slice:

            start = key.start if key.start is not None else 0
            start = start if start >= 0 else start+len(self)
            stop = key.stop if key.stop is not None else len(self)
            stop = stop if stop >= 0 else stop + len(self)
            step = key.step if key.step is not None else 1

            if step < 0:
                start, stop = stop-1, start-1

            arraylist = list()
            for ix in range(start, stop, step):
                arraylist.append(self.__arraylist[ix])

            return ArrayList(self.type, arraylist)

        return self.__arraylist[key]

    # ok
    def __setitem__(self, key, value):
        self.__arraylist[key] = value
        return

    # ok
    def __contains__(self, item):
        for ix in range(len(self)):
            if self[ix] == item:
                return True
        return False

    #ok
    def __reversed__(self):
        return iter(self[::-1])

    # ok
    def __iadd__(self, other):
        self.__arraylist = self.__arraylist + other.__arraylist
        return self

    # ok
    def __delitem__(self, key):
        if key != -1:
            self.__arraylist = self[:key].__arraylist + self[key+1:].__arraylist
        else:
            self.__arraylist = self[:key].__arraylist
        return

    # ok
    def index(self, x, start=0, stop=None):
        if not stop:
            end = len(self)

        for ix, elem in enumerate(self[start:stop]):
            if x == elem:
                return ix + start

        raise ValueError(f'{x} not in ArrayList')

    # ok
    def count(self, value):
        count = 0
        for elem in self:
            if elem == value:
                count += 1
        return count

    # ok
    def append(self, append_val):
        self.__arraylist = self.__arraylist + array(self.__type, [append_val])
        return

    # ok
    def insert(self, index, value):
        self.__arraylist = self[:index].__arraylist + array(self.__type, [value]) + self[index:].__arraylist
        return

    # ok
    def extend(self, iterable):
        arraylist = array(self.__type, iterable)
        self.__arraylist = self.__arraylist + arraylist
        return

    # ok
    def pop(self, index=-1):
        return_val = self[index]
        del self[index]
        return return_val

    # ok
    def remove(self, value):
        del_ix = -1
        for ix in range(0, len(self.__arraylist)):
            if self.__arraylist[ix] == value:
                del_ix = ix
                break
        if del_ix >= 0:
            del self[del_ix]
            return
        else:
            raise ValueError(f'{value} not in ArrayList')

    # ok
    def reverse(self):
        self.__arraylist = self[::-1].__arraylist
        return

    def __get_type_char(self):
        if self.type == float:
            return 'd'
        if self.type == str:
            return 'u'
        if self.type == int:
            return 'i'
        else:
            raise TypeError('Wrong type')



if __name__ == '__main__':

    # int

    arraylist_1 = ArrayList(int, [-1])
    arraylist_2 = ArrayList(int, [1, 2, 3])

    # test __str__
    print('test __str__ (arraylist_1):',arraylist_1)
    print('test __str__ (arraylist_2):', arraylist_2, '\n')

    # test __len__
    print('array: ', arraylist_1)
    print('test __len__:', len(arraylist_1))
    print('array: ', arraylist_2)
    print('test __len__ (arraylist_2):', len(arraylist_2), '\n')

    # test __getitem__
    print('array', arraylist_2)
    print('test __getitem__ [0]:', arraylist_2[0])
    print('test __getitem__ [-2]:', arraylist_2[-2])
    print('test __getitem__ [1:3:-1]:', arraylist_2[1:3:-1])
    print('test __getitem__ [::-2]:', arraylist_2[::-2])
    print('test __getitem__ [::-1]:', arraylist_2[::-1], '\n')

    # test __setitem__
    print('array:', arraylist_2)
    arraylist_2[0] = 32
    arraylist_2[-2] = 56
    print('test __setitem__ ([0] = 32) ([-2] = 56):', arraylist_2, '\n')

    # test __contains__
    print('array', arraylist_2)
    print('test __contains__ (56):', 56 in arraylist_2)
    print('test __contains__ (132):', 132 in arraylist_2, '\n')

    # test __reversed__
    print('array', arraylist_2)
    print('test __reversed__ (type):', reversed(arraylist_2))
    print('test __reversed__ (ArrayList):', ArrayList(int, reversed(arraylist_2)), '\n')

    # test __iter__
    print('array: ', arraylist_2)
    print('test __iter__ (return):', iter(arraylist_2))
    print('for:')
    for elem in arraylist_2:
        print(elem)
    print('\n')

    # test __iadd__
    print('arrays', arraylist_1, '+', arraylist_2)
    arraylist_1 += arraylist_2
    print('test __iadd__:', arraylist_1, '\n')

    # test __delitem__
    print('array', arraylist_1)
    del arraylist_1[1]
    print('test __delitem__ [1]:', arraylist_1)
    del arraylist_1[-2]
    print('test __delitem__ [-2]:', arraylist_1, '\n')

    # test index
    print('array', arraylist_2)
    print('test index (56):', arraylist_2.index(56))
    try:
        print('test index (431):', arraylist_2.index(431), '\n')
    except:
        print('test index (431): error', '\n')

    # test append
    print('array', arraylist_2)
    arraylist_2.append(32)
    arraylist_2.append(56)
    arraylist_2.append(32)
    print('test append (32) (56) (32): ', arraylist_2, '\n')

    # test count
    print('array', arraylist_2)
    print('test count (32): ', arraylist_2.count(32), '\n')

    # test insert
    print('array', arraylist_2)
    arraylist_2.insert(5, 987)
    print('test insert (5, 987): ', arraylist_2)
    arraylist_2.insert(-5, 7647)
    print('test insert (-5, 7647): ', arraylist_2, '\n')

    # test extend
    print('arrays', arraylist_2, 'extend', arraylist_1)
    arraylist_2.extend(arraylist_1)
    print('test extend: ', arraylist_2)
    print('arrays', arraylist_1, 'extend', [34, 23, 76])
    arraylist_1.extend([34, 23, 76])
    print('test extend: ', arraylist_1, '\n')

    # test pop
    print('array', arraylist_2)
    print('test pop (): ', arraylist_2.pop())
    print('array', arraylist_2)
    print('test pop (-2): ', arraylist_2.pop(-2))
    print('array', arraylist_2)
    print('test pop (4): ', arraylist_2.pop(4))
    print('array', arraylist_2, '\n')

    # test remove
    print('array', arraylist_2)
    arraylist_2.remove(7647)
    print('test remove (7647)', arraylist_2)
    arraylist_2.remove(-1)
    print('test remove (-1)', arraylist_2)
    try:
        arraylist_2.remove(4567)
        print('test remove (4567)', arraylist_2)
    except:
        print('test remove (4567): error', '\n')

    # test reverse
    print('array', arraylist_1)
    arraylist_1.reverse()
    print('test reverse', arraylist_1, '\n')

    # todo float

    arraylist_1 = ArrayList(float)
    arraylist_2 = ArrayList(float, [-3.6, 2.3, -1.1])

    # test __str__
    print('test __str__ (arraylist_1):', arraylist_1)
    print('test __str__ (arraylist_2):', arraylist_2, '\n')

    # test __len__
    print('array: ', arraylist_1)
    print('test __len__:', len(arraylist_1))
    print('array: ', arraylist_2)
    print('test __len__ (arraylist_2):', len(arraylist_2), '\n')

    # test __getitem__
    print('array', arraylist_2)
    print('test __getitem__ [0]:', arraylist_2[0])
    print('test __getitem__ [-2]:', arraylist_2[-2])
    print('test __getitem__ [1:3:-1]:', arraylist_2[1:3:-1])
    print('test __getitem__ [::-2]:', arraylist_2[::-2])
    print('test __getitem__ [1:3]:', arraylist_2[1:3], '\n')

    # test __setitem__
    print('array:', arraylist_2)
    arraylist_2[0] = 32.982
    arraylist_2[-2] = 56.542
    print('test __setitem__ ([0] = 32.982) ([-2] = 56.542):', arraylist_2, '\n')

    # test __contains__
    print('array', arraylist_2)
    print('test __contains__ (56.542):', 56.542 in arraylist_2)
    print('test __contains__ (-1.1):', -1.1 in arraylist_2)
    print('test __contains__ (132.890):', 132.890 in arraylist_2, '\n')

    # test __reversed__
    print('array', arraylist_2)
    print('test __reversed__ (type):', reversed(arraylist_2))
    print('test __reversed__ (ArrayList):', ArrayList(float, reversed(arraylist_2)), '\n')

    # test __iter__
    print('array: ', arraylist_2)
    print('test __iter__ (return):', iter(arraylist_2))
    print('for:')
    for elem in arraylist_2:
        print(elem)
    print('\n')

    # test __iadd__
    print('arrays', arraylist_1, '+', arraylist_2)
    arraylist_1 += arraylist_2
    print('test __iadd__:', arraylist_1, '\n')

    # test __delitem__
    print('array', arraylist_1)
    del arraylist_1[1]
    print('test __delitem__ [1]:', arraylist_1)
    del arraylist_1[-2]
    print('test __delitem__ [-2]:', arraylist_1, '\n')

    # test index
    print('array', arraylist_2)
    print('test index (56.542):', arraylist_2.index(56.542))
    try:
        print('test index (431):', arraylist_2.index(431.523), '\n')
    except:
        print('test index (431): error', '\n')

    # test append
    print('array', arraylist_2)
    arraylist_2.append(32.982)
    arraylist_2.append(56.678)
    arraylist_2.append(32.982)
    print('test append (32.982) (56.678) (32.982): ', arraylist_2, '\n')

    # test count
    print('array', arraylist_2)
    print('test count (32.982): ', arraylist_2.count(32.982), '\n')

    # test insert
    print('array', arraylist_2)
    arraylist_2.insert(5, 987.34234)
    print('test insert (5, 987): ', arraylist_2)
    arraylist_2.insert(-5, 7647.423623554)
    print('test insert (-5, 7647): ', arraylist_2, '\n')

    # test extend
    print('arrays', arraylist_2, 'extend', arraylist_1)
    arraylist_2.extend(arraylist_1)
    print('test extend: ', arraylist_2)
    print('arrays', arraylist_1, 'extend', [34.4134, 23.134, 76.23986])
    arraylist_1.extend([34.4134, 23.134, 76.23986])
    print('test extend: ', arraylist_1, '\n')

    # test pop
    print('array', arraylist_2)
    print('test pop (): ', arraylist_2.pop())
    print('array', arraylist_2)
    print('test pop (-2): ', arraylist_2.pop(-2))
    print('array', arraylist_2)
    print('test pop (4): ', arraylist_2.pop(4))
    print('array', arraylist_2, '\n')

    # test remove
    print('array', arraylist_2)
    arraylist_2.remove(7647.423623554)
    print('test remove (7647.423623554)', arraylist_2)
    try:
        arraylist_2.remove(4567.6356)
        print('test remove (4567.6356)', arraylist_2)
    except:
        print('test remove (4567.6356): error', '\n')

    # test reverse
    print('array', arraylist_1)
    arraylist_1.reverse()
    print('test reverse', arraylist_1, '\n')

    # str

    arraylist_1 = ArrayList(str)
    arraylist_2 = ArrayList(str, ['e', 'h', '3'])

    # test __str__
    print('test __str__ (arraylist_1):', arraylist_1)
    print('test __str__ (arraylist_2):', arraylist_2, '\n')

    # test __len__
    print('array: ', arraylist_1)
    print('test __len__:', len(arraylist_1))
    print('array: ', arraylist_2)
    print('test __len__ (arraylist_2):', len(arraylist_2), '\n')

    # test __getitem__
    print('array', arraylist_2)
    print('test __getitem__ [0]:', arraylist_2[0])
    print('test __getitem__ [-2]:', arraylist_2[-2])
    print('test __getitem__ [1:3:-1]:', arraylist_2[1:3:-1])
    print('test __getitem__ [::-2]:', arraylist_2[::-2])
    print('test __getitem__ [1:3]:', arraylist_2[1:3], '\n')

    # test __setitem__
    print('array:', arraylist_2)
    arraylist_2[0] = 'o'
    arraylist_2[-2] = 'r'
    print('test __setitem__ ([0] = "o") ([-2] = "r"):', arraylist_2, '\n')

    # test __contains__
    print('array', arraylist_2)
    print('test __contains__ ("r"):', "r" in arraylist_2)
    print('test __contains__ ("q"):', "q" in arraylist_2, '\n')

    # test __reversed__
    print('array', arraylist_2)
    print('test __reversed__ (type):', reversed(arraylist_2))
    print('test __reversed__ (ArrayList):', ArrayList(str, reversed(arraylist_2)), '\n')

    # test __iter__
    print('array: ', arraylist_2)
    print('test __iter__ (return):', iter(arraylist_2))
    print('for:')
    for elem in arraylist_2:
        print(elem)
    print('\n')

    # test __iadd__
    print('arrays', arraylist_1, '+', arraylist_2)
    arraylist_1 += arraylist_2
    print('test __iadd__:', arraylist_1, '\n')

    # test __delitem__
    print('array', arraylist_1)
    del arraylist_1[1]
    print('test __delitem__ [1]:', arraylist_1)
    del arraylist_1[-2]
    print('test __delitem__ [-2]:', arraylist_1, '\n')

    # test index
    print('array', arraylist_2)
    print('test index ("3"):', arraylist_2.index("3"))
    try:
        print('test index ("["):', arraylist_2.index("["), '\n')
    except:
        print('test index ("["): error', '\n')

    # test append
    print('array', arraylist_2)
    arraylist_2.append("8")
    arraylist_2.append("u")
    arraylist_2.append("3")
    print('test append ("8") ("u") ("3"): ', arraylist_2, '\n')

    # test count
    print('array', arraylist_2)
    print('test count ("3"): ', arraylist_2.count("3"), '\n')

    # test insert
    print('array', arraylist_2)
    arraylist_2.insert(5, "e")
    print('test insert (5, "e"): ', arraylist_2)
    arraylist_2.insert(-5, "n")
    print('test insert (-5, "n"): ', arraylist_2, '\n')

    # test extend
    print('arrays', arraylist_2, 'extend', arraylist_1)
    arraylist_2.extend(arraylist_1)
    print('test extend: ', arraylist_2)
    print('arrays', arraylist_1, 'extend', ['k', 'o', 's'])
    arraylist_1.extend(ArrayList(str, ['k', 'o', 's']))
    print('test extend: ', arraylist_1, '\n')

    # test pop
    print('array', arraylist_2)
    print('test pop (): ', arraylist_2.pop())
    print('array', arraylist_2)
    print('test pop (-2): ', arraylist_2.pop(-2))
    print('array', arraylist_2)
    print('test pop (4): ', arraylist_2.pop(4))
    print('array', arraylist_2, '\n')

    # test remove
    print('array', arraylist_2)
    arraylist_2.remove('o')
    print('test remove ("o")', arraylist_2)
    try:
        arraylist_2.remove("w")
        print('test remove ("w")', arraylist_2)
    except:
        print('test remove ("w"): error', '\n')

    # test reverse
    print('array', arraylist_1)
    arraylist_1.reverse()
    print('test reverse', arraylist_1)


















