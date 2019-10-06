#!/usr/bin/env python3

import unittest
from brace_expansion import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.expand("{a,b}c{d,e}f"), ["acdf", "acef", "bcdf", "bcef"])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
