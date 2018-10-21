"""

面试题27：二叉树的镜像
题目：请完成一个函数，输入一个二叉树，该函数输出它的镜像。

"""

class Node:
    def __init__(self, val):
        """
        二叉树节点
        :param val: 二叉树节点的值
        """
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def mirror(self, root):
        """
        输出二叉树镜像

        :param root: 根节点
        :return: 二叉树镜像
        """
        if root is None:
            return

        new_node = Node(root.val)
        new_node.right = self.mirror(root.left)
        new_node.left = self.mirror(root.right)

        return new_node

    def print_binary_tree(self, root):
        """
        二叉树先序遍历

        :param root: 根节点
        :return: 打印二叉树
        """
        if root is None:
            return

        print(root.val, end=' ')
        self.print_binary_tree(root.left)
        self.print_binary_tree(root.right)


if __name__ == '__main__':
    node1 = Node(8)
    node2 = Node(6)
    node3 = Node(10)
    node4 = Node(5)
    node5 = Node(7)
    node6 = Node(9)
    node7 = Node(11)
    node8 = Node(1)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node4.left = node8
    node = None

    S = Solution()
    print("原始二叉树：")
    S.print_binary_tree(node1)
    print("\n镜像二叉树：")
    mirror_node = S.mirror(node1)
    S.print_binary_tree(mirror_node)

