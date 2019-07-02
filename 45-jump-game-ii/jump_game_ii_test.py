#!/usr/bin/env python3

import unittest
from jump_game_ii import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.jump([2, 3, 1, 1, 4]), 2)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.jump([5]), 0)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.jump([1, 1, 1, 1, 1, 1, 1]), 6)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.jump([3, 2, 1]), 1)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
