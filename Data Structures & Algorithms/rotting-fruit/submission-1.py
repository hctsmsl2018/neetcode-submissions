OFFSETS = ((-1, 0), (1, 0), (0, -1), (0, 1))

'''
222
220
022
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        frontier = deque() # (2, 2, 4)
        total_oranges = 0 # 7
        rotten_oranges = 0 # 7

        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n == 2:
                    rotten_oranges += 1
                    frontier.append((i, j, 0))

                if n != 0:
                    total_oranges += 1

        last_minute = 0

        while len(frontier) > 0:
            i, j, minute = frontier.popleft() # 2, 2, 4

            last_minute = minute
            next_minute = minute + 1 # 4

            for i_offset, j_offset in OFFSETS:
                i_offsetted = i + i_offset
                j_offsetted = j + j_offset

                if 0 <= i_offsetted < len(grid) and 0 <= j_offsetted < len(grid[0]) and grid[i_offsetted][j_offsetted] == 1:
                    rotten_oranges += 1
                    grid[i_offsetted][j_offsetted] = 2
                    frontier.append((i_offsetted, j_offsetted, next_minute))

        return last_minute if total_oranges == rotten_oranges else -1