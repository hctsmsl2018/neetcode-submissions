class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        appropriate_triplet_found = [False, False, False] # t, t, t

        for t in triplets:
            curr_triplet_appropriateness = [] # f, t, t

            for curr_val, target_val in zip(t, target):
                if curr_val > target_val:
                    break

                curr_triplet_appropriateness.append(curr_val == target_val)
            else:
                for i, appropriate in enumerate(curr_triplet_appropriateness):
                    appropriate_triplet_found[i] = appropriate_triplet_found[i] or appropriate

        return all(appropriate_triplet_found)