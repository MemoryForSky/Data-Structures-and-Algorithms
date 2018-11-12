"""

面试题36：二叉搜索树与双向链表
题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求
不能创建任何新的结点，只能调整树中结点指针的指向。

思路：
1、本题画图分析，首先根据二叉搜索树的性质，想要从小到大输出，考虑使用中序遍历；
故递归包含下面三部分：递归遍历左子树，根节点处理，递归遍历右子树

2、分析得到终止条件和迭代公式：
- 终止条件：root.left is None and root.right is None
- 迭代公式：self.convert_node(root.left)
           self.convert_node(root.right)

3、处理根节点：
对左子树：连接最大值
对右子树：连接最小值

"""
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convert_node(self, root):
        """
        二叉搜索树转换双向链表

        :param root: 根节点
        :return: 链表头结点
        """
        if root is None:
            return

        if root.left is None and root.right is None:
            return root

        # 遍历左子树
        left_node = self.convert_node(root.left)

        # 处理根节点：对左子树连接最大值
        if left_node:
            while left_node.right:
                left_node = left_node.right
        root.left = left_node
        if left_node:
            left_node.right = root

        # 遍历右子树
        right_node = self.convert_node(root.right)

        # 对右子树连接最小值
        if right_node:
            while right_node.left:
                right_node = right_node.left
        root.right = right_node
        if right_node:
            right_node.left = root

        # 找到最小值作为链表头结点
        while root.left:
            root = root.left

        return root

    def print_tree(self, root):
        """
        打印二叉树
        """
        if root is None:
            return

        self.print_tree(root.left)
        print(root.val, end=" ")
        self.print_tree(root.right)

    def print_link(self, root):
        """
        打印双向链表
        """
        if root is None:
            return

        p_next = root
        while p_next:
            print("(", p_next.left.val if p_next.left else "None", p_next.val, p_next.right.val
            if p_next.right else "None", ")")
            p_next = p_next.right

class Test:
    def test1(self):
        node1 = Node(10)
        node2 = Node(6)
        node3 = Node(14)
        node4 = Node(4)
        node5 = Node(8)
        node6 = Node(12)
        node7 = Node(16)

        node1.left = node2
        node1.right = node3
        node2.left = node4
        node2.right = node5
        node3.left = node6
        node3.right = node7

        return node1

    def test2(self):
        node1 = Node(5)
        node2 = Node(4)
        node3 = Node(3)
        node4 = Node(2)
        node5 = Node(1)

        node1.left = node2
        node2.left = node3
        node3.left = node4
        node4.left = node5

        return node1

    def test3(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)

        node1.right = node2
        node2.right = node3
        node3.right = node4
        node4.right = node5

        return node1

    def test4(self):
        node1 = Node(1)
        return node1

    def test5(self):
        node1 = None
        return node1

if __name__ == '__main__':
    T = Test()
    node1 = T.test5()

    S = Solution()
    print("print binary tree in order")
    S.print_tree(node1)
    print("\n")
    p_head = S.convert_node(node1)
    print("print link")
    S.print_link(p_head)




