"""

面试题60：n个骰子的点数
题目：把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s
的所有可能的值出现的概率。

"""


class Solution1:
    """
    递归解法

    递归公式：
    for i in range(1, 7):
        f(sum, n) = i + f(n - 1)

    终止条件：
    只有一个骰子

    """
    def __init__(self, n):
        self.max_value = 6
        self.n = n
        self.max_sum = self.max_value * n
        self.prob = [0] * (self.max_sum - n + 1)

    def print_prob(self):
        if self.n < 1:
            return

        for i in range(1, self.max_value + 1):
            self.compute_prob(self.n, i)

        total = pow(self.max_value, self.n)

        for i in range(self.n, self.max_sum + 1):
            ratio = self.prob[i - self.n] / float(total)
            print("sum = %s, prob = %f" % (i, ratio))

    def compute_prob(self, n, sum):
        if n == 1:
            self.prob[sum - self.n] += 1
        else:
            for i in range(1, self.max_value+1):
                self.compute_prob(n - 1, sum + i)

class Solution2:
    """
    循环解法

    主要使用投骰子的规律：每一次新投一颗骰子，骰子数字相加的和只可能是之前6个数字叠加得到的，其它数字不可能得到当前值，即：
    f(n) = f(n-1) + f(n-2) + f(n-3) + f(n-4) + f(n-5) + f(n-6)

    """
    def print_prob(self, n):
        if n < 1:
            return

        max_value = 6
        prob = [[0] * (max_value * n + 1) for _ in range(2)]

        flag = 0
        for i in range(1, max_value + 1):
            prob[flag][i] = 1

        for k in range(2, n + 1):
            for i in range(0, k):
                prob[1 - flag][i] = 0

            for i in range(k, max_value * n + 1):
                prob[1 - flag][i] = 0
                for j in range(1, max_value + 1):
                    if j <= i:
                        prob[1 - flag][i] += prob[flag][i - j]

            flag = 1 - flag

        total = pow(max_value, n)

        for i in range(n, max_value * n + 1):
            ratio = prob[flag][i] / float(total)
            print("sum = %s, prob = %f" % (i, ratio))


if __name__ == '__main__':
    S = Solution1(3)
    S.print_prob()
    print("------------------")
    S =Solution2()
    S.print_prob(3)