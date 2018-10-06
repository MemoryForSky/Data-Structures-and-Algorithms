"""

二进制中1的个数
题目：请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。例如
把9表示成二进制是1001，有2位是1。因此如果输入9，该函数输出2。

思路：把一个整数减去1之后再与原来的整数作位与运算，得到的结果相当于把整数的二进制表示中最右边的1变成0.

"""

class Solution:
    def number_of_1(self, number):
        """
        二进制中1的个数

        :param number:
        :return:
        """
        count = 0
        if number < 0:
            number = number & 0xffffffff
        while number:
            count += 1
            number = (number - 1) & number
        return count

    def number_is_2_power(self, number):
        """
        判断一个整数是不是2的整数次方

        :param number:
        :return:
        """
        if number & (number - 1) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    S = Solution()
    result = S.number_of_1(-1)
    print(result)
    result2 = S.number_is_2_power()
    print(result2)


