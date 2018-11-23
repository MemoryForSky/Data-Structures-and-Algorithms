"""

面试题57（二）：为s的连续正数序列
题目：输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。
例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以结果打印出3个连续序列1～5、
4～6和7～8。

思路：
由（1）中双指针拓展而来

"""

class Solution:
    def find_continue_sequence(self, s):
        if not isinstance(s, int) or s < 0:
            return

        small = 1
        big = 2
        mid = (s + 1) // 2
        result_sequence = []

        sum = small + big

        while small < mid:
            if sum == s:
                result_sequence.append((small, big))

            if sum <= s:
                big += 1
                sum += big
            else:
                sum -= small
                small += 1

        return result_sequence


if __name__ == '__main__':
    S = Solution()
    result_sequence = S.find_continue_sequence(3)
    print(result_sequence)