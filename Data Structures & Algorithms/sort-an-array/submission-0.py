class Solution:
    def merge_sort_segment(self, start, end):
        if start == end:
            return [self.nums[start]]

        # 0, 5: 2
        # 0, 2: 1
        mid = (start + end) // 2 

        left_sorted = self.merge_sort_segment(start, mid) # [1, 5]
        right_sorted = self.merge_sort_segment(mid + 1, end) # [1]

        left_counter = 0
        right_counter = 0

        merged = [] # 1, 1, 5

        while left_counter < len(left_sorted) or right_counter < len(right_sorted):
            if left_counter == len(left_sorted) or right_counter != len(right_sorted) and right_sorted[right_counter] < left_sorted[left_counter]:
                merged.append(right_sorted[right_counter])
                right_counter += 1
            else:
                merged.append(left_sorted[left_counter])
                left_counter += 1
        
        return merged

    def sortArray(self, nums: List[int]) -> List[int]:
        self.nums = nums

        return self.merge_sort_segment(0, len(nums) - 1)