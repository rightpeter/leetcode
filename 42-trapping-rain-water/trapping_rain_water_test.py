#!/usr/bin/env python3

import unittest
from trapping_rain_water import Solution


class TestTrappingWater(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.trap([0, 1, 2, 2, 3, 4, 3, 3, 2, 3, 2, 1]), 1)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.trap([0, 1, 2, 2, 3, 4, 3, 3, 3, 3, 2, 1]), 0)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.trap([3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]), 10)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.trap([3, 2, 2, 2, 2, 100, 2, 2, 2, 2, 2, 3]), 9)

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.trap([]), 0)

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.trap([0, 5, 6, 4, 6, 1, 0, 0, 2, 7]), 23)


if __name__ == '__main__':
    unittest.main()
    # TestTrappingWater().test_8()
