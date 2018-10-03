import time
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
    def __init__(self):
        self.memo ={}

    def fibonacci(self, n):
        """
        动态规划实现fibonacci数列

        :param n: fibonacci数列第n项
        :return: 数列第n项的值
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        try:
            return self.memo[n]
        except KeyError:
            result = self.fibonacci(n-1) + self.fibonacci(n-2)
            self.memo[n] = result
            return result

def fibonacci2(n):
    """
    自底而上实现fibonacci数列

    :param n: fibonacci数列第n项
    :return: 数列第n项的值
    """
    default = [0, 1]
    if n < 2:
        return default[n]

    fibNsub1 = 1
    fibNsub2 = 0
    fibN = 0
    for i in range(2, n+1):
        fibN = fibNsub1 + fibNsub2
        fibNsub2 = fibNsub1
        fibNsub1 = fibN
    return fibN

if __name__ == '__main__':
    start_time = time.perf_counter()
    S = Solution()
    result = S.fibonacci(36)
    end_time = time.perf_counter()
    print(result)
    print("fibnacci sequense costs：", end_time - start_time)

    start_time2 = time.perf_counter()
    result2 = fibonacci2(36)
    end_time2 = time.perf_counter()
    print(result2)
    print("fibnacci sequense costs：", end_time2 - start_time2)
