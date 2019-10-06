#!/usr/bin/env python3

import unittest
from maximize_distance_to_closest_person import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]), 2)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.maxDistToClosest([1, 0, 0, 0]), 3)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
