from heapq import heappop, heappush

NEIGHBORS = ((-1, 0), (1, 0), (0, -1), (0, 1))

class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        answer = [None] * len(queries)
        smallest_neighbors = [(grid[0][0], 0, 0)]
        coors_in_queue = {(0, 0)}
        num_points = 0

        for q, ind in sorted((q, i) for i, q in enumerate(queries)):
            while len(smallest_neighbors) > 0 and smallest_neighbors[0][0] < q:
                _, i, j = heappop(smallest_neighbors)
                coors_in_queue.remove((i, j))
                grid[i][j] = 0
                num_points += 1

                for i_off, j_off in NEIGHBORS:
                    i_shift = i + i_off
                    j_shift = j + j_off

                    if 0 <= i_shift < len(grid) and 0 <= j_shift < len(grid[0]) and grid[i_shift][j_shift] != 0 and (i_shift, j_shift) not in coors_in_queue:
                        heappush(smallest_neighbors, (grid[i_shift][j_shift], i_shift, j_shift))
                        coors_in_queue.add((i_shift, j_shift))

            answer[ind] = num_points

        return answer