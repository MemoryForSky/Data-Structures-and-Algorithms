"""
递归比较简洁，但性能不如基于循环的实现：
递归由于是函数调用自身，而函数调用是有时间和空间的消耗的：每一次函数调用，都需要在内存栈中分配空间以保存参数、返回地址及临时变量，
而且往栈里压入数据和弹出数据都需要时间。
递归的另一个问题：如果层级太多，会引发调用栈溢出，循环则不会发生这种情况。
"""

"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
"""
class Solution:
    def fibonacci(self, n, memo = {}):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fibonacci(n-1) + self.fibonacci(n-2)

if __name__ == '__main__':
    S = Solution()
    result = S.fibonacci(20)
    print(result)
