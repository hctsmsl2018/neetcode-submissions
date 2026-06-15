from heapq import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [(-n, i) for i, n in enumerate(islice(nums, k))]

        heapify(heap)

        maximums = [-heap[0][0]]

        for i in range(k, len(nums)):
            heappush(heap, (-nums[i], i))

            lower_bound = i + 1 - k

            while heap[0][1] < lower_bound:
                heappop(heap)

            maximums.append(-heap[0][0])

        return maximums