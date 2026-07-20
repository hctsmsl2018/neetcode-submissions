class Solution:
    def _combinations_from_counter_index(self, start_ind, target):
        if target == 0:
            self._all_combinations.append(self._curr_combination.copy())
        elif start_ind < len(self._counter_list):
            val, count = self._counter_list[start_ind]

            next_ind = start_ind + 1

            self._combinations_from_counter_index(next_ind, target)

            for _ in range(count):
                target -= val

                if target < 0:
                    break

                self._curr_combination.append(val)
                self._combinations_from_counter_index(next_ind, target)

            while len(self._curr_combination) > 0 and self._curr_combination[-1] == val:
                self._curr_combination.pop()
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self._counter_list = list(Counter(candidates).items())
        self._curr_combination = []
        self._all_combinations = []

        self._combinations_from_counter_index(0, target)

        return self._all_combinations