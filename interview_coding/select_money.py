"""

给你六种面额 1、5、10、20、50、100 元的纸币，假设每种币值的数量都足够多，编写程序求组成N元（N为0~10000的非负整数）的不同组合的个数。
输入描述:
输入包括一个整数n(1 ≤ n ≤ 10000)


输出描述:
输出一个整数,表示不同的组合方案数

输入例子1:
1

输出例子1:
1

"""

"""

递归与循环(动态规划)：

思想：
用自上而下的递归思路分析问题，然后基于自下而上的循环实现代码；

解题思路：
这类问题主要包含三部分：(1)化为子问题；(2)终止条件；(3)迭代方式。

(1)化为子问题：一般写成树的形式，比较直观；
                               (N, 100)
                (N-100, 100)                (N, 50)
        (N-200, 100)  (N-100, 50)     (N-50, 50)  (N, 20)
                   ...                         ...
     (100,100)                                         (N,5)
 (0, 100)  (N-100, 50)                            (N-5, 5)  (N, 1)

(2)终止条件：树的叶子节点作为终止条件；
由上面的二叉树可以看出：叶子节点为(0, m)或(n, 1)，此时组合个数为1，将这两个条件作为终止条件。

(3)迭代方式：化成小问题的迭代公式。
由二叉树的生成方式可以得到：
f(n, m) = f(n-m, m) + f(n, m-1)      n >= m
f(n, m) = f(n, m-1)                  n < m

"""

import time

def get_n(n, m, money_list):
    """
    递归解法

    :param n: 总钱数
    :param m: 纸币种类
    :param money_list: 纸币数组
    :return: 不同组合个数
    """
    if n == 0:
        return 1

    if money_list[m] == 1:
        return 1

    if n >= money_list[m]:
        count = get_n(n-money_list[m], m, money_list) + get_n(n, m-1, money_list)
    else:
        count = get_n(n, m-1, money_list)

    return count

def get_n_dp(n, money_list):
    """
    循环（动态规划）

    :param n: 总钱数
    :param money_list: 纸币数组
    :return: 不同组合个数
    """
    dp = [1] * (n + 1)
    for i in range(1, 6):
        for j in range(0, n + 1):
            if j >= money_list[i]:
                dp[j] = dp[j] + dp[j - money_list[i]]
    return dp[-1]


if __name__ == '__main__':
    money = 1000
    money_lists = [1, 5, 10, 20, 50, 100]

    print("-----------递归----------")
    start1 = time.perf_counter()
    result = get_n(money, len(money_lists)-1, money_lists)
    end1 = time.perf_counter()
    print("不同组合个数：", result, "\n", "运行时间：", end1-start1)

    print("-----------动态规划----------")
    start2 = time.perf_counter()
    result2 = get_n_dp(money, money_lists)
    end2 = time.perf_counter()
    print("不同组合个数：", result2, "\n", "运行时间：", end2 - start2)



