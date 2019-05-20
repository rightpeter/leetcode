#!/usr/bin/env python3

import unittest
from container_with_most_water import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
