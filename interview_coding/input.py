import sys
"""
python input
"""

"""
# input a number in line
N = sys.stdin.readline().strip()


# input several number in line
n, m, h = sys.stdin.readline().split()

# or

line = sys.stdin.readline().split()
X, Y = list(map(int, line))


# input several line in lines
game_list = []
for line in sys.stdin:
    a = line.split()
    values = list(map(int, a))
    game_list.append(values)
"""

# 读入文件
with open('./test.txt', 'r') as f:
    new_data = []
    data = f.readlines()
    for i, line in enumerate(data):
        new_line = str(i) + ' ' + line
        new_data.append(new_line)

with open('./test2.txt', 'w') as f2:
    for line in new_data:
        f2.write(line)





