"""

面试题41：数据流中的中位数
题目：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么
中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
那么中位数就是所有数值排序之后中间两个数的平均值。

"""

class Solution:
    def __init__(self):
        self.max_heap = MaxHeap()
        self.min_heap = MinHeap()

    def insert(self, num):
        """
        插入从数据流中读出来的数据

        :param num: 读入数据
        :return: 最大堆和最小堆
        """
        if (self.max_heap.size() + self.min_heap.size()) & 1 == 0:
            if self.max_heap.size() > 0 and num < self.max_heap.max[0]:
                self.max_heap.push(num)
                num = self.max_heap.pop()

            self.min_heap.push(num)

        else:
            if self.min_heap.size() > 0 and num > self.min_heap.min[0]:
                self.min_heap.push(num)
                num = self.min_heap.pop()
            self.max_heap.push(num)

    def get_median(self):
        """
        得到已有数据的中位数

        :return: 中位数
        """
        size = self.max_heap.size() + self.min_heap.size()
        if size == 0:
            return "No numbers..."
        if size & 1 == 1:
            median = self.min_heap.min[0]
        else:
            median = (self.max_heap.max[0] + self.min_heap.min[0]) / 2

        return median


class MaxHeap:
    def __init__(self):
        """
        min: 堆数据
        """
        self.max = []

    def max_heap(self, data, start, end):
        """自上而下更新最大堆"""
        current = start
        left = current * 2 - 1
        tmp = data[current]
        while left <= end:
            if left < end and data[left] < data[left + 1]:
                left = left + 1
            if tmp >= data[left]:
                break
            else:
                data[current], data[left] = data[left], data[current]
            current = left
            left = current * 2 + 1

    def initial_heap(self, data):
        """给定数据初始化最大堆"""
        data_len = len(data)
        for i in range(data_len // 2 - 1, -1, -1):
            self.max_heap(data, i, data_len - 1)
        print(data)

    def push(self, num):
        """
        最大堆插入数据：自下而上更新最大堆
        """
        self.max.append(num)
        current = len(self.max) - 1
        parent = len(self.max) // 2 - 1
        tmp = self.max[current]
        while parent >= 0:
            if tmp <= self.max[parent]:
                break
            else:
                self.max[parent], self.max[current] = self.max[current], self.max[parent]
            current = parent
            parent = (current +1) // 2 - 1

    def pop(self):
        """最大堆删除最大值"""
        max_val = self.max[0]
        self.max[0] = self.max[-1]
        del self.max[-1]
        self.max_heap(self.max, 0, len(self.max)-1)
        return max_val

    def size(self):
        """最小堆数据个数"""
        return len(self.max)

class MinHeap:
    def __init__(self):
        """
        min: 堆数据
        """
        self.min = []

    def min_heap(self, data, start, end):
        """
        自上而下更新最小堆
        """
        current = start
        left = current * 2 + 1
        tmp = data[current]
        while left <= end:
            if left < end and data[left] > data[left + 1]:
                left = left + 1
            if tmp <= data[left]:
                break
            else:
                data[current], data[left] = data[left], data[current]
            current = left
            left = current * 2 + 1

    def initial_heap(self, data):
        """给定数据初始化最小堆"""
        data_len = len(data)
        for i in range(data_len // 2 - 1, -1, -1):
            self.min_heap(data, i, data_len - 1)
        print(data)

    def push(self, num):
        """
        最小堆插入数据：自下而上更新最小堆
        """
        self.min.append(num)
        current = len(self.min) - 1
        parent = len(self.min) // 2 - 1
        tmp = self.min[current]
        while parent >= 0:
            if tmp >= self.min[parent]:
                break
            else:
                self.min[parent], self.min[current] = self.min[current], self.min[parent]
            current = parent
            parent = (current +1) // 2 - 1

    def pop(self):
        """最小堆删除数据"""
        min_val = self.min[0]
        self.min[0] = self.min[-1]
        del self.min[-1]
        self.min_heap(self.min, 0, len(self.min)-1)
        return min_val

    def size(self):
        """最小堆数据个数"""
        return len(self.min)


if __name__ == '__main__':
    S = Solution()
    print(S.get_median())
    S.insert(5)
    print(S.get_median())
    S.insert(2)
    print(S.get_median())
    S.insert(3)
    print(S.get_median())
    S.insert(4)
    print(S.get_median())
    S.insert(1)
    print(S.get_median())
    S.insert(6)
    print(S.get_median())
    S.insert(7)
    print(S.get_median())
    S.insert(0)
    print(S.get_median())
    S.insert(8)
    print(S.get_median())
