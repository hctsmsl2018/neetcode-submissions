class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        start_end_vowel_prefix_sum = [0] # 0, 1, 1, 2, 3, 4
        vowels = {"a", "e", "i", "o", "u"}

        for w in words:
            start_end_vowel_prefix_sum.append(start_end_vowel_prefix_sum[-1] + int({w[0], w[-1]} < vowels))

        return [start_end_vowel_prefix_sum[e + 1] - start_end_vowel_prefix_sum[s] for s, e in queries] # 2, 3, 0