import random

class Solution1:
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


class Solution2:
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


if __name__ == '__main__':
    numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    S1 = Solution1()
    result1 = S1.find_half_freq(numbers)
    print(result1)

    S2 =Solution2()
    result2 = S2.more_than_half_num(numbers)
    print(result2)




