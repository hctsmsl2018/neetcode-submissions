class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        third_len = len(nums) // 3
        count1 = 0 # 3
        count2 = 0
        candidate1 = None # 3
        candidate2 = None

        for i in nums:
            if i == candidate1:
                count1 += 1
            elif i == candidate2:
                count2 += 1
            elif count1 == 0:
                count1 = 1
                candidate1 = i
            elif count2 == 0:
                count2 = 1
                candidate2 = i
            else:
                count1 -= 1
                count2 -= 1
                
        over_third_elements = []

        if sum(int(candidate1 == i) for i in nums) > third_len:
            over_third_elements.append(candidate1)
        
        if (len(over_third_elements) == 0 or over_third_elements[0] != candidate2) and sum(int(candidate2 == i) for i in nums) > third_len:
            over_third_elements.append(candidate2)

        return over_third_elements