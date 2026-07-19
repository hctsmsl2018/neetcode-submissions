class Solution:
    def _find_subsets_from_index(self, index):
        if index == -1:
            return [[]]

        prev_index_subsets = self._find_subsets_from_index(index - 1)

        for i in range(len(prev_index_subsets)):
            prev_index_subsets.append([*prev_index_subsets[i], self._nums[index]])

        return prev_index_subsets

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self._nums = nums

        return self._find_subsets_from_index(len(nums) - 1)