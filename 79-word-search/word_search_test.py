#!/usr/bin/env python3

import unittest
from word_search import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED'), True)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'SEE'), True)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCB'), False)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.exist([], 'ABCB'), False)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.exist([[]], 'ABCB'), False)

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.exist([['A', 'B', 'C', 'E']], 'ECB'), True)

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.exist([['A', 'B', 'C', 'E']], 'CEB'), False)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_3()
