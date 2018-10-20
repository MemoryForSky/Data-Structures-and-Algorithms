"""

面试题23：链表中环的入口结点

题目：一个链表中包含环，如何找出环的入口结点？

例如，在图3.8的链表中，环的入口结点是结点3。

         -----------
        |           |
1 - 2 - 3 - 4 - 5 - 6

"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def meet_index(self, p_head):
        """
        有环的话，获取环内的节点

        :param p_head: 链表入口节点
        :return: -1：链表没有环；其它：环内的节点
        """
        if p_head is None:
            return -1

        # 每次后移都需检查是否为空
        p_slow = p_head.next
        if p_slow is None:
            return -1

        p_fast = p_slow.next
        while p_fast is not None and p_slow is not None:
            # 快节点追上慢节点则有环，返回环内节点
            if p_fast == p_slow:
                return p_fast

            p_slow = p_slow.next

            p_fast = p_fast.next
            if p_fast is not None:
                p_fast = p_fast.next

        return -1

    def entry_node(self, p_head):
        """
        找到环的入口节点

        :param p_head: 链表入口
        :return: None：没有环；其它：环的入口节点；
        """
        # 检查是否有环
        meeting_node = self.meet_index(p_head)
        if meeting_node == -1:
            return

        # 有环，统计环的长度
        loop_length = 1
        p_node1 = meeting_node.next
        while p_node1 is not meeting_node:
            loop_length += 1
            p_node1 = p_node1.next

        # 第一个指针先移动环的长度，然后第二个指针开始移动，直到环的入口位置相遇
        p_node1 = p_head
        for i in range(loop_length):
            p_node1 = p_node1.next

        p_node2 = p_head
        while p_node1 is not p_node2:
            p_node1 = p_node1.next
            p_node2 = p_node2.next

        return p_node1


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
    node6.next = node3

    S = Solution()
    p_node = S.entry_node(node1)
    if p_node is not None:
        print("环的入口位置的值为：", p_node.val)
    else:
        print("the list link did not have a loop...")



