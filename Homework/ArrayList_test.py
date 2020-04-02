import unittest
# import List
from ArrayList import ArrayList
from collections import abc
from sys import getsizeof


class TestCase(unittest.TestCase):
    def test_init_and_len(self):
        # Увы, обычного теста на невылеты нет, так что пусть будет так
        list0 = ArrayList('i')
        list1 = ArrayList('i', 1, 2, 3, 1, 8, 9)
        list2 = ArrayList('u', '1', '2', '3')
        list3 = ArrayList('d', 1.1, 2.2, 3.3, 4.4, 5.5)

        self.assertEqual(len(list0), 0)
        self.assertEqual(len(list1), 6)
        self.assertEqual(len(list2), 3)
        self.assertEqual(len(list3), 5)

    def test_to_string(self):
        list1 = ArrayList('i', 1, 2, 3, 1, 8, 9)
        self.assertEqual(str(list1), "array('i', [1, 2, 3, 1, 8, 9])")

        list2 = ArrayList('u', '1', '2', '3')
        self.assertEqual(str(list2), "array('u', '123')")

    def test_contains(self):
        list1 = ArrayList('i', 1, 2, 3, 1, 8, 9)
        self.assertTrue(2 in list1)
        self.assertFalse(0 in list1)

        list2 = ArrayList('u', '1', '2', '3')
        self.assertTrue('2' in list2)
        self.assertFalse('0' in list2)

    def test_add_iadd(self):
        list1 = ArrayList('i', 1, 2, 3, 1, 8, 9)
        list01 = ArrayList('i', 0, 0, 0)

        self.assertEqual(ArrayList('i', 1, 2, 3, 1, 8, 9, 0, 0, 0), list1 + list01)
        self.assertEqual(ArrayList('i', 1, 2, 3, 1, 8, 9), list1)
        self.assertEqual(ArrayList('i', 0, 0, 0), list01)

        list01 += list1

        self.assertEqual(ArrayList('i',  0, 0, 0, 1, 2, 3, 1, 8, 9), list01)
        self.assertEqual(ArrayList('i', 1, 2, 3, 1, 8, 9), list1)

    def test_ordering(self):
        list0 = ArrayList('i')
        list10 = ArrayList('i', 1, 2, 3, 1, 8, 9)
        list11 = ArrayList('i', 1, 2, 3, 1, 8, 9)
        list20 = ArrayList('i', 1, 2, 3)
        list21 = ArrayList('i', 1, 2, 4)
        list3 = ArrayList('i', 1, 2, 3, 4, 5, 6, 7, 8, 9)

        self.assertTrue(list10 == list11)
        self.assertTrue(list10 >= list11)
        self.assertTrue(list10 <= list11)

        self.assertTrue(list10 > list0)
        self.assertFalse(list10 <= list0)

        self.assertTrue(list10 < list3)
        self.assertTrue(list20 < list21)

        self.assertTrue(list10 != list0)
        self.assertTrue(list20 != list0)
        self.assertTrue(list21 != list10)
        self.assertTrue(list3 != list10)

        self.assertFalse(list10 != list11)

    def test_mul_imul(self):
        list0 = ArrayList('i', 0, 0, 0)
        mult = 2

        self.assertEqual(ArrayList('i', 0, 0, 0, 0, 0, 0), list0 * mult)
        self.assertEqual(ArrayList('i', 0, 0, 0), list0)
        self.assertEqual(mult, 2)

        mult = 3
        list0 *= mult

        self.assertEqual(ArrayList('i', 0, 0, 0, 0, 0, 0, 0, 0, 0), list0)
        self.assertEqual(mult, 3)

    def test_append(self):
        list0 = ArrayList('i', 0, 0, 0)
        list0.append(1)

        self.assertEqual(ArrayList('i', 0, 0, 0, 1), list0)

        list0.append(2)

        self.assertEqual(ArrayList('i', 0, 0, 0, 1, 2), list0)

    def test_count(self):
        list0 = ArrayList('i', 0, 0, 0, 1)

        self.assertEqual(list0.count(0), 3)
        self.assertEqual(list0.count(1), 1)

        self.assertEqual(list0.count(25), 0)

    def test_index(self):
        list0 = ArrayList('i', 0, 0, 0, 1)

        self.assertEqual(list0.index(0), 0)
        self.assertEqual(list0.index(1), 3)

        with self.assertRaises(ValueError):
            list0.index(25)

    def test_extend(self):
        list0 = ArrayList('i', 0, 0, 0, 1)

        list0.extend([1, 2, 3])

        self.assertEqual(list0, ArrayList('i', 0, 0, 0, 1, 1, 2, 3))

    def test_insert(self):
        list0 = ArrayList('i', 0, 0, 0)
        list0.insert(1, 1)

        self.assertEqual(list0, ArrayList('i', 0, 1, 0, 0))

        list0.insert(-1, 1)
        self.assertEqual(list0, ArrayList('i', 0, 1, 0, 0, 1))

        list0.insert(-2, 2)
        self.assertEqual(list0, ArrayList('i', 0, 1, 0, 0, 2, 1))

    def test_iterable(self):
        list0 = ArrayList('i', 0, 1, 2)
        for i, e in enumerate(list0):
            self.assertEqual(i, e)

        list1 = ArrayList('i', 0)
        iterator = iter(list1)

        self.assertEqual(next(iterator), 0)

        list1.append(2)

        self.assertEqual(next(iterator), 2)

        with self.assertRaises(StopIteration):
            next(iterator)

    def test_pop(self):
        list0 = ArrayList('i', 0, 1, 2)

        self.assertEqual(list0.pop(), 2)
        self.assertEqual(list0, ArrayList('i', 0, 1))

        self.assertEqual(list0.pop(0), 0)
        self.assertEqual(list0, ArrayList('i', 1))

    def test_reverse(self):
        list0 = ArrayList('i', 3, 2, 1, 0)
        i = 0
        for e in reversed(list0):
            self.assertEqual(e, i)
            i += 1

    def test_remove(self):
        list0 = ArrayList('i', 3, 2, 1, 0)
        list0.remove(2)

        self.assertEqual(list0, ArrayList('i', 3, 1, 0))

    def test_del(self):
        list0 = ArrayList('i', 3, 2, 1, 0)
        del list0[0]

        self.assertEqual(list0, ArrayList('i', 2, 1, 0))

    def test_is_dz_done(self):
        my_array_list = ArrayList('i')
        self.assertTrue(isinstance(my_array_list, abc.Reversible))
        self.assertTrue(isinstance(my_array_list, abc.Collection))

        #self.assertTrue(isinstance(my_array_list, abc.Sequence))
        #self.assertTrue(isinstance(my_array_list, abc.MutableSequence))


def execute_tests():
    unittest.main()
        
if __name__ == '__main__':
    execute_tests()