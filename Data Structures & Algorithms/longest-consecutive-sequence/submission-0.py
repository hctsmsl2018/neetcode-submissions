class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_seq = 0

        while nums_set:
            seq_len = 1
            start = nums_set.pop()
            counter = start + 1

            while counter in nums_set:
                nums_set.remove(counter)
                seq_len += 1
                counter += 1

            counter = start - 1

            while counter in nums_set:
                nums_set.remove(counter)
                seq_len += 1
                counter -= 1

            if seq_len > longest_seq:
                longest_seq = seq_len

        return longest_seq