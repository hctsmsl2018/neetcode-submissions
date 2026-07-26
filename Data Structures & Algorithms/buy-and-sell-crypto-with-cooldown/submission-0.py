class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profits = [-prices[0], 0, 0] # [1, 1, 3]

        for i in islice(prices, 1, len(prices)):
            max_profits = [
                max(max_profits[0], max_profits[1] - i),
                max_profits[2],
                max(max_profits[2], max_profits[0] + i)
            ]
        
        return max_profits[2]