import random

def Bookie(n, n1, n2):
    for i in range(2*n-1-n1-n2):
        D = random.randint(1,2)
        if D == 1:
            n1 += 1
        else:
            n2 += 1

        if n == n1:
            return 1
        if n == n2:
            return 2

N = 10000
win = 0
for i in range(N):
    if Bookie(3, 2, 1) == 1:
        win += 1

print("甲赢得的概率为：%f" % (float(win)/float(N)))
print("乙赢得的概率为：%f" % (1 - float(win)/float(N)))



