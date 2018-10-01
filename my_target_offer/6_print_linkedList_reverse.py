class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def print_linked_list(self, array_list):
        print_list = []
        if array_list is None:
            return print_list

        while array_list:
            print_list.insert(0, array_list.val)
            array_list = array_list.next

        return  print_list

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    node3.next = None

    node = None

    S = Solution()
    result = S.print_linked_list(node2)
    print(result)

