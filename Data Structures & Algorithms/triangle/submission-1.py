class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev_path_sums = [] # 15, 11, 18, 14

        for layer in triangle: # 3
            curr_path_sums = [] # 15, 11, 18, 14

            for i, n in enumerate(layer):
                candidate_sums = []

                prev = i - 1

                if 0 <= prev < len(prev_path_sums):
                    candidate_sums.append(prev_path_sums[prev])

                if 0 <= i < len(prev_path_sums):
                    candidate_sums.append(prev_path_sums[i])

                curr_path_sums.append(min(candidate_sums, default=0) + n)

            prev_path_sums = curr_path_sums

        return min(prev_path_sums)