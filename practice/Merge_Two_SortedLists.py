# _*_ coding: utf-8 _*_
# 2019/3/24 15:58

__auther__ = "tanran"
"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes 
of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(x=None)
        cur = root
        while l1 and l2:
            if l1.val <= l2.val:
                cur.val = l1.val
                cur.next = temp_node = ListNode(x=None)
                cur = temp_node
                l1 = l1.next
            else:
                cur.val = l2.val
                cur.next = temp_node = ListNode(x=None)
                cur = temp_node
                l2 = l2.next
        if l1:
            cur.val = l1.val
            cur.next = l1.next
        else:
            cur.val = l2.val
            cur.next = l2.next
        return root
