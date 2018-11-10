#!/usr/bin/env python3

import unittest
from merge_k_sorted_lists_divide_conqure import Solution


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


def convert_string_to_list(in_str):
    ret = ListNode(-1)
    p = ret
    for c in in_str.split("->"):
        if bool(c):
            p.next = ListNode(int(c))
            p = p.next

    return ret.next


def convert_list_to_string(in_list):
    if not in_list:
        return ""

    ret = str(in_list.val)
    in_list = in_list.next
    while in_list:
        ret += "->" + str(in_list.val)
        in_list = in_list.next

    return ret


class TestMergeList(unittest.TestCase):

    def test_1(self):
        in_str = "1->4->5"
        self.assertEqual(
            convert_list_to_string(convert_string_to_list(in_str)), in_str)

    def test_2(self):
        sol = Solution()
        in_str = ["1->4->5", "1->3->4", "2->6"]
        in_lists = []
        for s in in_str:
            in_lists.append(convert_string_to_list(s))
        out_list = sol.mergeKLists(in_lists)
        self.assertEqual(convert_list_to_string(out_list), "1->1->2->3->4->4->5->6")

    def test_3(self):
        sol = Solution()
        in_str = ["1", "", "2"]
        in_lists = []
        for s in in_str:
            in_lists.append(convert_string_to_list(s))
        out_list = sol.mergeKLists(in_lists)
        self.assertEqual(convert_list_to_string(out_list), "1->2")

    def test_4(self):
        sol = Solution()
        in_str = ["1->1->1->1", "", "2->2->2"]
        in_lists = []
        for s in in_str:
            in_lists.append(convert_string_to_list(s))
        out_list = sol.mergeKLists(in_lists)
        self.assertEqual(convert_list_to_string(out_list), "1->1->1->1->2->2->2")


if __name__ == '__main__':
    unittest.main()
    # TestMergeList().test_2()
