#!/usr/bin/env python3

import unittest
from jump_game import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.canJump([2, 3, 1, 1, 4]), True)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.canJump([3, 2, 1, 0, 4]), False)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.canJump([1]), True)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.canJump([]), False)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.canJump([1, 1, 1, 1, 1, 1, 1]), True)

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.canJump([1, 1, 1, 1, 1, 1, 0]), True)

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.canJump([1, 1, 1, 0, 1, 1, 0]), False)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
