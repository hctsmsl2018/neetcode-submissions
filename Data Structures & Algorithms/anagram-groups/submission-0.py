class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_sets = defaultdict(list)

        for s in strs:
            anagram_sets[tuple(sorted(Counter(s).items()))].append(s)

        return list(anagram_sets.values())