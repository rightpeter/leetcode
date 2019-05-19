#!/usr/bin/env python3

import unittest
from code import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.solution(), "solution")


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
