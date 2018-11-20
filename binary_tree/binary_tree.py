import math
import queue
import copy

class TreeNode:
    """
    二叉树节点
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    二叉树的求解：递归 + 迭代
    """
    def __init__(self):
        self.result = []

    def max_depth(self, node):
        """
        求二叉树的最大深度
        """
        if node is None:
            return 0

        left = self.max_depth(node.left)
        right = self.max_depth(node.right)

        return max(left, right) + 1

    def min_depth(self, node):
        """
        求二叉树的最小深度
        """
        if node is None:
            return 0

        left = self.min_depth(node.left)
        right = self.min_depth(node.right)

        return min(left, right) + 1


    def node_count(self, node):
        """
        求二叉树中节点的个数
        """
        if node is None:
            return 0

        left = self.node_count(node.left)
        right = self.node_count(node.right)

        return left + right + 1

    def leaf_node_count(self, node):
        """
        求二叉树中叶子节点的个数
        """
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        left = self.leaf_node_count(node.left)
        right = self.leaf_node_count(node.right)

        return left + right

    def k_level_count(self, node, k):
        """
        求二叉树中第k层节点的个数
        """
        if k < 1 or node is None:
            return 0

        if k == 1:
            return 1

        left = self.k_level_count(node.left, k-1)
        right = self.k_level_count(node.right, k-1)

        return left + right

    def is_balance_binary_tree(self, node):
        """
        判断二叉树是否是平衡二叉树
        """
        return self.max_depth2(node) != -1

    def max_depth2(self, node):
        """
        检查树是否平衡
        """
        if node is None:
            return 0

        left = self.max_depth2(node.left)
        right = self.max_depth2(node.right)
        if left == -1 or right == -1 or math.fabs(left - right) > 1:
            return -1

        return max(left, right) + 1

    @staticmethod
    def is_complete_binary_tree(node):
        """
        判断二叉树是否是完全二叉树：层次遍历，如果一个节点缺少孩子，则剩下的节点都应该没有孩子。
        """
        if node is None:
            return True

        _queue = queue.Queue()
        _queue.put(node)
        has_no_child = False
        result = True
        while not _queue.empty():
            current_node = _queue.get()
            if not has_no_child:
                if current_node.left is not None and current_node.right is not None:
                    _queue.put(current_node.left)
                    _queue.put(current_node.right)
                elif current_node.left is None and current_node.right is not None:
                    result = False
                    break
                elif current_node.left is not None and current_node.right is None:
                    _queue.put(current_node.left)
                    has_no_child = True
                else:
                    has_no_child = True
            else:
                if current_node.left is not None or current_node.right is not None:
                    result = False
                    break
        return result

    def is_common_tree(self, node1, node2):
        """
        两个二叉树是否完全相同
        """
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False

        if node1.val != node2.val:
            return False

        left = self.is_common_tree(node1.left, node2.left)
        right = self.is_common_tree(node1.right, node2.right)

        return left and right

    def is_mirror(self, node1, node2):
        """
        两个二叉树是否互为镜像
        """
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False

        if node1.val != node2.val:
            return False

        left = self.is_mirror(node1.left, node2.right)
        right = self.is_mirror(node1.right, node2.left)

        return left and right

    def mirror_tree_node(self, node):
        """
        翻转二叉树 or 镜像二叉树
        """
        if node is None:
            return None

        left = self.mirror_tree_node(node.left)
        right = self.mirror_tree_node(node.right)

        # 每次都新建节点，不然会修改原始链表
        new_node = TreeNode(node.val)
        new_node.left = right
        new_node.right = left
        return new_node

    def get_last_common_parent(self):
        """
        求两个二叉树的最低公共祖先节点
        """
        pass

    def pre_order(self, node):
        """
        二叉树的先序遍历
        """
        result = []
        self.pre(node, result)
        return result

    def pre(self, node, result):
        if node is None:
            return

        result.append(node.val)
        self.pre(node.left, result)
        self.pre(node.right, result)

    def in_order(self, node):
        """
        二叉树的中序遍历
        """
        result = []
        self.inside(node, result)
        return result

    def inside(self, node, result):
        if node is None:
            return

        self.inside(node.left, result)
        result.append(node.val)
        self.inside(node.right, result)

    def post_order(self, node):
        """
        二叉树的后序遍历
        """
        result = []
        self.post(node, result)
        return result

    def post(self, node, result):
        if node is None:
            return

        self.post(node.left, result)
        self.post(node.right, result)
        result.append(node.val)

# 前序遍历和后序遍历构造二叉树


# 在二叉树中插入节点


    def find_path2(self, node, sum):
        sum -= node.val
        self.result.append(node.val)

        if node.left is None and node.right is None and sum == 0:
            print(self.result)

        if node.left is not None:
            self.find_path2(node.left, sum)
        if node.right is not None:
            self.find_path2(node.right, sum)
        if len(self.result) != 0:
            self.result.pop(-1)

    def find_path(self, node, sum):
        """输入一个二叉树和一个整数，打印出二叉树中节点值的和等于输入整数所有的路径"""
        if node is None:
            return

        stack = []
        path_sum = 0

        self.find_sum_core(node, sum, stack, path_sum)

    def find_sum_core(self, node, sum, stack, path_sum):
        stack.append(node.val)
        path_sum += node.val

        if node.left is None and node.right is None:
            if path_sum == sum:
                self.result.append(copy.deepcopy(stack))

        if node.left is not None:
            self.find_sum_core(node.left, sum, stack, path_sum)

        if node.right is not None:
            self.find_sum_core(node.right, sum, stack, path_sum)

        stack.pop(-1)

