from array import array


class ArrayList:

    def __init__(self, arr):
        if type(arr[0]) == int:
            self.myarr = array('i', arr)
        if type(arr[0]) == str:
            self.myarr = array('u', )
            for a in range(0, len(arr)):
                self.myarr.extend(arr[a])
        if type(arr[0]) == float:
            self.myarr = array('f', arr)

    def __len__(self):
        n = 0
        for a in self.myarr:
            n = n + 1
        return n

    def __count__(self, perem, ind):
        tmp = 0
        for a in range(0, self.__len__()):
            if type(perem) == float:
                if round(self.myarr[a], ind) == perem:
                    tmp = tmp + 1
            else:
                if self.myarr[a] == perem:
                    tmp = tmp + 1
        return tmp

    def __contains__(self, item):
        return item in self.myarr

    def __reversed__(self):
        return self.myarr[::-1]

    def __index__(self, item):
        for a in range(0, self.__len__()):
            if self.myarr[a] == item:
                return a

        return ValueError

    def __getitem__(self, item):
        if item > self.__len__():
            return TypeError
        else:
            return self.myarr[item]

    def __iter__(self):
        return self.myarr.__iter__()

    def __setitem__(self, key, value):
        self.myarr[key] = value

    def __delitem__(self, key):
        del self.myarr[key]

    def append(self,value):
        self.myarr += array(self.myarr.typecode, [value])

    def __clear__(self):
        for a in range(0, self.myarr.__len__()):
            del self.myarr[a]

    def pop(self, key):
        a = self.myarr[key]
        del self.myarr[key]
        return a

    def remove(self, value):
        for a in range(0, self.myarr.__len__()):
            if self.myarr[a] == value:
                del self.myarr[a]
                return
        return ValueError

    def __extend__(self, arr):
        for a in range(0,len(arr)):
            self.myarr += array(self.myarr.typecode, [arr[a]])

    def __insert__(self,key,value):
        arr = array(self.myarr.typecode)
        for a in range(0,key-1):
            arr.append(self.myarr[a])
        arr.append(value)
        for a in range(key,self.myarr.__len__()):
            arr.append(self.myarr[a])
        self.myarr = arr

    def reverse(self):
        arr = array(self.myarr.typecode,)
        arr.extend(self.myarr[::-1])
        self.myarr=arr









mas = (1, 2, 3, 0, 1, 1, 2, 1)
mas2 = (1.253, 2.4, 3.4, 4.4, 1.4, 1.2, 1.2)
mas1 = "hello World"
check = ArrayList(mas1)
# print(check.__len__())
# print(check.__count__(1,1))
# print(check.__contains__(1))
# print(check.__reversed__())
# print(check.__index__(1))
# check.__setitem__(0,8)
# print(check.__getitem__(0))
# check.__delitem__(0)
# print(check[0])
# print(check.__iter__())
# check.append("f")
# print(check[11])
# check.clear()
# print(check[0])
# print(check.pop(1))
# print(check[1])
# check.remove("h")
# print(check[0])
# mas3=" and you"
# # check.__extend__(mas3)
# # for a in range(check.__len__()):
# #     print(check[a])
# check.__insert__(0,"A")
# for a in range(check.__len__()):
#     print(check[a])
# print (check.__reversed__())