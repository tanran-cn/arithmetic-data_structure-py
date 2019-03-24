# _*_ coding: utf-8 _*_
# 2019/3/24 12:55

__auther__ = "tanran"


class BinTreeNode():
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right


class BinTree():
    def __init__(self, root=None):
        self.root = root

    def preorder_trav(self, subtree):
        """
        先序遍历
        :param subtree:节点
        :return: None
        """
        if subtree is not None:
            print(subtree.data)
            self.preorder_trav(subtree.left)
            self.preorder_trav(subtree.right)

    def inorder_trav(self, subtree):
        """
        中序遍历
        :param subtree:节点
        :return: None
        """
        if subtree is not None:
            self.inorder_trav(subtree.left)
            print(subtree.data)
            self.inorder_trav(subtree.right)

    def postorder_trav(self, subtree):
        """
        后序遍历
        :param subtree:节点
        :return: None
        """
        if subtree is not None:
            self.postorder_trav(subtree.left)
            self.postorder_trav(subtree.right)
            print(subtree.data)
