"""

计算两个字符串的最大公共子串（Longest Common Substring）的长度，字符不区分大小写。

输入：输入两个字符串
输出：输出一个整数

样例输入：asdfas werasdfaswer

样例输出：6

这里的最大公共字串要求的字串是连续的。

求字串的方法和求子序列方法类似：

当str1[i] == str2[j]时，子序列长度veca[i][j] = veca[i - 1][j - 1] + 1；
只是当str1[i] != str2[j]时，veca[i][j]长度要为0，而不是max{veca[i - 1][j], veca[i][j - 1]}。

"""
class Solution:
    def lcs(self, str1, str2):
        """
        求最长公共子串

        :param str1: 字符串1；
        :param str2: 字符串2；
        :return: max_length：最长子串长度； max_sub_str：输出一个最长子串；
        """
        if str1 is None or str2 is None:
            return

        len1 = len(str1)
        len2 = len(str2)
        veca = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        max_length = 0
        max_index = 0

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if str1[i-1] == str2[j-1]:
                    veca[i][j] = veca[i-1][j-1] + 1
                    if veca[i][j] > max_length:
                        max_length = veca[i][j]
                        max_index = j
                else:
                    veca[i][j] = 0

        max_sub_str = ''
        for i in range(max_index - max_length, max_index):
            max_sub_str += str2[i]

        return max_length, max_sub_str


if __name__ == '__main__':
    string1 = 'atdfas'
    string2 = 'werasdfaswer'

    S = Solution()
    max_length, max_sub_str = S.lcs(string1, string2)
    print("atdfas和werasdfaswer最长公共子串长度为：%d，其中一个最长公共子串为：%s" % (max_length, max_sub_str))




