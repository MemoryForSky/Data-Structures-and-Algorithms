"""
冒泡排序：

基本思想：
它会遍历若干次要排序的数列，每次遍历时，它都会从前往后依次的比较相邻两个数的大小；如果前者比后者大，则交换它们的位置。
这样，一次遍历之后，最大的元素就在数列的末尾！ 采用相同的方法再次遍历时，第二大的元素就被排列在最大元素之前。
重复此操作，直到整个数列都有序为止！

时间复杂度：O(n^2)
"""

def bubbleSort(data, data_len):
    flag = 0
    for i in range(data_len-1, 0, -1):
        for j in range(0, i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                flag = 1
        if flag == 0:
            break
    return data


import random
"""
快速排序：
使用分治法策略

基本思想：
选择一个基准数，通过一趟排序将要排序的数据分割成独立的两部分；其中一部分的所有数据都比另外一部分的所有数据都要小。
然后，再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

时间复杂度：O(nlog(n))
"""

def Patition(data, data_len, start, end):
    index = random.randint(start, end)
    data[index], data[end] = data[end], data[index]

    smallIndex = start - 1
    for index in range(start, end):
        if data[index] < data[end]:
            smallIndex += 1
            if smallIndex != index:
                data[smallIndex], data[index] = data[index], data[smallIndex]

    smallIndex += 1
    data[smallIndex], data[end] = data[end], data[smallIndex]

    return smallIndex


def quickSort(data, data_len, start, end):
    if start == end:
        return 0

    index = Patition(data, data_len, start, end)
    if index > start:
        quickSort(data, data_len, start, index - 1)
    if index < end:
        quickSort(data, data_len, index + 1, end)



if __name__ == '__main__':
    data = [20, 40, 30, 10, 60, 50]
    data_len = len(data)
    print("before sort:", data)

    quickSort(data, data_len, 0, data_len - 1)
    # bubbleSort(data, data_len)

    print("after sort:", data)

