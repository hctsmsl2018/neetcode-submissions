from math import ceil
from bisect import bisect_left

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        search_range = range(1, sum(piles) + 1)

        def _time_to_eat_bananas(speed):
            return -sum(ceil(i / speed) for i in piles)

        return bisect_left(search_range, -h, key=_time_to_eat_bananas) + 1