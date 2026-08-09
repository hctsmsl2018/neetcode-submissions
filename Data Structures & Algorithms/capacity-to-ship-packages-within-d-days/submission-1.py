from bisect import bisect_left

class Solution:
    def _find_days_for_capacity(self, capacity):
        tot_days = 0
        curr_ship_weight = 0

        for i in self._weights:
            if curr_ship_weight + i > capacity:
                tot_days += 1
                curr_ship_weight = i
            else:
                curr_ship_weight += i

        return -tot_days - int(bool(curr_ship_weight))

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self._weights = weights

        weights_sum = 0
        weights_max = 0

        for i in weights:
            weights_sum += i
            weights_max = max(i, weights_max)

        return bisect_left(range(weights_max, weights_sum + 1), -days, key=self._find_days_for_capacity) + weights_max