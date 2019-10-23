#!/usr/bin/env python3

import unittest
from friends_of_appropriates_ages_dp import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.numFriendRequests([16, 16]), 2)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.numFriendRequests([16, 17, 18]), 2)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.numFriendRequests([20, 30, 100, 110, 120]), 3)

    def test_4(self):
        sol = Solution()
        self.assertEqual(
            sol.numFriendRequests(
                [73, 106, 39, 6, 26, 15, 30, 100, 71, 35, 46, 112, 6, 60, 110]),
            29)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_4()
