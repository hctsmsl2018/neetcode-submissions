from heapq import heappop, heappush
from math import inf

NEIGHBORS = ((-1, 0), (1, 0), (0, -1), (0, 1))

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        time = 0
        next_squares_queue = [(grid[0][0], 0, 0)]

        final_row_ind = len(grid) - 1
        final_col_ind = len(grid[0]) - 1

        while True:
            height, i, j = heappop(next_squares_queue)

            grid[i][j] = inf

            if height > time:
                time = height

            if i == final_row_ind and j == final_col_ind:
                return time

            for i_offset, j_offset in NEIGHBORS:
                i_offsetted = i + i_offset
                j_offsetted = j + j_offset

                if 0 <= i_offsetted < len(grid) and 0 <= j_offsetted < len(grid[0]) and grid[i_offsetted][j_offsetted] != inf:
                    heappush(next_squares_queue, (grid[i_offsetted][j_offsetted], i_offsetted, j_offsetted))