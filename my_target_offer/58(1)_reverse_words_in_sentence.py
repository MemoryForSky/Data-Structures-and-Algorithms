"""

面试题58（一）：翻转单词顺序
题目：输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，
则输出"student. a am I"。

"""

class Solution:
    def reverse_sentence(self, string):
        if not isinstance(string, str):
            return "not string"

        words = string.split()
        words_rev = words[::-1]

        return " ".join(words_rev)


if __name__ == '__main__':
    string = "I am a student. "

    S = Solution()
    result = S.reverse_sentence(string)
    print(result)