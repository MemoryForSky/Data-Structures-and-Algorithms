
"""
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""

def replace_space(data):
    if type(data) != str:
        return

    result = ""
    for i in range(len(data)):
        if data[i] == " ":
            result += "%20"
        else:
            result += data[i]
    return result

def replace_space2(s):
    if type(s) != str:
        return
    return s.replace(' ', '%20')

if __name__ == '__main__':
    data = input()      # "we are happy."
    result = replace_space(data)
    print(result)

