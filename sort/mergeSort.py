"""
归并排序：

基本思想：
将两个的有序数列合并成一个有序数列，我们称之为"归并"。
① 分解 -- 将当前区间一分为二，即求分裂点 mid = (low + high)/2;
② 求解 -- 递归地对两个子区间a[low...mid] 和 a[mid+1...high]进行归并排序。递归的终结条件是子区间长度为1。
③ 合并 -- 将已排序的两个子区间a[low...mid]和 a[mid+1...high]归并为一个有序的区间a[low...high]。

时间复杂度：O(nlog(n))

参数说明：
data -- 包含两个有序区间的数组
start -- 第1个有序区间的起始地址。
mid   -- 第1个有序区间的结束地址。也是第2个有序区间的起始地址。
end   -- 第2个有序区间的结束地址。

"""
def merge(data, start, mid, end):
    tmp = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:      # O(n)
        if data[i] <= data[j]:
            tmp.append(data[i])
            i += 1
        else:
            tmp.append(data[j])
            j += 1

    for ii in range (i, mid + 1):
        tmp.append(data[ii])

    for jj in range(j, end + 1):
        tmp.append(data[jj])

    for k in range(len(tmp)):
        data[start + k] = tmp[k]


def mergeSort(data, start, end):
    if data == None or start >= end:
        return
    mid = (end + start) // 2      # O(log(n))
    mergeSort(data, start, mid)
    mergeSort(data, mid + 1, end)
    merge(data, start, mid, end)


if __name__ == '__main__':
    data = [20, 40, 30, 10, 60, 50]
    data_len = len(data)
    print("before sort:", data)

    mergeSort(data, 0, data_len-1)

    print("after sort:", data)