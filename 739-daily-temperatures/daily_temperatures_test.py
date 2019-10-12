#!/usr/bin/env python3

import unittest
from daily_temperatures import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
