#!/usr/bin/env python3


class Solution:

    def __init__(self):
        self.heap = []
        self.n = 0

    def heapify(self, i):
        left = i * 2 + 1
        right = i * 2 + 2

        if right < self.n:
            max_i = left if self.heap[left] > self.heap[right] else right
        elif left < self.n:
            max_i = left
        else:
            max_i = i

        max_i = max_i if self.heap[max_i] > self.heap[i] else i

        if max_i != i:
            self.heap[i], self.heap[max_i] = self.heap[max_i], self.heap[i]
            self.heapify(max_i)

    def buildHeap(self, nums):
        self.heap = nums
        self.n = len(nums)
        for i in range(len(nums) - 1, -1, -1):
            self.heapify(i)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        self.buildHeap(nums)

        for _ in range(k - 1):
            self.heap[0], self.heap[self.n - 1] = self.heap[self.n - 1], self.heap[0]
            self.n -= 1
            self.heapify(0)

        return self.heap[0]
