"""

面试题59（二）：队列的最大值
定义一个队列并实现函数max得到队列里的最大值，要求函数max、push_back、pop_front的时间复杂度都是O(1)。

思路：
本题同滑动窗口的最大值一样，利用队列的规律存储最大值在双端队列中。

"""

class Queue:
    def __init__(self):
        self.max = []
        self.queue = []

    def push_back(self, num):
        self.queue.append(num)
        while len(self.max) != 0 and self.max[-1] < num:
            self.max.pop(-1)
        self.max.append(num)

    def pop_front(self):
        if len(self.queue) == 0:
            raise Exception("queue is empty")

        pop_num = self.queue.pop(0)
        if pop_num == self.max[0]:
            self.max.pop(0)

    def max_num(self):
        if len(self.max) == 0:
            raise Exception("max is empty")

        return self.max[0] if len(self.max) > 0 else None

if __name__ == '__main__':
    Q = Queue()
    Q.push_back(3)
    print("queue = ", Q.queue, ", max = ", Q.max_num())
    Q.push_back(5)
    print("queue = ", Q.queue, ", max = ", Q.max_num())
    Q.push_back(2)
    Q.push_back(1)
    print("queue = ", Q.queue, ", max = ", Q.max_num())
    Q.push_back(9)
    Q.push_back(8)
    print("queue = ", Q.queue, ", max = ", Q.max_num())
    Q.pop_front()
    Q.pop_front()
    Q.pop_front()
    Q.pop_front()
    print("queue = ", Q.queue, ", max = ", Q.max_num())
    Q.pop_front()
    print("queue = ", Q.queue, ", max = ", Q.max_num())
    Q.pop_front()
    print("queue = ", Q.queue, ", max = ", Q.max_num())

