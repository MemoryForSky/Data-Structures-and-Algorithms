import copy

class Solution:
    def __init__(self):
        self.path = []
        self.path_sum = []

    def get_minimum_stones(self, road_stone_list):
        length = len(road_stone_list)

        path = []
        path_sum = 0

        return self.get_minimum_stones_core(road_stone_list, path, path_sum, length-1)

    def get_minimum_stones_core(self, data, path, path_sum, n):
        path.append(data[n])
        path_sum += data[n]

        if 3 <= n <= 5:
            self.path.append(copy.deepcopy(path))
            self.path_sum.append(path_sum)

        if n > 3:
            self.get_minimum_stones_core(data, path, path_sum, n - 3)
        if n > 4:
            self.get_minimum_stones_core(data, path, path_sum, n - 4)
        if n > 5:
            self.get_minimum_stones_core(data, path, path_sum, n - 5)

        path.pop(-1)


if __name__ == '__main__':
    data = [0, 3, 1, 3, 4, 1, 5, 6, 7]

    S = Solution()
    S.get_minimum_stones(data)
    print("所有可行的路径：", S.path)
    print("路径的长度：", S.path_sum)
    # 取其中一个最小值
    print("最短路径：", S.path[S.path_sum.index(min(S.path_sum))])



