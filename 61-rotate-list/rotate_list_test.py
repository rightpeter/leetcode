#!/usr/bin/env python3

import unittest
from rotate_list import Solution
from node_list_helper import NodeListHelper


class TestSolution(unittest.TestCase):
    def test_1(self):
        input_list = [1, 2, 3, 4, 5]
        output_list = [4, 5, 1, 2, 3]
        input_node_list = NodeListHelper.list_to_node_list(input_list)
        sol = Solution()
        output_node_list = sol.rotateRight(input_node_list, 2)
        self.assertEqual(output_list, NodeListHelper.node_list_to_list(output_node_list))

    def test_2(self):
        input_list = [0, 1, 2]
        output_list = [2, 0, 1]
        input_node_list = NodeListHelper.list_to_node_list(input_list)
        sol = Solution()
        output_node_list = sol.rotateRight(input_node_list, 4)
        self.assertEqual(output_list, NodeListHelper.node_list_to_list(output_node_list))

    def test_3(self):
        input_list = [0, 1, 2]
        output_list = [2, 0, 1]
        input_node_list = NodeListHelper.list_to_node_list(input_list)
        sol = Solution()
        output_node_list = sol.rotateRight(input_node_list, 28)
        self.assertEqual(output_list, NodeListHelper.node_list_to_list(output_node_list))

    def test_4(self):
        input_list = []
        output_list = []
        input_node_list = NodeListHelper.list_to_node_list(input_list)
        sol = Solution()
        output_node_list = sol.rotateRight(input_node_list, 28)
        self.assertEqual(output_list, NodeListHelper.node_list_to_list(output_node_list))

    def test_5(self):
        input_list = [1]
        output_list = [1]
        input_node_list = NodeListHelper.list_to_node_list(input_list)
        sol = Solution()
        output_node_list = sol.rotateRight(input_node_list, 28)
        self.assertEqual(output_list, NodeListHelper.node_list_to_list(output_node_list))


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
