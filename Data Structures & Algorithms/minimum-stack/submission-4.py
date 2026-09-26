class MinStack:

    def __init__(self):
        self.stack = []
        self.minIndex = 0

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.minIndex = 0
            return

        if val <= self.stack[self.minIndex]:
            self.minIndex = len(self.stack)

        self.stack.append(val)

    def pop(self) -> None:
        was_min = self.minIndex == len(self.stack) - 1

        self.stack.pop()

        if was_min and self.stack:
            self.minIndex = 0

            for i in range(len(self.stack)):
                if self.stack[i] < self.stack[self.minIndex]:
                    self.minIndex = i

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.minIndex]