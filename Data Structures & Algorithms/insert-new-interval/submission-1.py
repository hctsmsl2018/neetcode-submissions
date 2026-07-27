class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        after_insertion = []

        replacement_interval_start = None
        replacement_interval_end = None
        replacement_interval_passed = False

        for s, e in intervals:
            if e < newInterval[0]:
                after_insertion.append([s, e])
            elif s > newInterval[1]:
                if not replacement_interval_passed:
                    if replacement_interval_start is not None:
                        after_insertion.append([replacement_interval_start, replacement_interval_end])
                    else:
                        after_insertion.append(newInterval)

                    replacement_interval_passed = True

                after_insertion.append([s, e])
            else:
                if replacement_interval_start is None:
                    replacement_interval_start = min(s, newInterval[0])

                replacement_interval_end = max(e, newInterval[1])

        if not replacement_interval_passed:
            if replacement_interval_start is not None:
                after_insertion.append([replacement_interval_start, replacement_interval_end])
            else:
                after_insertion.append(newInterval)

        return after_insertion