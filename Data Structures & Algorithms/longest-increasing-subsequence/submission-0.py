class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis_from_back = [0] * len(nums)
        lis_from_back[-1] = 1

        for i in range(len(nums) - 2, -1, -1):
            lis_from_back[i] = 1 + max((lis_from_back[j] for j in range(i + 1, len(nums)) if nums[j] > nums[i]), default=0)

        return max(lis_from_back)