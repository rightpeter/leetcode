#!/usr/bin/env python3

import unittest
from license_key_formatting import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.licenseKeyFormatting("2-5g-3-J", 2), "2-5G-3J")

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.licenseKeyFormatting("5F3Z-2e-9-w", 4), "5F3Z-2E9W")


if __name__ == '__main__':
    # unittest.main()
    TestSolution().test_1()
