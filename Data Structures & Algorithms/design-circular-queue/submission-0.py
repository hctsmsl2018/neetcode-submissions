class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.k = k
        self.start = 0
        self.end = 0
        self.length = 0

    def enQueue(self, value: int) -> bool:
        if self.length == self.k:
            return False
        else:
            self.queue[self.end] = value
            self.end = (self.end + 1) % self.k
            self.length += 1

            return True

    def deQueue(self) -> bool:
        if self.length == 0:
            return False
        else:
            self.start = (self.start + 1) % self.k
            self.length -= 1

            return True
        
    def Front(self) -> int:
        return -1 if self.length == 0 else self.queue[self.start]

    def Rear(self) -> int:
        return -1 if self.length == 0 else self.queue[(self.end - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()