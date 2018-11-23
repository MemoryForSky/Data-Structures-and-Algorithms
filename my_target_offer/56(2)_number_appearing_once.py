"""

面试题56（二）：数组中唯一只出现一次的数字
题目：在一个数组中除了一个数字只出现一次之外，其他数字都出现了三次。请
找出那个只出现一次的数字。

"""

class Solution:
    def find_number_appear_once(self, nums):
        if not isinstance(nums, list) or len(nums) == 0:
            return

        bit_sum = [0] * 32
        for i in range(len(nums)):
            bit_mask = 1
            for j in range(31, -1, -1):
                if nums[i] & bit_mask:
                    bit_sum[j] += 1
                bit_mask <<= 1

        print(bit_sum)
        result = 0
        for i in range(len(bit_sum)):
            result <<= 1
            result += bit_sum[i] % 3

        return result


if __name__ == '__main__':
    data1 = [1, 1, 2, 2, 2, 1, 3]
    data2 = [4, 3, 3, 2, 2, 2, 3]
    data3 = [4, 4, 1, 1, 1, 7, 4]
    data4 = [-10, 214, 214, 214]
    data5 = [-209, 3467, -209, -209]
    data6 = [1024, -1025, 1024, -1025, 1024, -1025, 1023]
    data7 = [-1024, -1024, -1024, -1023]
    data8 = [-23, 0, 214, -23, 214, -23, 214]
    data9 = [0, 3467, 0, 0, 0, 0, 0, 0]

    S = Solution()
    result = S.find_number_appear_once(data9)
    print(result)