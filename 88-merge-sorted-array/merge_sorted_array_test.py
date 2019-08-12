#!/usr/bin/env python3

import unittest
from merge_sorted_array import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        sol.merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_2(self):
        sol = Solution()
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [4, 5, 6]
        sol.merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

    def test_3(self):
        sol = Solution()
        nums1 = [1, 2, 3, 4, 5, 6]
        nums2 = []
        sol.merge(nums1, 3, nums2, 0)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

    def test_4(self):
        sol = Solution()
        nums1 = [2, 0]
        nums2 = [1]
        sol.merge(nums1, 1, nums2, 1)
        self.assertEqual(nums1, [1, 2])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_4()
