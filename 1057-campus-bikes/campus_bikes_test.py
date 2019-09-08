#!/usr/bin/env python3

import unittest
from campus_bikes import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.assignBikes([[0, 0], [2, 1]], [[1, 2], [3, 3]]), [1, 0])

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.assignBikes([[3, 1], [1, 1]], [[2, 2], [2, 0]]), [0, 1])

    def test_3(self):
        sol = Solution()
        self.assertEqual(
            sol.assignBikes([[3, 1], [1, 1]], [[2, 1], [2, 2]]), [0, 1])

    def test_4(self):
        sol = Solution()
        self.assertEqual(
            sol.assignBikes([[1, 1], [3, 1]], [[2, 2], [2, 1]]), [1, 0])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
