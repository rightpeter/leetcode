#!/usr/bin/env python3


class ListNode:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.child = {}


class Solution:
    def simplifyPath(self, path: str) -> str:
        def path_to_str(child):
            res = ''
            while child.name != 'root':
                res = '/' + child.name + res
                # print(f'child.name: {child.name}, res: {res}')
                child = child.parent

            return res if res else '/'

        parent = ListNode('root', None)

        i = 0
        while i < len(path):
            j = i
            while j < len(path) and path[j] != '/':
                j += 1
            path_name = path[i:j]
            # print(f'path_name: {path_name}')

            if not path_name:
                pass
            elif path_name == '..':
                if parent.parent:
                    parent = parent.parent
            elif path_name != '.':
                if path_name not in parent.child:
                    parent.child[path_name] = ListNode(path_name, parent)
                parent = parent.child[path_name]

            i = j

            while i < len(path) and path[i] == '/':
                i += 1

        return path_to_str(parent)
