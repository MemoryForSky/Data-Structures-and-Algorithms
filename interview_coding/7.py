import sys

number = sys.stdin.readline()

l = list(number)

result = "".join(l[::-1])

print(result)