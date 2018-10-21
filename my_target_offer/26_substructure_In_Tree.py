"""

面试题26：树的子结构
题目：输入两棵二叉树A和B，判断B是不是A的子结构。

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def sub_struct(self, tree1, tree2):
        result = False

        # tree1中与tree2根节点相等的点判断是否是子结构
        if tree1 is not None and tree2 is not None:
            if tree1.val == tree2.val:
                result = self.is_sub(tree1, tree2)
            if not result:
                result = self.sub_struct(tree1.left, tree2)
            if not result:
                result = self.sub_struct(tree1.right, tree2)

        return result

    def is_sub(self, tree1, tree2):
        # node2分枝到叶节点均相等，返回True
        if tree2 is None:
            return True

        # tree2不为空，tree1为空，返回False
        if tree1 is None:
            return False

        # 中间节点不相等，返回False
        if tree1.val != tree2.val:
            return False

        # 返回子树是否相等
        return self.is_sub(tree1.left, tree2.left) and self.is_sub(tree1.right, tree2.right)

if __name__ == '__main__':
    node1 = Node(8)
    node2 = Node(8)
    node3 = Node(7)
    node4 = Node(9)
    node5 = Node(2)
    node6 = Node(4)
    node7 = Node(7)

    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(2)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node5.left = node6
    node5.right = node7

    node8.left = node9
    node8.right = node10

    S = Solution()
    is_sub_struct = S.sub_struct(node1, node8)
    if is_sub_struct:
        print("tree2 is substructure of tree1")
    else:
        print("tree2 is not substructure of tree1")
