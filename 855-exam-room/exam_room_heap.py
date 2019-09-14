#!/usr/bin/env python3


class MaxHeap:

    def __init__(self, N: int):
        self.N = N
        self.heap = []
        self.seg_map = {}
        self.students = 0
        self.min = -1
        self.max = -1

    def dis(self, i: int) -> int:
        return (self.heap[i][1] - self.heap[i][0]) // 2

    def larger(self, i, j: int) -> bool:
        if self.dis(i) > self.dis(j):
            return True

        if self.dis(i) < self.dis(j):
            return False

        if self.heap[i][0] < self.heap[j][0]:
            return True

        return False

    def smaller(self, i, j: int) -> bool:
        if self.dis(i) < self.dis(j):
            return True

        if self.dis(i) > self.dis(j):
            return False

        if self.heap[i][0] > self.heap[j][0]:
            return True

        return False

    def swap(self, i, j: int):
        self.seg_map[self.heap[i][0]][1] = j
        self.seg_map[self.heap[i][1]][0] = j
        self.seg_map[self.heap[j][0]][1] = i
        self.seg_map[self.heap[j][1]][0] = i

        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def shift_up(self, i: int):
        child = i
        while (child > 0):
            parent = (child - 1) // 2
            if self.larger(child, parent):
                self.swap(child, parent)
                child = parent
            else:
                return

    def shift_down(self, i: int):
        parent = i

        while (parent * 2 + 1 < len(self.heap)):
            child = parent * 2 + 1

            if child + 1 < len(self.heap) and self.larger(child + 1, child):
                child += 1

            if self.smaller(parent, child):
                self.swap(child, parent)
                parent = child
            else:
                return

    def insert(self, seg):
        i = len(self.heap)
        self.heap.append(seg)
        self.seg_map[seg[0]][1] = i
        self.seg_map[seg[1]][0] = i
        self.shift_up(len(self.heap) - 1)

    def remove_seg(self, i: int):
        self.swap(i, len(self.heap) - 1)
        self.heap = self.heap[:-1]
        self.shift_down(i)

    def new_seg(self):
        self.students += 1
        if self.students == 1:
            self.min = 0
            self.max = 0
            self.seg_map[0] = [-1, -1]

            return 0

        if self.students == 2:
            if self.N - 1 - self.min > self.min:
                self.max = self.N - 1
                self.seg_map[self.max] = [-1, -1]
                self.insert([self.min, self.max])

                return self.max
            else:
                self.min = 0
                self.seg_map[self.min] = [-1, -1]
                self.insert([self.min, self.max])

                return self.min

        if self.min >= self.dis(0):
            if self.min >= self.N - 1 - self.max:
                self.seg_map[0] = [-1, -1]
                self.insert([0, self.min])
                self.min = 0

                return 0
            else:
                self.seg_map[self.N - 1] = [-1, -1]
                self.insert([self.max, self.N - 1])
                self.max = self.N - 1

                return self.N - 1

        if self.N - 1 - self.max > self.dis(0):
            self.seg_map[self.N - 1] = [-1, -1]
            self.insert([self.max, self.N - 1])
            self.max = self.N - 1

            return self.N - 1

        max_seg = self.heap[0].copy()
        mid = max_seg[0] + (max_seg[1] - max_seg[0]) // 2

        self.heap[0][1] = mid
        self.seg_map[mid] = [0, -1]
        self.shift_down(0)

        i = len(self.heap)
        self.heap.append([mid, max_seg[1]])
        self.seg_map[max_seg[1]][0] = i
        self.seg_map[mid][1] = i
        self.shift_up(i)

        # print(f'min: {self.min}, max: {self.max}')
        # print(f'heap: {self.heap}')
        # print(f'seg_map: {self.seg_map}')

        return mid

    def delege_point(self, p: int):
        self.students -= 1

        if self.students == 0:
            del (self.seg_map[p])
            return

        if self.students == 1:
            if self.max == p:
                self.max = self.min
            else:
                self.min = self.max

            self.heap = []
            del (self.seg_map[p])
            return

        if p == self.min:
            seg = self.seg_map[p][1]
            self.min = self.heap[seg][1]
            self.remove_seg(seg)
        elif p == self.max:
            seg = self.seg_map[p][0]
            self.max = self.heap[seg][0]
            self.remove_seg(seg)
        else:
            left_seg = self.seg_map[p][0]
            left = self.heap[left_seg][0]
            # print(f'remove {p} left_seg: {self.heap[left_seg]}')
            self.remove_seg(left_seg)

            right_seg = self.seg_map[p][1]
            right = self.heap[right_seg][1]
            # print(f'remove {p} right_seg: {self.heap[right_seg]}')
            self.remove_seg(right_seg)

            del (self.seg_map[p])
            self.insert([left, right])

            # print(f'min: {self.min}, max: {self.max}')
            # print(f'heap: {self.heap}')
            # print(f'seg_map: {self.seg_map}')


class ExamRoom:

    def __init__(self, N: int):
        self.heap = MaxHeap(N)

    def seat(self) -> int:
        # print(f'---------- seat ----------')
        return self.heap.new_seg()

    def leave(self, p: int) -> None:
        # print(f'---------- {p} leave ----------')
        self.heap.delege_point(p)
