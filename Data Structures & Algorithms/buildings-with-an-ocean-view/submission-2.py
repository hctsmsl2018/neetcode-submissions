class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = 0 # 4
        ocean_view_indices = [] # 4, 3, 2, 0

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                max_height = heights[i]
                ocean_view_indices.append(i)

        return ocean_view_indices[::-1]