#!/usr/bin/env python3

import unittest
from set_matrix_zeroes import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        input_matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        sol.setZeroes(input_matrix)
        self.assertEqual(input_matrix, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

    def test_2(self):
        sol = Solution()
        input_matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        sol.setZeroes(input_matrix)
        self.assertEqual(input_matrix, [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])

    def test_3(self):
        sol = Solution()
        input_matrix = [[], []]
        sol.setZeroes(input_matrix)
        self.assertEqual(input_matrix, [[], []])

    def test_4(self):
        sol = Solution()
        input_matrix = []
        sol.setZeroes(input_matrix)
        self.assertEqual(input_matrix, [])

    def test_5(self):
        sol = Solution()
        input_matrix = [[-1], [2], [3]]
        sol.setZeroes(input_matrix)
        self.assertEqual(input_matrix, [[-1], [2], [3]])

    def test_6(self):
        sol = Solution()
        input_matrix = [[0], [1]]
        sol.setZeroes(input_matrix)
        self.assertEqual(input_matrix, [[0], [0]])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
