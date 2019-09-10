#!/usr/bin/env python3

import unittest
from redundant_connection_ii import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]]),
            [2, 3])

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1],
                                                 [1, 5]]), [4, 1])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
