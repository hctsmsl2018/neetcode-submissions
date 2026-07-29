class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)

        if nums_sum % 2 != 0:
            return False

        target_sum = nums_sum // 2

        array_width = len(nums) + 1
        array_height = target_sum + 1

        prev_sum_partitionable = [[False] * array_width for _ in range(array_height)]

        for i in range(array_width):
            prev_sum_partitionable[0][i] = True

        for i in range(1, array_height):
            for j in range(1, array_width):
                left_ind = j - 1

                sum_achievable = prev_sum_partitionable[i][left_ind]

                prev_sum_ind = i - nums[j - 1]

                if prev_sum_ind >= 0:
                    sum_achievable = sum_achievable or prev_sum_partitionable[prev_sum_ind][left_ind]

                prev_sum_partitionable[i][j] = sum_achievable

        return prev_sum_partitionable[-1][-1]