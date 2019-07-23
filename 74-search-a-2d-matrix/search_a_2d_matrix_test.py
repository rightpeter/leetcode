#!/usr/bin/env python3

import unittest
from search_a_2d_matrix import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3), True)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 13), False)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 0), False)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 51), False)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.searchMatrix([], 51), False)

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.searchMatrix([[1], [5], [8], [11]], 3), False)

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.searchMatrix([[1], [5], [8], [11]], 8), True)

    def test_8(self):
        sol = Solution()
        self.assertEqual(sol.searchMatrix([[]], 8), False)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_4()
