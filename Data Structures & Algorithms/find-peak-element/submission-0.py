class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0

        if nums[-1] > nums[-2]:
            return len(nums) - 1

        low = 0 # 4
        high = len(nums) - 1 # 6

        while low < high:
            mid = (low + high) // 2 # 5

            prev_num = nums[mid - 1]
            curr_num = nums[mid]
            next_num = nums[mid + 1]

            if prev_num > curr_num:
                high = mid
            elif prev_num < curr_num < next_num:
                low = mid
            else:
                return mid