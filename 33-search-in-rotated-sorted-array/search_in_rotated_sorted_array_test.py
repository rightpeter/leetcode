#!/usr/bin/env python3

import unittest
from search_in_rotated_sorted_array_compressed import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.search([4, 5, 6, 7, 0, 1, 2], 0), 4)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.search([4, 5, 6, 7, 0, 1, 2], 3), -1)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.search([], 3), -1)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.search([1], 3), -1)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.search([1], 1), 0)

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.search([4, 5, 6, 7, 0, 1, 2], 6), 2)

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.search([4, 5, 6, 7, 0, 1, 2], 8), -1)

    def test_8(self):
        sol = Solution()
        self.assertEqual(sol.search([88, 90, 0, 1, 4, 7, 9], 90), 1)

    def test_9(self):
        sol = Solution()
        self.assertEqual(sol.search([88, 90, 0, 1, 4, 7, 9], 9), 6)

    def test_10(self):
        sol = Solution()
        self.assertEqual(sol.search([88, 90, 0, 1, 4, 7, 9], 89), -1)

    def test_11(self):
        sol = Solution()
        self.assertEqual(sol.search([88, 90, 0, 1, 4, 7, 9], 5), -1)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_9()
