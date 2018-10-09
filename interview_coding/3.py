import sys

def takeFirst(elem):
    return elem[0]

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

game_list = []
for line in sys.stdin:
    a = line.split()
    values = list(map(int, a))
    game_list.append(values)

game_list.sort(key=takeFirst)

x_len = len(game_list)
sum = 0
for i in range(x_len):
    if n < game_list[i][0]:
        break
    n -= game_list[i][0]
    sum += game_list[i][1]

print(sum)


