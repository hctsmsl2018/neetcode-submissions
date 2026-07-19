from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = [-i for i in nums]
        heapify(queue)

        minimum = 0

        for _ in range(k):
            minimum = heappop(queue)

        return -minimum