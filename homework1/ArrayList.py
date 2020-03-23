from array import *

class ArrayList():
    def __init__(self, *args):
        if args.__len__() == 0:
            self._RList = array('i',)
        else:
         if type(args[0]) == int:
            self._RList = array('i', args)
         elif type(args[0]) == float:
            self._RList = array('f', args)
         elif type(args[0]) == str:
            self._RList = array('u',)
            for item in args:
                self._RList += array('u', item)

    def __getitem__(self, index):
        return self._RList[index]

    def __contains__(self, item):
        if item in self._RList:
            return True
        else:
            return False

    def __iter__(self):
        return iter(self._RList)

    def __len__(self):
        count = 0
        for el in self._RList:
          count += 1
        return count

    def __reversed__(self):
        self.reverse()
        return self._RList

    def count(self, elem):
        amount = 0
        for el in self._RList:
          if(el == elem):
            amount += 1
        return amount

    def index(self, elem):
        for i, el in enumerate(self._RList):
          if(el == elem):
              pos = i
              return pos

    # Добавляем все элементы второго списка к элементам первого
    def extend(self, elem):
      if type(elem) == ArrayList:
         self._RList += elem._RList
      else:
        buf = ArrayList(elem)
        self._RList += buf._RList

    # Добавление нового элемента в конец []
    def append(self, elem):
        if type(elem) == int or type(elem) == float or type(elem) == str:
            buf = ArrayList(elem)
            self._RList += buf._RList
    # Удаление по значению
    def remove (self, elem):
        buf = self._RList
        self._RList = array(self._RList.typecode, )
        for el in buf:
            if el != elem:
                self.extend(el)

    def reverse(self):# Переворачивает
        buf = self._RList
        self._RList = array(self._RList.typecode,)
        size_of_buf = buf.__len__()
        for i, x in enumerate(buf):
            self.extend(buf[size_of_buf-i-1])

    # Удаление по индексу
    def pop(self, index):
        buf = self._RList
        self._RList = array(self._RList.typecode, )
        for i, el in enumerate(buf):
            if i != index:
                self.extend(el)

    def insert(self, index, elem):# вставляет новые/ый элемент/ты на указанное место
        buf_l = ArrayList()
        buf_r = ArrayList()
        if type(elem) is not list:
          if type(elem) == float:
             buf_l._RList = array('f',)
             buf_r._RList = array('f',)
          elif type(elem) == str:
             buf_l._RList = array('u', )
             buf_r._RList = array('u', )
        else:
            if type(elem[0]) == float:
                buf_l._RList = array('f', )
                buf_r._RList = array('f', )
            elif type(elem[0]) == str:
                buf_l._RList = array('u', )
                buf_r._RList = array('u', )
        for i, el in enumerate(self._RList):
            if i < index:
                buf_l.extend(el)
            elif i > index:
                buf_r.extend(el)
        self._RList = array(self._RList.typecode,)
        if index != 0:
            self.extend(buf_l)
            g = type(elem)
            if type(elem) == list or type(elem) == str or type(elem) == tuple:
                 for el in elem:
                    self.extend(el)
            else:
                 self.extend(el)
            self.extend(buf_r)
        else:
            if type(elem) == list or type(elem) == str or type(elem) == tuple:
                for el in elem:
                    self.extend(el)
            else:
                self.extend(el)
            self.extend(buf_r)

    def print(self):
        print(self._RList)
