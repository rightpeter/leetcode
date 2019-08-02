#!/usr/bin/env python3

import unittest
from partition_list import Solution
from node_list_helper import NodeListHelper


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        input_list = [1, 4, 3, 2, 5, 2]
        output_node_list = sol.partition(NodeListHelper.list_to_node_list(input_list), 3)
        output_list = [1, 2, 2, 4, 3, 5]
        self.assertEqual(NodeListHelper.node_list_to_list(output_node_list), output_list)

    def test_2(self):
        sol = Solution()
        input_list = [1]
        output_node_list = sol.partition(NodeListHelper.list_to_node_list(input_list), 3)
        output_list = [1]
        self.assertEqual(NodeListHelper.node_list_to_list(output_node_list), output_list)

    def test_3(self):
        sol = Solution()
        input_list = [3, 1, 2]
        output_node_list = sol.partition(NodeListHelper.list_to_node_list(input_list), 3)
        output_list = [1, 2, 3]
        self.assertEqual(NodeListHelper.node_list_to_list(output_node_list), output_list)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
