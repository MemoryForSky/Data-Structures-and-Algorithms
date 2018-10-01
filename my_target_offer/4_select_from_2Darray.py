
"""
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

"""
查找方式从右上角开始查找
如果当前元素大于target, 左移一位继续查找
如果当前元素小于target, 下移一位继续查找
进行了简单的修改, 可以判定输入类型为字符的情况
"""

def search_num(array2D, target):
    if array2D == None:
        return 0

    rows, columns = len(array2D), len(array2D[0])
    row = 0
    column = columns - 1
    found = False
    while row < rows and column >= 0:
        if target == array2D[row][column]:
            found = True
            break
        elif target < array2D[row][column]:
            column -= 1
        else:
            row += 1

    return found

if __name__ == "__main__":
    array2D = [[]]
    if search_num(array2D, 10):
        print("found")
    else:
        print("not found")



