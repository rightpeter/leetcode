#!/usr/bin/env python3

import unittest
from car_fleet import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]), 3)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
