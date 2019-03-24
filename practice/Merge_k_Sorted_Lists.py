# _*_ coding: utf-8 _*_
# 2019/3/24 21:06
from heapq import heapify, heappop

__auther__ = "tanran"
"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        """
        1、读取所有链表值
        2、构造一个最小堆 用heapq
        3、根据最小堆构造一个链表
        :param lists:
        :return:
        """
        # 获取节点值
        h = []
        for node in lists:
            while node:
                h.append(node.val)
                node = node.next
        # 构造一个最小堆
        heapify(h)

        # 构造链表
        if h:
            root = ListNode(heappop(h))
        else:
            root = []
        curnode = root
        while h:
            nextnode = ListNode(heappop(h))
            curnode.next = nextnode
            curnode = nextnode
        return root