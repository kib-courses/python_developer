from array import array


class ArrayList:

    def __init__(self, arr):
        if type(arr[0]) == int:
            self.myarr = array('i', arr)
            print("Hell yea!")
        if type(arr[0]) == str:
            self.myarr = array('u', )
            for a in range(0, len(arr)):
                self.myarr.extend(arr[a])
            print("Hell yea!")
        if type(arr[0]) == float:
            self.myarr = array('f', arr)
            print("Hell yea!")

    def __len__(self):
        n = 0
        for a in self.myarr:
            n = n + 1
        return n

    def __count__(self, perem,ind):
        tmp = 0
        for a in range(0, self.__len__()):
            if (type(perem) == float):
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
            if self.myarr[a]==item:
                return a

        return ValueError
    def __getitem__(self, item):
        if item > self.__len__():
            return TypeError
        else:
            return self.myarr[item]


mas = (1, 2, 3, 0, 1, 1, 1, 1)
mas2 = (1.253, 2.4, 3.4, 4.4, 1.4, 1.2, 1.2)
mas1 = "hello World"
check = ArrayList(mas)
print(check.__len__())
print(check.__count__(1,1))
print(check.__contains__(1))
print(check.__reversed__())
print(check.__index__(1))
print(check.__getitem__(6))