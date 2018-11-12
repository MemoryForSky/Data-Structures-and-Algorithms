"""

面试题34：二叉树中和为某一值的路径
题目：输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所
有路径。从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

"""
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def find_path(self, p_node, target_sum):
        if p_node is Node:
            return

        stack = []
        current_sum = 0

        self.find_path_core(p_node, target_sum, stack, current_sum)


    def find_path_core(self, p_node, target_sum, stack, current_sum):
        # 递归前：对父节点先序遍历
        current_sum += p_node.val
        stack.insert(0, p_node.val)

        is_leaf = p_node.left is None and p_node.right is None
        if is_leaf and current_sum == target_sum:
            print("A path is found: ", stack[::-1])

        # 递归迭代
        if p_node.left:
            self.find_path_core(p_node.left, target_sum, stack, current_sum)
        if p_node.right:
            self.find_path_core(p_node.right, target_sum, stack, current_sum)

        # 递归后：需要返回的内容
        stack.pop(0)


if __name__ == "__main__":
    node1 = Node(10)
    node2 = Node(5)
    node3 = Node(12)
    node4 = Node(4)
    node5 = Node(7)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    number = 22

    S = Solution()
    S.find_path(node1, number)






