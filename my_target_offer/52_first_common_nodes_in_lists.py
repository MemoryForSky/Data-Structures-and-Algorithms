"""

面试题52：两个链表的第一个公共结点
题目：输入两个链表，找出它们的第一个公共结点。

"""
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    @staticmethod
    def find_first_common_node(p_head1, p_head2):
        if p_head1 is None or p_head2 is None:
            return

        node1_len = 0
        node2_len = 0
        node1 = p_head1
        node2 = p_head2

        while node1:
            node1_len += 1
            node1 = node1.next

        while node2:
            node2_len += 1
            node2 = node2.next

        if node1_len > node2_len:
            ahead_step = node1_len - node2_len
            for _ in range(ahead_step):
                p_head1 = p_head1.next
        else:
            ahead_step = node2_len - node1_len
            for _ in range(ahead_step):
                p_head2 = p_head2.next

        while p_head1 and p_head2:
            if p_head1 == p_head2:
                return p_head1.val

            p_head1 = p_head1.next
            p_head2 = p_head2.next


if __name__ == '__main__':
    node11 = Node(1)
    node12 = Node(2)
    node13 = Node(3)
    node14 = Node(4)
    node15 = Node(5)
    node21 = Node(6)
    node22 = Node(7)
    node23 = Node(8)

    node11.next = node12
    node12.next = node13
    node13.next = node14
    node14.next = node15
    node21.next = node22
    node22.next = node23

    S = Solution()
    common_node = S.find_first_common_node(node11, node21)
    print(common_node)



