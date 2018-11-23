"""

面试题56（一）：数组中只出现一次的两个数字
题目：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序
找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

思路：

本例利用异或的性质，同时保证时间复杂度和空间复杂度。
时间复杂度：O(n)
空间复杂度：O(1)

"""

class Solution:
    def find_nums_appear_once(self, nums):
        if not isinstance(nums, list) or len(nums) == 0:
            return

        # 数组内所有数字异或
        exclusion_or = 0
        for num in nums:
            exclusion_or ^= num

        # 找到第一个为1的位置
        index_of_1 = 0
        while exclusion_or & 1 == 0 and index_of_1 < 32:
            exclusion_or >>= 1
            index_of_1 += 1

        # 从两个数组中找到不重复的两个数字
        num1 = 0
        num2 = 0
        for num in nums:
            if self.is_bit1(num, index_of_1):
                num1 ^= num
            else:
                num2 ^= num

        return num1, num2

    @staticmethod
    def is_bit1(num, index_bit):
        num >>= index_bit
        return num & 1


if __name__ == '__main__':
    data = [2, 4, 3, 6, 3, 2, 5, 5]

    S = Solution()
    result = S.find_nums_appear_once(data)
    print(result)
