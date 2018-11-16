"""

面试题45：把数组排成最小的数
题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼
接出的所有数字中最小的一个。例如输入数组{3, 32, 321}，则打印出这3个数
字能排成的最小数字321323。

思路：
本题关键在于“构建新的比较规则”，数学上的比较大小是直接比较两个数字的数值大小，排序的话小的在前，大的在后；
这里将两个数用不同的方式连接，连接后较小的顺序为大小顺序。

"""

class Solution:
    @staticmethod
    def print_min_num(nums):
        if not isinstance(nums, list) or len(nums) == 0:
            return

        str_nums = [str(i) for i in nums]

        for i in range(len(nums)-1):
            for j in range(i + 1, len(nums)):
                if str_nums[i] + str_nums[j] > str_nums[j] + str_nums[i]:
                    str_nums[i], str_nums[j] = str_nums[j], str_nums[i]
        return "".join(str_nums)


data = [3, 32, 321]
S = Solution()
min_number = S.print_min_num(data)
print(min_number)
