#!/usr/bin/env python3

import unittest
from minimum_path_sum import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.minPathSum([[1, 2, 3], [4, 5, 6]]), 12)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_2()
