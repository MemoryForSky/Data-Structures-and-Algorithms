import time
"""

钢条切割

"""


class Solution1:
    """
    递归解法
    """
    def cut_rot(self, p, n):
        if not isinstance(price, list) or n < 1:
            return

        max_gain = self.cut_rot_core(p, n)

        return max_gain

    def cut_rot_core(self, p, n):
        if n == 0:
            max_price = 0
        else:
            max_price = -float("inf")
            for i in range(1, 11):
                if i <= n:
                    max_price = max(max_price, p[i] + self.cut_rot_core(p, n - i))

        return max_price


class Solution2:
    """
    动态规划：有缓存的自顶向下
    """
    def memoized_cut_rod(self, p, n):
        if not isinstance(price, list) or n < 1:
            return

        mem = [-float("inf")] * (n + 1)
        max_gain = self.memoized_cut_rod_core(p, n, mem)

        return max_gain

    def memoized_cut_rod_core(self, p, n, mem):
        if mem[n] >= 0:
            return mem[n]

        if n == 0:
            max_price = 0
        else:
            max_price = -float("inf")
            for i in range(1, 11):
                if i <= n:
                    max_price = max(max_price, p[i] + self.memoized_cut_rod_core(p, n - i, mem))
            mem[n] = max_price

        return max_price


class Solution3:
    """
    动态规划：自底向上
    """
    @staticmethod
    def bottom_up_cut_rod(p, n):
        mem = [0] * (n + 1)

        for j in range(1, n + 1):
            max_price = -float("inf")
            for i in range(1, 11):
                if i <= j:
                    max_price = max(max_price, p[i] + mem[j - i])
            mem[j] = max_price

        return mem[n]


class Solution4:
    """
    15.1-4: 拓展动态规划：自底向上，返回最优收益值，并保存切割方案
    """
    def print_extended_bottom_up_cut_rod(self, p, n):
        best_gain, s = self.extended_bottom_up_cut_rod(p, n)

        best_cut = []
        while n > 0:
            best_cut.append(s[n])
            n = n - s[n]

        return best_gain, best_cut

    @staticmethod
    def extended_bottom_up_cut_rod(p, n):
        mem = [0] * (n + 1)
        s = [0] * (n + 1)

        for j in range(1, n + 1):
            max_price = -float("inf")
            for i in range(1, 11):
                if i <= j and max_price < p[i] + mem[j - i]:
                    max_price = p[i] + mem[j - i]
                    s[j] = i
            mem[j] = max_price

        return mem[n], s


class Solution5:
    """
    15.1-3: 动态规划：自底向上（加入固定切割成本）
    """
    @staticmethod
    def bottom_up_cut_rod(p, n, c):
        mem = [0] * (n + 1)

        for j in range(1, n + 1):
            if j <= 10:
                # 不切割时最大收益为p[j]
                max_price = p[j]
            else:
                max_price = -float("inf")
            # i = 10时不用切割
            for i in range(1, 10):
                # 切割时减去固定成本c
                if i <= j and max_price < (p[i] + mem[j - i] - c):
                    max_price = p[i] + mem[j - i] - c
            mem[j] = max_price

        return mem[n]


class Solution6:
    """
    15.1-5：fibonacci数列的动态规划解法

    图中有 n+1 个顶点，其中 v2, v3, ... ,vn 都有两条边，v0, v1 没有边，所以图中有 2(n-1) 条边。
    """
    @staticmethod
    def fibonacci(n):
        fib = [0] * (n + 1)
        fib[0] = 1
        fib[1] = 1

        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]

        return fib[n]


if __name__ == '__main__':
    price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    N = 111
    c = 2

    '''
    start1 = time.perf_counter()
    S1 = Solution1()
    max_gain1 = S1.cut_rot(price, N)
    end1 = time.perf_counter()
    print("cut rot: max gain = ", max_gain1, ", cost time = ", (end1 - start1)*1000, "ms")

    start2 = time.perf_counter()
    S2 = Solution2()
    max_gain2 = S2.memoized_cut_rod(price, N)
    end2 = time.perf_counter()
    print("memoized cut rod: max gain = ", max_gain2, ", cost time = ", (end2 - start2)*1000, "ms")

    start3 = time.perf_counter()
    S3 = Solution3()
    max_gain3 = S3.bottom_up_cut_rod(price, N)
    end3 = time.perf_counter()
    print("bottom up cut rod: max gain = ", max_gain3, ", cost time = ", (end3 - start3) * 1000, "ms")

    start4 = time.perf_counter()
    S4 = Solution4()
    max_gain4, best_cut = S4.print_extended_bottom_up_cut_rod(price, N)
    end4 = time.perf_counter()
    print("bottom up cut rod: max gain = ", max_gain4, "extended bottom up cut rod: best cut =", best_cut, ", cost time = ", (end4 - start4) * 1000, "ms")

    start5 = time.perf_counter()
    S5 = Solution5()
    max_gain5 = S5.bottom_up_cut_rod(price, N, c)
    end5 = time.perf_counter()
    print("bottom up cut rod: max gain = ", max_gain5, ", cost time = ", (end5 - start5) * 1000, "ms")
    '''

    start6 = time.perf_counter()
    S6 = Solution6()
    result = S6.fibonacci(36)
    end6 = time.perf_counter()
    print("fibonacci: fib(n) = ", result, ", cost time = ", (end6 - start6) * 1000, "ms")




