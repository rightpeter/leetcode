#!/usr/bin/env python3

import unittest
from kth_largest_element_in_an_array import Solution


class TestKthLargest(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.findKthLargest([1, 2, 2, 2, 2, 2, 4], 3), 2)


if __name__ == '__main__':
    unittest.main()
