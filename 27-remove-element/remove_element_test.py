#!/usr/bin/env python3

import unittest
from remove_element import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        input_list = [3, 2, 2, 3]
        self.assertEqual(sol.removeElement(input_list, 3), 2)
        self.assertEqual(input_list[:2], [2, 2])

    def test_2(self):
        sol = Solution()
        input_list = [0, 1, 2, 2, 3, 0, 4, 2]
        self.assertEqual(sol.removeElement(input_list, 2), 5)
        self.assertEqual(input_list[:5], [0, 1, 3, 0, 4])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
