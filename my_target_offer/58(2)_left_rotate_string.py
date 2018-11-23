"""

面试题58（二）：左旋转字符串
题目：字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。比如输入字符串"abcdefg"和数
字2，该函数将返回左旋转2位得到的结果"cdefgab"。

"""

class Solution:
    def left_rotate_string(self, string, n):
        return string[n:] + string[:n]

if __name__ == '__main__':
    string = "abcdefg"

    S = Solution()
    result = S.left_rotate_string(string, 2)
    print(result)

