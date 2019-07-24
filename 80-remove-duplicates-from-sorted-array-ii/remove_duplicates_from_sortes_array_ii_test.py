#!/usr/bin/env python3

import unittest
from remove_duplicates_from_sortes_array_ii import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        input_list = [1, 1, 1, 2, 2, 3]
        n = sol.removeDuplicates(input_list)
        self.assertEqual(input_list[:n], [1, 1, 2, 2, 3])

    def test_2(self):
        sol = Solution()
        input_list = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        n = sol.removeDuplicates(input_list)
        self.assertEqual(input_list[:n], [0, 0, 1, 1, 2, 3, 3])

    def test_3(self):
        sol = Solution()
        input_list = []
        n = sol.removeDuplicates(input_list)
        self.assertEqual(input_list[:n], [])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