# 二叉树的搜索区间

    @staticmethod
    def level_order(node):
        """
        二叉树的层次遍历
        """
        if node is None:
            return

        result = []
        _queue = queue.Queue()
        _queue.put(node)
        while not _queue.empty():
            current_node = _queue.get()
            result.append(current_node.val)
            if current_node.left is not None:
                _queue.put(current_node.left)
            if current_node.right is not None:
                _queue.put(current_node.right)
        return result

# 二叉树内两个节点的最长距离


# 不同的二叉树


# 判断二叉树是否是合法的二叉查找树(BST)


if __name__ == '__main__':
    """
    tree1:                   tree2:
               a                    a         
            /     \              /     \      
           b        c           b        c    
          / \      / \         / \      /     
         d   e    f   g       d   e    f      
        /   / \              /   / \          
       k   h   i            k   h   i         
          /                                   
         j                                    
    """
    # tree1
    node_a = TreeNode("a")
    node_b = TreeNode("b")
    node_c = TreeNode("c")
    node_d = TreeNode("d")
    node_e = TreeNode("e")
    node_f = TreeNode("f")
    node_g = TreeNode("g")
    node_h = TreeNode("h")
    node_i = TreeNode("i")
    node_j = TreeNode("j")
    node_k = TreeNode("k")
    node_a.left = node_b
    node_a.right = node_c
    node_b.left = node_d
    node_b.right = node_e
    node_c.left = node_f
    node_c.right = node_g
    node_d.left = node_k
    node_e.left = node_h
    node_e.right = node_i
    node_h.left = node_j

    # tree2
    node2_a = TreeNode("a")
    node2_b = TreeNode("b")
    node2_c = TreeNode("c")
    node2_d = TreeNode("d")
    node2_e = TreeNode("e")
    node2_f = TreeNode("f")
    node2_h = TreeNode("h")
    node2_i = TreeNode("i")
    node2_k = TreeNode("k")
    node2_a.left = node2_b
    node2_a.right = node2_c
    node2_b.left = node2_d
    node2_b.right = node2_e
    node2_c.left = node2_f
    node2_d.left = node2_k
    node2_e.left = node2_h
    node2_e.right = node2_i


    root1 = node_a
    root2 = node2_a
    S = Solution()

    #-----------------Test-----------------
    '''
    print("****** Test max depth: ******")
    max_depth = S.max_depth(node_b)
    print("max depth is: ", max_depth)

    print("****** Test min depth: ******")
    min_depth = S.min_depth(node_k)
    print("min depth is: ", min_depth)

    print("****** Test node count: ******")
    node_count = S.node_count(root)
    print("node count is: ", node_count)

    print("****** Test leaf node count: ******")
    leaf_node_count = S.leaf_node_count(root)
    print("leaf node count is: ", leaf_node_count)
    '''


    print("****** Test k level count: ******")
    k_level_count = S.k_level_count(node_a, 1)
    print("k level count is: ", k_level_count)

    '''
    print("****** Test binary tree is balance: ******")
    is_balance_binary_tree = S.is_balance_binary_tree(node_e)
    print("binary tree is balance: ", is_balance_binary_tree)
    

    print("****** Test binary tree is complete: ******")
    is_complete_binary_tree = S.is_complete_binary_tree(node_j)
    print("binary tree is complete: ", is_complete_binary_tree)

    print("****** Test tree1 and tree2 is common tree: ******")
    is_common_tree = S.is_common_tree(node_d, node2_d)
    print("binary tree is common tree: ", is_common_tree)
    
    node1_a = TreeNode('a')
    node1_b = TreeNode('b')
    node1_c = TreeNode('c')
    node1_a.left = node1_b
    node1_a.right = node1_c

    node2_a = TreeNode('a')
    node2_b = TreeNode('b')
    node2_c = TreeNode('c')
    node2_a.left = node2_c
    node2_a.right = node2_b
    print("****** Test tree1 and tree2 is mirror: ******")
    is_mirror = S.is_mirror(node1_a, node2_a)
    print("binary tree is mirror: ", is_mirror)

    print("****** Test binary tree's mirror tree node: ******")
    mirror_tree = S.mirror_tree_node(root1)
    is_mirror = S.is_mirror(root1, mirror_tree)
    print("binary tree is mirror: ", is_mirror)

    print("****** Test binary tree's level order: ******")
    level_order = S.level_order(root1)
    print("binary tree level order is: \n", level_order)

    print("****** Test binary tree's pre order: ******")
    pre_order = S.pre_order(root1)
    print("binary tree pre order is: \n", pre_order)

    print("****** Test binary tree's in order: ******")
    in_order = S.in_order(root1)
    print("binary tree in order is: \n", in_order)

    print("****** Test binary tree's post order: ******")
    post_order = S.post_order(root1)
    print("binary tree post order is: \n", post_order)
    '''

    '''
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(7)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    print("****** Test the link of sum is target: ******")
    S.find_path(node1, 10)
    print(S.result)

    '''









