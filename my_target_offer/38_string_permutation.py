import copy
import random
"""

面试题38：字符串的排列
题目：输入一个字符串，打印出该字符串中字符的所有排列。例如输入字符串abc，
则打印出由字符a、b、c所能排列出来的所有字符串abc、acb、bac、bca、cab和cba。

"""
class Solution:
    def __init__(self):
        self.result = []

    def permutation(self, nums):
        """
        数组的排列：直接原地址操作，交换数据，不需要额外空间

        :param nums: 数组
        :return: 所有排列
        """
        if len(nums) == 0:
            return

        self.permutation_core(nums, 0)

    def permutation_core(self, nums, index):
        if index == len(nums)-1:
            self.result.append(copy.deepcopy(nums))
        else:
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                self.permutation_core(nums, index + 1)
                nums[index], nums[i] = nums[i], nums[index]

    def permutation2(self, string):
        """
        字符串排列：不交换原数据，排列结果放在额外的空间

        :param string: 字符串
        :return: 所有排列
        """
        if not len(string):
            return

        # 终止条件
        if len(string) == 1:
            return list(string)

        str_list = list(string)
        str_list.sort()
        pStr = []
        for i in range(len(str_list)):
            if i > 0 and str_list[i] == str_list[i-1]:
                continue

            # 迭代公式：1、递归
            sub_str = "".join(str_list[:i]) + "".join(str_list[i+1:])
            temp = self.permutation(sub_str)

            # 2、合并字符
            for j in temp:
                pStr.append(str_list[i] + j)

        return pStr

    def group(self, string):
        """
        组合同排列不一样在于，相同的字符只能出现一次：
        1、1中字符串的第一个字符取所有可能的结果，并把每个字符添加到字符串列表；
        2、相对于排列，组合中2的子串只取后面的字符，已经出现在字符串中的第i个元素不在子串中出现。

        """
        if not len(string):
            return []

        if len(string) == 1:
            return list(string)

        str_list = list(string)
        str_list.sort()
        pStr = []

        # 1
        for i in range(len(str_list)):
            if i > 0 and str_list[i] == str_list[i - 1]:
                continue
            pStr.append(str_list[i])

            # 2
            sub_str = "".join(str_list[i + 1:])
            temp = self.group(sub_str)

            # 3
            for j in temp:
                pStr.append(str_list[i] + j)

            # pStr = list(set(pStr))
            # pStr.sort()

        return pStr

    def cube_equal(self, perm_list):
        """
        求正方体的对面顶点和相等的排列

        :param perm_list: 全排列
        :return: 满足要求的排列
        """
        equal_list = []
        for item in perm_list:
            if item[0] + item[1] + item[2] + item[3] == item[4] + item[5] + item[6] + item[7] and \
                    item[0] + item[2] + item[4] + item[6] == item[1] + item[3] + item[5] + item[7] and \
                    item[0] + item[1] + item[4] + item[5] == item[2] + item[3] + item[6] + item[7]:
                equal_list.append(item)

        num_equal = len(equal_list)
        print("一共有 ", num_equal, " 种排列")
        print("其中一个： ", equal_list[random.randrange(num_equal)])

    def queue_8(self, queues):
        """
        八皇后问题

        :param queues: 全排列
        :return: 所有可行解
        """
        queue_result = []
        for queue in queues:
            flag = True
            for i in range(len(queue)):
                for j in range(i + 1, len(queue)):
                    if i - j == queue[i] - queue[j] or j - i == queue[i] - queue[j]:
                        flag = False
            if flag:
                queue_result.append(queue)
        return queue_result


if __name__ == "__main__":
    string = "abc"

    S = Solution()

    # permu_list = S.permutation(string)
    # print("permutation: ", permu_list)
    #
    # group_list = S.group(string)
    # print("group: ", group_list)

    # string2 = [1, 2, 3, 4, 5, 6, 7, 8]
    # S.permutation(string2)
    # print("一共有 ", len(S.result), " 种排列")
    # print("对于正方体的八个顶点，对面顶点和相等的排列：")
    # S.cube_equal(S.result)

    queue = [0, 1, 2, 3, 4, 5, 6, 7]
    S.permutation(queue)
    queue_result = S.queue_8(S.result)
    print(len(queue_result))







