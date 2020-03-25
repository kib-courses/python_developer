import unittest

from array_list import ArrayList


class TestArrayListMethods(unittest.TestCase):
    def test_init(self):
        example_int = ArrayList(1, 2, 3)
        example_float = ArrayList(1.0, 2, 3)
        example_str = ArrayList("1", "2", "3")

        self.assertEqual(example_int.array_type, int)
        self.assertEqual(example_float.array_type, float)
        self.assertEqual(example_str.array_type, str)

        self.assertEqual(example_int.array[1], 2)
        self.assertEqual(example_float.array[1], 2.)
        self.assertEqual(example_str.array[1], "2")

        self.assertEqual(example_int.word_lengths, None)
        self.assertEqual(example_float.word_lengths, None)
        self.assertNotEqual(example_str.word_lengths, None)

    def test_get_item(self):
        example_int = ArrayList(-2, -1, 0, 1, 2)
        example_float = ArrayList(-2.0, -1, 0, 1.5, 2)
        example_str = ArrayList("$", "abc", "python", "class")

        self.assertEqual(example_int[1], -1)
        self.assertEqual(example_float[1], -1.)
        self.assertEqual(example_str[2], "python")

    def test_len(self):
        example_int = ArrayList(1, 2, 3, 4, 5)
        example_float = ArrayList(1., 2, 3, 4)
        example_str = ArrayList("str_1", "str_2", "str_3")

        self.assertEqual(len(example_int), 5)
        self.assertEqual(len(example_float), 4)
        self.assertEqual(len(example_str), 3)

    def test_contains(self):
        example_int = ArrayList(1, 2, 3, 4, 5)
        example_float = ArrayList(1., 2, 3, 4)
        example_str = ArrayList("str_1", "str_2", "str_3")

        self.assertTrue(5 in example_int)
        self.assertTrue(4. in example_float)
        self.assertTrue("str_3" in example_str)

        self.assertFalse(5.5 in example_int)
        self.assertFalse(4.4 in example_float)
        self.assertFalse("str" in example_str)

    def test_reversed(self):
        example_int = ArrayList(1, 2, 3, 4, 5)
        example_float = ArrayList(1., 2, 3, 4, 5)
        example_str = ArrayList("first", "second", "third")

        example_int.reverse()
        example_float.reverse()
        example_str.reverse()

        self.assertEqual(example_int[0], 5)
        self.assertEqual(example_float[0], 5.)
        self.assertEqual(example_str[0], "third")

    def test_count(self):
        example_int = ArrayList(1, 2, 1, 4, 1)
        example_float = ArrayList(1., 2, 2., 2, 2.)
        example_str = ArrayList("first", "$", "second", "$", "third", "$")

        self.assertEqual(example_int.count(1), 3)
        self.assertEqual(example_float.count(2), 4)
        self.assertEqual(example_str.count("$"), 3)

    def test_index(self):
        example_int = ArrayList(1, 2, 1, 4, 1)
        example_float = ArrayList(1., 2, 2., 2, 2.)
        example_str = ArrayList("first", "$", "second", "$", "third", "$")

        self.assertEqual(example_int.index(1), 0)
        self.assertEqual(example_int.index(4), 3)
        self.assertEqual(example_float.index(1), 0)
        self.assertEqual(example_float.index(2), 1)
        self.assertEqual(example_str.index("$"), 1)
        self.assertEqual(example_str.index("third"), 4)

        self.assertRaises(ValueError, example_int.index, 10)
        self.assertRaises(ValueError, example_float.index, 10)
        self.assertRaises(ValueError, example_str.index, "&")

    def test_set_item(self):
        example_int = ArrayList(1, 2, 3, 4, 5)
        example_float = ArrayList(1., 2, 3, 4, 5)
        example_str = ArrayList("first", "second", "third")

        example_int[0] = 10
        example_float[0] = 15.
        example_str[0] = "str"

        self.assertEqual(example_int[0], 10)
        self.assertEqual(example_float[0], 15)
        self.assertEqual(example_str[0], "str")

    def test_del_item(self):
        example_int = ArrayList(1, 2, 3, 4, 5)
        example_float = ArrayList(1., 2, 3, 4, 5)
        example_str = ArrayList("first", "second", "third")

        del example_int[2]
        del example_float[2]
        del example_str[1]

        self.assertEqual(example_int[2], 4)
        self.assertEqual(example_float[2], 4)
        self.assertEqual(example_str[1], "third")

    def test_insert(self):
        example_int = ArrayList(1, 2, 3, 4, 5)
        example_float = ArrayList(1., 2, 3, 4, 5)
        example_str = ArrayList("first", "second", "third")

        example_int.insert(2, 10)
        example_float.insert(2, 15.)
        example_str.insert(1, "$")

        self.assertEqual(example_int[2], 10)
        self.assertEqual(example_float[2], 15)
        self.assertEqual(example_str[1], "$")

    def test_iadd(self):
        example_int_1 = ArrayList(1, 2, 3)
        example_int_2 = ArrayList(4, 5, 6)
        example_float_1 = ArrayList(1., 2, 3)
        example_float_2 = ArrayList(4., 5, 6)
        example_str_1 = ArrayList("1", "2", "3")
        example_str_2 = ArrayList("4", "5", "6")

        example_int_1 += example_int_2
        example_float_1 += example_float_2
        example_str_1 += example_str_2

        self.assertEqual(len(example_int_1), 6)
        self.assertEqual(len(example_float_1), 6)
        self.assertEqual(len(example_str_1), 6)

        self.assertEqual(example_int_1[5], 6)
        self.assertEqual(example_float_1[5], 6)
        self.assertEqual(example_str_1[5], "6")

    def test_append(self):
        example_int = ArrayList(1, 2, 3)
        example_float = ArrayList(1., 2, 3)
        example_str = ArrayList("1", "2", "3")

        example_int.append(4)
        example_float.append(4.)
        example_str.append("4")

        self.assertEqual(example_int[3], 4)
        self.assertEqual(example_float[3], 4)
        self.assertEqual(example_str[3], "4")

    def test_clear(self):
        example = ArrayList(1, 2, 3)

        example.clear()

        self.assertIsNone(example.array)
        self.assertIsNone(example.word_lengths)
        self.assertIsNone(example.array_type)

    def test_extend(self):
        example_int = ArrayList(1, 2, 3)
        example_str = ArrayList("1", "2", "3")

        example_int.extend([4, 5, 6])
        example_str.extend(["4", "5", "6"])

        self.assertEqual(len(example_int), 6)
        self.assertEqual(len(example_str), 6)

        self.assertEqual(example_int[5], 6)
        self.assertEqual(example_str[5], "6")

    def test_pop(self):
        example_int = ArrayList(1, 2, 3)
        example_float = ArrayList(1., 2, 3)
        example_str = ArrayList("1", "2", "3")

        example_int.pop()
        example_float.pop()
        example_str.pop()

        self.assertEqual(len(example_int), 2)
        self.assertEqual(len(example_float), 2)
        self.assertEqual(len(example_str), 2)

        self.assertEqual(example_int[1], 2)
        self.assertEqual(example_float[1], 2)
        self.assertEqual(example_str[1], "2")

        example_int.pop(0)
        example_float.pop(0)
        example_str.pop(0)

        self.assertEqual(len(example_int), 1)
        self.assertEqual(len(example_float), 1)
        self.assertEqual(len(example_str), 1)

        self.assertEqual(example_int[0], 2)
        self.assertEqual(example_float[0], 2)
        self.assertEqual(example_str[0], "2")

    def test_remove(self):
        example_int = ArrayList(1, 2, 3)
        example_float = ArrayList(1., 2, 3)
        example_str = ArrayList("1", "2", "3")

        example_int.remove(2)
        example_float.remove(2)
        example_str.remove("2")

        self.assertEqual(len(example_int), 2)
        self.assertEqual(len(example_float), 2)
        self.assertEqual(len(example_str), 2)

        self.assertEqual(example_int[1], 3)
        self.assertEqual(example_float[1], 3)
        self.assertEqual(example_str[1], "3")

        self.assertRaises(ValueError, example_int.remove, 2)
        self.assertRaises(ValueError, example_float.remove, 2)
        self.assertRaises(ValueError, example_str.remove, "2")


if __name__ == '__main__':
    unittest.main()
