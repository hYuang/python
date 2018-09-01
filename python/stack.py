class Stack (object):
    def __init__(self):
        self.stack = []
    def push(self,object):
        self.stack.append(object)
    def pop(self):
        return self.stack.pop()
    def length(self):
        return len(self.stack)


