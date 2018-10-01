"""
直接插入排序：

思想：从未排序的元素中寻找最小(or最大)元素，将其放到已排序序列的末尾。

时间复杂度：O(n^2)
"""

def selectSort(num_list, num_len):
    for i in range(num_len):      # O(n)
        min_index = i
        for j in range(i+1, num_len):      # O(n)
            if num_list[j] < num_list[min_index]:
                min_index = j      # 最小值索引存放在min_index
        if min_index != i:
            num_list[i], num_list[min_index] = num_list[min_index], num_list[i]
    return num_list


"""
堆排序：

思想：
① 初始化堆：将数列a[1...n]构造成最大堆。
② 交换数据：将num_list[0]和num_list[n-1]交换，使num_list[n-1]是num_list[0...n-1]中的最大值；
然后将num_list[0...n-2]重新调整为最大堆。 接着，将num_list[0]和num_list[n-2]交换，使a[n-2]是a[1...n-2]中的最大值；
然后将a[0...n-3]重新调整为最大值，依次类推，直到整个数列都是有序的。

时间复杂度：O(nlog(n))
"""
# 构造最大堆
def maxHeap(num_list, start, end):
    current = start
    left = 2*current + 1
    tmp = num_list[current]
    while left <= end:
        if left < end and num_list[left] < num_list[left + 1]:
            left += 1
        if tmp >= num_list[left]:
            break
        else:
            num_list[current], num_list[left] = num_list[left], num_list[current]
        current = left
        left = 2*left + 1

# 堆排序
def heapSort(num_list, num_len):
    # 初始化堆
    for i in range(num_len//2 - 1, -1, -1):
        maxHeap(num_list, i, num_len - 1)

    # 从最后一个元素开始调整排序：最后元素交换排序，前面元素重新生成最大堆
    for i in range(num_len - 1, -1, -1):      # O(n)
        num_list[0], num_list[i]= num_list[i], num_list[0]
        maxHeap(num_list, 0, i-1)      # O(log(n))
    return num_list

if __name__ == '__main__':
    num_list = [20, 40, 30, 10, 60, 50]
    num_len = len(num_list)
    print("before sort:", num_list)

    num_order = heapSort(num_list, num_len)

    print("after sort:", num_order)




