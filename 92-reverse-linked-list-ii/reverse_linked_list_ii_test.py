#!/usr/bin/env python3

import unittest
from reverse_linked_list_ii import Solution
from node_list_helper import NodeListHelper


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        input_list = [1, 2, 3, 4, 5]
        output_node_list = sol.reverseBetween(
            NodeListHelper.list_to_node_list(input_list), 2, 4)
        self.assertEqual(
            NodeListHelper.node_list_to_list(output_node_list), [1, 4, 3, 2, 5])

    def test_2(self):
        sol = Solution()
        input_list = [1, 2, 3, 4, 5]
        output_node_list = sol.reverseBetween(
            NodeListHelper.list_to_node_list(input_list), 1, 5)
        self.assertEqual(
            NodeListHelper.node_list_to_list(output_node_list), [5, 4, 3, 2, 1])

    def test_3(self):
        sol = Solution()
        input_list = [1]
        output_node_list = sol.reverseBetween(
            NodeListHelper.list_to_node_list(input_list), 1, 1)
        self.assertEqual(
            NodeListHelper.node_list_to_list(output_node_list), [1])

    def test_4(self):
        sol = Solution()
        input_list = [1, 2]
        output_node_list = sol.reverseBetween(
            NodeListHelper.list_to_node_list(input_list), 1, 2)
        self.assertEqual(
            NodeListHelper.node_list_to_list(output_node_list), [2, 1])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_3()
