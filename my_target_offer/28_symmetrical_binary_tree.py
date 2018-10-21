"""

面试题28：对称的二叉树
题目：请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def is_symmetrical(self, root):
        """
        调用判断是否对称的递归函数

        :param root: 根节点
        :return: 是否对称
        """
        return self.is_symmetrical_core(root, root)

    def is_symmetrical_core(self, p_root1, p_root2):
        """
        判断二叉树与镜像是否相等

        :param p_root1: 根节点
        :param p_root2: 根节点
        :return: 是否对称
        """
        if p_root1 is None:
            return True

        if p_root2 is None:
            return False

        if p_root1.val != p_root2.val:
            return False

        return self.is_symmetrical_core(p_root1.left, p_root2.right) and \
               self.is_symmetrical_core(p_root1.right, p_root2.left)


if __name__ == '__main__':
    node1 = Node(8)
    node2 = Node(6)
    node3 = Node(6)
    node4 = Node(5)
    node5 = Node(7)
    node6 = Node(7)
    node7 = Node(5)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node = None

    S = Solution()
    is_symmetrical = S.is_symmetrical(node1)
    if is_symmetrical:
        print("binary tree is symmetrical...")
    else:
        print("binary tree is not symmetrical...")


