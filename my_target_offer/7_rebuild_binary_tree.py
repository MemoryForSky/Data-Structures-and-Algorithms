"""

输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

"""

# 二叉树节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 重建二叉树
class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if not pre and not tin:
            return None
        root = TreeNode(pre[0])
        if set(pre) != set(tin):
            return None
        i = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:i + 1], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i + 1:], tin[i + 1:])
        return root

    # 链表的层次遍历：队列
    def PrintNodeByLevel(self, treeNode):
        q = []
        if treeNode is None:
            return 0

        t = treeNode
        while t:
            print(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
            if q:
                t = q.pop(0)
            else:
                break


if __name__ == '__main__':
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    S = Solution()
    root = S.reConstructBinaryTree(pre, tin)

    S.PrintNodeByLevel(root)





