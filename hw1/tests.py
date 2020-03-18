import unittest
from source import ArrayList, array


class TestArray(unittest.TestCase):

    def test_creating(self):
        self.assertEqual(ArrayList('i').container, array('l'))
        self.assertEqual(ArrayList('u', 'hello \u2641').container,
                         array('u', 'hello \u2641'))
        self.assertEqual(ArrayList('i', [1, 2, 3, 4, 5]).container,
                         array('l', [1, 2, 3, 4, 5]))
        self.assertEqual(ArrayList('f', [1.0, 2.0, 3.14]).container,
                         array('f', [1.0, 2.0, 3.14]))

    def test_getitem(self):
        source_array = array('l', [1, 2, 3, 4, 5])
        our_class = ArrayList('i', [1, 2, 3, 4, 5])
        for x in range(5):
            self.assertEqual(our_class[x], source_array[x])

    def test_len(self):
        our_class = ArrayList('i', [1, 2, 3, 4, 5])
        self.assertEqual(len(our_class), 5)

    def test_contains(self):
        our_class = ArrayList('i', [1, 2, 3, 4, 5])
        self.assertEqual(3 in our_class, True)
        self.assertEqual(3.0 in our_class, False)
        self.assertEqual(-10 in our_class, False)

        class_str = ArrayList('u', 'hello \u2641')
        self.assertEqual(3 in class_str, False)
        self.assertEqual("h" in class_str, True)
        self.assertEqual("l" in class_str, True)


    def test_iter(self):
        source_array = array('l', [1, 2, 3, 4, 5])
        for idx, x in enumerate(ArrayList('i', [1, 2, 3, 4, 5])):
            self.assertEqual(x, source_array[idx])

    def test_reverse(self):
        reverse_array = array('l', [5, 4, 3, 2, 1])
        for idx, x in enumerate(reversed(ArrayList('i', [1, 2, 3, 4, 5]))):
            self.assertEqual(x, reverse_array[idx])

    def test_index(self):
        our_class = ArrayList('i', [1, 2, 3, 4, 5])
        self.assertEqual(our_class.index(2), 1)
        self.assertEqual(our_class.index("h"), None)
        self.assertEqual(our_class.index(-2), None)

        class_str = ArrayList('u', 'hello \u2641')
        self.assertEqual(class_str.index(3), None)
        self.assertEqual(class_str.index("h"), 0)
        self.assertEqual(class_str.index("l"), 2)

    def test_count(self):
        our_class = ArrayList('i', [1, 2, 3, 4, 5])
        self.assertEqual(our_class.count(2), 1)
        self.assertEqual(our_class.count("h"), None)
        self.assertEqual(our_class.count(-2), 0)

        class_str = ArrayList('u', 'hello \u2641')
        self.assertEqual(class_str.count(3), None)
        self.assertEqual(class_str.count("h"), 1)
        self.assertEqual(class_str.count("l"), 2)

if __name__ == "__main__":
    unittest.main()

