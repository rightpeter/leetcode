#!/usr/bin/env python3

import unittest
from remove_nth_node_from_end_of_list import Solution
from node_list_helper import ListNode, NodeListHelper


class TestSolution(unittest.TestCase):

    def test_1(self):
        input_node_list = NodeListHelper.list_to_node_list([1, 2, 3, 4, 5])
        output_node_list = NodeListHelper.list_to_node_list([1, 2, 3, 5])
        sol = Solution()
        result_node_list = sol.removeNthFromEnd(input_node_list, 2)
        self.assertTrue(NodeListHelper.compare_two_node_list(result_node_list, output_node_list))

    def test_2(self):
        input_node_list = NodeListHelper.list_to_node_list([1, 2, 3, 4, 5])
        output_node_list = NodeListHelper.list_to_node_list([1, 3, 4, 5])
        sol = Solution()
        result_node_list = sol.removeNthFromEnd(input_node_list, 4)
        self.assertTrue(NodeListHelper.compare_two_node_list(result_node_list, output_node_list))

    def test_3(self):
        input_node_list = NodeListHelper.list_to_node_list([1, 2, 3, 4, 5])
        output_node_list = NodeListHelper.list_to_node_list([2, 3, 4, 5])
        sol = Solution()
        result_node_list = sol.removeNthFromEnd(input_node_list, 5)
        self.assertTrue(NodeListHelper.compare_two_node_list(result_node_list, output_node_list))


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_2()
