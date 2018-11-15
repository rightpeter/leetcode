#!/usr/bin/env python3

import unittest
from integer_to_english_words import Solution


class TestEnglish(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.numberToWords(123), "One Hundred Twenty Three")

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.numberToWords(12345),
            "Twelve Thousand Three Hundred Forty Five")

    def test_3(self):
        sol = Solution()
        self.assertEqual(
            sol.numberToWords(1234567),
            "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
        )

    def test_4(self):
        sol = Solution()
        self.assertEqual(
            sol.numberToWords(1234567891),
            "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
        )

    def test_5(self):
        sol = Solution()
        self.assertEqual(
            sol.numberToWords(100000001),
            "One Hundred Million One"
        )

    def test_6(self):
        sol = Solution()
        self.assertEqual(
            sol.numberToWords(100),
            "One Hundred"
        )

    def test_7(self):
        sol = Solution()
        self.assertEqual(
            sol.numberToWords(1000000),
            "One Million"
        )

    def test_8(self):
        sol = Solution()
        self.assertEqual(
            sol.numberToWords(1000),
            "One Thousand"
        )


if __name__ == '__main__':
    unittest.main()
    # TestEnglish().test_5()
