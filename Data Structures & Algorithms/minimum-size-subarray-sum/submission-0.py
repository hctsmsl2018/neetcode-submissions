class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        right = 0 # 6
        window_len = 0 # 3
        window_sum = 0 # 9
        min_window_len = len(nums) # 3
        subarray_possible = False

        for left in range(len(nums)): # 3
            if left != 0:
                window_len -= 1
                window_sum -= nums[left - 1]

            if right == len(nums) and window_sum < target:
                break

            while right < len(nums) and window_sum < target:
                window_len += 1
                window_sum += nums[right]
                right += 1

            if window_sum >= target:
                subarray_possible = True
                min_window_len = min(min_window_len, window_len)

        if not subarray_possible:
            return 0
        else:
            return min_window_len