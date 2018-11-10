#!/usr/bin/env python3

import unittest
from longest_consecutive_sequence import Solution


class TestLongest(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)


if __name__ == '__main__':
    unittest.main()
