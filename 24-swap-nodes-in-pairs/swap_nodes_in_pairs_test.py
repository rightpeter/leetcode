#!/usr/bin/env python3

import unittest
from swap_nodes_in_pairs import Solution
from node_list_helper import NodeListHelper


class TestSolution(unittest.TestCase):

    def test_1(self):
        input_list = [1, 2, 3, 4]
        output_list = [2, 1, 4, 3]
        sol = Solution()
        result_node_list = sol.swapPairs(NodeListHelper.list_to_node_list(input_list))
        output_node_list = NodeListHelper.list_to_node_list(output_list)
        self.assertTrue(NodeListHelper.compare_two_node_list(result_node_list, output_node_list))

    def test_2(self):
        input_list = [1]
        output_list = [1]
        sol = Solution()
        result_node_list = sol.swapPairs(NodeListHelper.list_to_node_list(input_list))
        output_node_list = NodeListHelper.list_to_node_list(output_list)
        self.assertTrue(NodeListHelper.compare_two_node_list(result_node_list, output_node_list))

    def test_3(self):
        input_list = [1, 2]
        output_list = [2, 1]
        sol = Solution()
        result_node_list = sol.swapPairs(NodeListHelper.list_to_node_list(input_list))
        output_node_list = NodeListHelper.list_to_node_list(output_list)
        self.assertTrue(NodeListHelper.compare_two_node_list(result_node_list, output_node_list))

    def test_4(self):
        input_list = [1, 2, 3]
        output_list = [2, 1, 3]
        sol = Solution()
        result_node_list = sol.swapPairs(NodeListHelper.list_to_node_list(input_list))
        output_node_list = NodeListHelper.list_to_node_list(output_list)
        self.assertTrue(NodeListHelper.compare_two_node_list(result_node_list, output_node_list))


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
