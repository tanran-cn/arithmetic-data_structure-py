# _*_ coding: utf-8 _*_
# 2019/3/24 10:36
from collections import deque
import copy

__auther__ = "tanran"


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        length = len(self.stack)
        return self.stack[length - 1]

    def getMin(self) -> int:
        temp_stack = copy.deepcopy(self.stack)
        if temp_stack:
            mix_nums = temp_stack.pop()
            while temp_stack:
                temp_num = temp_stack.pop()
                if mix_nums > temp_num:
                    mix_nums = temp_num
        else:
            mix_nums = None
        return mix_nums
