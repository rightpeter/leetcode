#!/usr/bin/env python3

import unittest
from list_helper import NodeListHelper


class TestHelper(unittest.TestCase):

    def test_list_to_node_list_and_reverse(self):
        test_list = [3, 2, 5, 6, 3, 2]
        tmp_node_list = NodeListHelper.list_to_node_list(test_list)
        self.assertEqual(NodeListHelper.node_list_to_list(tmp_node_list), test_list)

    def test_print(self):
        test_list = [3, 2, 5, 6, 3, 2]
        tmp_node_list = NodeListHelper.list_to_node_list(test_list)
        self.assertEqual(NodeListHelper.print_node_list(tmp_node_list), "3 -> 2 -> 5 -> 6 -> 3 -> 2")

    def test_compare1(self):
        test_list = [3, 2, 5, 6, 3, 2]
        tmp_node_list1 = NodeListHelper.list_to_node_list(test_list)
        tmp_node_list2 = NodeListHelper.list_to_node_list(test_list)
        self.assertTrue(NodeListHelper.compare_two_node_list(tmp_node_list1, tmp_node_list2))

    def test_compare2(self):
        test_list1 = [3, 2, 5, 6, 3, 2]
        test_list2 = [3, 2, 5, 5, 3, 2]
        tmp_node_list1 = NodeListHelper.list_to_node_list(test_list1)
        tmp_node_list2 = NodeListHelper.list_to_node_list(test_list2)
        self.assertFalse(NodeListHelper.compare_two_node_list(tmp_node_list1, tmp_node_list2))

    def test_compare3(self):
        test_list1 = [3, 2]
        test_list2 = [3, 2, 5, 5, 3, 2]
        tmp_node_list1 = NodeListHelper.list_to_node_list(test_list1)
        tmp_node_list2 = NodeListHelper.list_to_node_list(test_list2)
        self.assertFalse(NodeListHelper.compare_two_node_list(tmp_node_list1, tmp_node_list2))

    def test_compare4(self):
        test_list1 = []
        test_list2 = [3, 2, 5, 5, 3, 2]
        tmp_node_list1 = NodeListHelper.list_to_node_list(test_list1)
        tmp_node_list2 = NodeListHelper.list_to_node_list(test_list2)
        self.assertFalse(NodeListHelper.compare_two_node_list(tmp_node_list1, tmp_node_list2))

if __name__ == '__main__':
    unittest.main()
    # TestHelper().test_compare1()
