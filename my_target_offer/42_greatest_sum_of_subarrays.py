"""

面试题42：连续子数组的最大和
题目：输入一个整型数组，数组里有正数也有负数。数组中一个或连续的多个整
数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O(n)。

"""

class Solution1:
    @staticmethod
    def find_greatest_sub_sum(nums):
        if not isinstance(nums, list) or len(nums) == 0:
            return

        sub_sum = 0
        max_sum = float("-inf")
        for i in range(len(nums)):
            if sub_sum < 0:
                sub_sum = nums[i]
            else:
                sub_sum += nums[i]

            if sub_sum > max_sum:
                max_sum = sub_sum

        return max_sum

class Solution2:
    @staticmethod
    def find_greatest_sub_sum(nums):
        if not isinstance(nums, list) or len(nums) == 0:
            return

        sub_sum_list = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0 or sub_sum_list[i-1] <= 0:
                sub_sum_list[i] = nums[i]
            else:
                sub_sum_list[i] = nums[i] + sub_sum_list[i-1]

        return max(sub_sum_list)


if __name__ == '__main__':
    data = [1, -2, 3, 10, -4, 7, 2, -5]

    # S = Solution1()
    # max_sub_sum = S.find_greatest_sub_sum(data)
    # print(max_sub_sum)

    S2 = Solution2()
    max_sub_sum = S2.find_greatest_sub_sum(data)
    print(max_sub_sum)
