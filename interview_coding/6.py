import sys
"""
LeetCode-209
"""
line1 = sys.stdin.readline().split()
values1 = list(map(int, line1))
n, X = values1

line2 = sys.stdin.readline().split()
price = list(map(int, line2))

# print(n, X)
# print(price)
# --------
# price.sort()
# sum = 0
# for i in range(0, n):
#     X -= price[i]
#     sum += price[i]
#     if X <= 0:
#         break

#--------------------------

# result = []
# for i, _ in enumerate(price):
#     price_sum = 0
#     for j, tmp in enumerate(price[i:]):
#         price_sum += tmp
#         if price_sum >= X:
#             result.append(price_sum)
#
# print(min(result))


def minSubArrayLen(X, prices):
    l = 0
    r = 0
    price_sum = 0
    prices_len = len(prices)
    result = []
    while l < prices_len:
        if r < prices_len and price_sum < X:
            price_sum += prices[r]
            r += 1
        else:
            price_sum -= prices[l]
            l += 1

        if price_sum >= X:
            result.append(price_sum)

    return min(result)

xx = minSubArrayLen(X, price)

print(xx)











