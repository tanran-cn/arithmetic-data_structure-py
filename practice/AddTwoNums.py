# _*_ coding: utf-8 _*_
# 2019/3/23 23:05

__auther__ = "tanran"
"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""
import copy


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        length_l1 = self._ListLength(l1)
        length_l2 = self._ListLength(l2)

        l1_str = self._getList(l1)
        l2_str = self._getList(l2)

        if l1_str:
            l1_str = l1_str[::-1]
        else:
            return -1
        if l2_str:
            l2_str = l2_str[::-1]
        else:
            return -1
        new_nums = int(l1_str) + int(l2_str)
        for n in new_nums:
            pass

    def _ListLength(self, l: ListNode) -> int:
        """
        获取链表的长度
        :param l: 链表头节点
        :return: 长度
        """
        temp_Node = copy.deepcopy(l)
        length = 1
        if temp_Node.next:
            length += 1
            temp_Node = temp_Node.next
        else:
            return length

    def _getList(self, l: ListNode) -> str:
        """
        将链表转化为字符串方便反转
        :param l: 链表头节点
        :return: 字符串
        """
        list_str = ""
        temp_Node = copy.deepcopy(l)
        if temp_Node.next:
            list_str = list_str + str(temp_Node.val)
        else:
            list_str = list_str + str(temp_Node.val)
            return list_str
        return -1


if __name__ == '__main__':
    so = Solution()


