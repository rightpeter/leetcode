#!/usr/bin/env python3

import unittest
from smallest_rectangle_enclosing_black_pixels import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.minArea(["000100", "001100", "001000", "000000"], 0, 3), 6)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.minArea(["0010", "0110", "0100"], 0, 2), 6)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.minArea(["0000", "0100", "0000"], 1, 1), 1)

    def test_4(self):
        sol = Solution()
        self.assertEqual(
            sol.minArea(["000000", "000100", "001100", "001000", "000000"], 2,
                        2), 6)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.minArea(["1111", "1111", "1111"], 1, 1), 12)

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.minArea(["0010", "0010", "0010"], 1, 2), 3)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
