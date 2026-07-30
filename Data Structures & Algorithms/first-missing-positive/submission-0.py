class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        placeholder = len(nums) + 1

        for i, n in enumerate(nums):
            if n <= 0:
                nums[i] = placeholder

        for i, n in enumerate(nums):
            ind_to_change = abs(n) - 1

            if 0 <= ind_to_change < len(nums) and nums[ind_to_change] > 0:
                nums[ind_to_change] *= -1

        max_present = 0

        for n in nums:
            if n < 0:
                max_present += 1
            else:
                break

        return max_present + 1