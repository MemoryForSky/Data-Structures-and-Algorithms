import random

"""

面试题39：数组中出现次数超过一半的数字
题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例
如输入一个长度为9的数组{1, 2, 3, 2, 2, 2, 5, 4, 2}。由于数字2在数组中
出现了5次，超过数组长度的一半，因此输出2。

"""

class Solution1:
    """
    不使用额外空间，修改原数组
    """
    def __init__(self):
        self.is_invalid_input = False
        self.is_more_than_half = False

    def partition(self, data, start, end):
        index = random.randint(start, end)
        data[index], data[end] = data[end], data[index]

        small_index = start - 1
        for index in range(start, end):
            if data[index] < data[end]:
                small_index += 1
                if small_index != index:
                    data[small_index], data[index] = data[index], data[small_index]
        small_index += 1
        data[small_index], data[end] = data[end], data[small_index]
        return small_index

    def more_than_half_num(self, nums):
        if not isinstance(nums, list) or len(nums) == 0:
            self.is_invalid_input = True
            return

        start = 0
        end = len(nums) - 1
        middle = len(nums) >> 1

        index = self.partition(nums, start, end)

        while index != middle:
            if index > middle:
                end = index - 1
                index = self.partition(nums, start, end)
            elif index < middle:
                start = index + 1
                index = self.partition(nums, start, end)

        result = nums[index]

        if not self.check_more_than_half(nums, result):
            result = -1

        return result

    def check_more_than_half(self, data, target):
        self.is_more_than_half = True

        times = 0
        for item in data:
            if item == target:
                times += 1

        if times * 2 <= len(data):
            self.is_invalid_input = True
            self.is_more_than_half = False

        return self.is_more_than_half


class Solution2(Solution1):
    """
    使用额外空间
    """

    def find_half_freq(self, nums):
        """
        利用字典：需要额外空间

        :param nums:
        :return:
        """
        if not isinstance(nums, list) or len(nums) == 0:
            return

        result = -1
        nums_len = len(nums)
        nums_dict = {}
        for item in nums:
            nums_dict[item] = nums_dict.setdefault(item, 0) + 1
            if nums_dict[item] > nums_len // 2:
                result = item

        return result

    def find_half_freq2(self, nums):
        if not isinstance(nums, list) or len(nums) == 0:
            return

        result = nums[0]
        times = 1
        for i in range(1, len(nums)):
            if times == 0:
                result = nums[i]
            elif nums[i] == result:
                times += 1
            else:
                times -= 1

        if not self.check_more_than_half(nums, result):
            result = -1

        return result


if __name__ == '__main__':
    numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    S = Solution2()
    result1 = S.find_half_freq2(numbers)
    print(result1)

    result2 = S.more_than_half_num(numbers)
    print(result2)




