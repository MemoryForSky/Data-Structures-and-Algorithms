import time
"""

最长公共子序列

理解：
https://www.kancloud.cn/digest/pieces-algorithm/163624

"""
class Solution:
    def __init__(self, str1,str2):
        self.str1 = str1
        self.str2 = str2
        self.len1 = len(str1)
        self.len2 = len(str2)
        self.veca = [[0] * (self.len2+1) for _ in range(self.len1+1)]
        self.vecb = [[0] * (self.len2+1) for _ in range(self.len1+1)]

    def lcs_length(self):
        """
        自下而上循环解法
        """
        str1 = self.str1
        str2 = self.str2
        len1 = self.len1
        len2 = self.len2
        veca = self.veca
        vecb = self.vecb

        if str1 == "" and str2 == "":
            return 0

        # 自下而上循环
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if str1[i-1] == str2[j-1]:
                    veca[i][j] = veca[i-1][j-1] + 1
                    vecb[i][j] = 1
                elif veca[i-1][j] >= veca[i][j-1]:
                    veca[i][j] = veca[i-1][j]
                    vecb[i][j] = 2
                elif veca[i - 1][j] < veca[i][j - 1]:
                    veca[i][j] = veca[i][j-1]
                    vecb[i][j] = 3

        self.vecb = vecb
        return veca[len1][len2]

    def print_lcs(self, len1, len2):
        """
        输出一个最长子序列
        """
        if len1 <= 0 or len2 <= 0:
            return
        str1 = self.str1
        vecb = self.vecb
        if vecb[len1][len2] == 1:
            self.print_lcs(len1-1, len2-1)
            print(str1[len1-1], end="")
        elif vecb[len1][len2] == 2:
            self.print_lcs(len1-1, len2)
        elif vecb[len1][len2] == 3:
            self.print_lcs(len1, len2-1)

    def print_lcs_loop(self, len1, len2):
        """
        输出一个最长子序列(循环方式)
        """
        str1 = self.str1
        vecb = self.vecb
        res = []
        while len1 >= 0 and len2 >= 0:
            if vecb[len1][len2] == 1:
                res.insert(0, str1[len1-1])
                len1 -= 1
                len2 -= 1
            elif vecb[len1][len2] == 2:
                len1 -= 1
            else:
                len2 -= 1

        print(res)


    def lcs_rec(self):
        """
        递归解法
        """
        max_len = self.lcs_rec_core(0, 0)
        return max_len

    def lcs_rec_core(self, len1, len2):
        if len1 >= self.len1 or len2 >= self.len2:
            return 0

        str1 = self.str1
        str2 = self.str2

        # 自上而下递归
        if str1[len1] == str2[len2]:
            count = self.lcs_rec_core(len1 + 1, len2 + 1) + 1
        else:
            count = max(self.lcs_rec_core(len1 + 1, len2), self.lcs_rec_core(len1, len2 + 1))

        return count

    def lcs_dp(self):
        """
        递归解法(动态规划)
        """
        vec = [[-1] * self.len2 for _ in range(self.len1)]
        max_len = self.lcs_dp_core(vec, 0, 0)
        return max_len

    def lcs_dp_core(self, vec, len1, len2):
        if len1 >= self.len1 or len2 >= self.len2:
            return 0

        str1 = self.str1
        str2 = self.str2
        if vec[len1][len2] != -1:
            return vec[len1][len2]

        if str1[len1] == str2[len2]:
            count = self.lcs_dp_core(vec, len1 + 1,len2 + 1) + 1
        else:
            count = max(self.lcs_dp_core(vec, len1 + 1, len2), self.lcs_dp_core(vec, len1, len2 + 1))

        vec[len1][len2] = count

        return count

if __name__ == '__main__':
    string1 = "ABCBDAB"
    string2 = "BDCABA"
    S = Solution(string1, string2)

    print("------------lcs_dp_loop------------")
    start1 = time.perf_counter()
    sub_len = S.lcs_length()
    end1 = time.perf_counter()
    print(sub_len, "cost time: ", end1-start1)

    print("------------print one subsequence------------")
    S.print_lcs(len(string1), len(string2))
    print(end="\n")
    S.print_lcs_loop(len(string1), len(string2))

    print("------------lcs_dp_rec------------")
    start2 = time.perf_counter()
    sub_len2 = S.lcs_dp()
    end2 = time.perf_counter()
    print(sub_len2, "cost time: ", end2-start2)

    print("------------lcs_rec------------")
    start3 = time.perf_counter()
    sub_len3 = S.lcs_rec()
    end3 = time.perf_counter()
    print(sub_len3, "cost time: ", end3 - start3)





