"""

面试题31：栈的压入、弹出序列
题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是
否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1、2、3、4、
5是某栈的压栈序列，序列4、5、3、2、1是该压栈序列对应的一个弹出序列，但
4、3、5、1、2就不可能是该压栈序列的弹出序列。

"""
class Solution:
    def is_pop_order(self, push_data, pop_data):
        b_possible = False

        stack_data = []
        if push_data is not None and pop_data is not None:
            while len(push_data) > 0:
                stack_data.insert(0, push_data[0])
                push_data.pop(0)
                while len(stack_data) > 0 and len(pop_data) > 0 and stack_data[0] == pop_data[0]:
                    stack_data.pop(0)
                    pop_data.pop(0)

            if len(stack_data) == 0 and len(pop_data) == 0:
                b_possible = True

        return b_possible

if __name__ == "__main__":
    S = Solution()
    push_data = [1, 2, 3, 4, 5]
    push_data2 = [6]
    pop_data = [4, 5, 3, 2, 1, 6]
    pop_data2 = [4, 3, 5, 1, 2]
    pop_data3 = [6]
    result = S.is_pop_order(push_data2, pop_data3)
    print(result)


