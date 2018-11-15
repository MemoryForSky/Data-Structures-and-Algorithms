"""

面试题43：从1到n整数中1出现的次数
题目：输入一个整数n，求从1到n这n个整数的十进制表示中1出现的次数。例如
输入12，从1到12这些整数中包含 1 的数字有1，10，11和12，1一共出现了5次。

"""

class Solution:
    def number_of_1_to_n(self, num):
        if not isinstance(num, int) or num < 1:
            return

        count_all = 0
        for i in range(1, num+1):
            count = self.compute_1(i)
            count_all += count

        return count_all

    def compute_1(self, num):
        count = 0
        while num > 0:
            if num % 10 == 1:
                count += 1
            num //= 10
        return count

if __name__ == '__main__':
    S = Solution()
    count_1 = S.number_of_1_to_n(12)
    print(count_1)
