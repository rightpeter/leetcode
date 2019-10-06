#!/usr/bin/env python3

import unittest
from implement_magic_dictionary import MagicDictionary


class TestSolution(unittest.TestCase):

    def test_1(self):
        obj = MagicDictionary()
        obj.buildDict(["hello", "leetcode"])
        input_list = ['hello', 'hhllo', 'hell', 'leetcoded']
        output_list = [False, True, False, False]

        for i in range(len(input_list)):
            self.assertEqual(obj.search(input_list[i]), output_list[i])

    def test_2(self):
        obj = MagicDictionary()
        obj.buildDict(["hello", "hallo", "leetcode"])
        input_list = ["hello", "hhllo", "hell", "leetcoded"]
        output_list = [True, True, False, False]

        res = []
        for i in range(len(input_list)):
            res.append(obj.search(input_list[i]))

        self.assertEqual(res, output_list)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_2()
