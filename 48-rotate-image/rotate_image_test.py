#!/usr/bin/env python3

import unittest
from rotate_image import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        img = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        sol.rotate(img)
        self.assertEqual(img, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    def test_2(self):
        sol = Solution()
        img = [[1]]
        sol.rotate(img)
        self.assertEqual(img, [[1]])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
