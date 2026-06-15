class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods_except_self = [1]

        prefix_prod = 1

        for i in range(1, len(nums)):
            prefix_prod *= nums[i - 1]
            prods_except_self.append(prefix_prod)

        suffix_prod = 1

        for i in range(len(nums) - 2, -1, -1):
            suffix_prod *= nums[i + 1]
            prods_except_self[i] *= suffix_prod
        
        return prods_except_self