"""

面试题38：字符串的排列
题目：输入一个字符串，打印出该字符串中字符的所有排列。例如输入字符串abc，
则打印出由字符a、b、c所能排列出来的所有字符串abc、acb、bac、bca、cab和cba。

"""
class Solution:
    def permutation(self, string):
        if not len(string):
            return

        # 终止条件
        if len(string) == 1:
            return list(string)

        str_list = list(string)
        str_list.sort()
        pStr = []
        for i in range(len(str_list)):
            if i > 0 and str_list[i] == str_list[i-1]:
                continue

            # 迭代公式：1、递归
            temp = self.permutation("".join(str_list[:i]) + "".join(str_list[i+1:]))

            # 2、合并字符
            for j in temp:
                pStr.append(str_list[i] + j)

        return pStr

    def group(self, string):
        if not len(string):
            return []

        if len(string) == 1:
            return list(string)

        str_list = list(string)
        str_list.sort()
        pStr = []
        for i in range(len(str_list)):
            pStr.append(str_list[i])
            if i > 0 and str_list[i] == str_list[i - 1]:
                continue

            temp = self.group("".join(str_list[i + 1:]))

            for j in temp:
                pStr.append(str_list[i] + j)

            # pStr = list(set(pStr))
            # pStr.sort()

        return pStr

if __name__ == "__main__":
    string = "abc"

    S = Solution()
    str_list = S.permutation(string)
    print(str_list)

    str_list = S.group(string)
    print(str_list)




