# _*_ coding: utf-8 _*_
# 2019/3/24 9:54
from collections import deque


__auther__ = "tanran"


class Stack():
    def __init__(self):
        self.deque = deque()

    def push(self, value):
        self.deque.append(value)

    def pop(self):
        return self.deque.pop()