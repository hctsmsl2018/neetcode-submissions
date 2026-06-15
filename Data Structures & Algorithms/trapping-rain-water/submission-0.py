class Solution:
    def trap(self, height: List[int]) -> int:
        max_height = max(height)

        tot_volume = 0

        curr_ind = 0
        water_height = height[0]

        while height[curr_ind] < max_height:
            if height[curr_ind] > water_height:
                water_height = height[curr_ind]
            else:
                tot_volume += water_height - height[curr_ind]

            curr_ind += 1

        stop_ind = curr_ind

        curr_ind = len(height) - 1
        water_height = height[-1]

        while curr_ind > stop_ind:
            if height[curr_ind] > water_height:
                water_height = height[curr_ind]
            else:
                tot_volume += water_height - height[curr_ind]

            curr_ind -= 1

        return tot_volume