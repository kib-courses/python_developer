from array import array


class ArrayList:
    def __init__(self, type_list, data=[]):
        self.type = type_list
        if type_list == int:
            self.data = array('i', data)
        elif type_list == float:
            self.data = array('d', data)
        elif type_list == str:
            self.data = array('u', data)
        else:
            raise Exception

    def __str__(self):
        return str(list(self.data))
    # todo

    def __getitem__(self, index):
        stroka = ArrayList(self.type)
        if type(index) == slice:
            start = index.start
            stop = index.stop
            step = index.step
            if start == None:
                if step > 0:
                    start = 0
                else:
                    start = len(self.data) - 1
            if stop == None:
                if step > 0:
                    stop = len(self.data)
                else:
                    stop = 1185500000000000 # сюда очень большое число
            if step == None:
                step = 1
            if start < 0:
                start = len(self.data) + start
            if stop < 0:
                stop = len(self.data) + stop
            if stop == 1185500000000000:
                stop = -1
            if (step > 0 and start > stop):
                stroka.data = []
            elif (step < 0 and start < stop):
                stroka.data = []
            else:
                for i in range(start, stop, step):
                    if self.type == int:
                        dat = array('i', self[i].data)
                    elif self.type == float:
                        dat = array('d', self[i].data)
                    elif self.type == str:
                        dat = array('u', self[i].data)
                    stroka.data = stroka.data + dat
            return stroka
        else:
            stroka.data = [self.data[index]]
            return stroka

    def __len__(self):
        return len(self.data)

    def __contains__(self, element):
        # 'in' для array.array использовать нельзя
        for i in range(len(self.data)):
            if self.data[i] == element:
                return True
            elif i == len(self.data) - 1:
                return False
            else:
                pass

    def __iter__(self):
        return Iterator(self.data)

    def __reversed__(self):
        return iter(self[::-1])

    def index(self, element, start=0, end=None):
        if end is None:
            end = len(self.data)
        c = 0
        for i in range(start, end):
            if self.data[i] == element:
                return c
            else:
                c += 1
        raise Exception

    def count(self, element, start=0, end=None):
        count = 0
        if end is None:
            end = len(self.data)
        for i in range(start, end):
            if self.data[i] == element:
                count += 1
            else:
                continue
        return count



class Iterator:
    def __init__(self, arraylist):
        self.i = -1
        self.arraylist = arraylist

    def __next__(self):
        if self.i < len(self.arraylist) - 1:
            self.i += 1
            return self.arraylist[self.i]
        else:
            raise StopIteration

    def __iter__(self):
        return self


arraylist = ArrayList(int, range(0, 55, 6))
print(arraylist, '\n')
print(arraylist[4])
print(arraylist[3:6])
print(arraylist[::-1], '\n')
print(len(arraylist), '\n')
print(54 in arraylist)
print(634784 in arraylist, '\n')
print((ArrayList(int, reversed(arraylist))), '\n')
print(arraylist.index(42))
try:
    print(arraylist.index(34234))
except:
    print('error', '\n')
print(arraylist.count(42))
for i in arraylist:
    print(i)


