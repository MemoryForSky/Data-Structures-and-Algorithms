"""

矩阵链乘法

"""


class Solution1:
    @staticmethod
    def matrix_chain_order(p):
        """
        动态规划
        """
        n = len(p) - 1
        m = [[0] * (n + 1) for _ in range(n + 1)]
        s = [[0] * (n + 1) for _ in range(n)]

        for l in range(2, n + 1):
            for i in range(1, n - l + 2):
                j = i + l - 1
                m[i][j] = float("inf")
                for k in range(i, j):
                    q = m[i][k] + m[k + 1][j] + p[i-1] * p[k] * p[j]
                    if q < m[i][j]:
                        m[i][j] = q
                        s[i][j] = k

        return m[1][n], s

    def print_optimal_parens(self, s, i, j):
        """
        生成矩阵链最优括号化方案
        """
        if i == j:
            print("A%s" % i, end="")
        else:
            print("(", end="")
            self.print_optimal_parens(s, i, s[i][j])
            self.print_optimal_parens(s, s[i][j] + 1, j)
            print(")", end="")

    def matrix_chain_multiply(self, A, s, i, j):
        """
        15.2-2：实现矩阵链最优代价乘法计算
        """
        if i == j:
            return A[i-1]
        if i + 1 == j:
            return A[i-1] * A[j-1]
        b = self.matrix_chain_multiply(A, s, i, s[i][j])
        c = self.matrix_chain_multiply(A, s, s[i][j] + 1, j)
        return b * c


class Solution2:
    """
    递归解法
    """
    def recursive_matrix_chain(self, p, i, j):
        if i == j:
            return 0

        min_cost = float("inf")
        for k in range(i, j):
            q = self.recursive_matrix_chain(p, i, k) + self.recursive_matrix_chain(p, k + 1, j) + p[i-1] * p[k] * p[j]
            if q < min_cost:
                min_cost = q

        return min_cost


class Solution3:
    """
    带缓存的递归算法
    """
    def memorized_matrix_chain(self, p):
        n = len(p) - 1

        mem = [[float("inf")] * (n + 1) for _ in range(n + 1)]

        return self.memorized_matrix_chain_core(p, mem, 1, n)

    def memorized_matrix_chain_core(self, p, mem, i, j):
        if mem[i][j] < float("inf"):
            return mem[i][j]

        if i == j:
            mem[i][j] = 0

        for k in range(i, j):
            q = self.memorized_matrix_chain_core(p, mem, i, k) + self.memorized_matrix_chain_core(p, mem, k + 1, j) \
                + p[i - 1] * p[k] * p[j]
            if q < mem[i][j]:
                mem[i][j] = q

        return mem[i][j]


if __name__ == '__main__':
    dimensions = [30, 35, 15, 5, 10, 20, 25]
    # 15.2-1
    dimensions2 = [5, 10, 3, 12, 5, 50, 6]

    A = [2, 3, 3, 5, 6, 2]

    S1 = Solution1()
    min_cost1, s = S1.matrix_chain_order(dimensions2)
    print(min_cost1)
    # S.print_optimal_parens(s, 1, 6)
    # result = S1.matrix_chain_multiply(A, s, 1, 6)
    # print(result)

    S2 = Solution2()
    min_cost2 = S2.recursive_matrix_chain(dimensions2, 1, len(dimensions2)-1)
    print(min_cost2)

    S3 = Solution3()
    min_cost3 = S3.memorized_matrix_chain(dimensions2)
    print(min_cost3)

