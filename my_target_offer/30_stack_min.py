"""

"""

class Stack:
    """
    包含min函数的栈O(1)
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, data):
        self.stack1.insert(0, data)
        if len(self.stack2) == 0 or self.stack2[0] > data:
            self.stack2.insert(0, data)
        else:
            self.stack2.insert(0, self.stack2[0])

    def pop(self):
        data = self.stack1.pop(0)
        self.stack2.pop(0)
        return data

    def min(self):
        return self.stack2[0]

if __name__ == '__main__':
    S = Stack()
    S.push(5)
    S.push(2)
    S.push(3)
    S.push(1)
    S.push(6)
    print(S.min())
    S.pop()
    S.pop()
    print(S.min())
    print(S.stack1)
    print(S.stack2)



