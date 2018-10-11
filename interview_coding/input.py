import sys
"""
python input
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



