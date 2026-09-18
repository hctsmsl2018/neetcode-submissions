class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        prev_stones = {stones[0]} # 8, 6, 10, 0, 2, 18, 4, 12, 14, 20, 22

        for i in islice(stones, 1, len(stones)):
            curr_stones = set() # 7, 9, 5, 11, 1, 3, 17, 19, 13, 15, 21, 23

            for j in prev_stones:
                curr_stones |= {abs(i - j), abs(i + j)}

            prev_stones = curr_stones

        return min(prev_stones)