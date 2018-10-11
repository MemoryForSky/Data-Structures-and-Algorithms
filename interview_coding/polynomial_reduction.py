import sys
readline = sys.stdin.readline
string = readline().strip()
res = dict()
length = len(string)
i = 0
a = ''
while i < length:
    s = string[i]
    if s == 'X':
        b = ''
        j = 0
        for j, c in enumerate(string[i + 2:]):
            if c == '+' or c == '-':
                break
            b += c
        if b in res:
            res[b] += int(a)
        else:
            res[b] = int(a)
        a = ''
        i += j + 2
    else:
        a += s
        i += 1
express = []
for key, value in sorted(res.items(), key=lambda x:x[0], reverse=True):
    if value < 0:
        express.append(str(value) + 'X^' + key)
    elif value > 0:
        express.append('+' + str(value) + 'X^' + key)

if length == 0:
    print(0)
else:
    print(''.join(express).strip('+'))