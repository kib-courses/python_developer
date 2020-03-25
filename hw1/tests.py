import unittest
from ArrayList import ArrayList


class ArrayListTests(unittest.TestCase):

    def test_init(self):
        # array of int's:
        int_arr = ArrayList('i', *range(-10, 10))

        self.assertEqual(len(int_arr), 20)

        self.assertEqual(int_arr[0], -10)
        self.assertEqual(int_arr[-len(int_arr)], -10)

        self.assertEqual(int_arr.reverse()[0], 9)
        self.assertEqual(int_arr.reverse()[-len(int_arr)], 9)

        # array of char's:
        ch_arr = ArrayList('u', *list('Hello'))

        self.assertEqual(len(ch_arr), len('Hello'))

        self.assertEqual(ch_arr[0], 'H')
        self.assertEqual(ch_arr[-len(ch_arr)], 'H')

        self.assertEqual(''.join(ch_arr.reverse()), 'olleH')

    def test_elem_changing(self):
        # array of int's:
        int_arr = ArrayList('i', *range(-10, 10))

        int_arr[0] = -228
        self.assertEqual(int_arr[0], -228)

        self.assertEqual(int_arr.count(-228), 1)
        self.assertEqual(int_arr.count(-10), 0)

        int_arr.remove(-228)
        self.assertEqual(len(int_arr), 19)
        self.assertEqual(int_arr[0], -9)

        int_arr = ArrayList('i', *range(5))
        int_arr = int_arr.extend(ArrayList('i', *range(5, 10)))

        self.assertEqual(len(int_arr), 10)
        self.assertEqual((int_arr[0], int_arr[-1]), (0, 9))

        # array of char's:
        ch_arr = ArrayList('u', *list('Hello'))

        ch_arr.remove('H')
        self.assertEqual(ch_arr[0], 'e')

        ch_arr = ArrayList('u', *list('H')) + ch_arr
        self.assertEqual(ch_arr[0], 'H')
        self.assertEqual(''.join(ch_arr), 'Hello')

    def test_other_features(self):
        # array of int's:
        int_arr = ArrayList('i', *range(-10, 10))

        self.assertEqual(list(reversed(int_arr)),
                         list(reversed(range(-10, 10))))

        self.assertEqual(int_arr.pop(0), -10)
        self.assertEqual(len(int_arr), 19)

        del int_arr[int_arr.index(0)]
        self.assertEqual(0 in int_arr, False)
        self.assertEqual(len(int_arr), 18)

        int_arr.clear()
        self.assertEqual(len(int_arr), 0)


if __name__ == '__main__':
    unittest.main()
