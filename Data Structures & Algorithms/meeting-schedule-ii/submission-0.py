"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import *

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda r: r.start)

        rooms = []

        for interval in intervals:
            if len(rooms) > 0 and rooms[0] <= interval.start:
                heappop(rooms)

            heappush(rooms, interval.end)

        return len(rooms)