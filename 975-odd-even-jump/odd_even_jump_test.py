#!/usr/bin/env python3

import unittest
from odd_even_jump import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.oddEvenJumps([10, 13, 12, 14, 15]), 2)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.oddEvenJumps([2, 3, 1, 1, 4]), 3)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.oddEvenJumps([5, 1, 3, 4, 2]), 3)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.oddEvenJumps([5]), 1)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.oddEvenJumps([]), 0)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
