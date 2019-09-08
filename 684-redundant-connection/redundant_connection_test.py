#!/usr/bin/env python3

import unittest
from redundant_connection import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.findRedundantConnection([[1, 2], [1, 3], [2, 3]]), [2, 3])

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4],
                                         [1, 5]]), [1, 4])

    def test_3(self):
        sol = Solution()
        self.assertEqual(
            sol.findRedundantConnection([[1, 4], [3, 4], [1, 3], [1, 2],
                                         [4, 5]]), [1, 3])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_3()
