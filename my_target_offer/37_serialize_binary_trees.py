"""

面试题37：序列化二叉树
题目：请实现两个函数，分别用来序列化和反序列化二叉树。

思路：
本题的思路主要是二叉树的遍历和重构；    --> 思路是一样的，都是考虑终止条件和迭代公式

"""
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.string = ""

    def serialize(self, p_root):
        """
        二叉树的遍历
        """
        if p_root is None:
            self.string += "$, "
            return

        self.string += str(p_root.val) + ", "
        self.serialize(p_root.left)
        self.serialize(p_root.right)

    def deserialize(self, string):
        """
        二叉树的重构
        """
        data = string.split(", ")

        def buildBT():
            val = data.pop(0)
            if val == '$':
                return None
            else:
                root = Node(int(val))
                root.left = buildBT()
                root.right = buildBT()
                return root

        return buildBT()

    def print_tree(self, root):
        """
        打印二叉树
        """
        if root is None:
            return

        self.print_tree(root.left)
        print(root.val, end=" ")
        self.print_tree(root.right)

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
    node1 = T.test1()

    S = Solution()
    print("print origin binary tree: ")
    S.print_tree(node1)
    print()

    print("print serialize binary tree: ")
    S.serialize(node1)
    print(S.string)

    print("print deserialize binary tree: ")
    root = S.deserialize(S.string)
    S.print_tree(root)
