class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j == 0:
                        obstacleGrid[0][0] = -1
                    else:
                        left = i - 1

                        if i != 0 and obstacleGrid[left][j] != 1:
                            obstacleGrid[i][j] += obstacleGrid[left][j]

                        right = j - 1

                        if j != 0 and obstacleGrid[i][right] != 1:
                            obstacleGrid[i][j] += obstacleGrid[i][right]
        
        return -obstacleGrid[-1][-1] if obstacleGrid[-1][-1] != 1 else 0