#!/usr/bin/env python3

import unittest
from minimum_cost_to_hire_k_workers import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2), 105.000)

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.mincostToHireWorkers([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3),
            30.6666666666666666666666666666666667)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.mincostToHireWorkers([3, 4, 3], [13, 8, 20], 1), 8)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_3()
