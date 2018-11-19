"""

面试题50（一）：字符串中第一个只出现一次的字符
题目：在字符串中找出第一个只出现一次的字符。如输入"abaccdeff"，则输出
'b'。

面试题50（二）：字符流中第一个只出现一次的字符
题目：请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从
字符流中只读出前两个字符"go"时，第一个只出现一次的字符是'g'。当从该字
符流中读出前六个字符"google"时，第一个只出现一次的字符是'l'。

"""

class Solution1:
    @staticmethod
    def get_first_not_repeat_char(string):
        if not isinstance(string, str) or len(string) == 0:
            return

        str_count = {}

        for char in string:
            str_count[char] = str_count.setdefault(char, 0) + 1

        for char in string:
            if str_count[char] == 1:
                return char

        return -1

class Solution2:
    def __init__(self):
        self.str_flag = [-1] * 256
        self.index = 0

    def get_first_not_repeat_char(self):
        min_val = float('inf')
        min_index = 0
        for index, val in enumerate(self.str_flag):
            if val >= 0 and val < min_val:
                min_val = val
                min_index = index

        if min_val == float('inf'):
            return -1
        else:
            return chr(min_index)


    def insert(self, char):
        if self.str_flag[ord(char)] == -1:
            self.str_flag[ord(char)] = self.index
        elif self.str_flag[ord(char)] >= 0:
            self.str_flag[ord(char)] = -2

        self.index += 1


if __name__ == '__main__':
    string = "abacbcdeedff"

    # S1 = Solution1()
    # result = S1.get_first_not_repeat_char(string)
    # print(result)

    S2 = Solution2()
    S2.insert('g')
    S2.insert('o')
    S2.insert('o')
    S2.insert('g')
    S2.insert('l')
    S2.insert('e')
    result = S2.get_first_not_repeat_char()
    print(result)

