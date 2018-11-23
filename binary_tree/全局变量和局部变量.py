# 如果函数内无global关键字，优先读取局部变量，无局部变量读取全局变量，不能重新赋值

# name = 'jack'
#
# def change_name():
#     name = 'john'
#     print(name)
#
# change_name()
# print(name)


# 如果函数中有global关键字  可以读取或者重新给全局变量赋值

# name = 'jack'
#
# def change_name():
#     global name    # 修改全局变量
#     name = 'john'
#     print(name)
#
# change_name()
# print(name)


# 对于可变对象可以对内部元素进行操作

name = ['jack', 'john']

def change_name():
    name.append('tom')
    print(name)

change_name()
print(name)


name = ['Jack', 'John']

def change_name():
    name = ['Tom']
    print(name)

change_name()
print(name)



# 修改全局变量和修改上一级变量


# name = 'Jack'
#
# def one():
#     name = 'Tom'
#
#     def two():
#         global name
#         name = 'Jarry'
#
#     two()
#     print(name)
#
#
# print(name)
# one()
# print(name)



# name = 'Jack'
#
# def one():
#     name = 'Tom'
#
#     def two():
#         nonlocal name   #修改上一级变量
#         name = 'Jarry'
#
#     two()
#     print(name)
#
#
# print(name)
# one()
# print(name)


