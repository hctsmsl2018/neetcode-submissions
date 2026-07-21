class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr_subtree = self.trie

        for c in word:
            if c not in curr_subtree:
                curr_subtree[c] = {}
            
            curr_subtree = curr_subtree[c]

        curr_subtree["*"] = None

    def _search_subtree(self, word, subtree, word_ind):
        if len(word) == word_ind:
            return "*" in subtree
        elif word[word_ind] == ".":
            for subsubtree in subtree.values():
                if subsubtree is not None and self._search_subtree(word, subsubtree, word_ind + 1):
                    return True
        elif word[word_ind] in subtree:
            return self._search_subtree(word, subtree[word[word_ind]], word_ind + 1)

        return False

    def search(self, word: str) -> bool:
        return self._search_subtree(word, self.trie, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)