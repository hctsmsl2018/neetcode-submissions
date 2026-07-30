from bisect import bisect_left

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def _check_mountain_position_type(self, i):
        curr_ind = self._mountain.get(i)
        return int(self._mountain.get(i - 1) > curr_ind) + int(curr_ind > self._mountain.get(i + 1))

    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        self._mountain = mountainArr

        mid = bisect_left(range(1, mountainArr.length() - 1), 1, key=self._check_mountain_position_type) + 1

        left_range_ind = bisect_left(range(mid + 1), target, key=mountainArr.get)
            
        if mountainArr.get(left_range_ind) == target:
            return left_range_ind

        right_range_ind = bisect_left(range(mid, mountainArr.length()), -target, key=lambda x: -mountainArr.get(x)) + mid

        if right_range_ind < mountainArr.length() and mountainArr.get(right_range_ind) == target:
            return right_range_ind

        return -1