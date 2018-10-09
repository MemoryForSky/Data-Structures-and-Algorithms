"""

机器人的运动范围：
m行n列的方格，机器人从(0,0)出发，可以上下左右行走，但不能进入行坐标和列坐标的数位之和大于k的格子，计算机器人能够到达多少格子？

"""


def moving_count(matrix, rows, cols, k):

    if matrix is None or rows < 1 or cols < 1:
        return 0

    results = []
    for i in range(rows):
        rows_1 = [0] * cols
        results.append(rows_1)

    visits = [0] * (rows * cols)
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                counts = moving_count_core(matrix, rows, cols, row, col, visits, k)
                if counts == 0:
                    results[row][col] = 1

    return results

def moving_count_core(matrix, rows, cols, row, col, visits, k):
    """
    递归计算机器人行走范围
    """
    moving_count = 0
    if check(matrix, rows, cols, row, col, visits, moving_count, k):
        if matrix[row][col] == 1:
            return 1

        visits[row * cols + col] = 1

        moving_count = 1 + moving_count_core(matrix, rows, cols, row - 1, col, visits, k) \
                + moving_count_core(matrix, rows, cols, row, col - 1, visits, k) \
                + moving_count_core(matrix, rows, cols, row + 1, col, visits, k) \
                + moving_count_core(matrix, rows, cols, row, col + 1, visits, k)
    return moving_count

def check(matrix, rows, cols, row, col, visits, moving_count, k):
    """
    检查当前坐标是否满足要求，即坐标的数位之和小于threshold
    """
    if 0 <= row <rows and 0 <= col <cols and matrix[row][col] != -1 and visits[row*cols+col] == 0 and moving_count <= k:
        return True
    return False


if __name__ == '__main__':
    matrixes = [[0,-1,1,0],
                [0,0,0,-1],
                [0,-1,0,-1],
                [1,-1,0,0]]
    result = moving_count(matrixes, 4, 4, 3)
    print(result)




