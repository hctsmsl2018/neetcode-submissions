class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = {}

        for word in wordDict:
            curr_trie = trie

            for c in word:
                if c not in curr_trie:
                    curr_trie[c] = {}

                curr_trie = curr_trie[c]

            curr_trie["*"] = len(word)

        visited = set()
        queue = {0}

        while len(queue) > 0:
            curr_ind = queue.pop()
            visited.add(curr_ind)

            curr_trie = trie

            while curr_ind < len(s) and s[curr_ind] in curr_trie:
                if "*" in curr_trie and curr_ind not in visited:
                    queue.add(curr_ind)

                curr_trie = curr_trie[s[curr_ind]]
                curr_ind += 1

            if "*" in curr_trie and curr_ind not in visited:
                queue.add(curr_ind)

        return len(s) in visited