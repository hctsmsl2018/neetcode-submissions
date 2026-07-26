class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable_index = 0

        last_index = len(nums) - 1

        for i, n in enumerate(nums):
            max_reachable_index = max(max_reachable_index, i + n)

            if i >= last_index:
                return True
            elif i == max_reachable_index:
                return False