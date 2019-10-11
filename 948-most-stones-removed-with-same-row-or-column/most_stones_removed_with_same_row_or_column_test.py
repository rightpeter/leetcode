#!/usr/bin/env python3

import unittest
from most_stones_removed_with_same_row_or_column import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]),
            5)

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]), 3)

    def test_3(self):
        sol = Solution()
        self.assertEqual(
            sol.removeStones([[0, 0]]), 0)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
