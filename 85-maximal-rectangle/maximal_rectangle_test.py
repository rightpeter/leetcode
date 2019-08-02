#!/usr/bin/env python3

import unittest
from maximal_rectangle import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.maximalRectangle([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
                                  ["1", "0", "0", "1", "0"]]), 6)

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.maximalRectangle([["0", "0", "0", "1", "0", "1", "1", "1"],
                                  ["0", "1", "1", "0", "0", "1", "0", "1"],
                                  ["1", "0", "1", "1", "1", "1", "0", "1"],
                                  ["0", "0", "0", "1", "0", "0", "0", "0"],
                                  ["0", "0", "1", "0", "0", "0", "1", "0"],
                                  ["1", "1", "1", "0", "0", "1", "1", "1"],
                                  ["1", "0", "0", "1", "1", "0", "0", "1"],
                                  ["0", "1", "0", "0", "1", "1", "0", "0"],
                                  ["1", "0", "0", "1", "0", "0", "0", "0"]]), 4)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_2()
