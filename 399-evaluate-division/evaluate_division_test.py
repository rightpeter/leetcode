#!/usr/bin/env python3

import unittest
from evaluate_division import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.calcEquation(
                [["a", "b"], ["b", "c"]], [2.0, 3.0],
                [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]),
            [6.0, 0.5, -1.0, 1.0, -1.0])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
