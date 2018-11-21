"""

面试题53（一）：数字在排序数组中出现的次数
题目：统计一个数字在排序数组中出现的次数。例如输入排序数组{1, 2, 3, 3,
3, 3, 4, 5}和数字3，由于3在这个数组中出现了4次，因此输出4。


"""

class Solution:
    @staticmethod
    def times_of_k(nums, digit):
        """空间换时间"""
        nums_count = {}

        for i in nums:
            nums_count[i] = nums_count.setdefault(digit, 0) + 1

        return nums_count[digit]

    @staticmethod
    def times_of_k2(nums, digit):
        """
        二分查找：时间复杂度为O(n)，因为前后搜索可能要搜索整个数组
        """
        start = 0
        end = len(nums) - 1

        index = (start + end) // 2
        while start <= end:
            if nums[index] == digit:
                break
            elif nums[index] > digit:
                end = index
            else:
                start = index

        num_count = 0
        for i in range(index, -1, -1):
            if nums[i] == digit:
                num_count += 1
            else:
                break
        for j in range(index+1, len(nums)-1):
            if nums[j] == digit:
                num_count += 1
            else:
                break

        return num_count

    def times_of_k3(self, nums, digit):
        """二分查找改进"""
        if not isinstance(nums, list):
            return

        start = 0
        end = len(nums) - 1

        index1 = self.find_first_index(nums, digit, start, end)
        index2 = self.find_second_index(nums, digit, start, end)

        if index1 == -1:
            return -1
        else:
            return index2 - index1 + 1

    def find_first_index(self, nums, k, start, end):
        index = (start + end) // 2

        if start > end:
            return -1

        if nums[index] == k:
            if index== 0 or nums[index-1] < k:
                return index

        if nums[index] >= k:
            index = self.find_first_index(nums, k, start, index - 1)

        if nums[index] < k:
            index = self.find_first_index(nums, k, index + 1, end)

        return index

    def find_second_index(self, nums, k, start, end):
        index = (start + end) // 2

        if start > end:
            return -1

        if nums[index] == k:
            if index == len(nums)-1 or nums[index + 1] > k:
                return index

        if nums[index] <= k:
            index = self.find_second_index(nums, k, index + 1, end)

        if nums[index] > k:
            index = self.find_second_index(nums, k, start, index - 1)

        return index


if __name__ == '__main__':
    data = [1, 2, 3, 3, 3, 3, 4, 5, 10]

    S = Solution()

    # times = S.times_of_k2(data, 3)
    # print(times)

    times = S.times_of_k3(data, 5)
    print(times)


