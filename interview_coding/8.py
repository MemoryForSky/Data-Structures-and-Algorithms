import sys

# -7X^4+5X^6-3X^3+3X^3+1X^0
num_list = []
input = sys.stdin.readline().strip()
x = input.replace("-", "+-")
xx = x.split("+")
for i in xx:
    if i != '':
        num_list.append(i)

num_list2 = []
for item in num_list:
    ele_list = item.split("X^")
    num_list2.append(ele_list)

book = {}
for item in num_list2:
    if item[1] not in book:
        book[item[1]] = []
        book[item[1]].append(item[0])
    else:
        book[item[1]].append(item[0])

for item in book:
    values = list(map(int, book[item]))
    number = 0
    for value in values:
        number += value
    book[item] = number

sorted(book.keys())
print(book)
