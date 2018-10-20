"""
面试题18（一）：在O(1)时间删除链表结点
题目：给定单向链表的头指针和一个结点指针，定义一个函数在O(1)时间删除该
结点。
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __del__(self):
        self.val = None
        self.next = None

class Solution:
    def delete_node(self, p_head, to_be_delete):
        if p_head is None or to_be_delete is None:
            return

        if to_be_delete.next is not None:
            delete_next = to_be_delete.next
            to_be_delete.val = delete_next.val
            to_be_delete.next = delete_next.next
            delete_next.__del__()

        elif p_head == to_be_delete:
            to_be_delete.__del__()
            p_head.__del__()
        else:
            p_next = p_head
            while p_next.next is not to_be_delete:
                p_next = p_next.next
            to_be_delete.__del__()
            p_next.next = None

    @staticmethod
    def print_list(p_head):
        if p_head is None:
            return

        p_next = p_head
        while p_next is not None:
            print(p_next.val)
            p_next = p_next.next


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
    print("删除节点前：")
    S.print_list(node1)
    S.delete_node(node1, node6)
    print("删除节点后：")
    S.print_list(node1)




