"""

面试题33：二叉搜索树的后序遍历序列
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则返回true，否则返回false。假设输入的数组的任意两个数字都互不相同。

"""
class Solution:
    def verify_sequence_BST(self, array, start, end):
        if array is None or start > end:
            return False

        root_node = array[end]

        mid = 0
        for i in range(start, end+1):
            mid = i
            if array[i] > root_node:
                break

        for j in range(mid, end):
            if array[j] < root_node:
                return False

        left = True  # 终止条件（叶节点）
        if mid - start > 1:
            left = self.verify_sequence_BST(array, start, mid-1)

        right = True  # 终止条件（叶节点）
        if end - mid > 1:
            right = self.verify_sequence_BST(array, mid, end-1)

        return left and right

if __name__ == '__main__':
    S = Solution()
    array = [5, 7, 6, 9, 11, 10, 8]
    array2 = [4, 6, 7, 5]
    array3 = [1, 2, 3, 4, 5]
    array4 = [5]
    array5 = [7, 4, 6, 5]
    array6 = [4, 6, 12, 8, 16, 14, 10]
    verify = array6
    result = S.verify_sequence_BST(verify, 0, len(verify)-1)
    print(result)

