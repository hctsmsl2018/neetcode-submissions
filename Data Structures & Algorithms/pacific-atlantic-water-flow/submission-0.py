'''PACIFIC = 0
ATLANTIC = -1
BOTH = -2'''

OFFSETS = ((-1, 0), (1, 0), (0, -1), (0, 1))

class Solution:
    def find_reachable_cells(self, queue):
        drainage_basin = set(queue)

        while len(queue) != 0:
            i, j = queue.pop()

            for i_offset, j_offset in OFFSETS:
                i_new, j_new = i + i_offset, j + j_offset

                if 0 <= i_new < len(self.heights) and 0 <= j_new < len(self.heights[0]) and (i_new, j_new) not in drainage_basin and self.heights[i][j] <= self.heights[i_new][j_new]:
                    queue.append((i_new, j_new))
                    drainage_basin.add((i_new, j_new))

        return drainage_basin

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights

        max_row_ind = len(heights) - 1
        max_col_ind = len(heights[0]) - 1

        pacific_queue = [(0, 0), (0, max_col_ind), (max_row_ind, 0)]
        atlantic_queue = [(max_row_ind, max_col_ind), (0, max_col_ind), (max_row_ind, 0)]

        for i in range(1, max_row_ind):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, max_col_ind))

        for i in range(1, max_col_ind):
            pacific_queue.append((0, i))
            atlantic_queue.append((max_row_ind, i))

        pacific_drainage_basin = self.find_reachable_cells(pacific_queue)
        atlantic_drainage_basin = self.find_reachable_cells(atlantic_queue)

        return [list(cell) for cell in pacific_drainage_basin & atlantic_drainage_basin]
        '''max_row_ind = len(heights) - 1
        max_col_ind = len(heights[0]) - 1

        both_oceans = 2

        heights[0][0] = PACIFIC
        heights[max_row_ind][max_col_ind] = ATLANTIC
        heights[0][max_col_ind] = BOTH
        heights[max_row_ind][0] = BOTH

        queue = deque(((0, 0), (max_row_ind, max_col_ind)))

        for i in range(1, max_row_ind):
            heights[i][0] = PACIFIC
            heights[i][max_col_ind] = PACIFIC

            queue.extend(((i, 0), (i, max_col_ind)))

        for i in range(1, max_col_ind):
            heights[0][i] = ATLANTIC
            heights[max_row_ind][i] = ATLANTIC

            queue.extend(((0, i), (max_row_ind, i)))

        while not queue.empty():'''