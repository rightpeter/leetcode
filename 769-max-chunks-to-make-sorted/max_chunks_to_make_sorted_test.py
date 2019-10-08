#!/usr/bin/env python3

import unittest
from max_chunks_to_make_sorted import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.maxChunksToSorted([4, 3, 2, 1, 0]), 1)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.maxChunksToSorted([1, 0, 2, 3, 4]), 4)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.maxChunksToSorted([0]), 1)

    def test_4(self):
        sol = Solution()
        self.assertEqual(
            sol.maxChunksToSorted([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 10)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
