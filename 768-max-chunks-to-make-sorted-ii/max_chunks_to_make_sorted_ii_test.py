#!/usr/bin/env python3

import unittest
from max_chunks_to_make_sorted_ii import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.maxChunksToSorted([5, 4, 3, 2, 1]), 1)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.maxChunksToSorted([2, 1, 3, 4, 4]), 4)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
