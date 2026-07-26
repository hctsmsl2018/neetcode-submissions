class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        nums[1] = max(nums[:2])

        for i in range(2, len(nums)):
            nums[i] = max((nums[i - 1], nums[i - 2] + nums[i]))

        return nums[-1]