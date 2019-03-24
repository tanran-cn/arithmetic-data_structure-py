# _*_ coding: utf-8 _*_
# 2019/3/24 9:48
from collections import deque


__auther__ = "tanran"


class Queue:
    def __init__(self):
        self.items = deque()

    def append(self, val):
        return self.items.append(val)

    def pop(self):
        return self.items.popleft()

    def empty(self):
        return len(self.items) == 0


def test_queue():
    q = Queue()
    q.append(0)
    q.append(1)
    q.append(2)
    print(q.pop())


if __name__ == '__main__':
    test_queue()