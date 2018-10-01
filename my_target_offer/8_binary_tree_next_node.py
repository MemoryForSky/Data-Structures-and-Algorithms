"""

给定一颗二叉树和其中一个节点，如何找到中序遍历序列的下一个节点？
树中的节点除了有两个分别指向左、右子节点的指针，还有一个指向父节点的指针。

"""

# 二叉树节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

# 找下一个节点
class Solution:
    def binary_tree_next_node(self, node):
        if node is None:
            return 0

        if node.right:
            p_node = node.right
            while p_node.left:
                p_node = p_node.left
            return p_node.val
        elif node.parent and node.parent.left is node:
            return node.parent.val
        else:
            if node.parent:
                parent_node = node.parent
                while parent_node.parent:
                    if parent_node is parent_node.parent.left:
                        return parent_node.parent.val
                    else:
                        parent_node = parent_node.parent
            return 0


if __name__ == '__main__':
    node_a = TreeNode("a")
    node_b = TreeNode("b")
    node_c = TreeNode("c")
    node_d = TreeNode("d")
    node_e = TreeNode("e")
    node_f = TreeNode("f")
    node_g = TreeNode("g")
    node_h = TreeNode("h")
    node_i = TreeNode("i")
    node_a.left = node_b
    node_a.right = node_c
    node_b.left = node_d
    node_b.right = node_e
    node_b.parent = node_a
    node_c.left = node_f
    node_c.right = node_g
    node_c.parent = node_a
    node_d.parent = node_b
    node_e.left = node_h
    node_e.right = node_i
    node_e.parent = node_b
    node_f.parent = node_c
    node_g.parent = node_c
    node_h.parent = node_e
    node_i.parent = node_e

    node_o = TreeNode("o")
    S = Solution()
    print("含有右孩子：下个节点应为h")
    given_node = node_b
    result = S.binary_tree_next_node(given_node)
    print("下个节点：", result)

    print("没有右孩子，本节点为其父节点的左孩子：下个节点应为e")
    given_node = node_h
    result = S.binary_tree_next_node(given_node)
    print("下个节点：", result)

    print("没有右孩子，本节点为其父节点的右孩子：下个节点应为a")
    given_node = node_i
    result = S.binary_tree_next_node(given_node)
    print("下个节点：", result)

    print("没有右孩子，本节点为其父节点的右孩子，但没有下个节点：没有下个节点")
    given_node = node_g
    result = S.binary_tree_next_node(given_node)
    print("下个节点：", result)

    print("只有根节点：没有下个节点")
    given_node = node_o
    result = S.binary_tree_next_node(given_node)
    print("下个节点：", result)

    print("空树：没有下个节点")
    given_node = node_o
    result = S.binary_tree_next_node(given_node)
    print("下个节点：", result)

