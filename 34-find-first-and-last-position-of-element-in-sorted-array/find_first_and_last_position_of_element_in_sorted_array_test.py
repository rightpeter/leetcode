#!/usr/bin/env python3

import unittest
from find_first_and_last_position_of_element_in_sorted_array import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([5, 7, 7, 8, 8, 10], 6), [-1, -1])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([], 6), [-1, -1])

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([6], 6), [0, 0])

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([6, 6], 6), [0, 1])

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([6, 7], 6), [0, 0])

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([6, 6], 5), [-1, -1])

    def test_8(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([6, 6, 6, 6, 6], 6), [0, 4])

    def test_9(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([2, 3, 6, 6, 6], 6), [2, 4])

    def test_10(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([6, 6, 6, 7, 9, 10], 6), [0, 2])

    def test_11(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([1, 2, 3], 2), [1, 1])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_11()
