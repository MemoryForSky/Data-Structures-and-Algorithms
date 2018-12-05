"""

最优二叉搜索树

"""


class Solution:
    def optimal_BST(self, p, q, n):
        e = [[float("inf")] * (n + 1) for _ in range(n + 2)]
        w = [[0] * (n + 1) for _ in range(n + 2)]
        root = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 2):
            e[i][i-1] = q[i - 1]
            w[i][i-1] = q[i - 1]

        for l in range(1, n + 1):
            for i in range(1, n - l + 2):
                j = i + l - 1
                w[i][j] = w[i][j-1] + p[j] + q[j]
                for r in range(i, j + 1):
                    t = e[i][r-1] + e[r+1][j] + w[i][j]
                    if t < e[i][j]:
                        e[i][j] = t
                        root[i][j] = r

        return e, root

    def construct_optimal_BST(self, root, i, j):
        if i == 1 and j == len(root[0])-1:
            print("k", root[i][j], "是根")

        if i < j:
            r = root[i][j]
            if r != i:
                print("k", root[i][r-1], "是k", r, "的左孩子")
            self.construct_optimal_BST(root, i, r-1)

            if r != j:
                print("k", root[r+1][j], "是k", r, "的右孩子")
            self.construct_optimal_BST(root, r+1, j)

        # 叶节点
        if i == j:
            print("d", i - 1, "是k", i, "左孩子")
            print("d", i, "是k", i, "右孩子")

        if i > j:
            # 只有左子树
            print("d", j, "是k", j, "右孩子")
            # 只有右子树
            # print("d", j, "是k", i, "左孩子")
            # TODO


if __name__ == '__main__':
    p = [0.00, 0.15, 0.10, 0.05, 0.10, 0.20]
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]

    S = Solution()
    e, root = S.optimal_BST(p, q, 5)
    print(e[1][5])
    S.construct_optimal_BST(root, 1, 5)
