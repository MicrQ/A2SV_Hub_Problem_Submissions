# Problem: Min Stack - https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.current_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.current_min:
            self.current_min.append(
                min(self.current_min[-1], val)
            )
        else:
            self.current_min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.current_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.current_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()