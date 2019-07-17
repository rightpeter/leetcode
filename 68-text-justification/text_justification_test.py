#!/usr/bin/env python3

import unittest
from text_justification import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16),
                         ["This    is    an", "example  of text", "justification.  "])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.fullJustify(["This", "is", "an", "example", "of", "text", "justificationas.", "hehe"], 16),
                         ["This    is    an", "example  of text", "justificationas.", "hehe            "])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.fullJustify(["This"], 5),
                         ["This "])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
