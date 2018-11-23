"""

面试题55（一）：二叉树的深度
题目：输入一棵二叉树的根结点，求该树的深度。从根结点到叶结点依次经过的
结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree_depth(self, root):
        if root is None:
            return 0

        left = self.tree_depth(root.left)
        right = self.tree_depth(root.right)

        return max(left, right) + 1


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6
    node5.left = node7

    S = Solution()
    max_depth = S.tree_depth(node1)
    print(max_depth)
