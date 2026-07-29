class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max_prod = nums[0]

        curr_min_prod = nums[0]
        curr_max_prod = nums[0]

        for i in islice(nums, 1, len(nums)):
            min_prod_cont = curr_min_prod * i
            max_prod_cont = curr_max_prod * i

            curr_min_prod = min(min_prod_cont, max_prod_cont, i)
            curr_max_prod = max(min_prod_cont, max_prod_cont, i)

            global_max_prod = max(global_max_prod, curr_max_prod)

        return global_max_prod