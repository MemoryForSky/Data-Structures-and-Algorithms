import time
"""

面试题49：丑数
题目：我们把只包含因子2、3和5的数称作丑数（Ugly Number）。求按从小到
大的顺序的第1500个丑数。例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做第一个丑数。

"""

class Solution1:
    def get_ugly_number(self, index):
        count = 0
        digit = 0
        while count < index:

            digit += 1

            if self.is_ugly(digit):
                count += 1

        return digit


    def is_ugly(self, digit):
        while digit % 2 == 0:
            digit //= 2

        while digit % 3 == 0:
            digit //= 3

        while digit % 5 == 0:
            digit //= 5

        return True if digit == 1 else False

class Solution2:
    """

    提升算法：
    该算法通过规律只计算丑数，利用空间换取时间，使得随index的增加，时间复杂度不会显著提高，而采用solution1中遍历所有整数的方式，随
    index的增加，消耗的时间显著上升。

    """
    @staticmethod
    def get_ugly_number(index):
        if index <= 0:
            return 0

        ugly_num = [0] * index
        ugly_num[0] = 1
        ugly_index = 1

        p2, p3, p5 = 0, 0, 0

        while ugly_index < index:
            next_ugly = min(min(ugly_num[p2] * 2, ugly_num[p3] * 3), ugly_num[p5] * 5)
            ugly_num[ugly_index] = next_ugly

            while ugly_num[p2] * 2 <= ugly_num[ugly_index]:
                p2 += 1
            while ugly_num[p3] * 3 <= ugly_num[ugly_index]:
                p3 += 1
            while ugly_num[p5] * 5 <= ugly_num[ugly_index]:
                p5 += 1

            ugly_index += 1

        return ugly_num[index - 1]


if __name__ == '__main__':
    start1 = time.perf_counter()
    S1 = Solution1()
    number1 = S1.get_ugly_number(700)
    end1 = time.perf_counter()
    print("result: ", number1, "\ncost time: ", (end1 - start1) * 1000, "ms")

    start2 = time.perf_counter()
    S2 = Solution2()
    number2 = S2.get_ugly_number(100)
    end2 = time.perf_counter()
    print("result: ", number2, "\ncost time: ", (end2 - start2) * 1000, "ms")