#!/usr/bin/env python3

import unittest
from remove_duplicates_from_sorted_list_ii import Solution
from node_list_helper import NodeListHelper


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        input_node_list = NodeListHelper.list_to_node_list([1, 2, 3, 3, 4, 4, 5])
        output_list = [1, 2, 5]
        output_node_list = sol.deleteDuplicates(input_node_list)
        self.assertEqual(NodeListHelper.node_list_to_list(output_node_list), output_list)

    def test_2(self):
        sol = Solution()
        input_node_list = NodeListHelper.list_to_node_list([1, 1, 1, 2, 3])
        output_list = [2, 3]
        output_node_list = sol.deleteDuplicates(input_node_list)
        self.assertEqual(NodeListHelper.node_list_to_list(output_node_list), output_list)

    def test_3(self):
        sol = Solution()
        input_node_list = NodeListHelper.list_to_node_list([])
        output_list = []
        output_node_list = sol.deleteDuplicates(input_node_list)
        self.assertEqual(NodeListHelper.node_list_to_list(output_node_list), output_list)

    def test_4(self):
        sol = Solution()
        input_node_list = NodeListHelper.list_to_node_list([1, 1, 1, 1, 1])
        output_list = []
        output_node_list = sol.deleteDuplicates(input_node_list)
        self.assertEqual(NodeListHelper.node_list_to_list(output_node_list), output_list)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
