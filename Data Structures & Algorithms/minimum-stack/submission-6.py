class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minStack.append(val)
            return
        
        if val <= self.minStack[-1]:
            self.minStack.append(val)
        
        self.stack.append(val)
        

    def pop(self) -> None:
        top = self.stack.pop()
        if top == self.minStack[-1]:
            self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
