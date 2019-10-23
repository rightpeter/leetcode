#!/usr/bin/env python3

import unittest
from battleships_in_a_board import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.countBattleships(['X..X', '...X', '...X']), 2)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
