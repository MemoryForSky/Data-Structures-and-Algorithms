"""

面试题55（二）：平衡二叉树
题目：输入一棵二叉树的根结点，判断该树是不是平衡二叉树。如果某二叉树中
任意结点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

思路：

本题最直观的解题思路是自顶向下计算每个节点的左子树和右子树的深度，判断深度之差是否满足平衡二叉树

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    """自顶向下遍历每个节点，判断是不是平衡的，需要重复遍历节点多次，效率低"""
    def tree_depth(self, root):
        if root is None:
            return 0

        left = self.tree_depth(root.left)
        right = self.tree_depth(root.right)

        return max(left, right) + 1

    def is_balance(self, root):
        if root is None:
            return True

        left = self.tree_depth(root.left)
        right = self.tree_depth(root.right)

        if abs(left - right) > 1:
            return False

        return self.is_balance(root.left) and self.is_balance(root.right)

class Solution2:
    """使用后序遍历，每个节点只遍历一次，效率高"""
    def __init__(self):
        self.flag = True

    def is_balance(self, root):
        if root is None:
            return

        self.tree_depth(root)

        return self.flag

    def tree_depth(self, root):
        if root is None:
            return 0

        left = self.tree_depth(root.left) + 1
        right = self.tree_depth(root.right) + 1

        if abs(left - right) > 1:
            self.flag = False

        return max(left, right)


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6
    node5.left = node7
    node7.left = node8

    S = Solution2()
    is_balance = S.is_balance(node1)
    if is_balance:
        print("balance")
    else:
        print("not balance")
