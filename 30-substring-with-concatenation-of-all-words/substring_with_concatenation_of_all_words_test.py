#!/usr/bin/env python3

import unittest
from substring_with_concatenation_of_all_words import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.findSubstring('barfoothefoobarman', ['foo', 'bar']), [0, 9])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.findSubstring('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word']), [])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.findSubstring('barfoothefoob', ['foo', 'bar']), [0])

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.findSubstring('', []), [])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_2()
