import unittest
from ArrayList import ArrayList

'''
Реализовать свой домашний ArrayList
В отличии от стандартного списка, ваш должен быть типизированным.
Для проходного балла - класс должен реализовать протокол Sequence
Для мотивированных и любопытных - класс должен реализовать протокол MutableSequence

Каждый метод из протокола должен быть проверен.

ДЗ - нужно сделать форк от нашего репозитория и прислать в Slack ссылку на Pull Request

Hint 1 - изучите плоский массив: array.array, внутреннее хранение должно быть на нем.
Hint 2 - наследование от классов из collections.abc не лопускается!

array:
       Type code   C Type             Minimum size in bytes
        'b'         signed integer     1
        'B'         unsigned integer   1
        'u'         Unicode character  2 (see note)
        'h'         signed integer     2
        'H'         unsigned integer   2
        'i'         signed integer     2
        'I'         unsigned integer   2
        'l'         signed integer     4
        'L'         unsigned integer   4
        'q'         signed integer     8 (see note)
        'Q'         unsigned integer   8 (see note)
        'f'         floating point     4
        'd'         floating point     8

("['__add__', '__class__', '__contains__', '__copy__', '__deepcopy__', "
 "'__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', "
 "'__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', "
 "'__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', "
 "'__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', "
 "'__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__setitem__', "
 "'__sizeof__', '__str__', '__subclasshook__', 'append', 'buffer_info', "
 "'byteswap', 'count', 'extend', 'frombytes', 'fromfile', 'fromlist', "
 "'fromstring', 'fromunicode', 'index', 'insert', 'itemsize', 'pop', 'remove', "
 "'reverse', 'tobytes', 'tofile', 'tolist', 'tostring', 'tounicode', "
 "'typecode']")

list:
("['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', "
 "'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', "
 "'__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', "
 "'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', "
 "'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', "
 "'__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', "
 "'__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', "
 "'index', 'insert', 'pop', 'remove', 'reverse', 'sort']")

'''

class TestStringMethods(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        self.arri = ArrayList('i')
        self.arrf = ArrayList('f')
        self.arru = ArrayList('u')
        super().__init__(methodName)

    def test_append(self):
        self.arri.append(1)
        self.assertEqual(self.arri[0], 1)
        self.assertEqual(type(self.arri), ArrayList)
        self.assertEqual(type(self.arri[0]), int)
        self.assertTrue(isinstance(self.arri, ArrayList))

        with self.assertRaises(Exception):
            self.arri.append('a')

    def test_insert(self):
        self.arri.append(1)

        self.arri.insert(2, 3)
        self.assertEqual(self.arri[1], 3)

        self.arri.insert(121, 56)
        self.assertEqual(self.arri[2], 56)

        self.arri.insert(-21, -1)
        self.assertEqual(self.arri[0], -1)

        with self.assertRaises(Exception):
            self.arri.insert(-2123, 'a')

    def test_count(self):
        self.arri.append(1)
        self.arri.insert(2, 3)
        self.arri.insert(121, 56)
        self.arri.insert(-21, -1)
        self.arri.append(1)

        self.assertEqual(self.arri.count(-1), 1)
        self.assertEqual(self.arri.count(1), 2)

    def test_reverse(self):
        self.arri.append(1)
        self.arri.insert(2, 3)
        self.arri.insert(121, 56)
        self.arri.insert(-21, -1)
        self.arri.append(8)

        self.arri.reverse()

        arr = ArrayList('i')
        arr.append(8)
        arr.append(56)
        arr.append(3)
        arr.append(1)
        arr.append(-1)

        self.assertTrue(self.arri.array == arr.array)

    def test_remove(self):
        self.arri.append(1)
        self.arri.insert(2, 3)
        self.arri.insert(121, 56)
        self.arri.insert(-21, -1)
        self.arri.append(8)
        self.arri.append(1)

        self.arri.remove(-1)
        self.arri.remove(1)

        self.assertEqual(self.arri.count(-1), 0)
        self.assertEqual(self.arri.count(1), 1)

    def test_pop(self):
        self.arri.append(1)
        self.arri.insert(2, 3)
        self.arri.insert(121, 56)
        self.arri.insert(-21, -1)
        self.arri.append(8)
        self.arri.append(1)

        a = self.arri.pop(0)
        self.assertEqual(a, -1)

        a = self.arri.pop(-1)
        self.assertEqual(a, 1)

        a = self.arri.pop(1)
        self.assertEqual(a, 3)

    def test_index(self):
        self.arri.append(1)
        self.arri.insert(2, 3)
        self.arri.insert(121, 56)
        self.arri.insert(-21, -1)
        self.arri.append(8)
        self.arri.append(1)

        self.assertEqual(self.arri.index(1), 1)

    def test_extend(self):
        arr = ArrayList('i')
        arr.append(8)
        arr.append(56)

        self.arri.append(8)
        self.arri.append(1)
        self.arri.extend(arr)

        tmp = ArrayList('i')
        tmp.append(8)
        tmp.append(1)
        tmp.append(8)
        tmp.append(56)

        self.assertEqual(self.arri.array, tmp.array)

if __name__ == '__main__':
    unittest.main()