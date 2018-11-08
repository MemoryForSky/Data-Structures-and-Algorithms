"""

给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

示例 1：

输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。


注意:

1 <= k <= len(nums) <= 16
0 < nums[i] < 10000


递归过程：本部分递归迭代是can_partition_core中压栈1和压栈2重复入栈的过程，直到满足最后的终止条件k=0时返回True，对数组遍历一遍也无法
满足tmp=0，则从中间返回False。

"""

class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        length = len(nums)
        nums_sum = sum(nums)

        if nums_sum % k != 0:
            return False

        avg = nums_sum // k
        flag = [0] * length

        result = self.can_partition_core(nums, k, avg, avg, flag, 0)

        return result


    def can_partition_core(self, nums, k, avg, tmp, flag, index):
        # 终止条件（作为叶节点返回）
        if k == 0:
            return True

        if tmp == 0:
            return self.can_partition_core(nums, k-1, avg, avg, flag, 0)  # 压栈2

        # 迭代公式
        for i in range(index, len(nums)):
            if flag[i] == 1:
                continue

            flag[i] = 1
            if tmp - nums[i] >= 0 and self.can_partition_core(nums, k, avg, tmp-nums[i], flag, index+1):  # 压栈1
                return True  # 满足终止条件，出栈返回True（中间节点返回）
            flag[i] = 0

        return False  # 对数组遍历一遍也无法满足tmp=0，则返回False（中间条件不满足，直接返回）


if __name__ == '__main__':
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4

    S = Solution()
    can_partition = S.canPartitionKSubsets(nums, k)
    print(can_partition)