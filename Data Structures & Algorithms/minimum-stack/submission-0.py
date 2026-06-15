class MinStack:

    def __init__(self):
        self.all_elements = []
        self.min_at_addition = []

    def push(self, value: int) -> None:
        self.all_elements.append(value)

        if len(self.min_at_addition) == 0 or value < self.min_at_addition[-1][0]:
            self.min_at_addition.append((value, len(self.all_elements) - 1))

    def pop(self) -> None:
        last_val = self.all_elements.pop()

        if self.min_at_addition[-1][1] == len(self.all_elements):
            self.min_at_addition.pop()

    def top(self) -> int:
        return self.all_elements[-1]

    def getMin(self) -> int:
        return self.min_at_addition[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()