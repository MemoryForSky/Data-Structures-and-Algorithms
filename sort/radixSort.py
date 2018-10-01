"""
基数排序：

基本思想：
基数排序(Radix Sort)是桶排序的扩展，它的基本思想是：将整数按位数切割成不同的数字，然后按每个位数分别比较。

时间复杂度：O(d(n+r))
"""

def countSort(data, exp):
    data_order = [0] * len(data)
    # 初始化计数数组
    count_arr = [0] * ((max(data) - min(data)) + 1)
    # 统计i的次数
    for i in range(len(data)):      # O(n)
        count_arr[((data[i] - min(data))//exp)%10] += 1
    # 对所有的计数累加
    for i in range(len(count_arr)-1):      # O(r)  r表示基数，本例中为10
        count_arr[i+1] += count_arr[i]
    # 逆向遍历源数组（保证稳定性），根据计数数组中对应的值填充到先的数组中
    for i in range(len(data)-1, -1, -1):      # O(n)
        data_order[count_arr[((data[i] - min(data))//exp)%10]-1] = data[i]
        count_arr[((data[i] - min(data)) // exp) % 10] -= 1

    for i in range(len(data)):      # O(n)
        data[i] = data_order[i]

def getMax(data):
    max = data[0]
    for i in range(len(data)):
        if data[i] > max:
            max = data[i]
    return max

def radixSort(data):
    exp = 1
    max = getMax(data)

    while max/exp > 0:      # O(d)  d表示最大数的长度
        countSort(data, exp)
        exp *= 10


if __name__ == '__main__':
    data = [234, 48, 76, 10, 98, 1, 237, 227]
    print("before sort:", data)

    radixSort(data)

    print("after sort:", data)





