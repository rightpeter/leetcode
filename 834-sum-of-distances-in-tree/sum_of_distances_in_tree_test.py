#!/usr/bin/env python3

import unittest
from sum_of_distances_in_tree import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.sumOfDistancesInTree(6,
                                     [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]),
            [8, 12, 6, 10, 10, 10])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.sumOfDistancesInTree(2, [[1, 0]]), [1, 1])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
