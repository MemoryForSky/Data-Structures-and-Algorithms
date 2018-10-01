"""
计数排序：

基本思想：
当数据表长度为n，已知数据表中数据的范围有限，比如在范围0−k之间，而k又比n小许多，这样可以通过统计每一个范围点上的数据频次来实现计数排序。
"""

def countSort(data):
    data_order = [0] * len(data)
    # 初始化计数数组
    count_arr = [0] * ((max(data) - min(data)) + 1)
    # 统计i的次数
    for i in range(len(data)):
        count_arr[data[i] - min(data)] += 1
    # 对所有的计数累加
    for i in range(len(count_arr)-1):
        count_arr[i+1] += count_arr[i]
    # 逆向遍历源数组（保证稳定性），根据计数数组中对应的值填充到先的数组中
    for i in range(len(data)-1, -1, -1):
        data_order[count_arr[data[i] - min(data)]-1] = data[i]
        count_arr[data[i] - min(data)] -= 1
    return data_order


if __name__ == '__main__':
    data = [20, 40, 30, 10, 60, 50]
    print("before sort:", data)

    # num_order = insertSort(num_list, num_len)
    data_order = countSort(data)

    print("after sort:", data_order)

