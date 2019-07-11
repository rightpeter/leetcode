#!/usr/bin/env python3

import unittest
from spiral_matrix import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
                         [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.spiralOrder([[1]]),
                         [1])

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.spiralOrder([[1, 2, 3]]),
                         [1, 2, 3])

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.spiralOrder([[1], [2], [3]]),
                         [1, 2, 3])

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.spiralOrder([[]]),
                         [])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_2()
