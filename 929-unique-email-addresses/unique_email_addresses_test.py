#!/usr/bin/env python3

import unittest
from unique_email_addresses import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.numUniqueEmails([
                "test.email+alex@leetcode.com",
                "test.e.mail+bob.cathy@leetcode.com",
                "testemail+david@lee.tcode.com"
            ]), 2)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
