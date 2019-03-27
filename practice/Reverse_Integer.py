# _*_ coding: utf-8 _*_
# 2019/3/27 18:14

__auther__ = "tanran"
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer 
range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the 
reversed integer overflows.
"""


class Solution:
    def reverse(self, x: int) -> int:
        if not self.judge_range(x):
            return 0
        # 判断正负号
        if x >= 0:
            sign = True
        else:
            sign = False

        # 将int转换为str 方便反转
        str_x = str(abs(x))

        reverse_str = str_x[::-1]

        if sign:
            result_num = int(reverse_str)
        else:
            result_num = -int(reverse_str)
        if not self.judge_range(result_num):
            return 0
        return result_num

    @staticmethod
    def judge_range(x):
        if x >= 2**31 - 1 or x <= -2**31:
            return False
        else:
            return True


