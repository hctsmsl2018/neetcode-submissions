class Solution:
    def combination_sum_from_index(self, index, target):
        if target == 0:
            self.combinations.append(self.curr_combinations.copy())
        elif index < len(self.candidates):
            next_index = index + 1

            cases_range = range(0, target + 1, self.candidates[index])

            for i in cases_range:
                self.combination_sum_from_index(next_index, target - i)

                self.curr_combinations.append(self.candidates[index])

            del self.curr_combinations[-len(cases_range):]

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combinations = []

        self.curr_combinations = []
        self.candidates = candidates

        self.combination_sum_from_index(0, target)

        return self.combinations