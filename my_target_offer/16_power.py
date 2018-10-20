"""
面试题16：数值的整数次方
题目：实现函数double Power(double base, int exponent)，求base的exponent
次方。不得使用库函数，同时不需要考虑大数问题。
"""
class Solution:
    def __init__(self):
        # 标记是否是语法错误，分母为0
        self.flag_invalid = False

    def power(self, base, exponent):
        """
        针对底数、指数的不同情况进行处理
        """
        if base == 0.0 and exponent < 0:
            self.flag_invalid = True
            return 0

        exponent_p = exponent
        if exponent < 0:
            exponent_p = -exponent
        result = self.power_positive(base, exponent_p)

        if exponent < 0:
            return 1/result
        else:
            return result

    @staticmethod
    def power_positive(base, exponent):
        """
        计算正数的整数次方
        """
        result = 1
        for i in range(exponent):
            result *= base
        return result

if __name__ == '__main__':
    S = Solution()
    num = S.power(0, 4)
    print(num)
    print(S.flag_invalid)




