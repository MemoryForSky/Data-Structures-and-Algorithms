class TreeNode:
    """
    二叉树节点
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    二叉树的求解：递归 + 迭代
    """
    def max_depth(self, node):
        """
        求二叉树的最大深度
        """
        if node is None:
            return 0

        left = self.max_depth(node.left)
        right = self.max_depth(node.right)

        return max(left, right) + 1

    def min_depth(self, node):
        """
        求二叉树的最小深度
        """
        if node is None:
            return 0

        left = self.min_depth(node.left)
        right = self.min_depth(node.right)

        return min(left, right) + 1


    def node_count(self, node):
        """
        求二叉树中节点的个数
        :param node:
        :return:
        """
        if node is None:
            return 0

        left = self.node_count(node.left)
        right = self.node_count(node.right)

        return left + right + 1

    def leaf_node_count(self, node):
        """
        求二叉树中叶子节点的个数
        """
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        left = self.leaf_node_count(node.left)
        right = self.leaf_node_count(node.right)

        return left + right


# 求二叉树中第k层节点的个数
    def k_level_count(self):
        pass

# 判断二叉树是否是平衡二叉树
    def is_balance_binary_tree(self):
        pass

# 判断二叉树是否是完全二叉树
    def is_complete_binary_tree(self):
        pass

# 两个二叉树是否完全相同
    def is_common_tree(self):
        pass

# 两个二叉树是否互为镜像


# 翻转二叉树 or 镜像二叉树


# 求两个二叉树的最低公共祖先节点


# 二叉树的前序遍历


# 二叉树的中序遍历


# 二叉树的后序遍历


# 前序遍历和后序遍历构造二叉树


# 在二叉树中插入节点


# 输入一个二叉树和一个整数，打印出二叉树中节点值的和等于输入整数所有的路径


# 二叉树的搜索区间


# 二叉树的层次遍历


# 二叉树内两个节点的最长距离


# 不同的二叉树


# 判断二叉树是否是合法的二叉查找树(BST)


if __name__ == '__main__':
    """
    
    """
    node_a = TreeNode("a")
    node_b = TreeNode("b")
    node_c = TreeNode("c")
    node_d = TreeNode("d")
    node_e = TreeNode("e")
    node_f = TreeNode("f")
    node_g = TreeNode("g")
    node_h = TreeNode("h")
    node_i = TreeNode("i")
    node_k = TreeNode("k")
    node_a.left = node_b
    node_a.right = node_c
    node_b.left = node_d
    node_b.right = node_e
    node_c.left = node_f
    node_c.right = node_g
    node_e.left = node_h
    node_e.right = node_i
    node_h.left = node_k

    root = node_a
    S = Solution()

    #-----------------Test-----------------
    print("****** Test max depth: ******")
    max_depth = S.max_depth(node_b)
    print("max depth is: ", max_depth)

    print("****** Test min depth: ******")
    min_depth = S.min_depth(node_k)
    print("min depth is: ", min_depth)

    print("****** Test node count: ******")
    node_count = S.node_count(root)
    print("node count is: ", node_count)

    print("****** Test leaf node count: ******")
    leaf_node_count = S.leaf_node_count(root)
    print("leaf node count is: ", leaf_node_count)
