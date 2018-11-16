"""

面试题46：把数字翻译成字符串
题目：给定一个数字，我们按照如下规则把它翻译为字符串：0翻译成"a"，1翻
译成"b"，……，11翻译成"l"，……，25翻译成"z"。一个数字可能有多个翻译。例
如12258有5种不同的翻译，它们分别是"bccfi"、"bwfi"、"bczi"、"mcfi"和
"mzi"。请编程实现一个函数用来计算一个数字有多少种不同的翻译方法。

"""

class Solution:
    def get_translation_count(self, number):
        """翻译数字主程序"""
        if not isinstance(number, int) or number < 0:
            return 0

        number_str = str(number)

        # return self.get_translation_count_core(number_str, 0, len(number_str) - 1)

        return self.get_translation_count_core_dp(number_str)

    def get_translation_count_core(self, number_str, start, end):
        """
        递归解法

        :param number_str: 数字字符串
        :param start: 起始位置
        :param end: 终止位置
        :return: 翻译方法个数
        """
        # 终止条件
        if start >= end:
            return 1

        num = int(number_str[start] + number_str[start + 1])
        if 10 <= num <= 25:
            gi = 1
        else:
            gi = 0

        # 迭代公式
        return self.get_translation_count_core(number_str, start + 1, end) + \
        gi * self.get_translation_count_core(number_str, start + 2, end)

    @staticmethod
    def get_translation_count_core_dp(number_str):
        """
        动态规划

        :param number_str: 数字字符串
        :return: 翻译方法个数
        """
        length = len(number_str)
        counts = [0] * length

        for i in range(length-1, -1, -1):
            if i == length - 1:
                count = 1
            else:
                count = counts[i + 1]

                gi = int(number_str[i] + number_str[i+1])
                if 10 <= gi <= 25:
                    if i < length - 2:
                        count += counts[i+2]
                    else:
                        count += 1
            counts[i] = count

        count = counts[0]
        return count


if __name__ == '__main__':
    digit = 12258
    S = Solution()
    result = S.get_translation_count(digit)
    print(result)