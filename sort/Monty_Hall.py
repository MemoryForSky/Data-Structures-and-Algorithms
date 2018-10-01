import random

def MontyHall(Dselect, Dchange):
    Dcar = random.randint(1,3)
    if Dselect == Dcar and Dchange == 0:
        return 1
    elif Dselect == Dcar and Dchange == 1:
        return 0
    elif Dselect != Dcar and Dchange == 0:
        return 0
    else:
        return 1

# 不确定是否改变选择
def test1(N):
	win = 0
	for i in range(N):
	    Dselect = random.randint(1,3)
	    Dchange = random.randint(0,1)
	    win = win + MontyHall(Dselect, Dchange)
	print(float(win)/float(N))

# 确定不改变选择
def test2(N):
	win = 0
	for i in range(N):
	    Dselect = random.randint(1,3)
	    Dchange = 0
	    win = win + MontyHall(Dselect, Dchange)
	print(float(win)/float(N))

# 确定改变选择
def test3(N):
	win = 0
	for i in range(N):
	    Dselect = random.randint(1,3)
	    Dchange = 1
	    win = win + MontyHall(Dselect, Dchange)
	print(float(win)/float(N))

N = 10000
print("不确定是否改变选择概率：")
test1(N)
print("确定不改变选择概率：")
test2(N)
print("确定改变选择概率：")
test3(N)