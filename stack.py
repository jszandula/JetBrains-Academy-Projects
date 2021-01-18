class Stack():
    def __init__(self):
        self.stack = []
    def push(self, el):
        self.stack.append(el)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        # print(self.stack[-1])
        return self.stack[-1]
    def is_empty(self):
        # print(len(self.stack) == 0)
        return len(self.stack) == 0

stack = Stack()

stack.is_empty()
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.pop()
stack.pop()
stack.peek()
stack.pop()
stack.is_empty()

