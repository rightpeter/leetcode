#!/usr/bin/env python3


class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.students = []

    def seat(self) -> int:
        if not self.students:
            self.students.append(0)
            # print(f'students: {self.students}')
            return 0

        if len(self.students) == 1:
            if self.N - 1 - self.students[0] > self.students[0]:
                self.students.append(self.N - 1)
                # print(f'students: {self.students}')
                return self.N - 1
            else:
                self.students.insert(0, 0)
                # print(f'students: {self.students}')
                return 0

        d = 0
        x = 0
        for i in range(len(self.students) - 1):
            td = (self.students[i + 1] - self.students[i]) // 2
            if td > d:
                d = td
                x = i

        if self.students[0] >= d:
            if self.N - 1 - self.students[-1] > self.students[0]:
                self.students.append(self.N - 1)
                return self.N - 1
            else:
                self.students.insert(0, 0)
                return 0

        i = self.students[x]
        j = self.students[x + 1]

        student = i + (j - i) // 2
        self.students.insert(x + 1, student)

        # print(f'students: {self.students}')
        return student

    def leave(self, p: int) -> None:
        self.students.remove(p)
        # print(f'p: {p}, students: {self.students}')
