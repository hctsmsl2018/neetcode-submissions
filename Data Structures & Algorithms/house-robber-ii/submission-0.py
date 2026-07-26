class Solution:
    def find_max_money(self, interval):
        prev = next(interval)
        curr = max(prev, next(interval))

        for i in interval:
            prev, curr = curr, max(prev + i, curr)

        return curr

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
            
        exclude_first = islice(nums, 1, len(nums))
        exclude_last = islice(nums, len(nums) - 1)

        return max(self.find_max_money(exclude_first), self.find_max_money(exclude_last))