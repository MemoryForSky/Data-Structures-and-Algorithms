"""

面试题57（一）：和为s的两个数字
题目：输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们
的和正好是s。如果有多对数字的和等于s，输出任意一对即可。

思路：
使用双指针

"""

class Solution:
    def sum_2(self, nums, s):
        if not isinstance(nums, list) or len(nums) == 0:
            return

        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == s:
                return i, j
            elif nums[i] + nums[j] < s:
                i += 1
            else:
                j -= 1

        return -1


if __name__ == '__main__':
    data = [1, 2, 4, 7, 11, 15]


    S = Solution()
    result = S.sum_2(data, 20)
    print(result)