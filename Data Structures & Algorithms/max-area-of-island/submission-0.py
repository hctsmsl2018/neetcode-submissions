ADJACENT_OFFSETS = ((-1, 0), (1, 0), (0, -1), (0, 1))

class Solution:
    def _find_island_area(self, i, j):
        tot_island_area = 1

        self._grid[i][j] = 0

        for i_diff, j_diff in ADJACENT_OFFSETS:
            i_offset = i + i_diff
            j_offset = j + j_diff

            if 0 <= i_offset < len(self._grid) and 0 <= j_offset < len(self._grid[0]) and self._grid[i_offset][j_offset] == 1:
                tot_island_area += self._find_island_area(i_offset, j_offset)

        return tot_island_area
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self._grid = grid
        max_island_area = 0

        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n == 1:
                    curr_island_area = self._find_island_area(i, j)
                    max_island_area = max(curr_island_area, max_island_area)

        return max_island_area