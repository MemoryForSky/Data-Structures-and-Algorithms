import time
"""
朴素模式匹配：暴力匹配

直接逐个向下比较，子串和主串字符存在很多重复部分时时间复杂度较高，有些比较没有必要。
"""

def index(S, T, pos):
    i = pos
    j = 0
    while i < len(S) and j < len(T):
        if S[i] == T[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0

    if (j >= len(T)):
        return i - len(T)
    else:
        return 0

"""
KMP模式匹配算法:

基本思想：
利用已经部分匹配的有效信息，保持i指针不回溯，通过修改j指针，让模式串尽量地移动到有效的位置。
"""
def get_next(T, next_list):
    next_list[0] = -1
    j = 0
    k = -1
    while j < len(T) - 1:      # O(m)
        if k == -1 or T[j] == T[k]:
            j = j + 1
            k = k + 1
            if T[j] != T[k]:      # 跳过T[j] == T[k]的位置，因为T[j] != S[i],则T[k] != S[i]，故无须比较
                next_list[j] = k
            else:
                next_list[j] = next_list[k]
        else:
            k = next_list[k]


def index_KMP(S, T, pos):
    i = pos
    j = 0
    next = [0] * (len(T))

    get_next(T, next)      # O(m)
    print(next)

    while i < len(S) and j < len(T):      # O(n)
        # j == -1：首字母不相等i持续后移，j保持在首地址；S[i] == T[j]：字母相等时i,j持续后移比较；
        if j == -1 or S[i] == T[j]:
            i += 1
            j += 1
        else:
            j = next[j]

    if (j >= len(T)):
        return i - len(T)
    else:
        return 0


if __name__ == '__main__':
    S = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabxde"
    T = "aaaaaaaaaaab"
    pos = 0
    start1 = time.perf_counter()
    pos = index(S, T, pos)
    end1 = time.perf_counter()
    print("子串在主串中的位置为：", pos, "； 花费时间：", end1 - start1)

    start2 = time.perf_counter()
    pos2= index_KMP(S, T, pos)
    end2 = time.perf_counter()
    print("子串在主串中的位置为：", pos2, "； 花费时间：", end2 - start2)



