"""

面试题61：扑克牌的顺子
题目：从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王可以看成任意数字。

"""

class Solution:
    def is_continous(self, nums):
        if not isinstance(nums, list) or len(nums) == 0:
            return

        nums.sort()

        num_zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                num_zero += 1

        small = num_zero
        big = small + 1
        num_gap = 0
        while big < len(nums):
            if nums[big] == nums[small]:
                return False

            num_gap += nums[big] - nums[small] - 1
            small = big
            big += 1

        return True if num_gap <= num_zero else False


if __name__ == '__main__':
    data = []

    S = Solution()
    if S.is_continous(data):
        print("is continous")
    else:
        print("not continous")

