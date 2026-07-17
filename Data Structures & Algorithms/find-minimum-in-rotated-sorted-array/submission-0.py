class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_length = len(nums)
        if nums_length == 1:
            return nums[0]
        lower_bound = 0
        upper_bound = nums_length - 1
        while lower_bound + 1 != upper_bound:
            middle = (lower_bound + upper_bound) // 2
            if nums[middle] > nums[upper_bound]: # 15, 17; 11, 15
                lower_bound = middle
            else:
                upper_bound = middle

        return min(nums[lower_bound], nums[upper_bound])