"""

面试题54：二叉搜索树的第k个结点
题目：给定一棵二叉搜索树，请找出其中的第k大的结点。

思路：

本题参考二叉搜索树的中序遍历，先找右子树，再找左子树，最终可以得到从大到小的输出。

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def find_kth_node(self, root, k):
        if root is None or k <= 0:
            return

        kth = [0]

        self.find_kth_node_core(root, k, kth)

    def find_kth_node_core(self, node, k, kth):
        if node is None or k < 0:
            return

        self.find_kth_node_core(node.right, k, kth)
        kth[0] += 1
        if kth[0] == k:
            print("二叉搜索树中第 %s 大的数：%s" % (k, node.val))
        self.find_kth_node_core(node.left, k, kth)


if __name__ == '__main__':
    node1 = TreeNode(5)
    node2 = TreeNode(3)
    node3 = TreeNode(7)
    node4 = TreeNode(2)
    node5 = TreeNode(4)
    node6 = TreeNode(6)
    node7 = TreeNode(8)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    S = Solution()
    S.find_kth_node(node1, 6)
