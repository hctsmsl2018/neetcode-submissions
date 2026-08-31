class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False

        running_sum = 0
        seen_mods = set()
        next_mod = 0

        for i in nums:
            running_sum += i
            curr_mod = running_sum % k

            if curr_mod in seen_mods:
                return True
            else:
                seen_mods.add(next_mod)
                next_mod = curr_mod

        return False