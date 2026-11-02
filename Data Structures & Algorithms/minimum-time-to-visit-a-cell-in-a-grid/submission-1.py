from heapq import heappush, heappop
from math import inf

NEIGHBORS = ((-1, 0), (1, 0), (0, -1), (0, 1))

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        odd_coors_queue = []
        even_coors_queue = [(0, 0, 0)]
        curr_time = 0
        grid[0][0] = -1

        while True:
            if curr_time == 1 and odd_coors_queue[0][0] > 1:
                return -1
                
            if (len(odd_coors_queue) == 0 or odd_coors_queue[0][0] > curr_time) and (len(even_coors_queue) == 0 or even_coors_queue[0][0] > curr_time):
                curr_time = min(odd_coors_queue[0][0] if len(odd_coors_queue) > 0 else inf, even_coors_queue[0][0] if len(even_coors_queue) > 0 else inf)

            if curr_time % 2 == 0:
                pop_queue = even_coors_queue
                push_queue = odd_coors_queue
            else:
                pop_queue = odd_coors_queue
                push_queue = even_coors_queue

            while len(pop_queue) > 0 and pop_queue[0][0] <= curr_time:
                _, i, j = heappop(pop_queue)

                if i == max_row and j == max_col:
                    return curr_time

                for i_off, j_off in NEIGHBORS:
                    i_shifted = i + i_off
                    j_shifted = j + j_off

                    if 0 <= i_shifted < len(grid) and 0 <= j_shifted < len(grid[0]) and grid[i_shifted][j_shifted] > -1:
                        heappush(push_queue, (grid[i_shifted][j_shifted], i_shifted, j_shifted))
                        grid[i_shifted][j_shifted] = -1

            curr_time += 1