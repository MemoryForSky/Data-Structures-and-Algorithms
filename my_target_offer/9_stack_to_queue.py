
"""
栈：
- 后进先出；
- 操作系统会给每个线程创建一个栈用来存储函数调用时各个函数的参数，返回地址及临时变量等；
- 不考虑排序，O(n)时间找到栈的最大(最小)值，如果要在O(1)时间内找到，需要另外一个栈来存储。

队列：
- 先进先出；
- 树的宽度优先遍历算法（层次遍历）。
"""

"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""

class Cqueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, data):
        while self.stack1:
            self.stack2.insert(0, self.stack1.pop(0))
        self.stack1.insert(0, data)
        while self.stack2:
            self.stack1.insert(0, self.stack2.pop(0))

    def pop(self):
        if len(self.stack1) > 0:
            return self.stack1.pop(0)
        else:
            return None

    def empty(self):
        if len(self.stack1) == 0:
            return False
        else:
            return True

if __name__ == '__main__':
    q = Cqueue()
    q.push(1)
    q.push(2)
    q.push(3)
    while q.empty():
        print(q.pop())




