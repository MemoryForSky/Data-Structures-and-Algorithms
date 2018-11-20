# x = "123456"
# print(x[::-1])

# x = [5, 2, 6, 4, 1, 3]
# x.sort()
# print(x)

# x = [5, 2, 6, 4, 1, 3]
# x_sort = sorted(x, reverse=True)
# print(x_sort)
#
# y = [("a", 3), ("b", 1), ("c", 2)]
# y_sort = sorted(y, key=lambda k:  k[1], reverse=True)
# print(y_sort)

# z = {'a': 3, 'b': 1, 'c': 2}
# z_sorted = sorted(z.items(), key=lambda items: items[1])
# print(z_sorted)

G = {1:{1:0, 2:1, 3:12},
     2:{2:0, 3:9, 4:3},
     3:{3:0, 5:5},
     4:{3:4, 4:0, 5:13, 6:15},
     5:{5:0, 6:4},
     6:{6:0}}


min_path = {i:float('inf') for i in G}

print(min_path)
