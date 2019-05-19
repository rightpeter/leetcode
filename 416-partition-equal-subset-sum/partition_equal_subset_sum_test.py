#!/usr/bin/env python3

import unittest
from partition_equal_subset_sum import Solution


class TestPartitionEqualSubset(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.canPartition([1, 5, 11, 5]), True)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.canPartition([1, 2, 3, 5]), False)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.canPartition([1]), False)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.canPartition([1, 1, 1, 1]), True)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.canPartition([3, 3, 3, 4, 5]), True)

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.canPartition([3, 3, 3, 4, 5, 9, 11, 3, 4, 2, 1, 3, 51]), True)

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.canPartition([3, 3, 3, 4, 5, 9, 11, 3, 4, 2, 1, 3, 50]), False)


if __name__ == '__main__':
    unittest.main()
