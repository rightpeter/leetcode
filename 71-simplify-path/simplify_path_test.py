#!/usr/bin/env python3

import unittest
from simplify_path import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.simplifyPath('/home/'), '/home')

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.simplifyPath('/../'), '/')

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.simplifyPath('/home//foo/'), '/home/foo')

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.simplifyPath('/a/./b/../../c/'), '/c')

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.simplifyPath('/a/../../b/../c//.//'), '/c')

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.simplifyPath('/a//b////c/d//././/..'), '/a/b/c')

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.simplifyPath('/'), '/')


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_2()
