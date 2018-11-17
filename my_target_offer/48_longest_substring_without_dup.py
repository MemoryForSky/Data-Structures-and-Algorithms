import time
"""

面试题48：最长不含重复字符的子字符串
题目：请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子
字符串的长度。假设字符串中只包含从'a'到'z'的字符。

"""

class Solution1:
    """暴力解法"""
    def longest_sub_str_without_dup(self, string):
        if not isinstance(string, str):
            return

        longest = 0

        for i in range(len(string)):
            for j in range(i, len(string)):
                sub_str = string[i:j + 1]
                if not self.has_dup(sub_str):
                    if len(sub_str) > longest:
                        longest = len(sub_str)
                else:
                    break

        return longest

    @staticmethod
    def has_dup(sub_str):
        tmp = {}
        has_dup = False
        for alpha in sub_str:
            if alpha not in tmp:
                tmp[alpha] = 1
            else:
                has_dup = True
                break
        return has_dup


class Solution2:
    """动态窗口"""
    def longest_sub_str_without_dup(self, string):
        if not isinstance(string, str):
            return

        window = 0
        start = 0

        while start + window <= len(string):
            sub_str = string[start:start + window]
            if self.has_dup(sub_str) == -1:
                window += 1
            else:
                start = start + self.has_dup(sub_str) + 1

        window -= 1

        return window

    @staticmethod
    def has_dup(sub_str):
        tmp = {}
        has_dup = -1
        for i in range(len(sub_str)):
            if sub_str[i] not in tmp:
                tmp[sub_str[i]] = i
            else:
                has_dup = tmp[sub_str[i]]
                break
        return has_dup


class Solution3:
    """
    动态规划

    思路：
    1、若第i个字符之前没有出现过，则f(i) = f(i-1) + 1；
    2、若第i个字符之前出现过：第i个字符同之前出现的位置的距离为d
        1> d <= f(i-1): f(i) = d
        2> d > f(i-1): f(i) = f(i-1) + 1

    """
    def longest_sub_str_without_dup(self, string):
        if not isinstance(string, str):
            return

        length = len(string)
        max_sub_len = 0
        max_length = [1] * length

        for i in range(0, length):
            if string[i] not in string[:i]:
                if i > 0:
                    max_length[i] = max_length[i-1] + 1
            else:
                if i - self.get_dup_index(string, i) <= max_length[i-1]:
                    max_length[i] = i - self.get_dup_index(string, i)
                else:
                    max_length[i] = max_length[i-1] + 1

            if max_length[i] > max_sub_len:
                max_sub_len = max_length[i]

        return max_sub_len


    @staticmethod
    def get_dup_index(sub_str, index):
        for i in range(index-1, -1, -1):
            if sub_str[i] == sub_str[index]:
                return i


class Test:
    def test(self, string, expected):
        start = time.perf_counter()
        S = Solution3()
        output = S.longest_sub_str_without_dup(string)
        end = time.perf_counter()
        print("output: ", output, ", expected: ", expected, ", cost time: ", (end - start)*1000)

    def test1(self):
        string = "abcacfrar"
        expected  = 4
        self.test(string, expected)

    def test2(self):
        string = "acfrarabc"
        expected = 4
        self.test(string, expected)

    def test3(self):
        string = "arabcacfr"
        expected = 4
        self.test(string, expected)

    def test4(self):
        string = "aaaa"
        expected = 1
        self.test(string, expected)

    def test5(self):
        string = "abcdefg"
        expected = 7
        self.test(string, expected)

    def test6(self):
        string = "aaabbbccc"
        expected = 2
        self.test(string, expected)

    def test7(self):
        string = "abcdcba"
        expected = 4
        self.test(string, expected)

    def test8(self):
        string = "abcdaef"
        expected = 6
        self.test(string, expected)

    def test9(self):
        string = "a"
        expected = 1
        self.test(string, expected)

    def test10(self):
        string = ""
        expected = 0
        self.test(string, expected)


if __name__ == "__main__":
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
    T.test10()
