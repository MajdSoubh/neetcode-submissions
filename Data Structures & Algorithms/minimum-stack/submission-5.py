class MinStack:

    def __init__(self):
        self.min = None
        self.stack = []

    def push(self, val: int) -> None:
        if self.min == None:
            self.min = val
            self.stack.append(0)
        elif self.min <= val:
            self.stack.append(val-self.min)
        elif self.min > val:
            self.stack.append(val-self.min)
            self.min = val

    def pop(self) -> None:
        if len(self.stack) == 1:
            self.min = None
        elif self.stack[-1] < 0:
            self.min -= self.stack[-1]
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] + self.min if self.stack[-1] >= 0 else self.min

    def getMin(self) -> int:
        return self.min