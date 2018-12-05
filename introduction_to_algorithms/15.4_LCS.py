"""

LCS

"""


class Solution1:
    def lcs_length(self, X, Y):
        """
        自底向上的动态规划
        """
        m = len(X) + 1
        n = len(Y) + 1
        b = [[0] * n for _ in range(m)]      # 路径
        c = [[0] * n for _ in range(m)]      # 公共子串长度

        for i in range(1, m):
            for j in range(1, n):
                if X[i-1] == Y[j-1]:
                    c[i][j] = c[i-1][j-1] + 1
                    b[i][j] = "upper left"
                elif c[i-1][j] >= c[i][j-1]:
                    c[i][j] = c[i-1][j]
                    b[i][j] = "up"
                else:
                    c[i][j] = c[i][j-1]
                    b[i][j] = "left"

        return b, c

    # 习题15.4-4
    def lcs_length_boost(self, X, Y):
        """
        改进算法：只使用内存大小为2 * min(m, n)
        """
        mem = [[0] * len(Y) for _ in range(2)]

        for i in range(1, len(X) + 1):
            for j in range(len(Y)):
                flag = i % 2
                if j == 0:
                    mem[flag][0] = 1 if X[i-1] == Y[j] else 0
                elif X[i-1] == Y[j]:
                    mem[flag][j] = mem[1 - flag][j - 1] + 1
                elif mem[1 - flag][j] >= mem[flag][j - 1]:
                    mem[flag][j] = mem[1 - flag][j]
                else:
                    mem[flag][j] = mem[flag][j - 1]

        return mem[len(X) % 2][-1]

    # 习题15.4-4
    def lcs_length_boost2(self, X, Y):
        """
        改进算法：只使用内存大小为min(m, n)
        """
        mem = [0] * (len(Y) + 1)

        for i in range(len(X)):
            mem[0] = 0
            for j in range(1, len(Y) + 1):
                if X[i] == Y[j-1]:
                    tmp = mem[j]
                    mem[j] = mem[0] + 1
                    mem[0] = tmp
                elif mem[j] >= mem[j-1]:
                    mem[0] = mem[j]
                else:
                    mem[0] = mem[j]
                    mem[j] = mem[j-1]

        return mem[-1]

    def print_lcs(self, b, X, rows, cols):
        """
        使用路径指示矩阵
        """
        if rows == 0 or cols == 0:
            return

        if b[rows][cols] == "upper left":
            self.print_lcs(b, X, rows-1, cols-1)
            print(X[rows-1], end=" ")
        elif b[rows][cols] == "up":
            self.print_lcs(b, X, rows-1, cols)
        else:
            self.print_lcs(b, X, rows, cols-1)

    # 练习15.4-2
    def print_lcs2(self, c, X, Y, rows, cols):
        """
        节省空间开销，只使用子串的长度矩阵
        """
        if rows == 0 or cols == 0:
            return

        if X[rows-1] == Y[cols-1]:
            self.print_lcs2(c, X, Y, rows-1, cols-1)
            print(X[rows - 1], end=" ")
        elif c[rows-1][cols] >= c[rows][cols-1]:
            self.print_lcs2(c, X, Y, rows-1, cols)
        else:
            self.print_lcs2(c, X, Y, rows, cols-1)


class Solution2:
    # 习题15.4-3
    def lcs(self, X, Y):
        """
        带缓存的递归解法
        """
        m = len(X)
        n = len(Y)
        mem = [[-1] * (n + 1) for _ in range(m + 1)]
        max_length = self.lcs_length_mem(X, Y, mem, m, n)
        return max_length

    def lcs_length_mem(self, X, Y, mem, i, j):
        if mem[i][j] > -1:
            return mem[i][j]

        if i == 0 or j == 0:
            tmp = 0
        elif X[i-1] == Y[j-1]:
            tmp = self.lcs_length_mem(X, Y, mem, i-1, j-1) + 1
        elif self.lcs_length_mem(X, Y, mem, i-1, j) >= self.lcs_length_mem(X, Y, mem, i, j-1):
            tmp = self.lcs_length_mem(X, Y, mem, i-1, j)
        else:
            tmp = self.lcs_length_mem(X, Y, mem, i, j-1)

        mem[i][j] = tmp

        return mem[i][j]


if __name__ == '__main__':
    # X = "ABCBDAB"
    # Y = "BDCABA"

    # 练习15.4-1
    X = [1, 0, 0, 1, 0, 1, 0, 1]
    Y = [0, 1, 0, 1, 1, 0, 1, 1, 0]

    S1 = Solution1()
    # path, lcs_length = S1.lcs_length(X, Y)
    # print(lcs_length[len(X)][len(Y)])

    # 构造LCS
    # S1.print_lcs(path, X, len(X), len(Y))
    # print()
    # S1.print_lcs2(lcs_length, X, Y, len(X), len(Y))
    # print()

    # 测试带备忘的递归算法
    # S2 = Solution2()
    # result = S2.lcs(X, Y)
    # print(result)

    # 测试改进算法：只使用内存大小为2 * min(m, n)
    # result1 = S1.lcs_length_boost(X, Y)
    # print(result1)

    # 改进算法：只使用内存大小为min(m, n)
    # result2 = S1.lcs_length_boost2(X, Y)
    # print(result2)

    # 习题15.4-5: 求一个 n 个数的序列的最长单调递增子序列
    L = [2, 3, 1, 5, 4, 7, 8, 6, 9]

    path, lcs_length = S1.lcs_length(L, sorted(L))
    print(lcs_length[len(L)][len(L)])
    S1.print_lcs(path, L, len(L), len(L))





