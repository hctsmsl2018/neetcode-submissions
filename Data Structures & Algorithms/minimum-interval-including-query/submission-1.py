from heapq import heappush, heappop

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals_sorted = sorted((start, end) for start, end in intervals)
        queries_sorted = sorted((q, i) for i, q in enumerate(queries))
        solutions = [-1] * len(queries)

        curr_interval = 0
        intervals_queue = []

        for q, i in queries_sorted:
            while curr_interval < len(intervals) and intervals_sorted[curr_interval][0] <= q:
                start, end = intervals_sorted[curr_interval]
                interval_info = (end - start + 1, start, end)

                if start <= q <= end:
                    heappush(intervals_queue, interval_info)

                curr_interval += 1

            while len(intervals_queue) > 0 and (q < intervals_queue[0][1] or q > intervals_queue[0][2]):
                heappop(intervals_queue)

            if len(intervals_queue) > 0:
                solutions[i] = intervals_queue[0][0]

        return solutions