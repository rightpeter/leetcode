#!/usr/bin/env python3

import unittest
from edit_distance_1D import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.minDistance('horse', 'ros'), 3)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.minDistance('intention', 'execution'), 5)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.minDistance('', ''), 0)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.minDistance('', 'abcd'), 4)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
