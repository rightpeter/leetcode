#!/usr/bin/env python3

import unittest
from search_insert_position import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.searchInsert([1, 3, 5, 6], 5), 2)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.searchInsert([1, 3, 5, 6], 2), 1)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.searchInsert([1, 3, 5, 6], 7), 4)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.searchInsert([1, 3, 5, 6], 0), 0)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.searchInsert([], 112342), 0)

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.searchInsert([1], 1), 0)

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.searchInsert([1], 112342), 1)

    def test_8(self):
        sol = Solution()
        self.assertEqual(sol.searchInsert([1, 3], 0), 0)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_8()
