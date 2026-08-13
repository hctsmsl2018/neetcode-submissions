class Solution:
    def _find_words_from_ind(self, start):
        if start == len(self._s):
            self._solutions.append(" ".join(self._curr_words))

        subtrie = self._trie

        for i in range(start, len(self._s)):
            c = self._s[i]

            if c in subtrie:
                subtrie = subtrie[c]

                if "*" in subtrie:
                    end = i + 1
                    self._curr_words.append(self._s[start:end])
                    self._find_words_from_ind(end)
                    self._curr_words.pop()
            else:
                break

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self._s = s
        self._solutions = []
        self._curr_words = []
        self._trie = {}

        for w in wordDict:
            subtrie = self._trie

            for c in w:
                if c not in subtrie:
                    subtrie[c] = {}

                subtrie = subtrie[c]

            subtrie["*"] = "*"

        self._find_words_from_ind(0)

        return self._solutions