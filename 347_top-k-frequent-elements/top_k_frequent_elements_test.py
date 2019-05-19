#!/usr/bin/env python3

import unittest
from top_k_frequent_elements import Solution


class TestTopK(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2), [1, 2])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.topKFrequent([1], 1), [1])


if __name__ == '__main__':
    unittest.main()
