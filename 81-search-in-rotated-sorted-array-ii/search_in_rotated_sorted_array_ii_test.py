#!/usr/bin/env python3

import unittest
from search_in_rotated_sorted_array_ii import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.search([2, 5, 6, 0, 0, 1, 2], 0), True)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.search([2, 5, 6, 0, 0, 1, 2], 3), False)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
