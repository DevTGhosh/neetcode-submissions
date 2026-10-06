class MinStack:
    def __init__(self):
        self.stack = []
        self.minNum = []

    def push(self, val: int) -> None:
        if not self.minNum or self.minNum[-1] > val:
            self.minNum.append(val)
        else:
            self.minNum.append(self.minNum[-1])
        self.stack.append(val)

    def pop(self) -> None:

        self.stack.pop()
        self.minNum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minNum[-1]
