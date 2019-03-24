# _*_ coding: utf-8 _*_
# 2019/3/24 21:41

__auther__ = "tanran"
"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        beg = 0
        end = len(s) - 1
        while beg < end:
            if s[beg] != s[end]:
                return False
            else:
                beg += 1
                end -= 1
        return True
