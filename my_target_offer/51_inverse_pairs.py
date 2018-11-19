"""

面试题51：数组中的逆序对
题目：在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组
成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

"""

class Solution1:
    def inverse_pairs(self, nums):
        if not isinstance(nums, list) or len(nums) == 0:
            return 0

        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] < nums[i]:
                    count += 1

        return count

class Solution2:
    def inverse_pairs(self, nums):
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0

        start = 0
        end = len(nums) - 1

        return self.inverse_pairs_core(nums, start, end)

    def inverse_pairs_core(self, nums, start, end):
        if start == end:
            return 0

        mid = (end + start) // 2

        left = self.inverse_pairs_core(nums, start, mid)
        right = self.inverse_pairs_core(nums, mid + 1, end)
        count = self.merge(nums, start, mid, end)

        return left + right + count


    def merge(self, nums, start, mid, end):
        tmp = []
        count = 0

        i = mid
        j = end
        while i >= start and j >= mid + 1:
            if nums[i] > nums[j]:
                count += j - mid
                tmp.insert(0, nums[i])
                i -= 1
            else:
                tmp.insert(0, nums[j])
                j -= 1

        while i >= start:
            tmp.insert(0, nums[i])
            i -= 1

        while j >= mid + 1:
            tmp.insert(0, nums[j])
            j -= 1

        for k in range(len(tmp)):
            nums[start + k] = tmp[k]

        return count


class Test:
    def test(self, data, expected):
        S1 = Solution2()
        output = S1.inverse_pairs(data)
        print("output: ", output, "expected: ", expected)

    def test1(self):
        data = [1, 2, 3, 4, 7, 6, 5]
        expected = 3
        self.test(data, expected)

    def test2(self):
        data = [6, 5, 4, 3, 2, 1]
        expected = 15
        self.test(data, expected)

    def test3(self):
        data = [1, 2, 3, 4, 5, 6]
        expected = 0
        self.test(data, expected)

    def test4(self):
        data = [1]
        expected = 0
        self.test(data, expected)

    def test5(self):
        data = [1, 2]
        expected = 0
        self.test(data, expected)

    def test6(self):
        data = [2, 1]
        expected = 1
        self.test(data, expected)

    def test7(self):
        data = [1, 2, 1, 2, 1]
        expected = 3
        self.test(data, expected)

    def test8(self):
        data = None
        expected = 0
        self.test(data, expected)



if __name__ == '__main__':
    T = Test()
    T.test1()
    T.test2()
    T.test3()
    T.test4()
    T.test5()
    T.test6()
    T.test7()
    T.test8()
