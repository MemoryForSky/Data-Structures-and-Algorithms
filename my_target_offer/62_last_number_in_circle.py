"""

面试题62：圆圈中最后剩下的数字
题目：0, 1, …, n-1这n个数字排成一个圆圈，从数字0开始每次从这个圆圈里
删除第m个数字。求出这个圆圈里剩下的最后一个数字。

"""


class Solution1:
    """利用循环数组"""
    @staticmethod
    def last_remaining(n, m):
        if n < 1 or m < 1:
            return -1

        nums = [0] * n
        for i in range(n):
            nums[i] = i

        current = 0
        while len(nums) > 1:
            for i in range(1, m):
                current += 1
                if current == len(nums):
                    current = 0

            nums.pop(current)
            if current == len(nums):
                current = 0

        return nums[0]


class Solution2:
    """递推公式"""
    @staticmethod
    def last_remaining(n, m):
        pass
        # TODO


if __name__ == '__main__':
    S1 = Solution1()
    result = S1.last_remaining(4000, 997)
    print(result)

