class Solution:
    # index=1
    def _get_subsets_until_counter(self, index):
        if index == -1:
            return [[]]

        subsets = self._get_subsets_until_counter(index - 1) # [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]

        n, count = self._counter[index] # n=2, count=2

        curr_items_to_append = [] # [2, 2]

        num_prev_subsets = len(subsets)

        for _ in range(count): # 2
            curr_items_to_append.append(n)

            for subset in islice(subsets, num_prev_subsets): # 2
                curr_element = subset.copy() # 
                curr_element.extend(curr_items_to_append)
                subsets.append(curr_element)

        return subsets
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self._counter = list(Counter(nums).items()) # [(1, 1), (2, 2)]

        return self._get_subsets_until_counter(len(self._counter) - 1)