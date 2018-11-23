"""

面试题59（一）：滑动窗口的最大值
题目：给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。例如，
如果输入数组{2, 3, 4, 2, 6, 2, 5, 1}及滑动窗口的大小3，那么一共存在6个
滑动窗口，它们的最大值分别为{4, 4, 6, 6, 6, 5}，

"""

class Solution:
    def max_in_window(self, nums, n):
        if not isinstance(nums, list) or len(nums) == 0 or n <= 0 or len(nums) < n:
            return

        max_in_window = []
        deque = []

        for i in range(n):
            while len(deque) != 0 and nums[deque[-1]] <= nums[i]:
                deque.pop(-1)
            deque.append(i)

        for i in range(n, len(nums)):
            max_in_window.append(nums[deque[0]])

            while len(deque) != 0 and nums[deque[-1]] <= nums[i]:
                deque.pop(-1)
            if len(deque) != 0 and (i - n) >= deque[0]:
                deque.pop(0)

            deque.append(i)

        max_in_window.append(nums[deque[0]])

        return max_in_window

class Test:
    def test(self, data, expected, n):
        S = Solution()
        output = S.max_in_window(data, n)
        print("output = ", output, "expected = ", expected)

    def test1(self):
        data = [2, 3, 4, 2, 6, 2, 5, 1]
        expected = [4, 4, 6, 6, 6, 5]
        window = 3
        self.test(data, expected, window)

    def test2(self):
        data = [1, 3, -1, -3, 5, 3, 6, 7]
        expected = [3, 3, 5, 5, 6, 7]
        window = 3
        self.test(data, expected, window)

    def test3(self):
        data = [1, 3, 5, 7, 9, 11, 13, 15]
        expected = [7, 9, 11, 13, 15]
        window = 4
        self.test(data, expected, window)

    def test4(self):
        data = [16, 14, 12, 10, 8, 6, 4]
        expected = [16, 14, 12]
        window = 5
        self.test(data, expected, window)

    def test5(self):
        data = [10, 14, 12, 11]
        expected = [10, 14, 12, 11]
        window = 1
        self.test(data, expected, window)

    def test6(self):
        data = [10, 14, 12, 11]
        expected = [14]
        window = 4
        self.test(data, expected, window)

    def test7(self):
        data = [10, 14, 12, 11]
        expected = []
        window = 0
        self.test(data, expected, window)

    def test8(self):
        data = [10, 14, 12, 11]
        expected = []
        window = 5
        self.test(data, expected, window)

    def test9(self):
        data = []
        expected = []
        window = 5
        self.test(data, expected, window)


if __name__ == '__main__':
    data = [2, 3, 4, 2, 6, 2, 5, 1]
    window = 3

    T = Test()
    T.test1()
    T.test2()
    T.test3()
    T.test4()
    T.test5()
    T.test6()
    T.test7()
    T.test8()
    T.test9()

