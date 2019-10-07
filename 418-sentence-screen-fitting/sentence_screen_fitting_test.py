#!/usr/bin/env python3

import unittest
from sentence_screen_fitting import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.wordsTyping(["hello", "world"], 2, 8), 1)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.wordsTyping(["a", "bcd", "e"], 3, 6), 2)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.wordsTyping(["I", "had", "apple", "pie"], 4, 5), 1)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.wordsTyping(["I"], 4, 5), 12)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.wordsTyping(["III"], 4, 5), 4)

    def test_6(self):
        sol = Solution()
        self.assertEqual(
            sol.wordsTyping(["try", "to", "be", "better"], 10000, 9001), 5293333)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
