import unittest
# import List
from List import List


class TestCase(unittest.TestCase):
    def test_int(self):
        list = List('i', 1, 2, 3, 1, 8, 9)
        self.assertEqual(6, len(list))
        self.assertEqual(3, list[2])
        self.assertEqual(True, 8 in list)
        self.assertEqual(False, 0 in list)
        list2 = List('i', 1, 2)
        self.assertEqual(True, list2 < list)
        self.assertEqual(False, list2 > list)
        list3 = list2 * 4
        self.assertEqual(True, list3 > list)
        self.assertEqual(False, list3 < list)
        self.assertEqual(2, len(list2))

        self.assertEqual(False, list2 == list3)
        self.assertEqual(True, list2 != list)

        list.append(0)
        self.assertEqual(0, list.pop())

        self.assertEqual(2, list.count(1))
        self.assertEqual(0, list.count(0))

        list.extend([4, 5, 3])
        self.assertEqual(5, list.pop(7))

        list.insert(0, 6)
        self.assertEqual(6, list[0])

        list[0] = 0
        self.assertEqual(0, list[0])

        list.remove(2)
        self.assertEqual(False, 2 in list)

        list2.__reversed__()
        self.assertEqual(2, list2[0])
        self.assertEqual(1, list2[1])

        list3.clear()
        self.assertEqual(0, len(list3))

    def test_char(self):
        list = List('u', '1', '2', '3')
        self.assertEqual(3, len(list))
        list.append('4')
        self.assertEqual('4', list.pop())
        list.extend("892")
        self.assertEqual(6, len(list))
        self.assertEqual('8', list[3])


if __name__ == '__main__':
    unittest.main()
