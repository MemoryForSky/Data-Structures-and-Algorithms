class Solution:
    def print_n_num(self, n):
        if n < 1:
            return

        max_n_num = 1
        for i in range(n):
            max_n_num *= 10

        for num in range(1, max_n_num):
            print(num)

if __name__ == '__main__':
    S = Solution()
    S.print_n_num(2)




