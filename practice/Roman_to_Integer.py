# _*_ coding: utf-8 _*_
# 2019/3/28 11:10

__auther__ = "tanran"
"""
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:

输入: "III"
输出: 3
示例 2:

输入: "IV"
输出: 4
示例 3:

输入: "IX"
输出: 9
示例 4:

输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
示例 5:

输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
"""


class Solution:
    def __init__(self):
        self.roman_integer = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        self.special_dict = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        self.s = ""

    def romanToInt(self, s: str) -> int:
        self.s = s
        is_specia = self._handing_special()
        result_num = is_specia
        for s_single in self.s:
            amount = self.s.count(s_single)
            self.s = self.s.strip(s_single)
            try:
                single_num = self.roman_integer[s_single] * amount
            except KeyError:
                return result_num
            result_num = result_num + single_num

        return result_num

    def _handing_special(self):
        """
        I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
        X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
        C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
        :param s:
        :return:
        """
        temp_num = 0
        temp_index = 0
        for i in range(len(self.s)-1):
            i = i - temp_index
            couple = self.s[i:i+2]
            if couple in self.special_dict:
                temp_index = temp_index + 1
                self.s = self.s[:i] + self.s[i+2:]
                temp_num = temp_num + self.special_dict[couple]
        return temp_num


class Solution2:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i in range(len(s)):
            if i < len(s)-1 and a[s[i]] < a[s[i+1]]:
                ans -= a[s[i]]
            else:
                ans += a[s[i]]
        return ans


s = Solution2()
s.romanToInt("MCMXCIV")
