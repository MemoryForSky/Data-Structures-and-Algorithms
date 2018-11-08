"""

面试题32（一）：从上往下打印二叉树
题目：从上往下打印出二叉树的每个结点，同一层的结点按照从左到右的顺序打印。

"""

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def print_tree_level(self, p_node):
        """
        层次遍历不分行打印二叉树

        :param p_node: 根节点
        :return: 从左向右打印节点
        """
        if p_node is None:
            return

        stack = []
        stack.append(p_node)
        while len(stack) > 0:
            current_node = stack.pop(0)
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)
            print(current_node.val, end=" ")
        print(end="\n")

    def print_tree_level_lines(self, p_node):
        """
        层次遍历分行打印二叉树

        :param p_node: 根节点
        :return: 分行打印节点
        """
        if p_node is None:
            return

        stack = []
        stack.append(p_node)
        current_nums = 1
        next_nums = 0
        while len(stack) > 0:
            current_node = stack.pop(0)
            if current_node.left:
                stack.append(current_node.left)
                next_nums += 1
            if current_node.right:
                stack.append(current_node.right)
                next_nums += 1
            print(current_node.val, end=" ")
            current_nums -= 1
            if current_nums == 0:
                print("", end="\n")
                current_nums = next_nums
                next_nums = 0

    def print_tree_level_S(self, p_node):
        """
        层次遍历之字形打印二叉树

        :param p_node: 根节点
        :return: 分行打印节点
        """
        if p_node is None:
            return

        stack = [[] for _ in range(2)]
        current = 1
        next = 0

        stack[1].append(p_node)
        while len(stack[current]) > 0 or len(stack[next]) > 0:
            current_node = stack[current].pop(0)
            if current == 1:
                if current_node.left:
                    stack[next].insert(0, current_node.left)
                if current_node.right:
                    stack[next].insert(0, current_node.right)
            else:
                if current_node.right:
                    stack[next].insert(0, current_node.right)
                if current_node.left:
                    stack[next].insert(0, current_node.left)

            print(current_node.val, end=" ")

            if len(stack[current]) == 0:
                current = 1 - current
                next = 1 - next
                print("", end="\n")


if __name__ == '__main__':
    node1 = Node(8)
    node2 = Node(6)
    node3 = Node(10)
    node4 = Node(5)
    node5 = Node(7)
    node6 = Node(9)
    node7 = Node(11)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    S = Solution()
    # S.print_tree_level(node1)
    # S.print_tree_level_lines(node1)
    S.print_tree_level_S(node1)