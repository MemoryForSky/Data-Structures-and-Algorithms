"""

activity-selection problem

"""


class Solution1:
    """
    动态规划

    参考：https://blog.csdn.net/cyp331203/article/details/43242209
    """
    def activity_selector_dynamic(self, s, f, n):
        c = [[0] * (n + 2) for _ in range(n + 2)]
        act = [[0] * (n + 2) for _ in range(n + 2)]

        for step in range(2, n + 2):
            for i in range(n + 1):
                j = i + step
                k = j - 1
                if j <= n + 1:
                    while f[i] < f[k]:
                        if f[i] <= s[k] and f[k] <= s[j] and c[i][k] + c[k][j] + 1 > c[i][j]:
                            c[i][j] = c[i][k] + c[k][j] + 1
                            act[i][j] = k
                        k = k - 1
        print("最大兼容活动集包含的活动个数为：", c[0][n + 1])
        print("包含的活动为：", end="")
        self.print_activity(c, act, 0, n + 1)

    def print_activity(self, c, act, i, j):
        if c[i][j] > 0:
            k = act[i][j]
            print(k, end=" ")
            self.print_activity(c, act, i, k)
            self.print_activity(c, act, k, j)


class Solution2:
    """
    递归贪心算法
    """
    def activity_selector_recursive(self, s, f, k, n):
        m = k + 1

        # 查找最早结束的活动
        while m <= n and s[m] < f[k]:
            m = m + 1

        # 查找剩余时间的活动
        if m <= n:
            print("a" + str(m), end=" ")
            return self.activity_selector_recursive(s, f, m, n)

        else:
            return


class Solution3:
    """
    迭代贪心算法
    """
    def activity_selector_greedy(self, s, f):
        n = len(s)
        A = ["a1"]
        k = 1
        for m in range(2, n):
            if s[m] >= f[k]:
                A.append("a" + str(m))
                k = m
        return A


if __name__ == '__main__':
    # 增加活动开始节点和活动结束节点
    s1 = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12, 99]
    f1 = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16, 99]

    S1 = Solution1()
    S1.activity_selector_dynamic(s1, f1, 11)

    s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

    # S2 = Solution2()
    # S2.activity_selector_recursive(s, f, 0, 11)

    # S3 = Solution3()
    # result = S3.activity_selector_greedy(s, f)
    # print(result)
