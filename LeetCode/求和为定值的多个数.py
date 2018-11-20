class Solution:
    @staticmethod
    def two_sum1(nums, target):
        """
        使用哈希表

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                return nums_dict[nums[i]], i
            else:
                nums_dict[target - nums[i]] = i



    def two_sum2(self, nums, target):
        """
        使用双指针

        时间复杂度：有序O(n)  无序O(nlogn + n) = O(nlogn)
        空间复杂度：O(1)
        """
        nums.sort()
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] + nums[end] == target:
                return start, end
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                start += 1

    def three_sum(self, nums, target):
        for i in range(len(nums)):
            remain = target - nums[i]


    def n_sum(self):
        pass


if __name__ == '__main__':
    data = [1, 3, 5, 4, 2]

    S = Solution()
    result = S.two_sum1(data, 9)
    print(result)

    data_sorted = sorted(data)
    result = S.two_sum2(data_sorted, 9)
    print(result)





