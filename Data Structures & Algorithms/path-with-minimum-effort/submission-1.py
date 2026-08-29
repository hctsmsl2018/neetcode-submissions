from heapq import heappush, heappop
'''
0 1 1
2 -1 1
2 2 -1
'''

OFFSETS = ((-1, 0), (1, 0), (0, -1), (0, 1))

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        min_effort_queue = [(0, 0, 0)] # (2, 2, 2), (3, 2, 2), (5, 1, 1), (5, 1, 1), (6, 1, 1), (6, 1, 1)
        efforts = [[-1] * len(heights[0]) for _ in range(len(heights))]
        max_i = len(heights) - 1
        max_j = len(heights[0]) - 1
        
        while len(min_effort_queue) > 0:
            effort, i, j = heappop(min_effort_queue)
            
            if i == max_i and j == max_j:
                return effort
            elif efforts[i][j] == -1:
                efforts[i][j] = effort

                for i_offset, j_offset in OFFSETS:
                    i_offsetted = i + i_offset
                    j_offsetted = j + j_offset

                    if 0 <= i_offsetted < len(heights) and 0 <= j_offsetted < len(heights[0]) and efforts[i_offsetted][j_offsetted] == -1:
                        heappush(min_effort_queue, (max(effort, abs(heights[i][j] - heights[i_offsetted][j_offsetted])), i_offsetted, j_offsetted))