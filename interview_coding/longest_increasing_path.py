"""

给定一个整数矩阵,找到增加最长路径的长度。
从每一个单元格,你可以移到四个方向:左,右,向上或向下。你不能移到对角线移动或移动以外的边界(即缠绕是不允许的)。

比较本题与机器人行走问题：
机器人行走的范围问题只需一行递归语句，因为机器人的行走范围是持续累加的。
本题要找到顺序行走的最长路径，需要找到四个方向中的最大路径，因此需要四条递归语句(满足一定条件)，在四个方向上递归寻找，可理解为找树的
最大高度(左右孩子分别递归返回最大值)，本题为四个方向分别递归返回最大值，使用动态规划，即缓存，提高计算性能；

"""

class Solution:
    """
    给定一个整数矩阵,找到增加最长路径的长度。
    """
    def longest_increasing_path(self, matrix):
        """
        对矩阵中的每一个坐标计算最远距离

        :param matrix: 整数矩阵
        :return: 最长路径的长度
        """
        rows = len(matrix)
        cols = len(matrix[0])

        # 动态规划，用于保存已计算的坐标位置
        lens = [[-1] * cols for _ in range(rows)]

        max_path = 0
        for row in range(rows):
            for col in range(cols):
                max_path = max(max_path, self.longest_increasing_path_core(matrix, rows, cols, row, col, lens))

        return max_path + 1

    def longest_increasing_path_core(self, matrix, rows, cols, row, col, lens):
        """
        寻找四个方向上的最大路径

        :param matrix: 整数矩阵
        :param rows: 行数
        :param cols: 列数
        :param row: 当前行
        :param col: 当前列
        :param lens: 动态规划缓存数组
        :return: 最大路径长度
        """
        # 利用缓存节省计算时间
        if lens[row][col] != -1:
            return lens[row][col]

        # 每个坐标四个方向分别递归
        left, right, up, down = 0, 0, 0, 0
        if col - 1 >= 0 and matrix[row][col] < matrix[row][col-1]:
            left = 1 + self.longest_increasing_path_core(matrix, rows, cols, row, col-1, lens)
        if row - 1 >= 0 and matrix[row][col] < matrix[row-1][col]:
            up = 1 + self.longest_increasing_path_core(matrix, rows, cols, row-1, col, lens)
        if col + 1 < cols and matrix[row][col] < matrix[row][col+1]:
            right = 1 + self.longest_increasing_path_core(matrix, rows, cols, row, col+1, lens)
        if row + 1 < rows and matrix[row][col] < matrix[row+1][col]:
            down = 1 + self.longest_increasing_path_core(matrix, rows, cols, row+1, col, lens)

        # 求四个方向的最大路径
        lens[row][col] = max(max(left, right), max(up, down))

        return lens[row][col]

if __name__ == '__main__':
    nums1 = [[9, 9, 4],
            [6, 6, 8],
            [2, 1, 1]]

    nums2 = [[3,4,5],
             [3,2,6],
             [2,2,1]]

    S = Solution()
    result = S.longest_increasing_path(nums2)
    print(result)





