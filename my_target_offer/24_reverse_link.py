"""

面试题24：反转链表
题目：定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的
头结点。

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reverse_link(self, p_head):
        """
        反转链表

        :param p_head: 链表头
        :return: 新的链表头
        """
        # 传入空链表或单个节点的链表
        if p_head is None or p_head.next is None:
            return p_head

        # 链表有两个节点
        p_next = p_head.next
        p_head.next = None
        if p_next.next is None:
            p_next.next = p_head
            p_head = p_next
            return p_head

        # 链表三个节点以上
        p_pre_node = p_head
        p_current = p_next
        p_next = p_next.next
        while p_next is not None:
            p_current.next = p_pre_node
            p_pre_node = p_current
            p_current = p_next
            p_next = p_next.next
            p_current.next = p_pre_node

        p_head = p_current

        return p_head

    def reverse_link2(self, p_head):
        p_reverse_head = None
        p_node = p_head
        p_pre = None
        while p_node is not None:
            p_next = p_node.next

            if p_next is None:
                p_reverse_head = p_node

            p_node.next = p_pre

            p_pre = p_node
            p_node = p_next

        return p_reverse_head

    @staticmethod
    def print_list(p_head):
        if p_head is None:
            return

        p_next = p_head
        while p_next is not None:
            print(p_next.val, end=" ")
            p_next = p_next.next
        print(end="\n")


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)

    node1.next = node2

    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9


    S = Solution()

    print("------当输入为空指针：------")
    node = None
    S.print_list(node)
    node = S.reverse_link(node)
    S.print_list(node)

    print("------当输入链表只有一个节点：------")
    S.print_list(node2)
    node2 = S.reverse_link(node2)
    S.print_list(node2)

    print("------当输入链表有2个节点：------")
    S.print_list(node1)
    node1 = S.reverse_link(node1)
    S.print_list(node1)

    print("------当输入链表有多个节点：------")
    S.print_list(node3)
    node3 = S.reverse_link(node3)
    S.print_list(node3)







