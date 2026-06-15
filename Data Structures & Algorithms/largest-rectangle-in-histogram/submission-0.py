class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        monotonic_stack = []

        for i, h in enumerate(heights):
            if len(monotonic_stack) == 0 or h >= monotonic_stack[-1][0]:
                monotonic_stack.append((h, i))
            else:
                while len(monotonic_stack) != 0 and h < monotonic_stack[-1][0]:
                    prev_h, prev_i = monotonic_stack.pop()
                    max_area = max(max_area, prev_h * (i - prev_i))

                monotonic_stack.append((h, prev_i))

        while len(monotonic_stack) != 0:
            prev_h, prev_i = monotonic_stack.pop()
            max_area = max(max_area, prev_h * (len(heights) - prev_i))

        return max_area


