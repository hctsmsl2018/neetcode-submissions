class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                leads_to = []

                if j:
                    leads_to.append(grid[i][j - 1])

                if i:
                    leads_to.append(grid[i - 1][j])

                grid[i][j] += min(leads_to, default=0)

        return grid[-1][-1]