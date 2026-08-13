class Solution:
    def _at_most_k_ints(self, k):
        counter = Counter()

        total = 0
        right = 0
        prev_right = None

        for left in range(len(self._nums)):
            if left != 0:
                prev_element = self._nums[left - 1]

                counter[prev_element] -= 1

                if counter[prev_element] == 0:
                    del counter[prev_element]
                else:
                    continue

            while right < len(self._nums) and (len(counter) < k or self._nums[right] in counter):
                counter[self._nums[right]] += 1
                right += 1

            if len(counter) == k:
                segment_len = right - left
                total += segment_len * (segment_len + 1) // 2

                if prev_right is not None:
                    overlap_len = prev_right - left
                    total -= overlap_len * (overlap_len + 1) // 2

                prev_right = right

        return total

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        self._nums = nums

        at_most_k = self._at_most_k_ints(k)
        
        return 0 if at_most_k == 0 else at_most_k - self._at_most_k_ints(k - 1)