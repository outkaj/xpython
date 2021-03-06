import unittest
import operator

from list_ops import *


class ListOpsTest(unittest.TestCase):

    # tests for map
    def test_map_square(self):
        self.assertEqual(
            (1, 4, 9, 16, 25, 36, 49, 64, 81, 100),
            tuple(map_clone(
                lambda x: x**2, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
            )
        )

    def test_map_cube(self):
        self.assertEqual(
            (-1, 8, -27, 64, -125, 216, -343, 512, -729, 1000),
            tuple(map_clone(
                lambda x: x**3, (-1, 2, -3, 4, -5, 6, -7, 8, -9, 10))
            )
        )

    def test_map_absolute(self):
        self.assertEqual(
            (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
            tuple(map_clone(
                lambda x: abs(x), (-1, 2, -3, 4, -5, 6, -7, 8, -9, 10))
            )
        )

    # tests for length
    def test_pos_leng(self):
        self.assertEqual(10, length((-1, 2, -3, 4, -5, 6, -7, 8, -9, 10)))

    def test_empty_len(self):
        self.assertEqual(0, length([]))

    # tests for filter
    def test_filter_odd(self):
        self.assertEqual(
            (1, 3, 5),
            tuple(filter_clone(lambda x: x % 2 != 0, [1, 2, 3, 4, 5, 6]))
        )

    def test_filter_even(self):
        self.assertEqual(
            (2, 4, 6),
            tuple(filter_clone(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
        )

    # tests for reverse
    def test_reverse_small(self):
        self.assertEqual([1, 2, 3], reverse([3, 2, 1]))

    def test_reverse_mixed_types(self):
        self.assertEqual(
            (1, "cat", 4.0, "xyz"),
            reverse(("xyz", 4.0, "cat", 1))
        )

    def test_reverse_empty(self):
        self.assertEqual([], reverse(()))

    # tests for append
    def test_append_tuple(self):
        self.assertEqual(
            ["10", "python", "hello"],
            append(["10", "python"], "hello")
        )

    def test_append_range(self):
        self.assertEqual([100, range(1000)], append([100], range(1000)))

    # tests for foldl
    def test_foldl_sum(self):
        self.assertEqual(21, foldl(operator.add, [1, 2, 3, 4, 5, 6], 0))

    def test_foldl_product(self):
        self.assertEqual(720, foldl(operator.mul, [1, 2, 3, 4, 5, 6], 1))

    def test_foldl_minus(self):
        self.assertEqual(-15, foldl(operator.sub, [1, 2, 3, 4, 5], 0))

    # tests for foldr
    def test_foldr_quotient(self):
        try:
            self.assertEqual(0, foldr(operator.floordiv, [1, 2, 3, 4, 5], 1))
        except ZeroDivisionError as e:
            pass

    def test_foldr_minus(self):
        self.assertEqual(
            3, foldr((lambda x, y: operator.sub(x, y)), (1, 2, 3, 4, 5), 0)
        )

    # tests for flatten
    def test_flatten_nested(self):
        self.assertEqual([1, 2, 3, 4], flat([[[1, 2], [3]], [[4]]]))

    def test_flatten_once(self):
        self.assertEqual(["x", "y", "z"], flat([["x", "y", "z"]]))

    # tests for concat
    def test_concat_two(self):
        self.assertEqual(
            [1, 3, 5, 8, 9, 4, 5, 6],
            concat([1, 3, 5, 8], [9, 4, 5, 6])
        )

    def test_concat_nothing(self):
        self.assertEqual(
            ["orange", "apple", "banana"],
            concat(['orange', 'apple', 'banana'], None)
        )

if __name__ == '__main__':
    unittest.main()
