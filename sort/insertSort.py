"""
插入排序：

基本思想：
把n个待排序的元素看成为一个有序表和一个无序表。开始时有序表中只包含1个元素，无序表中包含有n-1个元素，
排序过程中每次从无序表中取出第一个元素，将它插入到有序表中的适当位置，使之成为新的有序表，重复n-1次可完成排序过程。

时间复杂度：O(n^2)
"""

def insertSort(num_list, num_len):
    for i in range(num_len):      # O(n)
        key = num_list[i]
        j = i - 1
        while j >= 0 and num_list[j] > key:      # O(n)
            num_list[j + 1] = num_list[j]
            j -= 1
        num_list[j + 1] = key
    return num_list


"""
希尔排序：

基本思想：
希尔排序实质上是一种分组插入方法。它的基本思想是：对于n个待排序的数列，取一个小于n的整数gap(gap被称为步长)将待排序元素分成若干个组子序列，
所有距离为gap的倍数的记录放在同一个组中；然后，对各组内的元素进行直接插入排序。 这一趟排序完成之后，每一个组的元素都是有序的。
然后减小gap的值，并重复执行上述的分组和排序。重复这样的操作，当gap=1时，整个数列就是有序的。

时间复杂度：O(n^3/2)
"""

def shellSort(num_list, num_len):
    gap =  num_len // 2
    while gap > 0:
        for i in range(gap):
            for j in range(i+gap, num_len, gap):
                if num_list[j] < num_list[j-gap]:
                    key = num_list[j]
                    k = j-gap
                    while k >= 0 and num_list[k] > key:
                        num_list[k + gap] = num_list[k]
                        k -= gap
                    num_list[k + gap] = key
        gap //= 2
    return num_list


if __name__ == '__main__':
    num_list = [20, 40, 30, 10, 60, 50]
    num_len = len(num_list)
    print("before sort:", num_list)

    # num_order = insertSort(num_list, num_len)
    num_order = shellSort(num_list, num_len)

    print("after sort:", num_order)

