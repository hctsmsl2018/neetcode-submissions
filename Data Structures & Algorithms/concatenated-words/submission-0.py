class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        trie = {}
        words.sort(key=len)
        concatenated = []

        for w in words:
            start_indices = [0]
            seen_indices = {0}

            while len(start_indices) > 0:
                ind = start_indices.pop()

                if ind == len(w):
                    concatenated.append(w)
                    break

                subtrie = trie

                while ind < len(w) and w[ind] in subtrie:
                    subtrie = subtrie[w[ind]]
                    ind += 1

                    if ind not in seen_indices and "*" in subtrie:
                        start_indices.append(ind)
                        seen_indices.add(ind)

            subtrie = trie

            for c in w:
                if c not in subtrie:
                    subtrie[c] = {}

                subtrie = subtrie[c]

            subtrie["*"] = None

        return concatenated