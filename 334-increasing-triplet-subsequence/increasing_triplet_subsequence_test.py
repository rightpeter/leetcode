#!/usr/bin/env python3

import unittest
from increasing_triplet_subsequence import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.increasingTriplet([1, 2, 3, 4, 5]), True)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.increasingTriplet([5, 4, 3, 2, 1]), False)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.increasingTriplet([4, 5, 1, 2, 3]), True)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.increasingTriplet([4, 5, 1, 2, 2, 2, 2, 2]), False)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.increasingTriplet([4, 4, 1, 2, 6]), True)

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.increasingTriplet([5, 1, 5, 5, 2, 5, 4]), True)

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.increasingTriplet([4, 4, 1, 6]), False)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_6()
