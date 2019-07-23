#!/usr/bin/env python3

import unittest
from combinations import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.combine(4, 2), [
            [1, 2],
            [1, 3],
            [1, 4],
            [2, 3],
            [2, 4],
            [3, 4],
        ])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.combine(5, 1), [
            [1],
            [2],
            [3],
            [4],
            [5],
        ])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.combine(5, 0), [])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
