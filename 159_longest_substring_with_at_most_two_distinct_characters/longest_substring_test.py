#!/usr/bin/env python3

import unittest
import longest_substring


class Test159(unittest.TestCase):
    sol = longest_substring.Solution()

    def test1(self):
        self.assertEqual(
            self.sol.lengthOfLongestSubstringTwoDistinct(
                "eceba"), 3)

    def test2(self):
        self.assertEqual(
            self.sol.lengthOfLongestSubstringTwoDistinct(
                "ccaabbb"), 5)


if __name__ == '__main__':
    unittest.main()
