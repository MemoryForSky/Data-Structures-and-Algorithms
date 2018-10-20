"""
面试题22：链表中倒数第k个结点
题目：输入一个链表，输出该链表中倒数第k个结点。为了符合大多数人的习惯，
本题从1开始计数，即链表的尾结点是倒数第1个结点。例如一个链表有6个结点，
从头结点开始它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个结点是
值为4的结点。
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def select_node(self, p_node, k):
        if p_node is None or k == 0:
            return

        p_node1 = p_node
        p_node2 = p_node
        for i in range(k):
            if p_node1 is not None:
                p_node1 = p_node1.next
            else:
                return

        while p_node1 is not None:
            p_node1 = p_node1.next
            p_node2 = p_node2.next

        return p_node2.val

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    S = Solution()
    result = S.select_node(node1, 3)
    print(result)




