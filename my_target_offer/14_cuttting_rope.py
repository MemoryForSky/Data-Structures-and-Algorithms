from math import pow
"""

剪绳子：
题目：给你一根长度为n绳子，请把绳子剪成m段（m、n都是整数，n>1并且m≥1）。
每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0]*k[1]*…*k[m]可能的最大乘
积是多少？例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此
时得到最大的乘积18。

"""

class Solution:
    def max_product_cutting(self, length):
        """
        动态规划：时间复杂度O(n^2),空间复杂度O(n)

        :param length: 绳子长度
        :return: 乘积最大值
        """
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2

        # 与前面不同，因为切分后的值为1、2、3可以直接相乘，但长度为1、2、3无法直接相乘，因为题目条件m≥1
        products = [0] * (length + 1)
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3

        # 迭代式：子问题
        for i in range(4, length + 1):
            max_product = 0
            for j in range(1, i // 2 + 1):
                product = products[j] * products[i - j]
                if max_product < product:
                    max_product = product
            products[i] = max_product

        max_product = products[length]
        return max_product

    def max_product_cutting2(self, length):
        """
        贪婪算法：时间复杂度O(1),空间复杂度O(1)

        :param length: 绳子长度
        :return: 乘积最大值
        """
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2

        times_3 = length // 3

        if (length - times_3 * 3) == 1:
            times_3 -= 1

        times_2 = (length - times_3 * 3) // 2

        return pow(3, times_3)*pow(2, times_2)

# ====================测试代码====================
class Test:
    """
    测试代码
    """
    def __init__(self):
        self.S = Solution()

    def test(self, test_name, length, expected):
        """
        测试输出结果

        :param test_name: 测试名称
        :param length: 绳子长度
        :param expected: 期望输出
        :return: 乘积最大值
        """
        if test_name is not None:
            print("%s begin：" % test_name)

        if self.S.max_product_cutting(length) == expected:
            print("pass.")
        else:
            print("Failed.")

    def test1(self):
        self.test("test1", 1, 0)

    def test2(self):
        self.test("test1", 2, 1)

    def test3(self):
        self.test("test1", 3, 2)

    def test4(self):
        self.test("test1", 4, 4)

    def test5(self):
        self.test("test1", 5, 6)

    def test6(self):
        self.test("test1", 6, 9)

    def test7(self):
        self.test("test1", 7, 12)

    def test8(self):
        self.test("test1", 8, 18)

    def test9(self):
        self.test("test1", 9, 27)

    def test10(self):
        self.test("test1", 10, 36)

    def test11(self):
        self.test("test1", 50, 86093442)



if __name__ == '__main__':
    T = Test()
    T.test1()
    T.test2()
    T.test3()
    T.test4()
    T.test5()
    T.test6()
    T.test7()
    T.test8()
    T.test9()
    T.test10()
    T.test11()






