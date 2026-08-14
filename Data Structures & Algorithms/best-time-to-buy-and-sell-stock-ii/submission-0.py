class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0] # 4
        total_profit = 0 # 7

        for i in range(1, len(prices)):
            prev = prices[i - 1]
            curr = prices[i]

            if prev > curr:
                total_profit += prev - start
                start = curr

        total_profit += prices[-1] - start

        return total_profit