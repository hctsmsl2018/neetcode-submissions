from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            if len(self.min_heap) == 0 or self.min_heap[0] <= num:
                heappush(self.min_heap, num)
            else:
                heappush(self.max_heap, -num)
        elif len(self.min_heap) > len(self.max_heap):
            if self.min_heap[0] >= num:
                heappush(self.max_heap, -num)
            else:
                heappush(self.max_heap, -heappop(self.min_heap))
                heappush(self.min_heap, num)
        else:
            if -self.max_heap[0] <= num:
                heappush(self.min_heap, num)
            else:
                heappush(self.min_heap, -heappop(self.max_heap))
                heappush(self.max_heap, -num)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return -self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()