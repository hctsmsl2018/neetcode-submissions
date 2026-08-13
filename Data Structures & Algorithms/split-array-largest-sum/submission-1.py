from bisect import bisect_left

class Solution:
    def _get_num_parts(self, split_size):
        curr_splits = 0
        curr_split_size = 0

        for i in self._nums:
            if curr_split_size + i > split_size:
                curr_splits += 1
                curr_split_size = i
            else:
                curr_split_size += i
 
        return -curr_splits - int(bool(curr_split_size != 0))

    def splitArray(self, nums: List[int], k: int) -> int:
        self._nums = nums

        nums_sum = 0
        nums_max = 0

        for i in nums:
            nums_sum += i
            nums_max = max(nums_max, i)

        return bisect_left(range(nums_max, nums_sum + 1), -k, key=self._get_num_parts) + nums_max