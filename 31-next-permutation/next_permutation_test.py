#!/usr/bin/env python3

import unittest
from next_permutation import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        input_list = [1, 2, 3]
        sol.nextPermutation(input_list)
        self.assertEqual(input_list, [1, 3, 2])

    def test_2(self):
        sol = Solution()
        input_list = [3, 2, 1]
        sol.nextPermutation(input_list)
        self.assertEqual(input_list, [1, 2, 3])

    def test_3(self):
        sol = Solution()
        input_list = [1, 1, 5]
        sol.nextPermutation(input_list)
        self.assertEqual(input_list, [1, 5, 1])

    def test_4(self):
        sol = Solution()
        input_list = [1, 5, 8, 4, 7, 6, 5, 3, 1]
        sol.nextPermutation(input_list)
        self.assertEqual(input_list, [1, 5, 8, 5, 1, 3, 4, 6, 7])

    def test_5(self):
        sol = Solution()
        input_list = [1]
        sol.nextPermutation(input_list)
        self.assertEqual(input_list, [1])

    def test_6(self):
        sol = Solution()
        input_list = []
        sol.nextPermutation(input_list)
        self.assertEqual(input_list, [])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_2()
