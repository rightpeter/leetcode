#!/usr/bin/env python3

import unittest
from sliding_window_maximum import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3),
            [3, 3, 5, 5, 6, 7])

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.maxSlidingWindow([1, 3, -1], 3),
            [3])

    def test_3(self):
        sol = Solution()
        self.assertEqual(
            sol.maxSlidingWindow([1], 1),
            [1])

    def test_4(self):
        sol = Solution()
        self.assertEqual(
            sol.maxSlidingWindow([1, 3, 5, 6], 1),
            [1, 3, 5, 6])

    def test_5(self):
        sol = Solution()
        self.assertEqual(
            sol.maxSlidingWindow([], 0),
            [])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
