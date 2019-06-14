#!/usr/bin/env python3

import unittest
from reverse_nodes_in_k_group import Solution
from node_list_helper import NodeListHelper


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        input_list = [1, 2, 3, 4, 5]
        input_node_list = NodeListHelper.list_to_node_list(input_list)

        output_list = [2, 1, 4, 3, 5]
        output_node_list = NodeListHelper.list_to_node_list(output_list)

        result_node_list = sol.reverseKGroup(input_node_list, 2)

        self.assertEqual(NodeListHelper.print_node_list(result_node_list), NodeListHelper.print_node_list(output_node_list))

    def test_2(self):
        sol = Solution()
        input_list = [1, 2, 3, 4, 5]
        input_node_list = NodeListHelper.list_to_node_list(input_list)

        output_list = [3, 2, 1, 4, 5]
        output_node_list = NodeListHelper.list_to_node_list(output_list)

        result_node_list = sol.reverseKGroup(input_node_list, 3)

        self.assertEqual(NodeListHelper.print_node_list(result_node_list), NodeListHelper.print_node_list(output_node_list))

    def test_3(self):
        sol = Solution()
        input_list = [1, 2, 3, 4, 5]
        input_node_list = NodeListHelper.list_to_node_list(input_list)

        output_list = [4, 3, 2, 1, 5]
        output_node_list = NodeListHelper.list_to_node_list(output_list)

        result_node_list = sol.reverseKGroup(input_node_list, 4)

        self.assertEqual(NodeListHelper.print_node_list(result_node_list), NodeListHelper.print_node_list(output_node_list))

    def test_4(self):
        sol = Solution()
        input_list = [1, 2, 3, 4, 5]
        input_node_list = NodeListHelper.list_to_node_list(input_list)

        output_list = [1, 2, 3, 4, 5]
        output_node_list = NodeListHelper.list_to_node_list(output_list)

        result_node_list = sol.reverseKGroup(input_node_list, 7)

        self.assertEqual(NodeListHelper.print_node_list(result_node_list), NodeListHelper.print_node_list(output_node_list))


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_2()
