"""

机器人的运动范围：
m行n列的方格，机器人从(0,0)出发，可以上下左右行走，但不能进入行坐标和列坐标的数位之和大于k的格子，计算机器人能够到达多少格子？

"""

class Solution:
    """
    计算机器人行走范围
    """
    def moving_count(self, threshold, rows, cols):
        """
        主函数，调用递归计算函数
        :param threshold: 坐标数位之和的阈值
        :param rows: 坐标行数
        :param cols: 坐标列数
        :return: 机器人行走范围之和
        """
        if threshold is None or rows < 1 or cols < 1:
            return 0

        visits = [0] * (rows * cols)

        counts = self.moving_count_core(threshold, rows, cols, 0, 0, visits)

        return counts

    def moving_count_core(self, threshold, rows, cols, row, col, visits):
        """
        递归计算机器人行走范围
        :param threshold: 坐标数位之和的阈值
        :param rows: 行数
        :param cols: 列数
        :param row: 开始行
        :param col: 开始列
        :param visits: 标识行走过的路径
        :return: 机器人行走范围之和
        """
        moving_count = 0
        if self.check(threshold, rows, cols, row, col, visits):
            visits[row*cols+col] = 1

            # 连续行走，只需要一行递归语句，行走距离累加
            moving_count = 1 + self.moving_count_core(threshold, rows, cols, row - 1, col, visits) \
                    + self.moving_count_core(threshold, rows, cols, row, col - 1, visits) \
                    + self.moving_count_core(threshold, rows, cols, row + 1, col, visits) \
                    + self.moving_count_core(threshold, rows, cols, row, col + 1, visits)

        return moving_count

    def check(self, threshold, rows, cols, row, col, visits):
        """
        检查当前坐标是否满足要求，即坐标的数位之和小于threshold
        :param threshold: 坐标数位之和的阈值
        :param rows: 行数
        :param cols: 列数
        :param row: 开始行
        :param col: 开始列
        :param visits: 标识行走过的路径
        :return: 是否满足条件
        """
        if  0 <= row <rows and 0 <= col <cols and self.get_digit_sum(row) + self.get_digit_sum(col) <= threshold \
            and visits[row*cols+col] == 0:
            return True
        return False

    def get_digit_sum(self, number):
        """
        获得一个数字的数位之和
        :param number: 数字
        :return: 数位之和
        """
        num_str = str(number)
        num_sum = 0
        for i in num_str:
            num_sum += int(i)
        return num_sum


# ====================测试代码====================
class Test:
    """
    测试用例
    """
    def __init__(self):
        """
        初始化Solution类
        """
        self.S = Solution()

    def test(self, test_name, threshold, rows, cols, expected):
        """
        测试代码
        :param test_name: 测试名称
        :param threshold: 阈值
        :param rows: 行数
        :param cols: 列数
        :param expected: 期望结果
        :return: 测试结果
        """
        if test_name is not None:
            print("%s begin: " % test_name)

        if self.S.moving_count(threshold, rows, cols) == expected:
            print("Passed.")
        else:
            print("Failed.")

    # 方格多行多列
    def test1(self):
        self.test("Test1", 5, 10, 10, 21)

    # 方格多行多列
    def test2(self):
        self.test("Test2", 15, 20, 20, 359)

    # 方格只有一行，机器人只能到达部分方格
    def test3(self):
        self.test("Test3", 10, 1, 100, 29)

    # 方格只有一行，机器人能到达所有方格
    def test4(self):
        self.test("Test4", 10, 1, 10, 10)

    # 方格只有一列，机器人只能到达部分方格
    def test5(self):
        self.test("Test5", 15, 100, 1, 79)

    # 方格只有一列，机器人能到达所有方格
    def test6(self):
        self.test("Test6", 15, 10, 1, 10)

    # 方格只有一行一列
    def test7(self):
        self.test("Test7", 15, 1, 1, 1)

    # 方格只有一行一列
    def test8(self):
        self.test("Test8", 0, 1, 1, 1)

    # 机器人不能进入任意一个方格
    def test9(self):
        self.test("Test9", -10, 10, 10, 0)


if __name__ == '__main__':
    T = Test()
    T.test1()
    T.test2()
    T.test3()
    T.test4()
    T.test5()
    T.test6()
    T.test7()
    T.test8()
    T.test9()
