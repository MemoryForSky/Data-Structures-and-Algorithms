def longest_com_sub(str1, str2):
    max_len = 0
    index = 0
    sub_str = ""
    # str_dict = {}
    str1_len = len(str1)
    str2_len = len(str2)
    for index1 in range(str1_len):
        count = longest_com_sub_core(str1, str2,str1_len, str2_len, index1, index)
        max_len = max(max_len, count)
        # str_dict[count] = sub_str
    return max_len

def longest_com_sub_core(str1, str2, str1_len, str2_len, index1, index):
    count1 = 0
    count2 = 0
    for index2 in range(index, str2_len):
        if index1 < str1_len and index2 == str2_len - 1:
            count1 = longest_com_sub_core(str1, str2, str1_len, str2_len, index1 + 1, index2)

        if index1 < str1_len and index2 < str2_len and str1[index1] == str2[index2]:
            count2 = 1 + longest_com_sub_core(str1, str2, str1_len, str2_len, index1 + 1, index2 + 1)

    return count1 + count2

if __name__ == '__main__':
    str1 = "BDCABA"
    str2 = "ABCBDAB"
    str_length= longest_com_sub(str1, str2)
    print(str_length)


