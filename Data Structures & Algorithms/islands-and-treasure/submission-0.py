INF = 2 ** 31 - 1
ADJ_OFFSETS = ((-1, 0), (1, 0), (0, -1), (0, 1))

'''
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
'''

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque() # (0, 0, 3), (3, 3, 4)
        
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n == 0:
                    queue.append((i, j, 0))

        while len(queue) > 0:
            i, j, dist = queue.popleft() # 

            next_dist = dist + 1

            for i_offset, j_offset in ADJ_OFFSETS:
                i_offsetted = i + i_offset
                j_offsetted = j + j_offset

                if 0 <= i_offsetted < len(grid) and 0 <= j_offsetted < len(grid[0]) and grid[i_offsetted][j_offsetted] == INF:
                    grid[i_offsetted][j_offsetted] = next_dist
                    queue.append((i_offsetted, j_offsetted, next_dist))