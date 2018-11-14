import random

"""

面试题40：最小的k个数
题目：输入n个整数，找出其中最小的k个数。例如输入4、5、1、6、2、7、3、8
这8个数字，则最小的4个数字是1、2、3、4。

"""

class Solution:
    def get_least_k(self, nums, k):
        if not isinstance(nums, list) or len(nums) == 0 or k > len(nums) or k <= 0:
            return

        start = 0
        end = len(nums) - 1

        index = self.partition(nums, start, end)
        while index != k - 1:
            if index > k - 1:
                end = index - 1
                index = self.partition(nums, start, end)
            elif index < k - 1:
                start = index + 1
                index = self.partition(nums, start, end)

        result = []
        for i in range(k):
            result.append(nums[i])

        return result

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


if __name__ == '__main__':
    data1 = [4, 5, 1, 6, 2, 7, 2, 8]
    data2 = None

    S = Solution()
    k_least_number1 = S.get_least_k(data1, 0)
    k_least_number2 = S.get_least_k(data1, 1)
    k_least_number3 = S.get_least_k(data1, 2)
    k_least_number4 = S.get_least_k(data1, 4)
    k_least_number5 = S.get_least_k(data1, 8)
    k_least_number6 = S.get_least_k(data1, 10)
    k_least_number7 = S.get_least_k(data2, 2)
    print(k_least_number1, k_least_number2, k_least_number3, k_least_number4,
          k_least_number5, k_least_number6, k_least_number7)