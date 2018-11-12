"""

面试题35：复杂链表的复制
题目：请实现函数ComplexListNode* Clone(ComplexListNode* pHead)，复
制一个复杂链表。在复杂链表中，每个结点除了有一个m_pNext指针指向下一个
结点外，还有一个m_pSibling 指向链表中的任意结点或者nullptr。

"""

class Node:
    def __init__(self, x):
        self.val = x
        self.m_pNext = None
        self.m_pSibling = None

class Solution1:
    def clone(self, p_head):
        if p_head is None:
            return

        sibling_dict = {}
        old_copy_node = p_head
        sibling_dict[p_head] = p_head.m_pSibling
        new_head = Node(old_copy_node.val)
        new_copy_node = new_head
        if old_copy_node.m_pNext:
            old_copy_node = old_copy_node.m_pNext

        while old_copy_node:
            sibling_dict[old_copy_node] = old_copy_node.m_pSibling

            new_next_node = Node(old_copy_node.val)
            new_copy_node.m_pNext = new_next_node
            new_copy_node = new_next_node

            old_copy_node = old_copy_node.m_pNext

        old_copy_node = p_head
        new_copy_node = new_head

        while old_copy_node:
            new_copy_node.m_pSibling = sibling_dict[old_copy_node]
            new_copy_node = new_copy_node.m_pNext
            old_copy_node = old_copy_node.m_pNext

        return new_head

    def print(self, p_head):
        if p_head is None:
            return

        while p_head:
            print("(", p_head.val, p_head.m_pNext.val if p_head.m_pNext else "None", p_head.m_pSibling.val if p_head.m_pSibling else "None", ")")
            p_head = p_head.m_pNext

class Solution2(Solution1):
    def clone(self, p_head):
        if p_head is None:
            return

        self.clone_nodes(p_head)
        self.connect_sibling_nodes(p_head)
        p_new_head = self.reconnect_nodes(p_head)
        return p_new_head

    def clone_nodes(self, p_head):
        p_node = p_head

        while p_node:
            p_cloned = Node(p_node.val)
            p_cloned.m_pNext = p_node.m_pNext
            p_node.m_pNext = p_cloned

            p_node = p_cloned.m_pNext

    def connect_sibling_nodes(self, p_head):
        p_old_node = p_head
        p_new_node = p_head.m_pNext
        while p_old_node:
            if p_old_node.m_pSibling:
                p_new_node.m_pSibling = p_old_node.m_pSibling.m_pNext
            else:
                p_new_node.m_pSibling = None
            p_old_node = p_new_node.m_pNext
            if p_old_node:
                p_new_node = p_old_node.m_pNext

    def reconnect_nodes(self, p_head):
        p_old_head = p_head
        p_new_head = p_head.m_pNext
        p_old_node = p_old_head
        p_new_node = p_new_head
        while p_new_node.m_pNext:
            p_old_node.m_pNext = p_new_node.m_pNext
            p_old_node = p_new_node.m_pNext
            p_new_node.m_pNext = p_old_node.m_pNext
            p_new_node = p_old_node.m_pNext

        p_old_node.m_pNext = None

        return p_new_head

class Test:
    def test1(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)

        node1.m_pNext = node2
        node1.m_pSibling = node3
        node2.m_pNext = node3
        node2.m_pSibling = node5
        node3.m_pNext = node4
        node4.m_pNext = node5
        node4.m_pSibling = node2

        return node1

    def test2(self):
        """
        m_pSibling形成环
        """
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)


        node1.m_pNext = node2
        node2.m_pNext = node3
        node2.m_pSibling = node4
        node3.m_pNext = node4
        node4.m_pNext = node5
        node4.m_pSibling = node2

        return node1

    def test3(self):
        """
        m_pSibling指向结点自身
        """
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)

        node1.m_pNext = node2
        node2.m_pNext = node3
        node2.m_pSibling = node5
        node3.m_pNext = node4
        node3.m_pSibling = node3
        node4.m_pNext = node5
        node4.m_pSibling = node2

        return node1

    def test4(self):
        """
        只有一个结点
        """
        node1 = Node(1)
        node1.m_pSibling = node1
        return node1

    def test5(self):
        """
        鲁棒性测试
        """
        node1 = None
        return node1

if __name__ == '__main__':
    T = Test()
    node1 = T.test1()

    # S1 = Solution1()
    # new_link = S1.clone(node1)
    # S1.print(new_link)

    S2 = Solution2()
    new_link = S2.clone(node1)
    print("-----------old link-----------")
    S2.print(node1)
    print("-----------new link-----------")
    S2.print(new_link)



