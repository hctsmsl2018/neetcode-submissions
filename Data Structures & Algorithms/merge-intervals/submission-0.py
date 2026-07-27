class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        merged_intervals = []

        curr_interval_start = intervals[0][0]
        curr_interval_end = intervals[0][1]

        for s, e in islice(intervals, 1, len(intervals)):
            if curr_interval_end < s:
                merged_intervals.append([curr_interval_start, curr_interval_end])

                curr_interval_start = s
                curr_interval_end = e
            else:
                curr_interval_end = max(curr_interval_end, e)

        merged_intervals.append([curr_interval_start, curr_interval_end])

        return merged_intervals