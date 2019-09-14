#!/usr/bin/env python3

import unittest
from exam_room_heap import ExamRoom

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)


class TestSolution(unittest.TestCase):

    def test_1(self):
        input_list1 = [
            "ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"
        ]
        input_list2 = [[10], [], [], [], [], [4], []]

        room = ExamRoom(input_list2[0][0])

        res = [None]
        for i in range(1, len(input_list1)):
            if input_list1[i] == 'seat':
                res.append(room.seat())
            else:
                room.leave(input_list2[i][0])
                res.append(None)

        self.assertEqual(res, [None, 0, 9, 4, 2, None, 5])

    def test_2(self):
        input_list1 = [
            "ExamRoom", "seat", "seat", "seat", "leave", "leave", "seat",
            "seat", "seat", "seat", "seat", "seat", "seat", "seat", "seat",
            "leave"
        ]
        input_list2 = [[10], [], [], [], [0], [4], [], [], [], [], [], [], [],
                       [], [], [0]]

        room = ExamRoom(input_list2[0][0])

        res = [None]
        for i in range(1, len(input_list1)):
            if input_list1[i] == 'seat':
                res.append(room.seat())
            else:
                room.leave(input_list2[i][0])
                res.append(None)

        self.assertEqual(
            res, [None, 0, 9, 4, None, None, 0, 4, 2, 6, 1, 3, 5, 7, 8, None])

    def test_3(self):
        input_list1 = [
            "ExamRoom", "seat", "seat", "seat", "leave", "leave", "seat",
            "seat", "seat", "seat", "seat", "seat", "seat", "seat", "seat",
            "leave", "leave", "seat", "seat", "leave", "seat", "leave", "seat",
            "leave", "seat", "leave", "seat", "leave", "leave", "seat", "seat",
            "leave", "leave", "seat", "seat", "leave"
        ]

        input_list2 = [[10], [], [], [], [0], [4], [], [], [], [], [], [], [],
                       [], [], [0], [4], [], [], [7], [], [3], [], [3], [], [9],
                       [], [0], [8], [], [], [0], [8], [], [], [2]]

        room = ExamRoom(input_list2[0][0])

        res = [None]
        for i in range(1, len(input_list1)):
            if input_list1[i] == 'seat':
                res.append(room.seat())
                # print(f'res: {res[-1]}')
            else:
                room.leave(input_list2[i][0])
                res.append(None)

        self.assertEqual(res, [
            None, 0, 9, 4, None, None, 0, 4, 2, 6, 1, 3, 5, 7, 8, None, None, 0,
            4, None, 7, None, 3, None, 3, None, 9, None, None, 0, 8, None, None,
            0, 8, None
        ])

    def test_4(self):
        input_list1 = [
            "ExamRoom", "seat", "seat", "seat", "seat", "leave", "leave", "seat"
        ]
        input_list2 = [[4], [], [], [], [], [1], [3], []]

        room = ExamRoom(input_list2[0][0])

        res = [None]
        for i in range(1, len(input_list1)):
            if input_list1[i] == 'seat':
                res.append(room.seat())
                # print(f'res: {res[-1]}')
            else:
                room.leave(input_list2[i][0])
                res.append(None)

        self.assertEqual(res, [None, 0, 3, 1, 2, None, None, 1])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_4()
