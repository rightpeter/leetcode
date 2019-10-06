#!/usr/bin/env python3

import unittest
from bricks_falling_when_hit import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.hitBricks([[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]]), [2])

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.hitBricks([[1, 0, 0, 0], [1, 1, 0, 0]], [[1, 1], [1, 0]]),
            [0, 0])

    def test_3(self):
        sol = Solution()
        self.assertEqual(
            sol.hitBricks([[1], [1], [1], [1], [1]],
                          [[3, 0], [4, 0], [1, 0], [2, 0], [0, 0]]),
            [1, 0, 1, 0, 0])

    def test_4(self):
        sol = Solution()
        self.assertEqual(
            sol.hitBricks([[1, 0, 1], [1, 1, 1]], [[0, 0], [0, 2], [1, 1]]),
            [0, 3, 0])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
