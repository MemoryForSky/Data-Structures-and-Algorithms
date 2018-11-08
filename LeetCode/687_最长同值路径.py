"""

给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:

输入:

              5
             / \\
            4   5
           / \   \\
          1   1   5
输出:

2

示例 2:

输入:

              1
             / \
            4   5
          // \\  \
          4   4   5
输出:

2

==>关于递归程序中的操作代码的位置：
操作代码在递归的前面可以理解为“自上而下”的操作，先进行系列操作，然后递归一步步向下重复该操作；==> 先序遍历
操作代码在递归的后面可以理解为“自下而上”的操作，先递归一步步向下直到终止条件，然后执行系列操作后返回，重复该操作直到根节点。==> 后序遍历

所以在递归程序中，除了要考虑终止条件、迭代公式外，还要考虑程序的逻辑是自上而下还是自下而上（对比二叉树的先序、中序、后序遍历）。

PS:
错误：注意程序中何时返回该路径的长度，何时返回0（只要和父节点不相等，路径断开则返回0）

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    本题核心在于自下而上与父节点比较，相等则加1，不相等则为0，最大长度保存在全局变量
    """
    def __init__(self):
        self.maxLen = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.max_path(root, root.val)

        return self.maxLen

    def max_path(self, root, val):
        if not root:
            return 0

        left = self.max_path(root.left, root.val)
        right = self.max_path(root.right, root.val)

        # 左右孩子都与父节点相等，则路径为两边相加；若一边不相等，则这条边长度为0，只算另一条边
        self.maxLen = max(self.maxLen, left + right)

        # 与父节点相等，则加一
        if root.val == val:
            return max(left, right) + 1

        # 与父节点不相等，则该分支为0
        return 0

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(4)
    node3 = TreeNode(5)
    node4 = TreeNode(4)
    node5 = TreeNode(4)
    node6 = TreeNode(5)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6

    S = Solution()
    max_len = S.longestUnivaluePath(node1)
    print(max_len)
