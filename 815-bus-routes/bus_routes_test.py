#!/usr/bin/env python3

import unittest
from bus_routes import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6), 2)

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 4), -1)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
