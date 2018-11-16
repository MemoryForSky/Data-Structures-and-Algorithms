"""

面试题47：礼物的最大价值
题目：在一个m×n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值
（价值大于0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向左或
者向下移动一格直到到达棋盘的右下角。给定一个棋盘及其上面的礼物，请计
算你最多能拿到多少价值的礼物？

"""

class Solution1:
    """
    递归解法

    (0, 0)------ 向右
      |   \
      |    \
      |     \ 递归（自上而下）
     向下

    迭代公式：
    向下：(row + 1, col)
    向右：(row, col + 1)

    """
    def get_max_value(self, matrix):
        if not isinstance(matrix, list) or len(matrix) == 0:
            return

        rows = len(matrix)
        cols = len(matrix[0])

        return self.get_max_value_core(matrix, rows, cols, 0, 0)

    def get_max_value_core(self, matrix, rows, cols, row, col):
        """递归过程"""
        if row == rows - 1 and col == cols - 1:
            return matrix[row][col]

        if row < rows and col < cols:
            down_val = matrix[row][col] + self.get_max_value_core(matrix, rows, cols, row + 1, col)
            right_val = matrix[row][col] + self.get_max_value_core(matrix, rows, cols, row, col + 1)
            return max(down_val, right_val)
        else:
            return 0

class Solution2:
    """
    动态规划

                  向上
     (自下而上) \    |
                \   |
                 \  |
       向左-------(0, 0)

    迭代公式：
    向上：(row - 1, col)
    向左：(row, col - 1)

    """
    def get_max_value(self, matrix):
        if not isinstance(matrix, list) or len(matrix) == 0:
            return

        rows = len(matrix)
        cols = len(matrix[0])

        return self.get_max_value_core(matrix, rows, cols)

    def get_max_value_core(self, matrix, rows, cols):
        max_value = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0

                # 保证第一行和第一列不会报错
                if i > 0:
                    up = max_value[i - 1][j]
                if j > 0:
                    left = max_value[i][j - 1]

                max_value[i][j] = max(left, up) + matrix[i][j]

        return max_value[rows - 1][cols - 1]

class Solution3:
    """

    动态规划：节省空间

    """
    def get_max_value(self, matrix):
        if not isinstance(matrix, list) or len(matrix) == 0:
            return

        rows = len(matrix)
        cols = len(matrix[0])

        return self.get_max_value_core(matrix, rows, cols)

    def get_max_value_core(self, matrix, rows, cols):
        max_value = [0] * cols

        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0

                if i > 0:
                    up = max_value[j]
                if j > 0:
                    left = max_value[j - 1]

                max_value[j] = max(left, up) + matrix[i][j]

        return max_value[cols-1]

class Test:
    def test(self, matrix, target):
        S = Solution3()
        output = S.get_max_value(matrix)
        print("output: ", output, ", max value: ", target)


    def test1(self):
        matrix = [[1, 10, 3, 8],
                   [12, 2, 9, 6],
                   [5, 7, 4, 11],
                   [3, 7, 16, 5]]
        target = 53

        self.test(matrix, target)

    def test2(self):
        matrix = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]
        target = 29

        self.test(matrix, target)

    def test3(self):
        matrix = [[1, 10, 3, 8]]
        target = 22

        self.test(matrix, target)

    def test4(self):
        matrix = [[1],
                   [12],
                   [5],
                   [3]]
        target = 21

        self.test(matrix, target)

    def test5(self):
        matrix = [[6]]
        target = 6

        self.test(matrix, target)

    def test6(self):
        matrix = None
        target = None
        self.test(matrix, target)

if __name__ == "__main__":
    # S1 = Solution1()
    # max_value = S1.get_max_value(matrix1)
    # print(max_value)

    T = Test()
    T.test1()
    T.test2()
    T.test3()
    T.test4()
    T.test5()
    T.test6()