"""

矩阵中的路径：

设计一个函数，用来判断在一个字符串中是否存在一条包含某字符串所有字符的路径。

"""

class Solution:
    def has_path(self, matrix, rows, cols, str):
        if matrix is None or rows < 1 or cols < 1 or str is None:
            return False

        visits = [0] * (rows * cols)
        str_index = 0
        for row in range(rows):
            for col in range(cols):
                if self.has_path_core(matrix, rows, cols, row, col, str, str_index, visits):
                    return True
        return False


    def has_path_core(self, matrix, rows, cols, row, col, str, str_index, visits):
        if str_index == len(str):
            return True

        has_path = False
        if 0 <= row < rows and 0 <= col < cols and matrix[row*cols + col] == str[str_index] \
                and visits[row*cols + col] == 0:
            str_index += 1
            visits[row*cols + col] = 1

            has_path = self.has_path_core(matrix, rows, cols, row, col-1, str, str_index, visits) \
                        or self.has_path_core(matrix, rows, cols, row-1, col, str, str_index, visits) \
            or self.has_path_core(matrix, rows, cols, row, col+1, str, str_index, visits) \
            or self.has_path_core(matrix, rows, cols, row+1, col, str, str_index, visits)

            if has_path is False:
                str_index -= 1
                visits[row*cols + col] = 0

        return has_path


if __name__ == '__main__':
    # matrix = ['a', 'b', 't', 'g', 'c', 'f', 'c', 's', 'j', 'd', 'e', 'h']
    # str = ['b', 'f', 'c', 's', 'h', 'e', 'd', 'j', 'c', 'a', '#']
    matrix = 'abtgcfcsjdeh'
    str = 'ab'
    S = Solution()
    result = S.has_path(matrix, 3, 4, str)
    print(result)
