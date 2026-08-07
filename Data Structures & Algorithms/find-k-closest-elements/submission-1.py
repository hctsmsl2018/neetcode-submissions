from bisect import bisect_right

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        lower_bound = bisect_right(arr, x)
        upper_bound = lower_bound

        if lower_bound == 0:
            return arr[:k]
        elif upper_bound == len(arr):
            return arr[-k:]

        direction_available = 0
        number_available = 0

        for i in range(k):
            d_lower = x - arr[lower_bound - 1]
            d_upper = arr[upper_bound] - x

            if d_lower > d_upper:
                upper_bound += 1

                if upper_bound == len(arr):
                    direction_available = -1
                    number_available = k - i - 1
                    break
            else:
                lower_bound -= 1

                if lower_bound == 0:
                    direction_available = 1
                    number_available = k - i - 1
                    break

        if direction_available == 1:
            upper_bound += number_available
        elif direction_available == -1:
            lower_bound -= number_available

        return arr[lower_bound: upper_bound]