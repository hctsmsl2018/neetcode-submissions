class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end_0 = 0 # 1
        end_1 = 0 # 3
        # 0,0,1,1,2,2
        for i, n in enumerate(nums): # 5
            match (n):
                case 0:
                    nums[end_0] = 0
                    
                    if end_0 != end_1:
                        nums[end_1] = 1
                    
                    if end_1 != i:
                        nums[i] = 2

                    end_0 += 1
                    end_1 += 1
                case 1:
                    nums[end_1] = 1

                    if end_1 != i:
                        nums[i] = 2

                    end_1 += 1
