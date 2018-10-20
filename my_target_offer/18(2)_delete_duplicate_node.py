"""
面试题18（二）：删除链表中重复的结点
题目：在一个排序的链表中，如何删除重复的结点？
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __del__(self):
        self.val = None
        self.next = None

class Solution:
    def delete_duplicate_node1(self, p_head):
        """
        去重
        """
        if p_head is None:
            return

        p_next = p_head
        while p_next is not None:
            flag_duplicate = False
            p_duplicate = p_next.next
            while p_duplicate is not None and p_duplicate.val == p_next.val:
                p_tmp = p_duplicate
                p_duplicate = p_duplicate.next
                p_tmp.__del__()
                flag_duplicate = True
            if flag_duplicate:
                p_next.next = p_duplicate
            p_next = p_next.next

    def delete_duplicate_node2(self, root):
        """
        保留唯一的节点
        """
        if root is None:
            return

        p_pre_node = None
        p_node = root
        while p_node is not None:
            p_next = p_node.next
            need_delete = False
            if p_next is not None and p_node.val == p_next.val:
                need_delete = True

            if not need_delete:
                p_pre_node = p_node
                p_node = p_next
            else:
                value = p_node.val
                p_to_be_delete = p_node

                while p_to_be_delete is not None and p_to_be_delete.val == value:
                    p_next = p_to_be_delete.next
                    p_to_be_delete.__del__()
                    p_to_be_delete = p_next

                if p_pre_node is None:
                    root = p_next
                else:
                    p_pre_node.next = p_next
                p_node = p_next


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
    node2 = Node(1)
    node3 = Node(1)
    node4 = Node(1)
    node5 = Node(1)
    node6 = Node(6)
    node7 = None

    root = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    S = Solution()
    print("节点去重前：")
    S.print_list(root)
    S.delete_duplicate_node2(root)
    print("节点去重后：")
    S.print_list(root)







