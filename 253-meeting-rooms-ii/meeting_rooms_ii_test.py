#!/usr/bin/env python3

import unittest
from meeting_rooms_ii import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]]), 2)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.minMeetingRooms([[7, 10], [2, 4]]), 1)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.minMeetingRooms([]), 0)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.minMeetingRooms([[5, 10], [1, 5]]), 1)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.minMeetingRooms([[1, 5], [5, 10]]), 1)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
