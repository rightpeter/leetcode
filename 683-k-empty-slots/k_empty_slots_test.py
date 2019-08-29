#!/usr/bin/env python3

import unittest
from k_empty_slots import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.kEmptySlots([1, 3, 2], 1), 2)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.kEmptySlots([1, 2, 3], 1), -1)

    def test_3(self):
        sol = Solution()
        self.assertEqual(
            sol.kEmptySlots([6, 5, 8, 9, 7, 1, 10, 2, 3, 4], 2), 8)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
