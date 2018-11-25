"""

面试题63：股票的最大利润
题目：假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖交易该股
票可能获得的利润是多少？例如一只股票在某些时间节点的价格为{9, 11, 8, 5,
7, 12, 16, 14}。如果我们能在价格为5的时候买入并在价格为16时卖出，则能
收获最大的利润11。

"""


class Solution:
    @staticmethod
    def max_diff(nums):
        if not isinstance(nums, list) or len(nums) == 0:
            return

        min = nums[0]
        max_diff = nums[1] - min

        for i in range(2, len(nums)):
            if nums[i - 1] < min:
                min = nums[i - 1]

            current_diff = nums[i] - min
            if current_diff > max_diff:
                max_diff = current_diff

        return max_diff


if __name__ == '__main__':
    data = [9, 11, 5, 7, 16, 1, 4, 2]

    S = Solution()
    result = S.max_diff(data)
    print(result)
