class Solution:
    def _get_permutations_from_ind(self, i):
        if i == self._nums_len:
            self._all_permutations.append(self._curr_permutation.copy())
            return

        next_i = i + 1

        for n, count in self._nums_counter.items():
            if count == 0:
                continue

            self._curr_permutation.append(n)
            self._nums_counter[n] -= 1

            self._get_permutations_from_ind(next_i)

            self._curr_permutation.pop()
            self._nums_counter[n] += 1

    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        self._nums_len = len(nums) # 3
        self._nums_counter = Counter(nums) # {1: 1}
        self._curr_permutation = [] # 2, 1, 1
        self._all_permutations = [] # (1, 1, 2), (1, 2, 1), (2, 1, 1)

        self._get_permutations_from_ind(0)

        return self._all_permutations