#!/usr/bin/env python3

import unittest
from my_calendar_ii import MyCalendarTwo

# Your MyCalendarTwo object will be instantiated and called as such:


class TestSolution(unittest.TestCase):

    def test_1(self):
        obj = MyCalendarTwo()
        self.assertEqual(obj.book(10, 20), True)
        self.assertEqual(obj.book(50, 60), True)
        self.assertEqual(obj.book(10, 40), True)
        self.assertEqual(obj.book(5, 15), False)
        self.assertEqual(obj.book(5, 10), True)
        self.assertEqual(obj.book(25, 55), True)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
