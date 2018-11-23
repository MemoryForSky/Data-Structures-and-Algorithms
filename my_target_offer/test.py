x = -10
base = 1
x_list = [0] * 32
for i in range(31, -1, -1):
    if x & base != 0:
        x_list[i] += 1
    base <<= 1

print(x_list)

print(-10 & 2)