class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prev_end = intervals[0][1]
        removals = 0

        for s, e in islice(intervals, 1, len(intervals)):
            if s >= prev_end:
                prev_end = e
            else:
                removals += 1
                prev_end = min(e, prev_end)

        return removals