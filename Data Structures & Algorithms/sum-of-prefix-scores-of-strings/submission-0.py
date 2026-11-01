class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        trie = {}

        for w in words:
            subtrie = trie

            for c in w:
                if c not in subtrie:
                    subtrie[c] = {"score": 0}

                subtrie[c]["score"] += 1
                subtrie = subtrie[c]

        score_sums = []

        for w in words:
            score_sum = 0

            subtrie = trie

            for c in w:
                score_sum += subtrie[c]["score"]
                subtrie = subtrie[c]

            score_sums.append(score_sum)

        return score_sums