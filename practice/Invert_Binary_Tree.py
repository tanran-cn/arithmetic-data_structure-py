# _*_ coding: utf-8 _*_
# 2019/3/24 20:10

__auther__ = "tanran"
"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            temp_TreeNode = root.left
            root.left = root.right
            root.right = temp_TreeNode
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root