#!/usr/bin/env python3

import unittest
from sort_colors_dij import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        input_list = [2, 0, 2, 1, 1, 0]
        sol.sortColors(input_list)
        self.assertEqual(input_list, [0, 0, 1, 1, 2, 2])

    def test_2(self):
        sol = Solution()
        input_list = []
        sol.sortColors(input_list)
        self.assertEqual(input_list, [])

    def test_3(self):
        sol = Solution()
        input_list = [2]
        sol.sortColors(input_list)
        self.assertEqual(input_list, [2])

    def test_4(self):
        sol = Solution()
        input_list = [2, 1]
        sol.sortColors(input_list)
        self.assertEqual(input_list, [1, 2])

    def test_5(self):
        sol = Solution()
        input_list = [2, 1, 0]
        sol.sortColors(input_list)
        self.assertEqual(input_list, [0, 1, 2])

    def test_6(self):
        sol = Solution()
        input_list = [2, 0, 1]
        sol.sortColors(input_list)
        self.assertEqual(input_list, [0, 1, 2])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
