"""

面试题53（三）：数组中数值和下标相等的元素
题目：假设一个单调递增的数组里的每个元素都是整数并且是唯一的。请编程实
现一个函数找出数组中任意一个数值等于其下标的元素。例如，在数组{-3, -1,
1, 3, 5}中，数字3和它的下标相等。

"""

class Solution:
    def find_index_equal_value(self, nums):
        if not isinstance(nums, list):
            return

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) >> 1

            if nums[mid] == mid:
                return mid
            elif nums[mid] > mid:
                end = mid - 1
            else:
                start = mid + 1

        return -1

if __name__ == "__main__":
    data = [0, 2, 3, 4, 5, 6]

    S = Solution()

    number = S.find_index_equal_value(data)
    print(number)


