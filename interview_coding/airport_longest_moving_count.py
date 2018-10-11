"""
华为：最长陆地飞机场

问题：演练场的范围为M*N，海平面高度为H，若演练场中的坐标高度小于海平面高度且与边缘相连，
则为海洋，其余均为陆地，如下例中(0,3), (1,3)为海洋，(1,1)不与边缘相连视为陆地。
在陆地上海拔高度持续降低的路径可以作为飞机场，求出给定矩阵中可以作为飞机场的最长路径。
比如：下例中最长路径为13 -> 12 -> 11 -> 10 -> 9 -> 2 -> 0

输入：
3 5 0
14 2 9 10 11
7 0 9 0 12
7 7 10 0 13

输出：
7
"""

class Solution:
    def moving_count(self, matrix, rows, cols, H):
        """
        对每个陆地坐标计算其能达到的最远距离

        :param matrix: 整数矩阵
        :param rows: 行数
        :param cols: 列数
        :param H: 海平面高度
        :return: 最大递减距离
        """
        ocean = [[0] * cols for i in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] <= H:
                    is_ocean = self.verify(matrix, rows, cols, row, col, H)
                    if is_ocean:
                        ocean[row][col] = 1

        lens = [[-1] * cols for _ in range(rows)]
        max_path = 0
        for row in range(rows):
            for col in range(cols):
                if ocean[row][col] == 0:
                    max_path = max(max_path, self.moving_count_core(matrix, rows, cols, row, col, lens, ocean))

        return max_path + 1

    def moving_count_core(self, matrix, rows, cols, row, col, lens, ocean):
        """
        寻找四个方向上的最大路径

        :param matrix: 整数矩阵
        :param rows: 行数
        :param cols: 列数
        :param row: 当前行
        :param col: 当前列
        :param lens: 缓存数组
        :param ocean: 海洋坐标标志数组
        :return: 某坐标可达到的最远距离

        """
        if lens[row][col] != -1:
            return lens[row][col]

        left, right, up, down = 0, 0, 0, 0
        if col - 1 >= 0 and ocean[row][col - 1] == 0 and matrix[row][col] > matrix[row][col - 1]:
            left = 1 + self.moving_count_core(matrix, rows, cols, row, col - 1, lens, ocean)
        if row - 1 >= 0 and ocean[row - 1][col] == 0 and matrix[row][col] > matrix[row - 1][col]:
            up = 1 + self.moving_count_core(matrix, rows, cols, row - 1, col, lens, ocean)
        if col + 1 < cols and ocean[row][col + 1] == 0 and matrix[row][col] > matrix[row][col + 1]:
            right = 1 + self.moving_count_core(matrix, rows, cols, row, col + 1, lens, ocean)
        if row + 1 < rows and ocean[row + 1][col] == 0 and matrix[row][col] > matrix[row + 1][col]:
            down = 1 + self.moving_count_core(matrix, rows, cols, row + 1, col, lens, ocean)

        lens[row][col] = max(max(left, right), max(up, down))

        return lens[row][col]

    def verify(self, matrix, rows, cols, row, col, H):
        """
        判断矩阵内的海洋坐标

        :param matrix: 整数矩阵
        :param rows: 行数
        :param cols: 列数
        :param row: 当前行
        :param col: 当前列
        :param H: 海平面高度
        :return: 当前坐标是否海洋
        """
        if matrix[row][col] > H:
            return False

        if row == 0 or col == 0 or row == rows-1 or col == cols-1:
            return True

        is_ocean = self.verify(matrix, rows, cols, row, col - 1, H) \
                   or self.verify(matrix, rows, cols, row - 1, col, H) \
                   or self.verify(matrix, rows, cols, row, col + 1, H) \
                   or self.verify(matrix, rows, cols, row + 1, col, H)

        return is_ocean


# Test
if __name__ == '__main__':
    M = 3
    N = 5
    Height = 0
    matrix1 = [[14, 2, 9, 10, 11],
              [7, 0, 9, 0, 12],
              [7, 7, 10, 0, 13]]

    S = Solution()
    result = S.moving_count(matrix1, M, N, Height)
    print(result)



