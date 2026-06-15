class Solution:
    def get_next_highest_left(self, curr_left):
        next_highest_left = curr_left + 1

        while next_highest_left < len(self.height):
            if self.height[next_highest_left] > self.height[curr_left]:
                return next_highest_left

            next_highest_left += 1

        return None

    def get_next_highest_right(self, curr_right):
        next_highest_right = curr_right - 1

        while next_highest_right >= 0:
            if self.height[next_highest_right] > self.height[curr_right]:
                return next_highest_right

            next_highest_right -= 1

        return None

    def maxArea(self, height: List[int]) -> int:
        self.height = height

        left = 0
        right = len(height) - 1

        next_highest_left = self.get_next_highest_left(left)
        next_highest_right = self.get_next_highest_right(right)

        volumes_to_consider = [(right - left) * min(height[left], height[right])]

        while next_highest_left is not None or next_highest_right is not None:
            if next_highest_left is None or next_highest_right is not None and height[left] > height[right]:
                right = next_highest_right
                next_highest_right = self.get_next_highest_right(right)
            else:
                left = next_highest_left
                next_highest_left = self.get_next_highest_left(left)

            volumes_to_consider.append((right - left) * min(height[left], height[right]))

        return max(volumes_to_consider)