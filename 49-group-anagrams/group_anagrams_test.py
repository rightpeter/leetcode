#!/usr/bin/env python3

import unittest
from group_anagrams import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
                         [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.groupAnagrams([]), [])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.groupAnagrams(['a']), [['a']])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
