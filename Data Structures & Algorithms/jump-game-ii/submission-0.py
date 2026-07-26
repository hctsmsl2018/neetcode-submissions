class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        prev_jumpable_ind = 0
        prev_num_jumps = 0
        curr_jumpable_ind = nums[0]
        curr_num_jumps = 1

        final_ind = len(nums) - 1

        for i, n in enumerate(nums):
            if i > prev_jumpable_ind:
                prev_jumpable_ind = curr_jumpable_ind
                prev_num_jumps = curr_num_jumps
                curr_jumpable_ind = 0
                curr_num_jumps += 1

            max_jumpable_ind = i + n

            if max_jumpable_ind >= final_ind:
                return curr_num_jumps

            if max_jumpable_ind > curr_jumpable_ind:
                curr_jumpable_ind = max_jumpable_ind