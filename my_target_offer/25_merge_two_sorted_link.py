"""
面试题25：合并两个排序的链表
题目：输入两个递增排序的链表，合并这两个链表并使新链表中的结点仍然是按
照递增排序的。例如输入图3.11中的链表1和链表2，则合并之后的升序链表如链
表3所示。
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def merge_sorted_link(self, p_head1, p_head2):
        p_link1 = p_head1
        p_link2 = p_head2

        if p_link1 is None:
            return p_link2
        if p_link2 is None:
            return p_link1

        if p_link1.val <= p_link2.val:
            p_new_head = p_link1
        else:
            p_new_head = p_link2

        # 循环实现
        while p_link1 is not None and p_link2 is not None:
            if p_link1.val <= p_link2.val:
                p_next = p_link1.next
                # 考虑相邻节点相等
                while p_next is not None and p_next.val == p_link1.val:
                    p_link1 = p_next
                    p_next = p_next.next
                p_link1.next = p_link2
                p_link1 = p_next
            else:
                p_next = p_link2.next
                while p_next is not None and p_next.val == p_link2.val:
                    p_link2 = p_next
                    p_next = p_next.next
                p_link2.next = p_link1
                p_link2 = p_next

        return p_new_head

    def merge(self, p_head1, p_head2):
        p_link1 = p_head1
        p_link2 = p_head2

        if p_link1 is None:
            return p_link2
        if p_link2 is None:
            return p_link1

        # 递归实现
        if p_link1.val < p_link2.val:
            p_new_head = p_link1
            p_new_head.next = self.merge(p_link1.next, p_link2)
        else:
            p_new_head = p_link2
            p_new_head.next = self.merge(p_link1, p_link2.next)

        return p_new_head

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
    node11 = Node(1)
    node12 = Node(3)
    node13 = Node(3)
    node14 = Node(7)

    node21 = Node(2)
    node22 = Node(4)
    node23 = Node(7)
    node24 = Node(8)

    node11.next = node12
    node12.next = node13
    node13.next = node14

    node21.next = node22
    node22.next = node23
    node23.next = node24

    S = Solution()

    print("------当输入为空指针：------")
    node1 = None
    node2 = None
    node = S.merge(node1,node2)
    S.print_list(node)

    print("------当输入为两个排序链表：------")
    node = S.merge(node11, node21)
    S.print_list(node)





