#!/usr/bin/env python3


class ListNode:

    def __init__(self, key=None, val=None, parent=None, next_node=None):
        self.key = key
        self.val = val
        self.parent = parent
        self.next = next_node


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.usage = 0
        self.cache = {}
        self.head = ListNode(0, 0, None, None)
        self.tail = ListNode(-1, -1, self.head, None)
        self.head.next = self.tail

    def access(self, key):
        if not self.cache.get(key):
            return
        node = self.cache[key]
        node.parent.next = node.next
        node.next.parent = node.parent
        node.next = self.head.next
        node.parent = self.head
        self.head.next.parent = node
        self.head.next = node

    def delete_lru_from_cache(self):
        node = self.tail.parent
        node.parent.next = self.tail
        self.tail.parent = node.parent
        del(self.cache[node.key])
        self.usage -= 1

    def insert_to_cache(self, key, value):
        if self.usage >= self.capacity:
            return
        node = ListNode(key, value, self.head, self.head.next)
        self.head.next.parent = node
        self.head.next = node
        self.cache[key] = node
        self.usage += 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.access(key)
        return self.cache[key].val if self.cache.get(key) else -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.get(key) != -1:
            self.cache[key].val = value
            return
        else:
            if self.usage >= self.capacity:
                self.delete_lru_from_cache()
            self.insert_to_cache(key, value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
