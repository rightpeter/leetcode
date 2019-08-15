#!/usr/bin/env python3

import unittest
from restore_ip_addresses import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.restoreIpAddresses("25525511135"),
            ["255.255.11.135", "255.255.111.35"])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.restoreIpAddresses("111"), [])

    def test_3(self):
        sol = Solution()
        self.assertEqual(
            sol.restoreIpAddresses("19216802"),
            ["19.216.80.2", "192.16.80.2", "192.168.0.2"])

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.restoreIpAddresses("0000"), ["0.0.0.0"])


if __name__ == '__main__':
    unittest.main()
    TestSolution().test_4()
