class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums_sum = [nums[0]]

        for i in islice(nums, 1, None):
            nums_sum.append(nums_sum[-1] + i)

        min_prefix = min((nums[0], 0))
        subarray_sum = nums[0]

        for i in islice(nums_sum, 1, None):
            diff = i - min_prefix
            
            if subarray_sum < diff:
                subarray_sum = diff

            if i < min_prefix:
                min_prefix = i

        return subarray_sum