# _*_ coding: utf-8 _*_
# 2019/3/24 21:28

__auther__ = "tanran"
"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
"""


class Solution_simple:
    def reverseString(self, s: list) -> None:
        """
        直接用内置函数
        """
        s.reverse()

class Solution:
    def reverseString(self, s: list) -> None:
        """
        不用内置函数
        :param s: Sting
        :return: None
        """
        beg = 0
        end = len(s) - 1
        while beg < end:
            s[beg], s[end] = s[end], s[beg]
            beg += 1
            end -= 1
