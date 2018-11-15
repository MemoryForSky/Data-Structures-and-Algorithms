import math
"""

面试题44：数字序列中某一位的数字
题目：数字以0123456789101112131415…的格式序列化到一个字符序列中。在这
个序列中，第5位（从0开始计数）是5，第13位是1，第19位是4，等等。请写一
个函数求任意位对应的数字。

"""

class Solution:
    def digit_of_index(self, index):
        if index < 0:
            return -1

        digit = 1
        while True:
            numbers = self.count_of_digits(digit)
            if index < numbers * digit:
                return self.find_digit(index, digit)

            index -= numbers * digit
            digit += 1

    @staticmethod
    def count_of_digits(digits):
        if digits == 1:
            return 10
        else:
            return 9 * int(math.pow(10, digits-1))

    def find_digit(self, index, digit):
        base = self.find_first_digit(digit)
        num = base + index / digit
        return int(str(num)[index % digit])

    @staticmethod
    def find_first_digit(digit):
        if digit == 1:
            return 0
        else:
            return math.pow(10, digit-1)


if __name__ == '__main__':
    S = Solution()
    number = S.digit_of_index(1001)  # 7
    print(number)
