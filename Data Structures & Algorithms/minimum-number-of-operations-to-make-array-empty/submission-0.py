class Solution:
    def minOperations(self, nums: List[int]) -> int:
        tot_operations = 0

        for i in Counter(nums).values():
            if i == 1:
                return -1
            else:
                tot_operations += (i - 1) // 3 + 1

        return tot_operations