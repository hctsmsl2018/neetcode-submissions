class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if total < target or (total - target) % 2:
            return 0

        sub_target = (total - target) // 2
        dp = [0] * (sub_target + 1)
        dp[0] = 1

        for num in nums:

            for i in range(sub_target, num - 1, -1):
                if dp[i - num] != 0:
                    dp[i] += dp[i - num]

        return dp[sub_target]