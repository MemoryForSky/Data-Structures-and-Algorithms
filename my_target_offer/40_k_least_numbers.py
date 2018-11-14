import random

"""

面试题40：最小的k个数
题目：输入n个整数，找出其中最小的k个数。例如输入4、5、1、6、2、7、3、8
这8个数字，则最小的4个数字是1、2、3、4。

"""

class Solution1:
    def get_least_k(self, nums, k):
        """
        快排的思想解决取最大/最小k个数的问题：
        时间复杂度：n + n/2 + n/4 + n/8 + ... = n + (n - n/2) + (n/2 - n/4) + ... = 2n = O(n)

        :param nums: 数组
        :param k: 最小数字个数
        :return: 最小k个数字
        """
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

        return nums[:k]

    def partition(self, data, start, end):
        """
        快排：partition

        :param data: 数组
        :param start: 起始位置
        :param end: 终止位置
        :return: 划分索引
        """
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

class Solution2:
    def get_least_k(self, nums, k):
        """
        利用堆解决取最大/最小k个数的问题：
        时间复杂度：O(nlog(k))

        :param nums: 数组
        :param k: 最小数字个数
        :return: 最小k个数字
        """
        if not isinstance(nums, list) or len(nums) == 0 or k > len(nums) or k <= 0:
            return

        # 初始化大小为k的最大堆
        nums_k = nums[:k]
        for i in range(k // 2 - 1, -1, -1):
            # 切片之后生成新的对象，因此需对原数组做更新，不然原数组不改变
            nums_k = self.max_heap(nums_k, i, k - 1)

        print("initialize heap: ", nums_k)

        # 剩余数据与堆顶比较
        for i in range(k, len(nums)):
            if nums[i] < nums_k[0]:
                nums_k[0] = nums[i]
                nums_k = self.max_heap(nums_k, 0, k-1)

        return nums_k

    def max_heap(self, nums, start, end):
        """
        初始化堆

        :param nums: 数组
        :param start: 起始位置
        :param end: 终止位置
        :return: 初始化后的堆
        """
        current = start
        left = current * 2 + 1
        tmp = nums[current]
        while left <= end:
            if left < end and nums[left] < nums[left + 1]:
                left += 1
            if tmp >= nums[left]:
                break
            else:
                nums[current], nums[left] = nums[left], nums[current]
            current = left
            left = current * 2 + 1
        return nums

if __name__ == '__main__':
    data1 = [4, 5, 1, 6, 2, 7, 2, 8]
    data2 = None

    # S = Solution1()
    # k_least_number1 = S.get_least_k(data1, 0)
    # k_least_number2 = S.get_least_k(data1, 1)
    # k_least_number3 = S.get_least_k(data1, 2)
    # k_least_number4 = S.get_least_k(data1, 4)
    # k_least_number5 = S.get_least_k(data1, 8)
    # k_least_number6 = S.get_least_k(data1, 10)
    # k_least_number7 = S.get_least_k(data2, 2)
    # print(k_least_number1, k_least_number2, k_least_number3, k_least_number4,
    #       k_least_number5, k_least_number6, k_least_number7)

    # # test the build_max_heap
    # data = [20, 40, 30, 10, 60, 50]
    # S = Solution()
    # S.build_max_heap(data)
    # print(data)

    S2 = Solution2()
    k_least_number = S2.get_least_k(data1, 6)
    print(k_least_number)
