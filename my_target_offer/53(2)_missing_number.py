"""

面试题53（二）：0到n-1中缺失的数字
题目：一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字
都在范围0到n-1之内。在范围0到n-1的n个数字中有且只有一个数字不在该数组
中，请找出这个数字。

"""

class Solution:
    def find_missing_num(self, nums, n):
        if not isinstance(nums, list):
            return

        start = 0
        end = n - 1

        while start <= end:
            mid = (start + end) >> 1

            if nums[mid] == mid:
                start = mid + 1
            else:
                if mid == 0 or nums[mid - 1] == mid - 1:
                    return mid
                end = mid - 1

            if start == n:
                return n

if __name__ == '__main__':
    data = [0, 1, 2, 3, 5, 6, 7, 8]

    S = Solution()
    missing_number = S.find_missing_num(data, len(data))
    print(missing_number)