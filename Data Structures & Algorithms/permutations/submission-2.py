class Solution:
    # 2
    def _permute_until_index(self, index):
        if index == 0:
            return [[self._nums[0]]]

        prev_permutations = self._permute_until_index(index - 1) # [[2, 1], [1, 2]]

        permutations_to_index = [] # [[3, 2, 1], [2, 3, 1], [2, 1, 3]]

        num_at_index = self._nums[index] # 3

        for permutation in prev_permutations: # 2 iter, [2, 1]
            for i in range(len(permutation)): # 2 iter
                curr_permutation = [] # 

                for j, n in enumerate(permutation): # 2 iter
                    if i == j:
                        curr_permutation.append(num_at_index)

                    curr_permutation.append(n)

                permutations_to_index.append(curr_permutation)

            permutation.append(num_at_index)
            permutations_to_index.append(permutation)

        return permutations_to_index

    def permute(self, nums: List[int]) -> List[List[int]]:
        self._nums = nums

        return self._permute_until_index(len(nums) - 1) # 2