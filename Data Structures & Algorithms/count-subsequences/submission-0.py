class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[0] = 1
        for c in s:
            # iterate backwards to use previous row values
            for j in range(len(t), 0, -1):
                if j != 0 and c == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[len(t)]