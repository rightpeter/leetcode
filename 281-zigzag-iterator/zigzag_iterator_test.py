#!/usr/bin/env python3

import unittest
from zigzag_iterator import ZigzagIterator


class TestSolution(unittest.TestCase):

    def test_1(self):
        i, v = ZigzagIterator([1, 2], [3, 4, 5, 6]), []
        while i.hasNext():
            v.append(i.next())

        self.assertEqual(v, [1, 3, 2, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
